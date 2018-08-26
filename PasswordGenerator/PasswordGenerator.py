import string
import secrets
import sys
import pyperclip


def generator(limit):
	if limit > 30 :
		print("Enter limit less than 20 !!!")
		sys.exit()	
	generated_string = "".join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for x in range(30))
	generated_password= "".join(secrets.choice(generated_string) for x in range(limit))
	pyperclip.copy(generated_password)
	print("The generated password has been copied to your clipboard !!")

if __name__ == "__main__":
	
	print("						Welcome to password generator")
	print("Enter the required length of the generated password (max 20 chracters!)")
	limit = int(input())
	generator(limit)
