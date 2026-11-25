# word = input('Enter your word:  ')

# print(len(word))




# 1 ЗАДАНИЕ: Запроси имя персонажа, его расу, возраст и профессию. Выведи красивую анкету через f-строку.


# name = input('Enter your name:  ')
# race = input('Enter your race:  ')
# age = int(input('Enter your age:  '))
# profession = input('Enter your profession: ')

# print(f'  === CHARACTER ===  \n  Name: {name} \n  Race: {race} \n  Age: {age} \n  Profession: {profession}')




# 2 ЗАДАНИЕ: Запроси сумму в гривнах и курс доллара. Рассчитай, сколько долларов получит пользователь.


# amount = float(input('Enter amount in hryvnias:  '))
# dollar_rate = float(input('Enter dollar exchange rate:  '))

# print(f"Dollars received: {amount // dollar_rate}")




# 3 ЗАДАНИЕ: Пользователь вводит количество секунд. Программа переводит их в часы, минуты и оставшиеся секунды.


# second = int(input('Enter the numbers of seconds:  ')) 
# hour = second // 3600
# remainder_hour = second % 3600 
# minute = remainder_hour // 60 
# remainder_minute = remainder_hour % 60
# print(hour, minute, remainder_minute)




# 4 ЗАДАНИЕ: Запроси два числа, сохрани их в переменные a и b, поменяй значения местами и выведи результат.


# a = int(input('Enter number :  '))
# b = int(input('Enter number :  '))
# a, b = b, a

# print(a, b)




# 5. Анализ слова
# Запроси непустое слово и выведи его длину, первый и последний символ, а также само слово, повторённое три раза.


# word = input('Enter your word:  ')

# print(len(word), word[0], word[-1], word, word, word)




# 6. Чётное или нечётное
# Запроси целое число. Определи, чётное оно или нечётное. Дополнительно сообщи, является ли оно положительным, отрицательным или нулём.


# num = int(input('Enter your number:  '))

# if num % 2 == 0:
#     print('Even')
# else:
#     print('Odd number')

# if num > 0: 
#     print('Number is positive')    

# elif num < 0:
#     print('Number is negative')
            
# else:
#     print('Number is 0')




# 7. Наибольшее число
# Пользователь вводит три числа. Программа выводит наибольшее из них.


# num1 = int(input('Enter your first number:  '))
# num2 = int(input('Enter your second number: '))
# num3 = int(input('Enter your third number:  '))

# if num1 > num2 and num1 > num3:
#     print(num1)
# elif num2 > num1 and num2 > num3: 
#     print(num2)
# else:
#     print(num3)




# 8. Проверка пароля
# Запроси пароль пользователя и оцени его по длине.


# password = input('Enter your password:  ')

# if len(password) < 6: 
#     print('Poor')
# elif 6 <= len(password) <= 9:
#     print('Mid')
# elif 10 <= len(password) <= 15: 
#     print('Good')
# else:
#     print('Excellent')




# 9. Определение времени суток


# day_time = int(input('Enter the time of day:  '))


# if 0 <= day_time <= 5:
#     print('night')
# elif 6 <= day_time <= 11:
#     print('Morning')
# elif 12 <= day_time <= 17:
#     print('Day')
# elif 17 <= day_time <= 23:
#     print('Evening')
# else:
#     print('ERROR')




# 10. Стоимость доставки


# order_cost = float(input("Enter the order value:  "))
# distance_km = int(input("Enter the delivery distance:  "))

# if order_cost >= 1000:
#     print(f' Order cost: {order_cost} \n Delivery if FREE \n Final price: {order_cost}')

# elif distance_km <= 5:
#     print(f' Order cost: {order_cost} \n Delivery cost: 50 uah \n Final price: {order_cost + 50}')
# elif distance_km > 5:
#      print(f' Order cost: {order_cost} \n Delivery cost: 100 uah \n Final price: {order_cost + 100}')



# order_cost = float(input("Enter the order value:  "))
# distance_km = int(input('Enter the delivery distance:  '))
# delivery_cost = 0

# if order_cost >= 1000:
#     print(f' Order cost: {order_cost} \n Delivery is FREE \n Final price: {order_cost}')
# elif distance_km <= 5:
#     delivery_cost = 50
#     print(f' Order cost: {order_cost} \n Delivery cost: {delivery_cost} \n Final price: {order_cost + delivery_cost}')
# else:
#     delivery_cost = 100
#     print(f' Order cost: {order_cost} \n Delivery cost: {delivery_cost} \n Final price: {order_cost + delivery_cost}')



# order_cost = float(input('Enter the order value:  '))
# distance_km = int(input('Enter the delivery distance:  '))

# if order_cost >= 1000:
#     delivery_cost = 0
# elif distance_km <= 5:
#     delivery_cost = 50 
# else:
#     delivery_cost = 100

# final_price = order_cost + delivery_cost
# print(f' Order cost: {order_cost} \n Delivery cost: {delivery_cost} \n Final price: {final_price}')




# 11. Система авторизации


# login = input('Enter login:  ')
# password = input('Enter password:  ')

# correct_login = "admin"
# correct_password = "python123"
# is_banned = False

# if login != correct_login:
#     print('Access denied: Incorrect login') 
# elif password != correct_password:
#     print('Access denied: Incorrect password')
# elif is_banned:
#     print('Access denied: User is banned')
# else:
#     print('Access granted')




# 12. Система покупки игры
# Пользователь вводит свой баланс, стоимость игры и наличие промокода (yes или no).
# Промокод даёт скидку 15%. Если денег достаточно, покупка успешна и программа выводит остаток баланса.
# Если недостаточно — сообщает, сколько денег не хватает.


# balance = float(input('Enter your balance: '))
# game_price = float(input('Enter price of game:  '))
# promo = input('Do you have promo?(yes/no):  ')
 

# if promo == 'yes':
#     discount = 15
# else:
#     discount = 0

# discount_amount = game_price * discount / 100
# final_price = game_price - discount_amount

# if balance >= game_price:
#     remaining_balance = balance - final_price
#     print('Purchase successfull')
#     print(f'Remaining balance: {remaining_balance}')
# else:
#     missing_money = final_price - balance
#     print(f'Not enough money! You need {missing_money} more.')


































