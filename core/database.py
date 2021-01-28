import sqlite3

#function
def create_connection():
	
	connection = sqlite3.connect("core/memory.db")
	return connection

def printslow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)
	
#questions and answer table	
def get_questions_and_answers():
	
	con = create_connection()
	cur = con.cursor()
	
	cur.execute("SELECT * FROM questionsandanswers")
	
	return cur.fetchall()
	
def insert_questions_and_answers(questions, answers):
	con = create_connection()
	cur = con.cursor()
	#insert into table value question and answers
	query = "INSERT INTO questionsandanswers values('"+questions+"', '"+answers+"')"
	cur.execute(query)
	con.commit()


def get_answers_from_memory(questions):
	rows = get_questions_and_answers()
	answers = ""
	for row in rows:
		if row[0].lower() in questions.lower():
			answers = row[1]
			break
	return answers
	
	
#Chat System Table
def get_chat_system():
	
	con = create_connection()
	cur = con.cursor()
	
	cur.execute("SELECT * FROM ChatSystem")
	
	return cur.fetchall()
	
def get_reply_from_chatsystem(ask):
	rows = get_chat_system()
	reply = ""
	for row in rows:
		if row[0].lower() in ask.lower():
			reply = row[1]
			break
	return reply
	
#Basic Commands Table
def get_Basic_Commands():
	
	con = create_connection()
	cur = con.cursor()
	
	cur.execute("SELECT * FROM BasicCommands")
	
	return cur.fetchall()
	
def get_reply_from_Basic_Commands(QBasic):
	rows = get_Basic_Commands()
	ABasic = ""
	for row in rows:
		if row[0].lower() in QBasic.lower():
			ABasic = row[1]
			break
	return ABasic
	
#memory Table
def get_memory():
	
	con = create_connection()
	cur = con.cursor()
	
	cur.execute("SELECT * FROM memory")
	
	return cur.fetchall()
	
def get_name():
	con = create_connection()
	cur = con.cursor()
	#insert into table value question and answers
	query = "select value from memory where name ='assistant_name'"
	cur.execute(query)
	return cur.fetchall()[0][0]
	
def get_age():
	con = create_connection()
	cur = con.cursor()
	#insert into table value question and answers
	query = "select value from memory where name ='age'"
	cur.execute(query)
	return cur.fetchall()[0][0]
	
def get_developers():
	con = create_connection()
	cur = con.cursor()
	#insert into table value question and answers
	query = "select value from memory where name ='developers'"
	cur.execute(query)
	return cur.fetchall()[0][0]

def get_address():
	con = create_connection()
	cur = con.cursor()
	#insert into table value question and answers
	query = "select value from memory where name ='address'"
	cur.execute(query)
	return cur.fetchall()[0][0]
	
def get_gender():
	con = create_connection()
	cur = con.cursor()
	#insert into table value question and answers
	query = "select value from memory where name ='Gender'"
	cur.execute(query)
	return cur.fetchall()[0][0]

def get_uname():
	con = create_connection()
	cur = con.cursor()
	#insert into table value question and answers
	query = "select value from memory where name ='user_name'"
	cur.execute(query)
	return cur.fetchall()[0][0]
	
def get_uage():
	con = create_connection()
	cur = con.cursor()
	#insert into table value question and answers
	query = "select value from memory where name ='user_age'"
	cur.execute(query)
	return cur.fetchall()[0][0]
	
	
def get_idname():
	con = create_connection()
	cur = con.cursor()
	#insert into table value question and answers
	query = "select value from memory where name ='id_name'"
	cur.execute(query)
	return cur.fetchall()[0][0]

def get_ai_version():
	con = create_connection()
	cur = con.cursor()
	#insert into table value question and answers
	query = "select value from memory where name ='version'"
	cur.execute(query)
	return cur.fetchall()[0][0]
	
def update_name(new_name):
	con = create_connection()
	cur = con.cursor()
	#insert into table value question and answers
	query = "update memory set value ='"+new_name+"'where name = 'assistant_name'"
	cur.execute(query)
	con.commit()
	
def update_uname(new_uname):
	con = create_connection()
	cur = con.cursor()
	#insert into table value question and answers
	query = "update memory set value ='"+new_uname+"'where name = 'user_name'"
	cur.execute(query)
	con.commit()
	
def update_uage(new_uage):
	con = create_connection()
	cur = con.cursor()
	#insert into table value question and answers
	query = "update memory set value ='"+new_uage+"'where name = 'user_age'"
	cur.execute(query)
	con.commit()

def update_idname(new_idname):
	con = create_connection()
	cur = con.cursor()
	#insert into table value question and answers
	query = "update memory set value ='"+new_idname+"'where name = 'id_name'"
	cur.execute(query)
	con.commit()
