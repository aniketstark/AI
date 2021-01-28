# encoding: utf-8
#愚かinstallation file
import ai_detail
import os
import sys
import time
from database import get_name, get_age, get_uname, get_uage, get_idname, update_uname, update_uage, update_idname
from ai_detail import name, age, developers, uname, uage, idname
os.system("pip2 install termcolor")
from termcolor import colored

#functions

def printslow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

def fillup():
	print(colored("""Before You start AI we need some information from you\nNot Credit/Debit card bruhhh\nWe need your name and age only\n\n""","green"))
	yourname = input("Name > ")
	if yourname == "":
		print("you didn't write your name")
		os.system("clear")
		fillup()
	else:
		update_uname(yourname)
		ai_detail.uname = yourname
		print(colored("""a.... your name is """ + yourname,"green"))
		printslow(colored("""aa a a hajimemashte watashi wa aiko desu He.. Hell..\n""","red"))
		print(colored("""Hello my name is Aiko Nice to meet you""", 'red'))
		fillup2()
		
def fillup2():	
	yourage = input("Enter Your Age > ")
	update_uage(yourage)
	ai_detail.uage = yourage
	print(colored("""ano... your age is """ + yourage,"green"))
	if int(ai_detail.uage) <= 2:
		update_idname("ototo")
		print(colored("""Your so much small than me """+ str(idname),"yellow"))
		print(ai_detail.idname())
		time.sleep(3)
		print(colored("""Now Your can start with using this command python3 start.py""","green"))
		os.system("echo clearing terminal in 15sec | lolcat -a -d 150")
		os.system("clear")
		sys.exit()
	elif int(ai_detail.uage) > 2 and int(ai_detail.uage) < 25:
		update_idname("Oni-Chan")
		print(colored("""Your bigger than me """+ str(idname),"red"))
		time.sleep(3)
		print(colored("""Now Your can start with using this command python3 start.py""","green"))
		os.system("echo clearing terminal in 15sec | lolcat -a -d 150")
		os.system("clear")
		sys.exit()
	elif int(ai_detail.uage) >= 25:
		update_idname("Goshujinsama")
		print(colored("""ahhh... wuaa.. your so much bigger than me """+ str(idname),"white"))
		os.system("termux-open assets/happy/greeting/new_greeting.mp4")
		time.sleep(3)
		print(colored("""Now Your can start with using this command python3 start.py""","green"))
		os.system("echo clearing terminal in 15sec | lolcat -a -d 150")
		os.system("clear")
		sys.exit()
		
	#stashcode age greater than less than and 100 limit

def installpkg():
	printslow(colored("""INSTALLING PACKAGES""","green"))
	os.system("pkg install -y python python2 python3 ruby php termux-api zip screenfetch")
	printslow(colored("""INSTALLING PYTHON MODULES""","green"))
	os.system("pip3 install lolcat beautifulsoup4 argparse requests pysocks mpv termcolor")
	printslow(colored("""DOWNLOADING ASSETS and Server""","green"))
	os.system("wget https://www.dropbox.com/s/xdrg1l49ddf0lo3/ai_asste.zip")
	os.system("unzip ai_asset.zip")
	os.system("rm -rf ai_asset.zip")
	printslow(colored("""PLEASE INSTALL TERMUX API FROM PLAYSTORE\nIF ITS ALREADY INSTALL SO IGNORE THIS MESSAGE""","green"))
	os.system("termux-open-url https://play.google.com/store/apps/details?id=com.termux.api")
	print(colored("""ALL PACKAGES INSTALLED""", "green"))
	time.sleep(3)
	os.system("clear")
	fillup()

def information():
	os.system("clear")
	printslow(colored("""Before We send our AI Child to you Please Read this Info.""","green"))
	print(colored("""
	 =====================================================
	                      AI v0.1Beta
	 =====================================================""","red"), colored("""
	 1. This AI only worked on Termux
	 
	 2. I know many of the pepole getting questions like a
	 "Child AI", yeah my nigg she is my daughter
	 Ok That was joke -_-
	 Main Reason is some of the algorithm and somethings
	 are still underwork/pending thats why she is child
		
	 3. She didn't had lots of knowledge because of she is
	 child (bruhhh)
		
	 4. If you mess with her. so her bodyguard will punished
	 you well so be carefull
		
	 5. I don't knos why the flick we add japanese in AI
	 
	 6. Sometime she express her feeling with using video
	 so don't ignore that
		
	 7. If something Wrong happend like you get punishment so
	 we are not responsible for that
		
	 8. Don't worry this AI still under work, we are trying
	 to turn her into adult so be patience for that""","green"), colored("""
	 =======================================================\n\n""","red"))
	print(colored("""SO ARE YOU READY, FOR TAKING RESPONSIBLITY OF OUR AI""","green"))
	say = input("Say(Y/N) > ")
	if say == "Y" or say == "y":
		installpkg()
		os.system("termux-open assets/install.mp4")
	elif say == "N" or say == "n":
		sys.exit()
	else:
		printslow(colored("""say it right answer""","green"))
		information()

information()
