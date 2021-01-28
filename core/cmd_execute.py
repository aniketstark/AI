import os
import sys
import time
import socket
import random
import netifaces as ni 
from datetime import datetime
from core.emotions import *
from core.input_module import take_input
from core.ai_detail import *
from core.database import *
from core.ai_detail import name, age, address, developers, address, gender, uname, uage, idname
from termcolor import colored


#function
def netcheck():
	print(colored("""Checking Intornet Connection""","cyan"))
	try:
		sock = socket.create_connection(("www.google.com", 80))
		if sock is not None:
			print(colored("""Connected""","green"))
			random.choice(internet_list)()
			sock.close
	except OSError:
		print(colored(""" check your intornet connection """+idname,"red"))
		random.choice(no_internet_list)()
		exit()


   
#utility function
def ctime():
	now = datetime.now()
	
	current_time = now.strftime("%H hours %M minnutes")
	return current_time
	
def cdate():
	now = datetime.now()
	
	current_date = now.strftime("%d-%b-%Y")
	return current_date
	
def device_detail():
	os.system("screenfetch")

def flash():
	print(colored("""
	===============
	1. On
	2. Off
	===============
	B. Return
	===============""","green"))
	torch = input("flash > ")
	if torch == "1" or torch == "on":
		os.system("termux-torch on")
		os.system("clear")
	elif torch == "2" or torch == "off":
		os.system("termux-torch off")
		os.system("clear")
	elif torch == "B" or torch == "b":
		return("")
	else:
		print(colored(name+""": look like you enter wrong keyword """+idname,"green"))
		return("")
def flash_on():
	os.system("termux-torch on")
def flash_off():
	os.system("termux-torch off")

def take_photo():
	print(colored("""
	================""","white"), colored("""
	  Take Photo""","blue"),colored("""+_+""","yellow"),colored("""
	================""","white"),colored("""
	1. Back
	2. Front        ""","green"),colored("""
	================""","white"))
	tp = input("Photo > ")
	if tp == "1" or tp == "back":
		os.system("termux-camera-photo -c 0 /sdcard/back.jpg")
		print(colored(name+""": photo has been saved in /sdcard/back.jpg""","green"))
	elif tp == "2" or tp == "front":
		os.system("termux-camera-photo -c 1 /sdcard/front.jpg")
		print(colored(name+""": photo has been save in /sdcard/front.jpg""","green"))
	else:
		print(colored(name+""": look like you enter wrong keyword """+idname,"green"))

def battery_info():
	os.system("termux-battery-status")
	
def text_to_speech():
	print(colored("""Enter your text """+idname,"green"))
	txtsp = input("text > ")
	os.system("termux-tts-speak "+ txtsp +".")


#Ai and User Data Function	
def change_name():
	#sad and angry
	print(colored("""Ok Set new name for me""","yellow"))
	mname = input("New Name > ")
	if mname == "":
	 return("you didn't write anything")
	else:
	 update_name(mname)
	 ai_detail.name = mname
	 print(colored("""From now you can call me """+ mname,"green"))
	 
def change_yourname():
	print(colored("""Ok tell me your new name""","green"))
	yname = input("New Name > ")
	if yname == "":
	 return("you didn't write anything")
	else:
	 update_uname(yname)
	 ai_detail.uname = yname
	 print(colored("""From now your name is """+ yname +""", """+ idname,"green"))

def change_name_function():
	print(colored("""which one ?""","blue"))
	print(colored("""
	======================""","white"), colored("""
	1. My
	2. Your""","green"), colored("""
	======================""","white"))
	which = input("say > ")
	if which == "1" or which == "my" or which == "My":
		change_yourname()
	elif which == "2" or which == "your" or which == "yours" or which == "Your":
		change_name()
	else:
		random.choice(confused_list)()
		print("(wakarimasen) i don't understand "+ idname)
		
def change_user_age():
	print(colored(idname+""" now enter your new age""","green"))
	yourage = input("Enter Your Age > ")
	update_uage(yourage)
	ai_detail.uage = yourage
	print(colored("""ano... your age is """ + yourage,"green"))
	if int(ai_detail.uage) <= 2:
		update_idname("ototo")
		print(colored("""Your so much small than me ""","yellow"))
		print(ai_detail.idname())
		time.sleep(3)
		print(colored("""please restart me for effect""","green"))
		os.system("echo clossing ai in 15sec | lolcat -a -d 150")
		os.system("clear")
		sys.exit()
	elif int(ai_detail.uage) > 2 and int(ai_detail.uage) < 25:
		update_idname("Oni-Chan")
		print(colored("""Your bigger than me ""","red"))
		time.sleep(3)
		print(colored("""please restart me for effect""","green"))
		os.system("echo clossing ai in 15sec | lolcat -a -d 150")
		os.system("clear")
		sys.exit()
	elif int(ai_detail.uage) >= 25:
		update_idname("Goshujinsama")
		print(colored("""ahhh... wuaa.. your so much bigger than me ""","white"))
		time.sleep(3)
		print(colored("""please restart me for effect""","green"))
		os.system("echo clossing ai in 15sec | lolcat -a -d 150")
		os.system("clear")
		sys.exit()



#net core

def localip():
	ni.ifaddresses('wlan0')
	ip = ni.ifaddresses('wlan0')[ni.AF_INET][0]['addr']
	print(colored("Your ip is "+(ip),"green"))




#termux core
def clear_terminal():
	os.system("clear")



def update_pakage():
	#ok emotion
	netcheck()
	print(colored("""Updating Pakages\n""","green"))
	os.system("pkg install -y python python2 git php wget zip screenfetch")
	print(colored("""Updating Python Modules\n""","green"))
	os.system("pip3 install lolcat beautifulsoup4 argparse requests pysocks mpv termcolor")
	print(colored("""Updated!""","green"))
	time.sleep(3)
	os.system("clear")



def install_metasploit():
	netcheck()
	print(colored("""are you sure """+ idname +""" you want to install metasploit framework""","green"))
	say = input("y/n > ")
	if say == "y" or say == "Y" or say == "yes":
		print(colored("""installing...""","green"))
		print(colored("""it will take some time """+ idname,"green")) 
		os.system("pkg install -y unstable-repo metasploit")
	elif say == "n" or say == "N" or say == "no":
		print(colored("""ok i am cancelling this process""","green"))
	else:
		print(colored("""(ano ne)i think you type wrong word you need to type\n "y" stands for install\n "n" stands for cancel\n now you get it """+ idname,"green"))		




PATH='/data/data/com.termux/files/home/.vnc'
def vnc_folder_detection():
	if os.path.isdir(PATH) and os.access(PATH, os.R_OK):
		print(colored(name +""": ano ne ano ne """+ idname +""" looks like you already setup vnc""","green"))
		print(colored("""do you want to remove old vnc and setup new""","green"))
		say3 = input("y/n > ")
		if say3 == "y" or say3 == "Y" or say3 == "yes":
			print(colored(name +""": removing old vncserver""","red"))
			os.system("rm -rf /data/data/com.termux/files/home/.vnc")
			print(colored("""installing new""","green"))
		elif say3 == "n" or say3 == "N" or say3 == "No":
			random.choice(sorry_list)()
			print(colored(name +""": (gomenasai) """+ idname +""" i am sorry i am installing new ones""","red"))
			os.system("rm -rf /data/data/com.termux/files/home/.vnc")
	else:
		print(colored("""looks like you didn't installed vnc yet ahh mo..""","green"))	
def install_vnc():
	netcheck()
	print(colored(name +""": are you sure """+ idname +""" you want to install VNC/GUI in termux""","green"))
	say = input("y/n > ")
	if say == "y" or say == "Y" or say == "yes":
		vnc_folder_detection()
		print(colored(name +""": installing...""","green"))
		print(colored("""it will take some time """+ idname,"green")) 
		os.system("pkg install -y tigervnc x11-repo fluxbox geany openbox pypanel geany xfce4-session")
		print(colored(idname +""" would you like to setup vncserver""","green"))
		say1 = input("y/n > ")
		if say1 == "y" or say1 == "Y" or say1 == "yes":
			setup_vnc()
			print(colored(name +""": now you can start vncserver with using this command\n vncserver :1\n or\n you can ask me "start vnc","start vncserver","start gui" any time""","green"))
		elif say1 == "n" or say1 == "N" or say1 == "no":
			print(colored("""\n"""+ name +""": if you dont setup a vnc then\nthen you need to setup vnc manually\nand in manually your rection like be like me""","green"))
			random.choice(confused_list)()
			#its okay emotion
			print(colored("""daijobu """+ idname +""" you can ask me any time if you wanna setup vnc""","green"))
			print(colored("""like "setup vnc", "setup vncserver" ""","green"))
	elif say == "n" or say == "N" or say == "no":
		print(colored("""ok i am cancelling this process""","green"))
	else:
		print(colored("""(ano ne)i think you type wrong word you need to type\n "y" stands for install\n "n" stands for cancel\n now you get it """+ idname,"green"))		
def setup_vnc():
	print(colored(name +""": ok """+ idname +""" now You need to enter pass for VNC\n after that it will ask you question there you need to say\ny/n i am not explaining you whats that mean but\nif you pro """+ idname +""" you will get it quickly\n if you dont get it anything. just type "y" and hit enter\n then type same password again 2 times""","green"))
	os.system("vncserver")
	os.system("rm -rf /data/data/com.termux/files/home/.vnc/xstartup")
	os.system("cp tools/xstartup /data/data/com.termux/files/home/.vnc/")
	os.system("chmod +x /data/data/com.termux/files/home/.vnc/xstartup")
	print(colored("""\n"""+ name +""": now """+ idname +""" go to vnc application add new connection""","green"))
	print(colored("""ip adress " localhost::5901 " and gave name what ever you like it\nthen connect and enter same password that you entered in terminal\nwhen your setuping vncserver""","green"))
	print(colored("""now you can start vncserver with using this command\nvncserver :1\n or\nyou can use me "start vnc","start vncserver","start gui" any time""","green"))

def start_vnc():
	print(colored(name+""": ok """+idname,"green"))
	os.system("vncserver :1")
	
def stop_vnc():
	os.system("vncserver -kill :1")



#Help Section
def which_help():
	print(colored("""which help do you wanted ? """+idname,"green"))
	print(colored("""
	1. My Manual (how to use me)
	2. other help""","green"))
	say = input("which > ")
	if say == "1" or say == "your manual" or say == "manual" or say == "how to use you":
		help_section()
	else:
		print(colored(""" ""","green"))
	
def help_section():
	print(colored("""
	=========================================""","white"),colored("""
	            AI CONFIG COMMANDS			 ""","green"),colored("""
	=========================================""","white"),colored("""
	change your name -: for changing ai name ""","green"),colored("""
	
	=========================================""","white"),colored("""
	      USER/YOUR DATA CONFIG COMMANDS     ""","green"),colored("""
	=========================================""","white"),colored("""
	change my name -: for changing your name
	change my age  -: for changing your age  ""","green"),colored("""
	
	=========================================""","white"),colored("""
	              BASIC COMMANDS			 ""","green"),colored("""
	=========================================""","white"),colored("""
	whar is time -: for knowing current time
	what is date -: for knowing current date
	setup vnc    -: for setuping vnc/GUI
	start vnc    -: for start vnc/GUI server
	stop vnc     -: for stop vnc/GUI server
	device information-: it will show your 
	                     device detail
	flash light  -: for turn on and off flash 
	                light
	capture photo-: for capture photo from
	                back/front without opening
	                camera
	battery status-:for knowing your battery
	                status
	text to speech-:a.. its just like game 
	                type whatever you want. it
	                will convert into speach
	                (usefull for teasing your
	                friend ;)""","green"),colored("""
	
	=========================================
	      PACKAGE INSTALLATION COMMANDS      ""","green"),colored("""       
	=========================================""","white"),colored("""
	
	install vnc  -: for installing vnc/GUI
	install metasploit-:for installing 
	                    metasploit           
	update pacakges-: for updating termux imp.
	                  packages               ""","green"),colored(""" 
	=========================================
	               STASH COMMANDS            ""","green"),colored("""       
	=========================================""","white"),colored("""
	For these command require intornet connec
	tion                                     
	                                         ""","red"),colored("""
	play songs      -: it will play some songs
	play lofi music -: it will play some lofi
	                   musics
	play old songs  -: it will play some old
	                   songs
	play racing songs-:it will play racing songs
	play emotional songs-:it will play some 
	                    emotional/sad songs
	play good songs -: it will play some good
	                   songs
	play rage songs -: songs with some destruction
	play party songs-: it will play some party
	                   songs                 ""","green"),colored("""
	=========================================""","white"),colored("""
	some offline stash commands              ""","magenta"),colored("""
	
	recommend me some anime_• it will start anime
	recommend me anime      • server picked by aniket""","green"),colored("""
	=========================================""","white"),colored("""
	                       and some chit chat""","cyan"))
				
