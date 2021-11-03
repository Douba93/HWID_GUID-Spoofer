import winreg
from time import sleep
from os import system

def Change_HWID():
	system("cls")
	print("\t\t|Use generator command before using this!|\n")
	input("Enter to continue...\n")
	try:
		choixProfile = input("{xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}> ")
		system("cls")
		show_HWID()
		print("\n\t\tChanging HWID...\n")
		sleep(5)
		system("cls")
		key = winreg.OpenKey( winreg.HKEY_LOCAL_MACHINE, 'SYSTEM\\CurrentControlSet\\Control\\IDConfigDB\\Hardware Profiles\\0001',0, winreg.KEY_SET_VALUE)
		winreg.SetValueEx(key, 'HwProfileGuid', 0, winreg.REG_SZ, choixProfile)
		winreg.CloseKey(key)
		print("\n\tHWID changed successfully!\n")
		show_HWID()
		input("\nEnter to continue...")
	except PermissionError:
		system("cls")
		print("\n\t|The program must be started as administrator!|\n")
		input("Enter to continue...")
		exit(0)

def Change_GUID():
	system("cls")
	print("\t\t|Use generator command before using this!|\n")
	input("Enter to continue...\n")

	try:
		choixMachine = input("xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx > ")
		show_GUID()
		print("\n\t\tChanging GUID...\n")
		sleep(5)
		system("cls")
		key = winreg.OpenKey( winreg.HKEY_LOCAL_MACHINE, 'SOFTWARE\\Microsoft\\Cryptography',0, winreg.KEY_SET_VALUE)
		winreg.SetValueEx(key, 'MachineGuid', 0, winreg.REG_SZ, choixMachine)
		winreg.CloseKey(key)
		print("\n\tGUID changed successfully!\n")
		show_GUID()
		input("\nEnter to continue...")
	except PermissionError:
		system("cls")
		print("\n\t|The program must be started as administrator!|\n")
		input("Enter to continue...")

def show_HWID():
	key = winreg.OpenKey( winreg.HKEY_LOCAL_MACHINE, 'SYSTEM\\CurrentControlSet\\Control\\IDConfigDB\\Hardware Profiles\\0001',0, winreg.KEY_READ)
	(valeur,typevaleur) = winreg.QueryValueEx(key,'HwProfileGuid')
	winreg.CloseKey(key)
	print('-'*20)
	print('|Current HWID|')
	print(valeur, typevaleur)
	print('-'*20)

def show_GUID():
	key = winreg.OpenKey( winreg.HKEY_LOCAL_MACHINE, 'SOFTWARE\\Microsoft\\Cryptography',0, winreg.KEY_READ)
	(valeur,typevaleur) = winreg.QueryValueEx(key,'MachineGuid')
	winreg.CloseKey(key)
	print("-"*20)
	print('|Current GUID|')
	print(valeur, typevaleur)
	print("-"*20)

def fakeMail():
	system("start https://temp-mail.org/en/")
def GuidGenerator():
	system("start https://www.guidgenerator.com/online-guid-generator.aspx")

def help():
	print("-"*50)
	print("\n\tsetHWID -> Change your GUID\n")
	print("\tsetGUID -> Change your HWID\n")
	print("\tdisHWID -> Show Current HWID\n")
	print("\tdisGUID -> Show Current GUID\n")
	print("\tquit -> Exit Application\n")
	print("\tcls -> Clear Terminal\n")
	print("\tfakemail -> Free email generator\n")
	print("\tgenerator -> Free GUID|HWID generator\n")
	print("\tRestart your computer to apply the changes\n")
	print("-"*50)