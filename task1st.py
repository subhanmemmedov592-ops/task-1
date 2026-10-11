height=float(input('Enter your hight:'))
weight=float(input('Enter your weight:'))
BMI=weight/height**2
if BMI<18.5:
    print('Underwight')
elif BMI<=24.9:
    print('Normal weight')
elif BMI<=29.9:
    print('Overweight')
else:
    print('Obese')