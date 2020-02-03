#!/usr/bin/env python
"""Hello"""
import sqlite3
import pymysql
import ujson as json
import copy
"""
DB = sqlite3.connect("db.sqlite3")
CURSOR = DB.cursor()
"""

class SuperStore:
    """Store in ram server options"""
    def __init__(self, db, serv_id_list):
        """Load db and store in ram"""
        self.db_creds = db
        self.connect()
        self.ram = {}
        self.serv_id_list = serv_id_list
        self.load_ram(use_id_list=False)
        
    def connect(self):
        self.db = pymysql.connect(host=self.db_creds['host'],user=self.db_creds['user'],password=self.db_creds['password'],db=self.db_creds['db'],charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.db.cursor()

    def composer_sqlite(self, tupler):
        sender = {
            'id': tupler[3],
            'customcommand' : tupler[5],
            'customtext' : tupler[6],
            'nsfw' : tupler[7],
            'ashprotector' : tupler[8],
            'music_voteskip' : tupler[9],
            'music_modernplayer' : tupler[10],
            'say' : tupler[11],
            'prefix' : tupler[13],
            'language' : tupler[12],
            'options' : tupler[13]}
        return sender

    def composer_mysql(self, tupler):
        sender = {
            'id': tupler['serverId'],
            'customcommand' : json.loads(tupler['customcommand']),
            'customtext' : json.loads(tupler['customtext']),
            'nsfw' : tupler['nsfw'],
            'ashprotector' : tupler['ashprotector'],
            'music_voteskip' : tupler['music_voteskip'],
            #'music_modernplayer' : tupler['music_modernplayer'],
            'say' : tupler['say'],
            'prefix' : tupler['prefix'],
            'language' : tupler['language'],
            'options' : tupler['options']}
        return sender



    def load_ram(self, use_id_list=True):
        self.ram = {}
        self.connect()
        REQ = """SELECT * FROM `discordaccount_guild`,`guildoption_settings` WHERE discordaccount_guild.id = guildoption_settings.guild_id"""
        self.cursor.execute(REQ)
        result = self.cursor.fetchall()
        if use_id_list:
            ider = copy.copy(self.serv_id_list)
            for server in result:
                if str(server['serverId']) in ider:
                    self.ram[server['serverId']] = self.composer_mysql(server)
                    ider.remove(str(server['serverId']))
        else:
           for server in result:
               self.ram[server['serverId']] = self.composer_mysql(server)

    def get_server(self, id):
        if str(id) in self.ram.keys():
            return self.ram[str(id)]
        else:
            the_return = {'id': str(id), 'customcommand': [], 'customtext': [], 'nsfw': 1, 'ashprotector': 0, 'music_voteskip': 0, 'music_modernplayer': 1, 'say': 0, 'prefix': '!!', 'language': 'en'}
            return the_return

    def update_server(self, id, sender):
        if str(id) in self.ram.keys():
            if sender != self.ram[str(id)]:
                self.ram[str(id)] = sender
                return True
            else:
                return False

        else:
            self.ram[str(id)] = sender
            return True





