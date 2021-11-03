import logging
import time
import os
from os import system
import pickle
import winreg
import m1.HWID as hwid
system("color C")
system("cls")
print("+"*30)
print("\t|DoubaCorp|\n")
print("\t\\HWID|GUID/ ||Spoofer||\n")
print("+"*30)

rootlog = logging.getLogger()
handler = logging.FileHandler('process.logs')
rootlog.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
rootlog.addHandler(handler)
logging.info('<Process Start>')

try:
	if not os.path.exists("usr.data"):
		User = input(f"[{time.strftime('%H:%M:%S')}]: Choose User Name>")
		passWd = input(f"[{time.strftime('%H:%M:%S')}]: Choose PassWord>")
		Username = [User]
		PassWord = [passWd]
		Username1 = [Username]
		PassWord1 = [PassWord]
		with open('usr.data', 'wb') as f:
			pickle.dump(Username1,f)
			pickle.dump(PassWord1,f)
			logging.info('<New usr.data Created!>')
except KeyboardInterrupt:
	system("cls")
	print('Bye!')
	logging.info('Shutdown Process!')
	exit(0)
logging.info('<Connected!>')
system("cls")
try:
	while True:
		Command = input(f"[{time.strftime('%H:%M:%S')}]: help for comands list>")
		if Command == "disHWID":
			hwid.show_HWID()
			logging.info('|disHWID command called!|')
		elif Command == "disGUID":
			hwid.show_GUID()
			logging.info('|disGUID command called!|')
		elif Command == "cls":
			system("cls")
			logging.info('|cls command called!|')
		elif Command == "quit":
			system("cls")
			print("Bye!")
			logging.info('|Shutdown Process!|')
			exit(0)
		elif Command == "help":
			hwid.help()
			logging.info('|help command called!|')
		elif Command == "generator":
			hwid.GuidGenerator()
			logging.info('|generator command called!|')
		elif Command == "fakemail":
			hwid.fakeMail()
			logging.info('|fakemail command called!|')
		elif Command == "setHWID":
			hwid.Change_HWID()
			logging.info("|setHWID command called!|")
		elif Command == "setGUID":
			hwid.Change_GUID()
			logging.info("|setGUID comand called!|")
except KeyboardInterrupt:
	system("cls")
	print("Bye!")
	logging.info('Shutdown Process!')
	exit(0)