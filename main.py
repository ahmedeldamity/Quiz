import json
from User import userClass
import questions

enter = input("Are you have account? Y/N: ")

if enter == 'Y' or enter == 'N':
	userName = str(input("Enter your user name: "))
	password = str(input("Enter your password: "))

	if enter == 'Y':

		ckUserNameForLogin = userClass.checkOnUserNameForLogin(userName)

		if ckUserNameForLogin:
			
			ckPasswordForLogin = userClass.checkOnPasswordForLogin(userName, password)

			if ckPasswordForLogin:

				print(f"Welcome {userName}")

				topic = str(input("Enter topic you need to solve in: (OOP, CPP, CSharp): "))

				print()

				userInstance = userClass.CreateUserInstanceForLogIn(userName, password, topic)

				questions.Topic(userInstance, topic)

			else:
				print("Your pass invalid")

		else:
			print("Your user name invalid")
		
	else:
		
		ckUserNameForRegister = userClass.checkOnUserNameForRegister(userName)

		if ckUserNameForRegister:

			print(f"Welcome {userName}")

			topic = str(input("Enter topic you need to solve in: (OOP, C++ Programming, C# Programming): "))

			userInstance = userClass.CreateUserInstanceForRegister(userName, password, topic)

			userInstance.addUser()

			questions.Topic(userInstance, topic)

		else:
			print("Your user name entered before")

else: 
	print("Invalid answer.")

