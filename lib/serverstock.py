import pymysql
import sqlite3

class ServerInfo:
	"""Get and write server info on database"""
	def __init__(self,type,connection):
		"""
		type : "sqlite3" or mysql"
		connection : dic{"host":host,"database":database,"user":user,"mdp":mdp}
		"""
		self.type = type
		self.host = connection['host']
		self.database = connection['database']
		self.user = connection['user']
		self.mdp = connection['mdp']
		self.load_ram = 0
		self.ram=None

		INITIAL_SCHEMA = """CREATE TABLE IF NOT EXISTS server(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,discord_server_id TEXT,NSFW TEXT,last_music_play TEXT)"""
		if self.type == "sqlite3":
			self.db = sqlite3.connect(self.database+".db")
			self.cursor = self.db.cursor()
			self.cursor.execute(INITIAL_SCHEMA)
			self.db.commit()
		if self.type == "mysql":
			self.db = pymysql.connect(host=self.host,
							 user=self.user,
							 password=self.mdp,
							 db=self.database,
							 charset='utf8mb4',
							 cursorclass=pymysql.cursors.DictCursor)
			self.cursor = self.db.cursor()
			self.cursor.execute(INITIAL_SCHEMA)
			self.db.commit()

	def __str__(self):
		return "ServerInfo v 0.1"

	def convert_list_to_str(self,list):
		ret = ""
		for ele in list:
			ret= ret+str(ele)+"#@#"
		return ret

	def convert_str_to_list(self,ttr):
		ret = ttr.split("#@#")
		return ret 

	def add_server(self,id,NSFW=[],music=[]):
		REQ = """INSERT INTO `server`(`discord_server_id`, `NSFW`, `last_music_play`) VALUES ("{0}", "{1}", "{2}")""".format(
			id,
			self.convert_list_to_str(NSFW),
			self.convert_list_to_str(music))
		# REQ = """INSERT INTO `server`(`discord_server_id`, `NSFW`, `last_music_play`) VALUES ("1234", "ele#@#rrr", "lo#@#la")"""
		self.cursor.execute(REQ)
		self.db.commit()
		print("REQUESTS ! me i m a serv adder")
		self.load_ram=1

	def add_NSFW(self,id,chan):
		lNSFW = self.get_serv(id)["NSFW"]
		lNSFW.remove("")
		lNSFW.append(chan)
		self.change_server(id,NSFW=lNSFW)
		self.load_ram=1
		return True

	def remove_NSFW(self,id,chan):
		try:
			lNSFW = self.get_serv(id)["NSFW"]
			lNSFW.remove("")
			lNSFW.remove(chan)
			self.change_server(id,NSFW=lNSFW)
			self.load_ram=1
			return True
		except:
			return False

	def ld_ram(self):
		self.ram=[]
		REQ = """SELECT * FROM `server`"""
		self.cursor.execute(REQ)
		print("REQUESTS !, we load new ram !")
		result = self.cursor.fetchall()
		for ele in result:
			self.ram.append({"id":int(ele[1]),"NSFW": self.convert_str_to_list(ele[2]),"music": self.convert_str_to_list(ele[3])})
		self.load_ram = 0

	def get_serv(self,id):
		"""WARNING : ALL INFO IS REGISTER IN STR, PLEASE CONVERT !"""
		if self.ram == None:
			self.ld_ram()
		if self.load_ram== 1:
			self.ld_ram()
		#REQ = """SELECT * FROM `server` WHERE `discord_server_id`={0}"""
		for el in self.ram:
			if el["id"] == int(id):
				return el

	def change_server(self,id,NSFW=None,music=None):
		"""Use :
		the id is the id of serv what change
		Add NSFW=[...]
		Or/and music=[...]
		to change it.
		"""
		if NSFW==None and music==None:
			return False
		if NSFW!=None:
			if music!=None:
				REQ ="""UPDATE `server` SET `NSFW` = "{0}",`last_music_play`="{1}" WHERE `discord_server_id`="{2}" """.format(self.convert_list_to_str(NSFW),self.convert_list_to_str(music),id)
			else:
				REQ ="""UPDATE `server` SET `NSFW` = "{0}" WHERE `discord_server_id`="{1}" """.format(self.convert_list_to_str(NSFW),id)
		if music!=None:
			if NSFW ==None:
				REQ ="""UPDATE `server` SET `last_music_play`="{0}" WHERE `discord_server_id`="{1}" """.format(self.convert_list_to_str(music),id)
			else:
				REQ ="""UPDATE `server` SET `NSFW` = "{0}",`last_music_play`="{1}" WHERE `discord_server_id`="{2}" """.format(self.convert_list_to_str(NSFW),self.convert_list_to_str(music),id)

		self.cursor.execute(REQ)
		print("REQUESTS !")
		self.db.commit()










