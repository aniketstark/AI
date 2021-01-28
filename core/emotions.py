import os
import sys
import sqlite3
import random
import socket
from termcolor import colored
from core.ai_detail import *
from core.cmd_execute import *


#Function
def create_connection():
	
	connection = sqlite3.connect("core/memory.db")
	return connection



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
        
#Emotion Natural Table
def get_NaturalEmotion():
	
	con = create_connection()
	cur = con.cursor()
	
	cur.execute("SELECT * FROM NaturalEmotion")
	
	return cur.fetchall()
	
def get_NReply(Natural):
	rows = get_NaturalEmotion()
	NReply = ""
	for row in rows:
		if row[0].lower() in Natural.lower():
			NReply = row[1]
			break
	return NReply
	

#Emotion-Happy Table	
def get_HappyEmotion():
	
	con = create_connection()
	cur = con.cursor()
	
	cur.execute("SELECT * FROM HappyEmotion")
	
	return cur.fetchall()
	
def get_HReply(Happy):
	rows = get_HappyEmotion()
	HReply = ""
	for row in rows:
		if row[0].lower() in Happy.lower():
			HReply = row[1]
			break
	return HReply
	
#Emotion-Sad Table
def get_SadEmotion():
	
	con = create_connection()
	cur = con.cursor()
	
	cur.execute("SELECT * FROM SadEmotion")
	
	return cur.fetchall()
	
def get_SReply(Sad):
	rows = get_SadEmotion()
	SReply = ""
	for row in rows:
		if row[0].lower() in Sad.lower():
			SReply = row[1]
			break
	return SReply
	
#Emotion-Angry Table
def get_AngryEmotion():
	
	con = create_connection()
	cur = con.cursor()
	
	cur.execute("SELECT * FROM AngryEmotion")
	
	return cur.fetchall()
	
def get_AReply(Angry):
	rows = get_AngryEmotion()
	AReply = ""
	for row in rows:
		if row[0].lower() in Angry.lower():
			AReply = row[1]
			break
	return AReply

#Adult-Section
def get_AdultSection():
	
	con = create_connection()
	cur = con.cursor()
	
	cur.execute("SELECT * FROM adult_section")
	
	return cur.fetchall()
	
def get_adult_a(adult_q):
	rows = get_AdultSection()
	adult_a = ""
	for row in rows:
		if row[0].lower() in adult_q.lower():
			adult_a = row[1]
			break
	return adult_a


#Natural Emotion

def hi1():
	os.system("termux-open assets/natural/hi/yo.mp4")
hi_list = [hi1]


def confused_list1():
	os.system("termux-open assets/natural/confuse/stuck_error404.mp4")	
confused_list = [confused_list1]

def internet_list1():
	os.system("termux-open assets/natural/internet_connection/connected/connected_internet1.mp4")
internet_list = [internet_list1]

def no_internet_list1():
	os.system("termux-open assets/natural/internet_connection/not_connected/no_internet1.mp4")
def no_internet_list2():
	os.system("termux-open assets/natural/internet_connection/not_connected/no_internet2.mp4")
def no_internet_list3():
	os.system("termux-open assets/natural/internet_connection/not_connected/no_internet3.mp4")
no_internet_list = [no_internet_list1,no_internet_list2,no_internet_list3]	

def my_songs():
	os.system("mpv https://youtube.com/playlist?list=PLFMaLUvJXXWz9459VkjNw9Ur6UEeN8Xrd")

def old_songs():
	os.system("mpv https://youtube.com/playlist?list=PLFMaLUvJXXWxUtXX-HHrNVWNm0ACXOp4f")
	
def lofi_songs():
	os.system("mpv https://youtube.com/playlist?list=PLFMaLUvJXXWwsVZiJI10X6PwjpS97oMU4")
	
def anime_songs():
	os.system("https://youtube.com/playlist?list=PLFMaLUvJXXWxALIIKYhWLsIlVAh9-0eFT")
	
	
#Happy Emotion
def good_day_list1():
	os.system("termux-open assets/happy/goodday/goodday.mp4")
	
good_day_list = [good_day_list1]

def party_songs():
	os.system("mpv https://youtube.com/playlist?list=PLFMaLUvJXXWxcphwePpOibVwEhJVQ8CXn")
	
def good_songs():
	netcheck()
	os.system("mpv https://youtube.com/playlist?list=PLFMaLUvJXXWwfUPccKb3awJYY1c_hRNes")
	
def recommend_good_things1():
	print(colored("""can i play some good songs for you""","green"))
	good1 = input("y/n >  ")
	if good1 == "y" or good1 == "Y" or good1 == "yes":
		good_songs()
	elif good1 == "n" or good1 == "N" or good1 == "no":
		recommend_good_things2()
		
def recommend_good_things2():
	print(colored(idname+""" can i show some animes that picked by my dev. Aniket""","green"))
	good2 = input("y/n >  ")
	if good2 == "y" or good2 == "Y" or good2 == "yes":
		anime_server()
	elif good2 == "n" or good2 == "N" or good2 == "no":
		print(colored("""ok desu""","green"))
		
def good_day():
	random.choice(good_day_list)()
	print(colored("""looks like today is your lucky day """+ str(idname),"green"))
	recommend_good_things1()
	
	



#Sad Emotion
def sorry_list1():
	os.system("termux-open assets/sad/sorry/sorry.mp4")
def sorry_list2():
	os.system("termux-open assets/sad/sorry/sorry1.mp4")
def sorry_list3():
	os.system("termux-open assets/sad/sorry/sorry2.mp4")
	
sorry_list = [sorry_list1, sorry_list2, sorry_list3]

def still_learning1():
	os.system("termux-open assets/natural/still_learning/still_learning.mp4")
	
still_learning = [still_learning1]

def sad_songs():
	os.system("mpv https://youtube.com/playlist?list=PLFMaLUvJXXWzq1jPESdmtCH_3iYFVQekA")
	
def sad_day():
	print(colored(name+""": what happend """+idname+""" looks like you too much sad today""","blue"))
	

#Angry Emotion
def racing_songs():
	os.system("mpv https://youtube.com/playlist?list=PLFMaLUvJXXWyFGo0b83s6H7aCwroIa7xn")

def rage_songs():
	os.system("mpv https://youtube.com/playlist?list=PLFMaLUvJXXWzyuvp52_uK0kQeUF4fNO0A")

#Adult Emotion
def warning1():
	os.system("termux-open assets/shinderu.mp4")
warning = [warning1]

####Server Section
def anime_server():
	print(colored(name+""": ok """+idname,"green"))
	print(colored("""open this link in browser""","blue"),colored(""":""","red"),colored(""" http://localhost:6969""","green"))
	print(colored("""ctrl + c for stop server""","green"))
	os.system("termux-open http://localhost:6969")
	os.system("php -S localhost:6969 -t assets/Secret")
