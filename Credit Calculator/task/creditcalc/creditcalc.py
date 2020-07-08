import math
import argparse
import sys


def main():
    if __name__ == '__main__':
        parser = argparse.ArgumentParser(description='Credit calculator')

        parser.add_argument('-t', '--type', help='Type of payment (Annuity or Differential)')
        parser.add_argument('-y', '--payment', help='Monthly payment', type=int)
        parser.add_argument('-p', '--principal', help='Credit principal', type=int)
        parser.add_argument('-r', '--periods', help='Count of months', type=int)
        parser.add_argument('-n', '--interest', help='Credit interest', type=float)

        args = parser.parse_args()

        for itm in sys.argv:
            for i, el in enumerate(itm):
                if el == '=':
                    itm = itm[i + 1:]
                    break
            if itm.isdigit():
                itm = int(itm)
                if itm < 0:
                    print('Incorrect parameters')

        if args.interest is None or args.interest < 0:
            print('Incorrect parameters')
            exit(0)
        else:
            i = args.interest / (12 * 100)

        if args.type not in ['annuity', 'diff']:
            print('Incorrect parameters')
            exit(0)

        else:
            if args.type == 'annuity':
                if args.payment is None:
                    def calc_annuity(principal, periods, interest):
                        args.principal = principal
                        args.periods = periods
                        args.interest = interest
                        annuity = principal * ((i * (i + 1) ** periods) / (((1 + i) ** periods) - 1))
                        print(f'Your annuity payment = {math.ceil(annuity)}')
                        print(f'Overpayment = {math.ceil(annuity) * periods - principal}')

                    calc_annuity(args.principal, args.periods, args.interest)

                elif args.periods is None:
                    def calc_period(principal, payment, interest):
                        args.principal = principal
                        args.payment = payment
                        args.interest = interest
                        period = math.ceil(math.log((payment / (payment - i * principal)), 1 + i))
                        if period % 12 != 0:
                            print(
                                f'You need {int(period // 12)} years and'
                                f'{int(period % 12)} months to repay this credit!')
                        elif period == 12:
                            print(f'You need {int(period // 12)} year to repay this credit!')
                        else:
                            print(f'You need {int(period // 12)} years to repay this credit!')

                        print(f'Overpayment = {math.ceil(period) * payment - principal}')

                    calc_period(args.principal, args.payment, args.interest)

                elif args.principal is None:
                    def calc_principal(payment, interest, periods):
                        args.periods = periods
                        args.payment = payment
                        args.interest = interest
                        principal = payment / ((i * ((i + 1) ** periods)) / (((i + 1) ** periods) - 1))
                        print(f'Your credit principal = {int(principal)}')
                        print(f'Overpayment = {math.ceil(payment * periods - principal)}')

                    calc_principal(args.payment, args.interest, args.periods)

                else:
                    print('Incorrect parameters')

            else:
                def calc_diff(principal, interest, periods):
                    args.principal = principal
                    args.periods = periods
                    args.interest = interest
                    month = 1
                    monthly_payment = []
                    while month <= periods:
                        payment = principal / periods + i * (principal - (principal * (month - 1) / periods))
                        print(f'Month {month}: paid out {math.ceil(payment)}')
                        month += 1
                        monthly_payment.append(math.ceil(payment))
                    print()
                    print(f'Overpayment = {math.ceil(sum(monthly_payment) - principal)}')

                calc_diff(args.principal, args.interest, args.periods)

    else:
        exit(0)


main()
