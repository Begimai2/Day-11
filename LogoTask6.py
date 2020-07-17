user1 = input()
user2 = input()
user3 = input()
if user1 == user2 == user3:
    print("Все значения равны")
elif user1 == user2 or user1 == user3:
    print("Два из этих значений равны")
elif user2 == user1 or user2 == user3:
    print("Два из этих значений равны")
else:
    print("Ничего не равно")
print("Введите 1 значение")
print("Введите 2 значение")
print("Введите 3 значение")