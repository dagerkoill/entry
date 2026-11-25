# Напиши програму которая принимает число score (количество баллов от 0 до 100 ( надо проверить ) и возвращает оценку в виде строки:
# Если баллов 90 и больше — возвращает "Отлично"
# Если баллов от 70 до 89 — возвращает "Хорошо"
# Если баллов от 50 до 69 — возвращает "Удовлетворительно"
# Во всех остальных случаях — возвращает "Неудовлетворительно"



# score = int(input('Enter your score: '))

# if score < 0 or score > 100:
#     print('Enter the correct number!!!')

# elif score >= 90 :
#     print('NICE WORK!!!!')

# elif score >= 70 and score <= 89 :
#     print('Good!')

# elif score >= 50 and score <= 69 :
#     print('Satisfactorily')

# else: 
#     print('Unsatisfactory')





# score = int(input('Enter your csore: '))

# if score < 0 or score > 100 :
#     print('Enter the correct number!!!!!!!!!!!')

# elif score >= 90 :
#     print('NICE WORK!!!!!!')

# elif 70 <= score <= 89 :
#     print('Good!') 

# elif 50 <= score <= 69 : 
#     print('Satisfactorily')

# else:
#     print('Unsatisfactory')





# score = int(input('Enter your score: '))

# if score < 0 or score > 100:
#     print('Enter the correct number!!!')
# elif score >= 90:
#     print('NICE WORK!!!!')
# elif score >= 70:
#     print('Good!')
# elif score >= 50:
#     print('Satisfactorily')
# else:
#     print('Unsatisfactory')





# Простой калькулятор
# Сделать программу, которая принимает два числа и знак операции, а затем считает результат.

# Запроси у пользователя:
#        • Первое число (num1)
#        • Знаки операции: +, -, *, / (operation)
#        • Второе число (num2)

# В зависимости от operation выполни нужную математическую операцию:

#      • Если + — сложи числа
#      • Если - — вычти num2 из num1
#      • Если * — перемножь
#      • Если / — раздели num1 на num2

# Защита: Если operation == '/' и num2 == 0, выведи "Ошибка: деление на ноль!"
# Если введен неизвестный знак операции (например, % или ^), выведи "Неизвестная операция!"

# В остальных случаях выведи результат вычисления.



# num1 = float(input('Enter first number:  '))
# operation = input('Enter your operation: ')
# num2 = float(input('Enter second number:  '))

# if operation == '/' and num2 == 0 :
#     print('ERROR: division by zero! ')
# if operation == '%' or operation == '^' or operation == '**' :
#     print("Incorrect operation! ")

# if operation == '+' :
#     print(num1 + num2)
# elif operation == '-' :
#     print(num1 - num2)
# elif operation == '*' :
#     print(num1 * num2)
# elif operation == '/' :
#     print(num1 / num2)
