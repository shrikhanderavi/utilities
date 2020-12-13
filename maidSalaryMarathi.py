'''author : ravi shrikhande'''

print('तुमचा या महिन्याचा पगार जाणून घेण्यासाठी खालील माहिती भरा :\n')
poli_days = int(input('पोळीचे एकूण दिवस टाका: '))
bhandi_days = int(input('भांड्यांचे एकूण दिवस टाका: '))
farshi_days = int(input('फर्शीचे एकूण दिवस टाका: '))

#adding paid days to each
poli_total_days = poli_days + 3
bhandi_total_days = bhandi_days + 3
farshi_total_days = farshi_days + 1

#multiplying by per day salary
poli_pay = poli_total_days * 33.34
bhandi_pay = bhandi_total_days * 20
farshi_pay = farshi_total_days * 20

#adding overall
total_pay = poli_pay + bhandi_pay + farshi_pay

print('\nया  महिन्याचा एकूण पगार आहे : %s रुपये. सेवेबद्दल धन्यवाद...!! रक्कम तुमच्या बँकेच्या खात्यावर जमा केली जाईल. '%total_pay)

#for detailed salary
details = input('\nतुम्हाला पगाराची सविस्तर माहिती हवी आहे का?(press yes/no): ')

if details == 'yes':
    print('\nपोळीचे एकूण दिवस (३ खाडे पकडून ) %s आहेत , त्याचे %s रुपये ,\nभांड्यांचे एकूण दिवस (३ खाडे पकडून ) %s आहेत , त्याचे %s रुपये\nफर्शीचे एकूण दिवस (1 खाडे पकडून ) %s आहेत, त्याचे %s रुपये'%(poli_total_days,poli_pay,bhandi_total_days,bhandi_pay,farshi_total_days,farshi_pay))
elif details =='no':
    print('\nआमच्यावर विश्वास ठेवल्याबद्दल धन्यवाद..!! )')
else:
    print('कृपया योग्य पर्याय निवडा..!!')
#print('\ntotal poli days:%s \ntotal bhandi days:%s \ntotal farshi days:%s'%(poli_total_days,bhandi_total_days,farshi_total_days))


