import math

while True:
    payment_choise = input('''What do you want to calculate?
type \"n\" - for count of months,
type \"a\" - for annuity monthly payment,
type \"p\" - for monthly payment:\n''')
    if payment_choise == 'n':
        credit_principal = float(input('Enter the credit principal:\n'))
        monthly_payment = float(input('Enter monthly payment:\n'))
        credit_interest = float(input('Enter credit interest:\n'))
        nominal_interest = credit_interest / (12 * 100)
        count_of_periods = math.log(monthly_payment / (monthly_payment - nominal_interest * credit_principal), 1 +
                                    nominal_interest)
        years = round(count_of_periods // 12)
        months = math.ceil(count_of_periods % 12)
        if months == 12:
            years += 1
            months -= 12
        if years == 0 and months == 1:
            print(f'You need {months} month to repay this credit!')
            break
        elif years == 0 and 1 < months < 12:
            print(f'You need {months} months to repay this credit!')
            break
        elif years == 1 and months == 0:
            print(f'You need {years} year to repay this credit!')
            break
        elif years > 1 and months == 0:
            print(f'You need {years} years to repay this credit!')
            break
        elif years == 1 and months == 1:
            print(f'You need {years} year and {months} month to repay this credit!')
            break
        elif years == 1 and 1 < months < 12:
            print(f'You need {years} year and {months} months to repay this credit!')
            break
        elif years > 1 and months == 1:
            print(f'You need {years} years and {months} month to repay this credit!')
            break
        elif years > 1 and 1 < months < 12:
            print(f'You need {years} years and {months} months to repay this credit!')
            break
        else:
            # if credit_principal % monthly_payment == 0:
            #     print(f'It takes {months} months to repay the credit')
            #     break
            # else:
            #     print(f'It takes {months + 1} months to repay the credit')
            break
    # elif payment_choise == 'p':
    #     count_of_months = int(input('Enter count of months:\n'))
    #     monthly_payment = credit_principal // count_of_months + 1
    #     last_payment = credit_principal - (count_of_months - 1) * monthly_payment
    #     if credit_principal % count_of_months == 0:
    #         print(f'Your monthly payment = {credit_principal // count_of_months}')
    #         break
    #     else:
    #         print(f'Your monthly payment = {monthly_payment} with last month payment = {last_payment}')
    #         break
    elif payment_choise == 'a':
        credit_principal = float(input('Enter the credit principal:\n'))
        count_of_periods = float(input('Enter count of periods:\n'))
        credit_interest = float(input('Enter credit interest:\n'))
        nominal_interest = credit_interest / (12 * 100)
        annuity_payment = math.ceil(credit_principal * ((nominal_interest *
                                                         pow(1 + nominal_interest, count_of_periods))) /
                                    (pow(1 + nominal_interest, count_of_periods) - 1))
        print(f'Your annuity payment = {annuity_payment}!')
        break
    elif payment_choise == 'p':
        monthly_payment = float(input('Enter monthly payment:\n'))
        count_of_periods = float(input('Enter count of periods:\n'))
        credit_interest = float(input('Enter credit interest:\n'))
        nominal_interest = credit_interest / (12 * 100)
        credit_principal = round(monthly_payment / ((nominal_interest * pow(1 + nominal_interest, count_of_periods)) /
                                                    (pow(1 + nominal_interest, count_of_periods) - 1)))
        print(f'Your credit principal = {credit_principal}!')
        break
    else:
        break
