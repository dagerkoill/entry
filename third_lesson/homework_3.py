# 1. Спроси у пользователя его балл за тест (от 1 до 12).

# - Если балл от 10 до 12 — выведи: "Красава, отличник!"
# - Если балл от 7 до 9 — выведи: "Нормально, хорошист."
# - Если балл от 4 до 6 — выведи: "Ну такое, тройка..."
# - В остальных случаях — выведи: "Двойка, пересдача!"



# grade = int(input('Enter your grade '))


# if grade >= 10 and grade <= 12 :
#     print('Nice work!')

# elif grade >= 7 and grade <= 9 : 
#     print('Good')

# elif grade >= 4 and grade <= 6 :
#     print('So-so')

# else:
#     print('Bad')




# 2. Спроси у пользователя его возраст и имя.

# Если его имя "Святик" или ему меньше 18 лет — выведи: "Вход воспрещён!"

# Иначе — выведи: "Проходи, добро пожаловать!"



# name = input('Enter your name ')

# age = int(input('Enter your age '))


# if name == "Святик" or age < 18 :
#     print('Entry prohibited')

# else:
#     print('Welcome')




# 3. Запроси у пользователя число от 1 до 100.

# Проверь, находится ли число строго в диапазоне от 20 до 50 (включительно).
# Если да — выведи: "Число попало в цель!"
# Если нет — выведи: "Мимо!"



# num = int(input('Enter your number '))


# if num >= 20 and num <= 50 :
#     print('nice')

# else:
#     print('falt')




# 4. Создай переменную is_banned = False и is_admin = True.

# Напиши условие: если пользователь НЕ забанен (not is_banned) И он админ (is_admin) — выведи: "Доступ к панели управления разрешён!"

# Иначе — выведи: "Отказано в доступе!"



# is_banned = False

# is_admin = True 


# if not is_banned and is_admin :
#     print('Access to the control panel is permitted')

# else:
#     print('Access denied')




# 5. Система скидок в магазине :

# Спроси у пользователя сумму покупки.

# Если сумма больше или равна 1000:

# Запроси вопрос: "Есть ли у вас VIP-карта? (да/нет)":

# Если ввёл "да" — выведи: "Скидка 20%!"

# Если "нет" — выведи: "Скидка 10%!"

# Если сумма меньше 1000 — выведи: "Скидки нет, покупай больше!"


# P.S. везде надо выводить итоговую сумму 



#  ПЕРВЫЙ ВАРИАНТ 


# total = int(input('Enter the amount of your purchase '))

# if total >= 1000 :
#     vip = input('Do you have VIP-card? (yes/no) ')

#     if vip == "yes" :
#         final_price = total * 0.8
#         print(f' Discount 20%! \n Final price {final_price}')

#     else:
#         final_price = total * 0.9
#         print(f" Diccount 10%! \n Final price {final_price} ")
# else:
#     print("No discount! Buy nore stuff !!!")
        

# ВТОРОЙ ВАРИАНТ 



# total = int(input('Enter the amount of your purchase '))

# if total >= 1000 :
#     vip = input('Do you have VIp-card? (yes/no) ')
#     if vip == "yes" :
#         discount = 20
#         final_price = total * (1 - discount / 100)
#         print(f' Discount 20%! \n Final price {final_price} ')
#     else:
#         discount = 10
#         final_price = total * (1 - discount / 100)
#         print(f' Discount 10% \n Final price {final_price} ')
# else:
#     print('No discount!!! Buy more stuff!!! ')





