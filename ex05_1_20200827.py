my_name = input("Your name: ")
my_age =  input("Your age: ")
my_hair = input("Your hair's color: ")
my_height = int(input("Your height: "))

print(f"Hello, your name is {my_name}.")
print(f"I know ,your age is {my_age}.")
print(f"Haha, the color of your hair is {my_hair}.")


if my_height > 50:
	print(f"Your height is {my_height}, you are too heavy.")
else:
	print("You are healthy.")
