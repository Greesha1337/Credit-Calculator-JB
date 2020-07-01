credit_principal = int(input('Enter the credit principal: \n'))

while True:
    payment_choise = input('''What do you want to calculate?
type \"m\" - for count of months,
type \"p\" - for monthly payment:\n''')
    if payment_choise == 'm':
        monthly_payment = int(input('Enter monthly payment:\n'))
        months = credit_principal // monthly_payment
        if months == 1:
            print(f'It takes {months} month to repay the credit')
            break
        else:
            if credit_principal % monthly_payment == 0:
                print(f'It takes {months} months to repay the credit')
                break
            else:
                print(f'It takes {months + 1} months to repay the credit')
                break
    elif payment_choise == 'p':
        count_of_months = int(input('Enter count of months:\n'))
        monthly_payment = credit_principal // count_of_months + 1
        last_payment = credit_principal - (count_of_months - 1) * monthly_payment
        if credit_principal % count_of_months == 0:
            print(f'Your monthly payment = {credit_principal // count_of_months}')
            break
        else:
            print(f'Your monthly payment = {monthly_payment} with last month payment = {last_payment}')
            break
