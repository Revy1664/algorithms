# Калькулятор

operation = input("Выберите операцию: ")

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

if operation == "+":
	c = a + b
	print(f"Ответ: {c}")
elif operation == "-":
	c = a - b
	print(f"Ответ: {c}")
else: 
	print("Неверная операция")
