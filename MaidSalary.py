'''author : ravi shrikhande'''

poli_days = int(input('Add number of present days for POLI: '))
bhandi_days = int(input('Add number of present days for BHANDI: '))
farshi_days = int(input('Add number of present days for FARSHI:'))

#adding paid days to each
poli_total_days = poli_days + 3
bhandi_total_days = bhandi_days + 3
farshi_total_days = farshi_days + 1

#multiplying by per day salary
poli_pay = poli_total_days * 34
bhandi_pay = bhandi_total_days * 20
farshi_pay = farshi_total_days * 20

#adding overall
total_pay = poli_pay + bhandi_pay + farshi_pay

print('Your total pay for this month is : %s सेवेबद्दल धन्यवाद '%total_pay)

#for detailed salary
details = input('Do you want details of salary, Like present days(Press yes/no): ')

if details == 'yes':
    print('\nTotal poli days including 3 days paid is %s, hence Rs : %s\nTotal bhandi days including 3 days paid is %s, hence Rs : %s\nTotal farshi days including 1 day paid is %s, hence Rs: %s'%(poli_total_days,poli_pay,bhandi_total_days,bhandi_pay,farshi_total_days,farshi_pay))
elif details =='no':
    print('\nThanks for trusting us..!!!:)')
else:
    print('Please provide valid input')
#print('\ntotal poli days:%s \ntotal bhandi days:%s \ntotal farshi days:%s'%(poli_total_days,bhandi_total_days,farshi_total_days))


