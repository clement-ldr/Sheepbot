#!/usr/bin/python3.6

#Loading time !

import os
import io
__path__= [os.path.dirname(os.path.abspath(__file__))]
import re
import sys
import socket
import ast
try:
    sys.path.append('../')
except:
    pass
import time
import pydeepl
from PIL import Image, ImageDraw, ImageFont
import glob
import functools
import json
import enum
import string
import requests
import random
import asyncio
import discord
import logging
import wikipedia
import wolframalpha
#import subprocess
#import credentials
import datetime
from datetime import datetime
import pymysql.cursors
import pymysql
import urllib
import giphypop
import inspect
import configparser
import aiohttp
import urllib.parse
import urllib.request
import youtube_dl
import pyspeedtest
import uuid
import copy
from imgurpython import ImgurClient
from discord import opus
from random import randint, choice
#from cleverbot import Cleverbot
from lxml import etree
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
from array import array
from bs4 import BeautifulSoup
from .lib.P4 import Board
from .lib.count import count
from youtube_dl import YoutubeDL
from urllib.parse import urlencode, urlparse, parse_qs
from lxml.html import fromstring
from requests import get
from lxml import html
from logging.handlers import RotatingFileHandler
from urllib.request import Request, urlopen
import textwrap
from .lib.DbInterface import SuperStore
from .lib.serverstock import ServerInfo
import sqlite3
import ujson as therealjson
from collections import deque
import difflib
import psutil

#Finish to load, start to create object utilities



try:
    import uvloop
except ImportError:
    print('uvloop not loaded')
    logging.warning('uvloop not loaded')
    pass
else:
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

loop = asyncio.get_event_loop()
permi = {}

permi['NSFW']= ServerInfo("sqlite3",{'host':None,'database':'nsfw','user':'','mdp':''})

url_re = re.compile(r'(https?://[^\s]+)')
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


try:
    imgur_client = ImgurClient("", "")
except:
    pass


##########Soundbox

soundB = []
for i in os.listdir('./sounds'):
    if i.endswith('.opus'):
        soundB.append(i.replace('.opus',''))

##########/soundbox




cfg = configparser.ConfigParser()
cfg.read('config.ini')
TOKEN = cfg.get('General','token')
VERSION = cfg.get('General','version')
DESC = cfg.get('General','description')

MSG_rcvd = 0

#SHARD
try:
    Scount = int(sys.argv[2])
    Sid = int(sys.argv[1])
except:
    print('whoops')
    logging.warning('shard number error')
    Scount = 1
    Sid = 0
#/SHARD


wolfbot = wolframalpha.Client('')
#LOGS
try:
    logger = logging.getLogger()
    logger.setLevel(logging.WARNING)
    formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s \n')
    file_handler = RotatingFileHandler('log/activity'+str(Sid+1)+'.log', 'a', 100000, 1)
    file_handler.setLevel(logging.WARNING)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
except:
    pass
#/LOGS
OPUS_LIBS = ['libopus-0.dll', 'libopus.so.0', 'libopus.0.dylib', 'libopus.so.1']
cb = None
Pause = []
ytdl = YoutubeDL()
CBState = {}
tStop = {}
last_meme = []


spdtobj=pyspeedtest.SpeedTest()



morseAlphabet ={"A" : ".-","B" : "-...","C" : "-.-.","D" : "-..","E" : ".","F" : "..-.","G" : "--.","H" : "....","I" : "..","J" : ".---","K" : "-.-","L" : ".-..","M" : "--","N" : "-.","O" : "---","P" : ".--.","Q" : "--.-","R" : ".-.","S" : "...","T" : "-","U" : "..-","V" : "...-","W" : ".--","X" : "-..-","Y" : "-.--","Z" : "--.."," " : "/"}





#### FFMPEG NB


def proc_name(name):
    "Return a list of processes matching 'name'."
    ls = []
    for p in psutil.process_iter(attrs=['name']):
        if name in p.info['name']:
            ls.append(p)
    return ls


def is_ok(ide):
    if len(proc_name('ffmpeg'))<40:
        return True

    with open('prem.txt','r') as f:
        f = f.readlines()
        if ide in f:
            return True
    return False


####\FFMPG






CLVRIO_USR = ''
CLVRIO_TOKEN = ''
CLVRIO_DATA = {'user':CLVRIO_USR,'key':CLVRIO_TOKEN}



#RDOM_SONG
try:
    RDOM_SONGS = open("songs.txt",'r').read()
    RDOM_SONGS = RDOM_SONGS.split('\n')


    billboard = eval(RDOM_SONGS[0])
    most_viewed = eval(RDOM_SONGS[1])
    latest = eval(RDOM_SONGS[2])
    popular = eval(RDOM_SONGS[3])
    week_top = eval(RDOM_SONGS[4])
except Exception as e:
    print(e)
    logging.warning(str(e))
#/RDOM_SONG



#we load Opus for Voice
def load_opus_lib(name=OPUS_LIBS):
    if opus.is_loaded():
        return True

    for opus_lib in opus_libs:
        try:
            opus.load_opus(opus_lib)
            return
        except OSError:
            pass


    if not discord.opus.is_loaded():
        for opuss in opus_libs:
            try:
                discord.opus.load_opus(opuss)
            except:
                logging.warning('Opus non charger!')
#Utililities for command
def is_me(m):
    return m.author == bot.user
#The json parser



class fmrt(string.Formatter):
    def __init__(self, default='{{{0}}}'):
        self.default=default

    def get_value(self, key, args, kwds):
        if isinstance(key, str):
            return kwds.get(key, self.default.format(key))
        else:
            Formatter.get_value(key, args, kwds)

fm = fmrt()


def json(url):
    try:
        response = urlopen(url)
        data = response.read().decode("utf-8")
        return json.loads(data)
    except Exception as e:
        logging.warning(str(e))
        html = requests.get(url).text
        return json.loads(html)

def ping(lol):
    pong = [spdtobj.ping(),spdtobj.download(),spdtobj.upload()]
    return pong

def cowsay(str, length=40):
    return build_bubble(str, length) + build_cow()

def build_cow():
    return """
         \   ^__^
          \  (oo)\_______
             (__)\       )\/\\
                 ||----w |
                 ||     ||
    """

def build_bubble(str, length=40):
    bubble = []
    lines = normalize_text(str, length)
    bordersize = len(lines[0])
    bubble.append("  " + "_" * bordersize)
    for index, line in enumerate(lines):
        border = get_border(lines, index)
        bubble.append("%s %s %s" % (border[0], line, border[1]))
        bubble.append("  " + "-" * bordersize)
    return "\n".join(bubble)

def normalize_text(str, length):
    lines  = textwrap.wrap(str, length)
    maxlen = len(max(lines, key=len))
    return [ line.ljust(maxlen) for line in lines ]

def get_border(lines, index):
    if len(lines) < 2:
        return [ "<", ">" ]
    elif index == 0:
        return [ "/", "\\" ]
    elif index == len(lines) - 1:
        return [ "\\", "/" ]
    else:
        return [ "|", "|" ]




mouths = [
    'v', 'ᴥ', 'ᗝ', 'Ѡ', 'ᗜ', 'Ꮂ', 'ᨓ', 'ᨎ', 'ヮ', '╭͜ʖ╮', ' ͟ل͜', ' ͜ʖ', ' ͟ʖ', ' ʖ̯', 'ω', ' ³', ' ε ', '﹏', '□', 'ل͜',
    '‿', '╭╮', '‿‿', '▾', '‸', 'Д', '∀', '!', '人', '.', 'ロ', '_', '෴', 'ꔢ', 'ѽ', 'ഌ', '⏠', '⏏', '⍊', '⍘', 'ツ', '益',
    '╭∩╮', 'Ĺ̯', '◡', ' ͜つ', '◞ ', 'ヘ'
]
eyes = [
    ('⌐■', '■'),
    (' ͠°', ' °'),
    ('⇀', '↼'),
    ('´• ', ' •`'),
    ('´', '`'),
    ('`', '´'),
    ('ó', 'ò'),
    ('ò', 'ó'),
    ('⸌', '⸍'),
    ('<', '>'),
    ('Ƹ̵̡', 'Ʒ'),
    ('ᗒ', 'ᗕ'),
    ('⟃', '⟄'),
    ('⪧', '⪦'),
    ('⪦', '⪧'),
    ('⪩', '⪨'),
    ('⪨', '⪩'),
    ('⪰', '⪯'),
    ('⫑', '⫒'),
    ('⨴', '⨵'),
    ('⩿', '⪀'),
    ('⩾', '⩽'),
    ('⩺', '⩹'),
    ('⩹', '⩺'),
    ('◥▶', '◀◤'),
    ('◍', '◎'),
    ('/͠-', ' ͝-\\'),
    ('⌣', '⌣”'),
    (' ͡⎚', ' ͡⎚'),
    '≋', '૦ઁ', '  ͯ', '  ͌', 'ꗞ', 'ꔸ', '꘠', 'ꖘ', '܍', 'ළ', '◉', '☉', '・', '▰', 'ᵔ', ' ﾟ', '□', '☼', '*', '`', '⚆', '⊜',
    '>', '❍', '￣', '─', '✿', '•', 'T', '^', 'ⱺ', '@', 'ȍ', '  ', '  ', 'x', '-', '$', 'Ȍ', 'ʘ', 'Ꝋ', '', '',
    '⸟', '๏', 'ⴲ', '■', ' ﾟ', '◕', '◔', '✧', '■', '♥', ' ͡°', '¬', ' º ', '⨶', '⨱', '⏓', '⏒', '⍜', '⍤', 'ᚖ', 'ᴗ', 'ಠ',
    'σ', '☯', 'の', '￢ ', 'э'
]
ears = [
    ('q', 'p'),
    ('ʢ', 'ʡ'),
    ('⸮', '?'),
    ('ʕ', 'ʔ'),
    ('ᖗ', 'ᖘ'),
    ('ᕦ', 'ᕥ'),
    ('ᕦ(', ')ᕥ'),
    ('ᕙ(', ')ᕗ'),
    ('ᘳ', 'ᘰ'),
    ('ᕮ', 'ᕭ'),
    ('ᕳ', 'ᕲ'),
    ('(', ')'),
    ('[', ']'),
    ('¯\\_', '_/¯'),
    ('୧', '୨'),
    ('୨', '୧'),
    ('⤜(', ')⤏'),
    ('☞', '☞'),
    ('(╭☞', ')╭☞'),
    ('ᑫ', 'ᑷ'),
    ('ᑴ', 'ᑷ'),
    ('ヽ(', ')ﾉ'),
    ('\\(', ')/'),
    ('乁(', ')ㄏ'),
    ('└[', ']┘'),
    ('(づ', ')づ'),
    ('(ง', ')ง'),
    ('⎝', '⎠'),
    ('ლ(', 'ლ)'),
    ('ᕕ(', ')ᕗ'),
    ('(∩', ')⊃━☆ﾟ.*'),
    ('【', '】'),
    ('﴾', '﴿'),
    ('(╯', '）╯︵ ┻━┻'),
    '|'
]


def lenny():
    mouth = random.choice(mouths)
    eyes_ = random.choice(eyes)
    ears_ = random.choice(ears)

    if isinstance(eyes_, tuple):
        left_eye, right_eye = eyes_
    else:
        left_eye = right_eye = eyes_

    if isinstance(ears_, tuple):
        left_ear, right_ear = ears_
    else:
        left_ear = right_ear = ears_

    face = '{0}{1}{2}{3}{4}'

    return face.format(left_ear, left_eye, mouth, right_eye, right_ear)





def zaldef(tex):
    ocur = 0
    zalgo = ['̀','็' ,'́', '̂', '̃', '̄', '̅', '̆', '̇', '̈', '̉', '̊', '̋', '̌', '̍', '̎', '̏', '̐', '̑', '̒', '̓', '̔', '̕', '̖', '̗', '̘', '̙', '̚', '̛', '̜', '̝', '̞', '̟', '̠', '̡', '̢', '̣', '̤', '̥', '̦', '̧', '̨', '̩', '̪', '̫', '̬', '̭', '̮', '̯', '̰', '̱', '̲', '̳', '̴', '̵', '̶', '̷', '̸', '̹', '̺', '̻', '̼', '̽', '̾', '̿', '̀', '́', '͂', '̓', '̈́', 'ͅ', '͆', '͇', '͈', '͉', '͊', '͋', '͌', '͍', '͎', '͏', '͐', '͑', '͒', '͓', '͔', '͕', '͖', '͗', '͘', '͙', '͚', '͛', '͜', '͝', '͞', '͟', '͠', '͡', '͢', 'ͣ', 'ͤ', 'ͥ', 'ͦ', 'ͧ', 'ͨ', 'ͩ', 'ͪ', 'ͫ', 'ͬ', 'ͭ', 'ͮ', 'ͯ', '҈', '҉']
    for zal in zalgo:
        ocur += tex.count(zal)
    if ocur*2 > len(tex):
        return True
    else:
        return False

#weird
def zalgo(text, intensity=10):
    zalgo_threshold = intensity
    zalgo_chars = [chr(i) for i in range(0x0300, 0x036F + 1)]
    zalgo_chars.extend([u'\u0488', u'\u0489'])
    source = text.upper()
    if not _is_narrow_build:
        source = _insert_randoms(source)
    zalgoized = []
    for letter in source:
        zalgoized.append(letter)
        zalgo_num = randint(0, zalgo_threshold) + 1
        for _ in range(zalgo_num):
            zalgoized.append(choice(zalgo_chars))
    response = choice(zalgo_chars).join(zalgoized)
    return response.encode('utf-8', 'ignore')


def _insert_randoms(text):
    random_extras = [chr(i) for i in range(0x1D023, 0x1D045 + 1)]
    newtext = []
    for char in text:
        newtext.append(char)
        if randint(1, 5) == 1:
            newtext.append(choice(random_extras))
    return u''.join(newtext)


def _is_narrow_build():
    try:
        chr(0x10000)
    except ValueError:
        return True
    return False

#Make meme
def valid(link,start=0):
    bcl = 1
    for i in link:
        bcl += 1
        if bcl > start:
            try:
                yo = None
                yo = urllib.request.Request(i, method="HEAD", headers={'User-Agent': 'Mozilla/5.0'})
                yo = urllib.request.urlopen(yo, timeout=5)
                if yo.code == 200:
                    return i,i
            except:
                pass
        else:
            pass


def mememaker(search='search',Words='add,some text',nb=0):
    if search.startswith('http'):
        search = search.replace(' ','')
        Words = Words.split(',')
        try:
            word2 = Words[1]
        except:
            word2 = ''
        memeurl = 'https://memegen.link/custom/'+Words[0]+'/'+word2+'.jpg?alt='+search+'?w=393&h=590'
        return memeurl,search
        
    search = search.replace(' ','%20')
    Words = Words.replace(' ','_')
    Ending = []
    url = 'https://www.google.fr/search?q='+search+'&num=100&espv=2&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjO3J618dDSAhVDPxoKHYhEC94Q_AUICCgB&biw=1280&bih=591#imgrc=_'
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    req = urllib.request.Request(url, headers = headers)
    resp = urllib.request.urlopen(req)
    respData = str(resp.read())
    bs = BeautifulSoup(respData, "lxml")
    possible_links = bs.find_all('div')
    for link in possible_links:
        if link.has_attr('class'):
            ref = link.get('class')
            if ref[0] == 'rg_meta':
                try:
                    data = eval(link.string)
                    Ending.append(data['ou'])
                except Exception as e:
                    logging.warning(str(e))
                    print('OUPS')
                    pass

    #meme url
    Ending = valid(Ending,nb)
    Words = Words.split(',')
    try:
        word2 = Words[1]
    except:
        word2 = ''
    memeurl = 'https://memegen.link/custom/'+Words[0]+'/'+word2+'.jpg?alt='+Ending[0]+'?w=393&h=590'
    return memeurl,Ending[1]

#Decode a playlist

def playlist(url):
    playlist = []
    nb=0
    info = ytdl.extract_info(url, download=False)
    ytinfo = { 'creator', 'duration', 'description', 'dislike_count','thumbnails','like_count','age_limit','id','is_live','view_count','uploader','webpage_url','playlist','title','thumbnail','upload_date','categories','tags','entries' }
    info = { key:value for key,value in info.items() if key in ytinfo }
    for items in info['entries']:
        if items:
            try:
                ytinfo = { 'creator', 'duration', 'description', 'dislike_count','thumbnails','like_count','age_limit','id','is_live','view_count','uploader','webpage_url','playlist','title','thumbnail','upload_date','categories','tags','entries' }
                items = { key:value for key,value in items.items() if key in ytinfo }
            except:
                pass
            try:
                playlist.append(items['webpage_url'])
                nb +=1
                if nb >= 5:
                    return playlist
            except Exception as e:
                logging.warning(str(e))
                print('§FAIL§')
    return playlist

#Shortcut for check if the channel is NSFW
    
def is_permi(typo,serv_id,chan_id):
    if permi[typo].get_serv(serv_id) !=None:
        lNSFW = permi[typo].get_serv(serv_id)['NSFW']
        if chan_id in lNSFW:
            return True
        else:
            return False
    else:
        return False



#Translate using DeepL

def translate(args):
    args = list(args)
    ln = args[0].upper()
    args.remove(ln)
    Final = pydeepl.translate(' '.join(args), ln, from_lang="auto")
    #print(Final)
    return Final



#Search a image oh GImage

def img(search,safe=False):
    if safe:
         url = 'https://www.google.fr/search?q='+search+'&client=opera&hs=cTQ&source=lnms&tbm=isch&sa=X&ved=0ahUKEwig3LOx4PzKAhWGFywKHZyZAAgQ_AUIBygB&biw=1920&bih=982'+'&safe=active'
    else:
         url = 'https://www.google.fr/search?q='+search+'&client=opera&hs=cTQ&source=lnms&tbm=isch&sa=X&ved=0ahUKEwig3LOx4PzKAhWGFywKHZyZAAgQ_AUIBygB&biw=1920&bih=982'
    fin = []
    page = requests.get(url,headers={'User-Agent' : "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"}).text
    Ending =[]
    bs = BeautifulSoup(page, "lxml")
    possible_links = bs.find_all('div')
    for link in possible_links:
        if link.has_attr('class'):
            ref = link.get('class')
            if ref[0] == 'rg_meta':
                try:
                    data = ast.literal_eval(link.string)
                    Ending.append(data['ou'])
                except:
                    pass


    return Ending
    


#Search Wikipedia post

def wiki(kik):
    wiki = wikipedia.summary(kik, sentences=1)
    return str(wiki)

#Search a gif

def gif(search):
    r = requests.get("https://api.giphy.com/v1/gifs/random?tag=funny&api_key="+KEY+"&limit=1")
    return str(therealjson.loads(r.text)['data']['image_url'])



#Function to cut str in * lenght

def chunkstring(string, length):
    return (string[0+i:length+i] for i in range(0, len(string), length))






#Go Music  !

#======================================================
#==============M  U  S  I  C===========================
#======================================================

class Music:
    def __init__(self, bot):
        self.bot = bot
        self.queue = {}
        self.is_play = {}
        self.autoplay = {}
        self.loopqueue = {}
        self.volumeS = {}
        self.music = {}
        self.meming = {}
        self.queue_showing = {}
        self.play_next_song = {}
        self.song_histo = {}
        self.meme_over = {}






    def autoembed(self,state,mode="music",colaps=None):
        infi = discord.Embed()
        if mode =="music":
            infi.title = 'Now Playing :'
            infi.colour = random.randint(0, 0xFFFFFF)
            try:
                thum = state.url.replace('https://www.youtube.com/watch?v=','https://img.youtube.com/vi/')
                thumb = thum+'/hqdefault.jpg'
                infi.set_thumbnail(url=thumb)
            except:
                pass
            if state.title:
                infi.add_field(name='Title :', value=state.title)
            infi.add_field(name='duration :', value='{0[0]}m {0[1]}s'.format(divmod(int(state.duration), 60)))
            if state.is_live:
                infi.add_field(name='live :', value='True')
            if state.uploader:
                infi.add_field(name='author :', value=str(state.uploader))
            if state.views:
                infi.add_field(name='views :', value=str(state.views))
            if state.url:
                infi.add_field(name='url :', value=str(state.url))
            if not len(str(state.description)) > 300:
                infi.add_field(name='description : :', value=state.description)
            return infi
        if mode =="q":
            infi.title = 'Queue {0[0]} / {0[1]} :'.format(colaps)
            infi.colour = random.randint(0, 0xFFFFFF)
            try:
                thum = state["webpage_url"].replace('https://www.youtube.com/watch?v=','https://img.youtube.com/vi/')
                thumb = thum+'/hqdefault.jpg'
                infi.set_thumbnail(url=thumb)
            except:
                pass
            if state["title"]:
                infi.add_field(name='Title :', value=state["title"])
            infi.add_field(name='duration :', value='{0[0]}m {0[1]}s'.format(divmod(int(state["duration"]), 60)))
            if state["is_live"]:
                infi.add_field(name='live :', value='True')
            if state["uploader"]:
                infi.add_field(name='author :', value=str(state["uploader"]))
            if state["view_count"]:
                infi.add_field(name='views :', value=str(state["view_count"]))
            if state["webpage_url"]:
                infi.add_field(name='url :', value=str(state["webpage_url"]))
            if not len(str(state["description"])) > 300:
                infi.add_field(name='description : :', value=state["description"])
            return infi



    def toggle_next(self,srv):
        self.bot.loop.call_soon_threadsafe(self.play_next_song.get(srv).set)





    async def player(self,ctx):
        opts = {
        "format":"bestaudio/best",
        'default_search': 'auto',
        'no_warnings': True,
        'quiet': True,
        'nocheckcertificate': True,
        'ignoreerrors': True,
        'geo-bypass':True,
        'logtostderr': False,
        'restrictfilenames': True,
        'outtmpl': 'downloads/%(extractor)s-%(id)s-%(title)s-%(autonumber)s.%(ext)s'
        }
        state = self.bot.voice_client_in(ctx.message.server)
        if state:
            pass
        else:
            return
        try:
            self.play_next_song[ctx.message.server.id] = asyncio.Event()
            while True:
                self.play_next_song.get(ctx.message.server.id).clear()
                if self.is_play.get(ctx.message.server.id):
                    pass
                else:
                    return
                state = self.bot.voice_client_in(ctx.message.server)
                if state:
                    pass
                else:
                    return
                if not await self.is_active_voice(state):
                    return
                song = self.queue.get(ctx.message.server.id)
                if song:
                    if len(song) > 0:
                        self.music[ctx.message.server.id] = await state.create_ytdl_player(song[0].get('webpage_url'), ytdl_options=opts ,before_options='-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', after=lambda: self.toggle_next(ctx.message.server.id))
                        try:
                            self.music[ctx.message.server.id].volume = self.volumeS.get(ctx.message.server.id) or 0.4
                        except:
                            pass
                        self.music[ctx.message.server.id].start()
                        try:
                            await self.bot.send_message(ctx.message.channel, '<a:320:409020448806797312> Now playing `' + str(self.music[ctx.message.server.id].title)+'`'+','+'`length: {0[0]}m {0[1]}s`'.format(divmod(self.music[ctx.message.server.id].duration, 60)))
                        except:
                            await self.bot.send_message(ctx.message.channel, ':notes: Now playing `' + str(self.music[ctx.message.server.id].title)+'`'+','+'`length: {0[0]}m {0[1]}s`'.format(divmod(self.music[ctx.message.server.id].duration, 60)))
                        if self.loopqueue.get(ctx.message.server.id):
                            song.append(song[0])
                        song.remove(song[0])
                        self.queue[ctx.message.server.id] = song
                        await self.play_next_song.get(ctx.message.server.id).wait()
                        #self.music[ctx.message.server.id] = None
                    else:
                        if self.autoplay.get(ctx.message.server.id):
                            self.queue[ctx.message.server.id].append(self.find_next_sng(self.music[ctx.message.server.id].url,ctx))
                        else:
                            return
                else:
                    if self.autoplay.get(ctx.message.server.id):
                        sung = await self.find_next_sng(self.music[ctx.message.server.id].url,ctx)
                        sung = await self.extract_song(sung[0])
                        self.queue[ctx.message.server.id].append(sung[0])
                    else:
                        return

        except Exception as e:
            logging.warning(str(e))
            print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno))
            fmt = ':fire: An error occurred while processing this request: ```py\n{}: {}\n```'
            await self.bot.send_message(ctx.message.channel, fmt.format(type(e).__name__, e))



    async def playerz(self,ctx):
        try:
            if not is_ok(ctx.message.author.id):
                self.loopqueue[ctx.message.server.id] = False
                self.autoplay[ctx.message.server.id] = False
                self.music[ctx.message.server.id] = None
                self.is_play[ctx.message.server.id] = None
                await self.bot.send_message(ctx.message.channel, 'Too many users using the music right now, sorry :(')
                return
        except Exception as e:
            await self.bot.send_message(ctx.message.channel, str(e))
            print(e)
            
        self.is_play[ctx.message.server.id] = True
        #await self.player(ctx)
        try:
            await asyncio.wait_for(self.player(ctx),7200)
            self.is_play[ctx.message.server.id] = None
        except Exception as e:
            logging.warning(str(e))
            print(e)
            pass
        try:
            self.loopqueue[ctx.message.server.id] = False
            self.autoplay[ctx.message.server.id] = False
            self.music[ctx.message.server.id] = None
            #del self.music[ctx.message.server.id]
        except:
            pass
        #del self.music[ctx.message.server.id]
        self.is_play[ctx.message.server.id] = None


    async def find_next_sng(self,song,ctx):
        final = []
        conn = aiohttp.TCPConnector(
        family=socket.AF_INET,
        verify_ssl=False,
        )
        async with aiohttp.ClientSession(connector=conn) as session:
            async with session.get(song) as resp:
                html = await resp.text()
        bs = BeautifulSoup(html,'lxml')
        possible_links = bs.find_all('a')
        for link in possible_links:
            if link.has_attr('href'):
                ref = link.attrs['href']
                if '/watch?v=' in ref:
                    if not ref in final:
                        final.append(ref)

        to_return = []
        for i in final:
            daim = i
            if not 'www.youtube.com' in i:
                daim = "".join('https://www.youtube.com'+i)
            daim.replace(' ','')
            if not 'list' in daim:
                to_return.append(daim)
            else:
                pass
        nb = 0
        if self.song_histo.get(ctx.message.server.id):
            pass
        else:
            self.song_histo[ctx.message.server.id] = deque(maxlen=5)
        while True:
            if to_return[nb] not in self.song_histo.get(ctx.message.server.id):
                self.song_histo.get(ctx.message.server.id).appendleft(to_return[nb])
                break
            else:
                nb+=1
        return self.song_histo.get(ctx.message.server.id)

    async def is_active_voice(self,voice):
        try:
            if voice:
                for client in voice.channel.voice_members:
                    if client.bot:
                        pass
                    else:
                        return True
                return False
            else:
                return True
        except Exception as e:
            logging.warning(str(e))
            print(e)
            return True




    async def leave_unused_voices(self):
        for i in self.bot.servers:
            voice = self.bot.voice_client_in(i)
            if voice:
                if voice.is_connected():
                    if await self.is_active_voice(voice):
                        pass
                    else:
                        try:
                            self.is_play[i.id] = None
                            self.queue[i.id] = None
                            try:
                                self.music[i.id].stop()
                            except:
                                pass
                            try:
                                await voice.disconnect()
                            except:
                                pass
                            self.is_play[i.id] = None
                            self.music[i.id] = None
                            self.queue_showing[i.id] = None
                        except Exception as e:
                            logging.warning(str(e))
                            print('crotte')
        return True

    async def extract_song(self,song):
        opts = {
        "format":"bestaudio/best",
        'default_search': 'auto',
        'no_warnings': True,
        'quiet': True,
        'nocheckcertificate': True,
        'ignoreerrors': True,
        'geo-bypass':True,
        'logtostderr': False,
        'restrictfilenames': True,
        }
        playlist = False
        ytdl = youtube_dl.YoutubeDL(opts)
        func = functools.partial(ytdl.extract_info, song, download=False)
        song = await loop.run_in_executor(None, func)
        playl = song.get('entries')
        try:
            if playl:
                inf = []
                for info in playl:
                    ytinfo = { 'creator', 'duration', 'description', 'dislike_count','thumbnails','like_count','age_limit','id','is_live','view_count','uploader','webpage_url','playlist','title','thumbnail','upload_date','categories','tags','entries' }
                    inf.append({ key:value for key,value in info.items() if key in ytinfo })
                playl = inf
        except:
            pass
        
        if playl:
            song = playl
            playlist = True
        else:
            try:
                ytinfo = { 'creator', 'duration', 'description', 'dislike_count','thumbnails','like_count','age_limit','id','is_live','view_count','uploader','webpage_url','playlist','title','thumbnail','upload_date','categories','tags','entries' }
                song = { key:value for key,value in song.items() if key in ytinfo }
            except:
                pass
            playlist = False

        return song,playlist
                


    @commands.command(pass_context=True, no_pm=True,name='autoplay',aliases=['autop','autoP','Pauto','pauto'])
    async def autoP(self, ctx):
        """Auto queue some song when the queue is empty"""
        state = self.bot.voice_client_in(ctx.message.server)
        if state is None:
            await self.bot.say(':fire: Not playing any song, please add at least one song')
            return
        status = self.is_play.get(ctx.message.server.id)
        if status:
            if self.autoplay.get(ctx.message.server.id):
                self.autoplay[ctx.message.server.id] = False
                await self.bot.say('<:magicwand:410121666841149440> autoplay disabled')
                return
            self.autoplay[ctx.message.server.id] = True
            await self.bot.say('<:magicwand:410121666841149440> autoplay enabled')
        else:
            await self.bot.say(':fire: Not playing any song, please add at least one song')


    @commands.command(pass_context=True, no_pm=True,name='loopqueue',aliases=['lq','loopq','loop'])
    async def loopsong(self, ctx):
        """Auto loopqueue"""
        state = self.bot.voice_client_in(ctx.message.server)
        if state is None:
            await self.bot.say(':fire: Not playing anything.')
        status = self.is_play.get(ctx.message.server.id)
        if status:
            if self.loopqueue.get(ctx.message.server.id):
                self.loopqueue[ctx.message.server.id] = False
                return
            self.loopqueue[ctx.message.server.id] = True
            await self.bot.say('<:LQ:410161932344098826> loopqueue enabled')
        else:
            await self.bot.say(':fire: Not playing any song, please add at least one song')



    @commands.command(pass_context=True, no_pm=True,name='shuffle',aliases=['randomize'])
    async def shuffle(self, ctx):
        """shuffle music queue"""
        state = self.bot.voice_client_in(ctx.message.server)
        if state is None:
            await self.bot.say(':fire: Not playing anything.')
        status = self.is_play.get(ctx.message.server.id)
        if status:
            song = self.queue.get(ctx.message.server.id)
            if song and len(song)>1:
                random.shuffle(song)
                await self.bot.say('<:shuffle:409733638670778369> Shuffled !')
        else:
            await self.bot.say(':fire: Not playing any song, please add at least one song')



    def memO(self,srv):
        self.bot.loop.call_soon_threadsafe(self.meme_over.get(srv).set)



    @commands.command(pass_context=True, no_pm=True,aliases=['soundlist','soundboxlist','soundboxl','soundl'])
    async def soundbox_list(self, ctx):
        A = soundB
        B = A[:int(len(A)/2)]
        C = A[int(len(A)/2):]
        B=str(B).replace('[','').replace(']','').replace('\'','')
        C=str(C).replace('[','').replace(']','').replace('\'','')
        infi = discord.Embed()
        infi.colour = random.randint(0, 0xFFFFFF)
        infi.add_field(name='Memes :', value=B,inline=False)
        infi.set_footer(text='Note : You don\'t need to use the exact name')
        a = await self.bot.say(embed=infi)

        left = discord.Emoji(id=410121666249883651,server=289494695845953536)
        right = discord.Emoji(id=410121668263149568,server=289494695845953536)
        #await self.bot.add_reaction(a,':leftarrow:410121666249883651')
        await self.bot.add_reaction(a,':rightarrow:410121668263149568')
        await asyncio.sleep(0.2)
        try:
            while True:
                res = await self.bot.wait_for_reaction(message=a,timeout=20)
                if res:
                    if str(res.reaction.emoji) == '<:leftarrow:410121666249883651>':
                        infi.clear_fields()
                        infi.add_field(name='Memes :', value=B,inline=False)
                        await self.bot.remove_reaction(a, ':leftarrow:410121666249883651', self.bot.user)
                        try:
                            await self.bot.remove_reaction(a, res.reaction.emoji, res.user)
                        except Exception as e:
                            logging.warning(str(e))
                            print(e)
                        await self.bot.add_reaction(a,':rightarrow:410121668263149568')
                        infi.set_footer(text='1/2')
                        
                    if str(res.reaction.emoji) == '<:rightarrow:410121668263149568>':
                        infi.clear_fields()
                        infi.add_field(name='Memes :', value=C,inline=False)
                        await self.bot.remove_reaction(a, ':rightarrow:410121668263149568', self.bot.user)
                        try:
                            await self.bot.remove_reaction(a, res.reaction.emoji, res.user)
                        except Exception as e:
                            logging.warning(str(e))
                            print(e)
                        await self.bot.add_reaction(a,':leftarrow:410121666249883651')
                        infi.set_footer(text='2/2')
                    await self.bot.edit_message(a,embed=infi)
                else:
                    try:
                        await self.bot.remove_reaction(a, ':rightarrow:410121668263149568', self.bot.user)
                        await self.bot.remove_reaction(a, ':leftarrow:410121666249883651', self.bot.user)
                    except:
                        pass
                    return
        except Exception as e:
            logging.warning(str(e))
            print(e)
            pass
    




    @commands.command(pass_context=True, no_pm=True,aliases=['sb','audiomemes','soundb'])
    async def soundbox(self, ctx, *, song : str=None):
        try:
            timeR = time.time()
            self.meme_over[ctx.message.server.id] = asyncio.Event()
            if self.meming.get(ctx.message.server.id):
                self.meming[ctx.message.server.id].stop()

            if self.music.get(ctx.message.server.id):
                self.music.get(ctx.message.server.id).stop()
                await asyncio.sleep(0.1)

                
            self.is_play[ctx.message.server.id] = True
            state = self.bot.voice_client_in(ctx.message.server)
            if state is None:
                timeR = time.time()
                success = await self.bot.join_voice_channel(ctx.message.author.voice_channel)
                if ctx.message.author.voice_channel == None:
                    await self.bot.say(':fire: Your not in a voice channel')
                    return
                    
                #print(time.time() - timeR)
                if not success:
                    await self.bot.say(':fire: Error joining voice channel')
                    return
                state = self.bot.voice_client_in(ctx.message.server)

            if song:
                song = difflib.get_close_matches(song.replace(' ','').lower(), soundB, n=1, cutoff=0.2)
                if song:
                    song = song[0]
                    #print(song)
                else:
                    song = random.choice(soundB)
                    await self.bot.say(':anger: No sound found, I choosed `'+str(song)+'` for you.')
            else:
                song = random.choice(soundB)
                await self.bot.say(':game_die: No sound name given, I choosed `'+str(song)+'` for you.')
            self.meming[ctx.message.server.id] = state.create_ffmpeg_player('sounds/'+song+'.opus',after=lambda: self.memO(ctx.message.server.id))
            self.meming[ctx.message.server.id].start()
            #print(time.time() - timeR)
            await self.meme_over.get(ctx.message.server.id).wait()


            self.is_play[ctx.message.server.id] = None
            self.meme_over[ctx.message.server.id] = None
        except Exception as e:
            logging.warning(str(e))
            print(e)
            self.is_play[ctx.message.server.id] = None
            self.meme_over[ctx.message.server.id] = None
        self.is_play[ctx.message.server.id] = None
        self.meme_over[ctx.message.server.id] = None








    @commands.command(pass_context=True, no_pm=True,aliases=['*play*','add_song','p'])
    async def play(self, ctx, *, song : str=None):
        """Plays a song (youtube, soundcloud,etc...) .
        If there is a song currently in the queue, then it is
        queued until the next song is done playing.
        This command automatically searches from YouTube.
        The list of supported sites can be found here:
        https://rg3.github.io/youtube-dl/supportedsites.html
        """

        #await self.bot.say('disabled temporarly for technical reasons')
        #return
        if song == 'random':
            song = None
        
        
        try:
            await self.leave_unused_voices()
        except:
            pass
        state = self.bot.voice_client_in(ctx.message.server)
        if state == None:
            success = await ctx.invoke(self.join)
            if not success:
                await self.bot.say(':warning: error joinning voice channel')
                return
        if True:
            if song == None:
                try:
                    x = random.choice([week_top,week_top,week_top,most_viewed,latest,popular,popular,billboard,billboard])
                except Exception as e:
                    fmt = ':fire: An error occurred while processing this request: ```py\n{}: {}\n```'
                    await self.bot.send_message(ctx.message.channel, fmt.format(type(e).__name__, e))
                    logging.warning(str(e))
                    print(e)
                try:
                    if random.randint(0,2):
                        if random.randint(0,1):
                            x = random.choice(x[:int(len(x)/4)])
                        else:
                            x = random.choice(x[:int(len(x)/2)])
                    else:
                        x = random.choice(x)
                except Exception as e:
                    fmt = ':fire: An error occurred while processing this request: ```py\n{}: {}\n```'
                    await self.bot.send_message(ctx.message.channel, fmt.format(type(e).__name__, e))
                    logging.warning(str(e))
                    print(e)
                    x = random.choice(x) or x[0]
                song = x
                #await self.bot.say(':warning: Usage : !!play *song name or url*')
                #return
        else:
            if song == None:
                try:
                    if self.music.get(ctx.message.server.id).is_playing():
                        x = random.choice([week_top,week_top,week_top,most_viewed,latest,popular,popular,billboard,billboard])
                        try:
                            if random.randint(0,2):
                                if random.randint(0,1):
                                    x = random.choice(x[:int(len(x)/4)])
                                else:
                                    x = random.choice(x[:int(len(x)/2)])
                            else:
                                x = random.choice(x)
                        except Exception as e:
                            fmt = ':fire: An error occurred while processing this request: ```py\n{}: {}\n```'
                            await self.bot.send_message(ctx.message.channel, fmt.format(type(e).__name__, e))
                            print(e)
                            x = random.choice(x) or x[0]
                        song = x
                        #await self.bot.say(':warning: Usage : !!play *song name or url*')
                    self.music.get(ctx.message.server.id).resume()
                    #return
                except Exception as e:
                    logging.warning(str(e))
                    fmt = ':fire: An error occurred while processing this request: ```py\n{}: {}\n```'
                    await self.bot.send_message(ctx.message.channel, fmt.format(type(e).__name__, e))
                    pass
        try:
            if 'list' in song:
                await self.bot.say(':information_source: Extracting your playlist... it should take around 2-3s per songs')
            song = await self.extract_song(song)
            if '@everyone' in song or '@here' in song:
                return

        except Exception as e:
            logging.warning(str(e))
            fmt = ':fire: An error occurred while processing this request: ```py\n{}: {}\n```'
            await self.bot.send_message(ctx.message.channel, fmt.format(type(e).__name__, e))
            return
        playlist = song[1]
        song = song[0]
        if '@everyone' in song or '@here' in song:
            return
        if False:
            pass
        else:
            try:
                status = self.is_play.get(ctx.message.server.id)
                if status:
                    queue = self.queue.get(ctx.message.server.id)
                    if queue:
                        if playlist:
                            for snog in song:
                                queue.append(snog)
                        else:
                            queue.append(song)
                        self.queue[ctx.message.server.id] = queue
                        try:
                            dur = divmod(int(song[0]["duration"]), 60)
                            if '@everyone' in song[0]["title"] or '@here' in song[0]["title"]:
                                return
                            await self.bot.send_message(ctx.message.channel,'<:checked2:410164097481703445> Enqueued `'+song[0]["title"]+'` by `'+song[0]["uploader"]+'` ,`length: {0[0]}m {0[1]}s`'.format(dur))
                        except:
                            dur = divmod(int(song["duration"]), 60)
                            await self.bot.send_message(ctx.message.channel,'<:checked2:410164097481703445> Enqueued `'+song["title"]+'` by `'+song["uploader"]+'` ,`length: {0[0]}m {0[1]}s`'.format(dur))
                    else:
                        self.queue[ctx.message.server.id] = []
                        if playlist:
                            for im in song:
                                self.queue[ctx.message.server.id].append(im)
                        else:
                            self.queue[ctx.message.server.id].append(song)
                        try:
                            dur = divmod(int(song[0]["duration"]), 60)
                            await self.bot.send_message(ctx.message.channel,'<:checked2:410164097481703445> Enqueued `'+song[0]["title"]+'` by `'+song[0]["uploader"]+'` ,`length: {0[0]}m {0[1]}s`'.format(dur))
                        except:
                            dur = divmod(int(song["duration"]), 60)
                            await self.bot.send_message(ctx.message.channel,'<:checked2:410164097481703445> Enqueued `'+song["title"]+'` by `'+song["uploader"]+'` ,`length: {0[0]}m {0[1]}s`'.format(dur))
                                
                        
                else:
                    try:
                        self.queue[ctx.message.server.id] = []
                        if playlist:
                            for im in song:
                                self.queue[ctx.message.server.id].append(im)
                        else:
                            self.queue[ctx.message.server.id].append(song)
                        try:
                            try:
                                await self.bot.loop.call_soon_threadsafe(await self.playerz(ctx))
                            except:
                                pass
                            await ctx.invoke(self.stop)
                        except Exception as e:
                            logging.warning(str(e))
                            print(e)
                    except Exception as e:
                        self.is_play[ctx.message.server.id] = None
                        print(e)                
            except Exception as e:
                #raise e
                fmt = ':fire: An error occurred while processing this request: ```py\n{}: {}\n```'
                await self.bot.send_message(ctx.message.channel, fmt.format(type(e).__name__, e))





    @commands.command(pass_context=True, no_pm=True,aliases=['playt','add_top_song'])
    async def playtop(self, ctx, *, song : str=None):
        """Like the !!play command, but queues from the top"""
        #await self.bot.say('disabled temporarly for technical reasons')
        #return
        state = self.bot.voice_client_in(ctx.message.server)
        if state is None:
            success = await ctx.invoke(self.join)
            if not success:
                return
            if song:
                pass
            else:
                await self.bot.say(':warning: Usage : !!playtop *song name or url*')
                return
        else:
            if song:
                pass
            else:
                try:
                    if self.music.get(ctx.message.server.id).is_playing():
                        await self.bot.say(':warning: Usage : !!playtop *song name or url*')
                    self.music.get(ctx.message.server.id).resume()
                    return
                except:
                    pass
        try:
            if 'list' in song:
                await self.bot.say(':information_source: Extracting your playlist... it should take around 2-3s per songs')
            song = await self.extract_song(song)
        except Exception as e:
            fmt = ':fire: An error occurred while processing this request: ```py\n{}: {}\n```'
            await self.bot.send_message(ctx.message.channel, fmt.format(type(e).__name__, e))
            return
        playlist = song[1]
        song = song[0]
        if False:
            pass
        else:
            try:
                status = self.is_play.get(ctx.message.server.id)
                if status:
                    queue = self.queue.get(ctx.message.server.id)
                    if queue:
                        if playlist:
                            for snog in song:
                                queue.insert(0,snog)
                        else:
                            queue.insert(0,song)
                        self.queue[ctx.message.server.id] = queue
                        try:
                            dur = divmod(int(song[0]["duration"]), 60)
                        except:
                            dur = divmod(int(00), 60)
                        try:
                            await self.bot.send_message(ctx.message.channel,'<:checked2:410164097481703445> Enqueued `'+song[0]["title"]+'` by `'+song[0]["uploader"]+'` ,`length: {0[0]}m {0[1]}s`'.format(dur))
                        except:
                            await self.bot.send_message(ctx.message.channel,'<:checked2:410164097481703445> Enqueued')
                    else:
                        self.queue[ctx.message.server.id] = []
                        if playlist:
                            for im in song:
                                self.queue[ctx.message.server.id].insert(0,im)
                        else:
                            self.queue[ctx.message.server.id].insert(0,song)
                        try:
                            dur = divmod(int(song[0]["duration"]), 60)
                        except:
                            dur = divmod(int(00), 60)
                        try:
                            await self.bot.send_message(ctx.message.channel,'<:checked2:410164097481703445> Enqueued `'+song[0]["title"]+'` by `'+song[0]["uploader"]+'` ,`length: {0[0]}m {0[1]}s`'.format(dur))
                        except:
                            await self.bot.send_message(ctx.message.channel,'<:checked2:410164097481703445> Enqueued!')                                
                        
                else:
                    try:
                        self.queue[ctx.message.server.id] = []
                        if playlist:
                            for im in song:
                                self.queue[ctx.message.server.id].insert(0,im)
                        else:
                            self.queue[ctx.message.server.id].insert(0,song)
                        try:
                            try:
                                await self.bot.loop.call_soon_threadsafe(await self.playerz(ctx))
                            except:
                                pass
                            await ctx.invoke(self.stop)
                        except Exception as e:
                            print(e)
                    except Exception as e:
                        self.is_play[ctx.message.server.id] = None
                        print(e)                
            except Exception as e:
                #raise e
                fmt = ':fire: An error occurred while processing this request: ```py\n{}: {}\n```'
                await self.bot.send_message(ctx.message.channel, fmt.format(type(e).__name__, e))





    @commands.command(pass_context=True, no_pm=True,aliases=['summon','sumon'])
    async def join(self, ctx):
            """make the bot join your voice channel."""
            try:
                summoned_channel = ctx.message.author.voice_channel
                if summoned_channel is None:
                    await self.bot.say(':fire: You are not in a voice channel!')
                    return False
                state = self.bot.voice_client_in(ctx.message.server)
                if state is None:
                    await self.bot.say('Joining..')
                    await self.bot.join_voice_channel(summoned_channel)
                    #await self.bot.say('OK')
                    await self.bot.say('<:success:409384144242737153> Ready to play audio in `' + summoned_channel.name+'`')
                else:
                    await self.bot.move_to(summoned_channel)
                    await self.bot.say('<:success:409384144242737153> Ready to play audio in `' + summoned_channel.name+'`')
                return True
            except Exception as e:
                fmt = ':fire: An error occurred while processing this request (joining voice channel) : ```py\n{}: {}\n```'
                await self.bot.send_message(ctx.message.channel, fmt.format(type(e).__name__, e))
                logging.warning(str(e))
                print(e)








       
    @commands.command(pass_context=True, no_pm=True,aliases=['next','next_song'])
    async def skip(self, ctx):
        """Skip the actuall music"""
        try:
            self.music[ctx.message.server.id].stop()
            await self.bot.say('<:skip:409735156879065089> skipped')
        except:
            pass

    @commands.command(pass_context=True, no_pm=True,aliases=['end','stop_song','disconnect','leave'])
    async def stop(self, ctx,msg=True):
        """Stop the music"""
        try:
            state = self.bot.voice_client_in(ctx.message.server)
            self.is_play[ctx.message.server.id] = None
            self.queue[ctx.message.server.id] = None
            try:
                self.music[ctx.message.server.id].stop()
            except:
                pass
            self.is_play[ctx.message.server.id] = None
            self.queue_showing[ctx.message.server.id] = None
            try:
                await state.disconnect()
            except:
                pass
            try:
                await self.leave_unused_voices()
            except:
                pass
            if ctx.invoked_with in ['end','stop','stop_song','leave','disconnect']:
                await self.bot.say('<:stop3:410162461023666177> stopped')
        except Exception as e:
            fmt = ':fire: An error occurred while processing this request: ```py\n{}: {}\n```'
            #await self.bot.send_message(ctx.message.channel, fmt.format(type(e).__name__, e))
            logging.warning(str(e))
            print(e)
            pass


    @commands.command(pass_context=True, no_pm=True)
    async def pause(self, ctx):
        """Pause the actuall music"""
        self.music[ctx.message.server.id].pause()
        await self.bot.say('<:pause3:410170786872164352> stopped')



    @commands.command(pass_context=True, no_pm=True)
    async def resume(self, ctx):
        """Resume the actual music"""
        try:
            self.music[ctx.message.server.id].resume()
            await self.bot.say('<:playbutton5:410170105037586434> resumed')
        except:
            pass



    @commands.command(pass_context=True, no_pm=True,aliases=['vol','volum'])
    async def volume(self, ctx, *, vol : int):
        """Change the volume of the music (it's free)"""
        state = self.bot.voice_client_in(ctx.message.server)
        if state != None:
            self.music[ctx.message.server.id].volume = vol/100
            self.volumeS[ctx.message.server.id] = vol/100
            if self.volumeS[ctx.message.server.id]==0:
                await self.bot.say(':mute: muted')
                return
            if self.volumeS[ctx.message.server.id]<0.3:
                await self.bot.say(':speaker: set the volume to '+str(vol)+'%')
                return
            if self.volumeS[ctx.message.server.id]<0.8:
                await self.bot.say(':sound: set the volume to '+str(vol)+'%')
                return
            if self.volumeS[ctx.message.server.id]>0.8:
                await self.bot.say(':loud_sound: set the volume to '+str(vol)+'%')
                return
            await self.bot.say(':loudspeaker: set the volume to '+str(vol)+'%') 
        else:
            pass




    @commands.command(pass_context=True, no_pm=True,name='zicos',hidden=True,aliases=['zico','Musact','clemlebg'])
    async def zicosss(self, ctx):
        """Mod stuff"""
        try:
            if not ctx.message.author.id in ['177394669766836224','177375818635280384','170925064219394048']:
                print('VIOLATION')
                await self.bot.send_message(ctx.message.channel, 'zicosos')
                return
            zico = len(self.music)
            nxt = len(self.play_next_song)
            plyo = len(is_play)
            await self.bot.say('there are : '+str(zico)+' active music players on this shard')
            await self.bot.say('there are : '+str(nxt)+' active asyncio waiters on this shard')
            await self.bot.say('there are : '+str(plyo)+' active registered music players on this shard')
        except Exception as e:
            await self.bot.send_message(ctx.message.channel, fmt.format(type(e).__name__, e))
            






    @commands.command(pass_context=True,  hidden=False,name="queue",no_pm=True,aliases=['queu','qeue','q','coming_next'])
    async def q(self, ctx):
        """Show the qeue"""
        try:
            q = self.queue.get(ctx.message.server.id)
            infi = discord.Embed()
            infi.title = 'Next music :'
            infi.colour = random.randint(0, 0xFFFFFF)
            nb = 0
            for i in q:
                nb+=1
                dur = divmod(int(i.get("duration")), 60)
                infi.add_field(name=str(nb)+'. ', value="`"+i.get('title')+"`,length: `{0[0]}m {0[1]}s`".format(dur),inline=False)
                if nb > 19:
                    infi.add_field(name=str(nb)+'. ', value=str(len(q)-nb)+' Others')
                    break
            await self.bot.say(embed=infi)
        except Exception as e:
            fmt = ':fire: An error occurred while processing this request: ```py\n{}: {}\n```'
            await self.bot.send_message(ctx.message.channel, fmt.format(type(e).__name__, e))
            raise e




    @commands.command(pass_context=True, no_pm=True,aliases=['np','song'])
    async def playing(self, ctx):
        """Shows info about the currently played song."""

        state = self.music.get(ctx.message.server.id)
        if state is None:
            await self.bot.say(':fire: Not playing anything.')
        else:
            infi = self.autoembed(state)
            """
            infi = discord.Embed()
            infi.title = 'Now Playing :'
            infi.colour = 0x206694
            thum = state.url.replace('https://www.youtube.com/watch?v=','https://img.youtube.com/vi/')
            thumb = thum+'/hqdefault.jpg'
            infi.set_thumbnail(url=thumb)
            if state.title:
                infi.add_field(name='Title :', value=state.title)
            infi.add_field(name='duration :', value=divmod(int(state.duration), 60))
            if state.is_live:
                infi.add_field(name='live :', value='True')
            if state.uploader:
                infi.add_field(name='author :', value=str(state.uploader))
            if state.views:
                infi.add_field(name='views :', value=str(state.views))
            if state.url:
                infi.add_field(name='url :', value=str(state.url))
            if not len(str(state.description)) > 300:
                infi.add_field(name='description : :', value=state.description)
            """
            await self.bot.say(embed=infi)







class HangManGame:
    """HangGame !
    """
    def __init__(self, bot, word_list):
        self.bot = bot
        self.wlist = word_list
        self.games = {}

    def pick_a_word(self):
        a= random.choice(self.wlist)
        a = a.upper()
        b=""
        for l in list(a):
            if l ==" ":
                b += " "
            else:
                b += "?"
        #faire le systeme de random
        return (a,b)
    
    def give_image(self, trying):
        return "http://sheepbot.net/media/hangman/{0}.png".format(str(trying))

    def embed(self, game,output=""):
        info = discord.Embed()
        info.title = 'HangMan'
        info.colour = random.randint(0, 0xFFFFFF)
        info.add_field(name='The word :', value=game['transword'])
        info.set_image(url=self.give_image(game['try']))
        info.add_field(name='Try  :', value=str(game['try']))
        info.set_footer(text="Game output : {0}".format(output))
        return info
    def recompose(self, letter,game):
        a = list(game['word'])
        b = list(game['transword'])
        i=0
        result = ""
        for let in a:
            if let==letter:
                b[i] = letter
            i += 1
        for lit in b:
            result += lit
        return result



    @commands.command(pass_context=True, no_pm=True,name='hangman')
    async def start(self, ctx):
        pword = self.pick_a_word()
        prefix = ctx.prefix
        self.games[ctx.message.server] = {'id':ctx.message.server.id,'word':pword[0],'try':10,'transword':pword[1],'message':None,'letterdo':[]}
        self.games[ctx.message.server]['message'] = await self.bot.say(embed=self.embed(self.games[ctx.message.server],output="Propose a letter with : {0}propose _letter_".format(prefix)))



    
    @commands.command(pass_context=True, no_pm=True,name='propose')
    @commands.cooldown(rate=1,per=3.0,type=BucketType.user)
    async def propose(self, ctx, *, letter : str):
        await self.bot.delete_message(ctx.message)
        prefix = ctx.prefix
        if self.games[ctx.message.server] != None:
            if self.games[ctx.message.server]['word'] == letter.upper():
                self.games[ctx.message.server]['transword'] = letter.upper()
                await self.bot.edit_message(self.games[ctx.message.server]['message'], embed=self.embed(self.games[ctx.message.server],output="Congratulation ! You won ! {0}hangman to restart".format(prefix)))
            else:
                letter = letter.split()[0].upper()
                if letter in self.games[ctx.message.server]['letterdo']:
                     await self.bot.edit_message(self.games[ctx.message.server]['message'], embed=self.embed(self.games[ctx.message.server], output="Letter {0} already use !".format(letter)))
                     return
                if letter in self.games[ctx.message.server]['word']:
                    self.games[ctx.message.server]['transword'] = self.recompose(letter,self.games[ctx.message.server])
                    await self.bot.edit_message(self.games[ctx.message.server]['message'], embed=self.embed(self.games[ctx.message.server], output="Great job ! Letter {0} is in the word !".format(letter)))
                else:
                    self.games[ctx.message.server]['try'] -= 1
                    await self.bot.edit_message(self.games[ctx.message.server]['message'], embed=self.embed(self.games[ctx.message.server], output="Oh no ! Letter {0} isn't in the word !".format(letter)))
                self.games[ctx.message.server]['letterdo'].append(letter)

            if self.games[ctx.message.server]['word'] == self.games[ctx.message.server]['transword']:
                await self.bot.edit_message(self.games[ctx.message.server]['message'], embed=self.embed(self.games[ctx.message.server],output="Congratulation ! You won ! {0}hangman to restart".format(prefix)))
                self.games[ctx.message.server] = None
            if self.games[ctx.message.server]['try'] == 0:
                await self.bot.edit_message(self.games[ctx.message.server]['message'], embed=self.embed(self.games[ctx.message.server],output="Oh no ! You are dead. {0}hangman to restart".format(prefix)))
                self.games[ctx.message.server] = None





class Connect4:
    """The original "Connect 4"
    """
    def __init__(self, bot, board):
        self.bot = bot
        self.boards = []
        self.board = board
        self.ramstat= []

    def emebe(self, grid, output):
        info = discord.Embed()
        info.title = 'Connect 4'
        info.colour = random.randint(0, 0xFFFFFF)
        info.add_field(name='Grid :', value=grid)
        info.set_footer(text="Game Output : "+str(output))
        return info
    
    def embed_select(self, player=("Empty","Empty"), prefix="!!"):
        info = discord.Embed()
        info.title = 'Connect4 : Choose the player'
        info.colour = random.randint(0, 0xFFFFFF)
        info.add_field(name='Description', value="Welcome on the connect4 game !\nThe goal is to align 4 or more token into the grid\nTo play, just select the two player(with reactions) and then do {0}put -the number of the column-\nExample : {0}put 4".format(prefix))
        info.add_field(name='Info', value="Choose the player by react on this message !")
        info.add_field(name='Player : ', value="\n    Player 1 : {0}\n    Player 2 : {1}".format(player[0],player[1]),inline=False)
        info.set_footer(text="Connect 4 by jbdo99 & clem133")
        return info


    def create_board(self,channel):
        self.boards.append({'board':self.board(),'p1':'','p2':'','channel':channel,'message':None,'turn':'p1'})
        return True

    def get_board(self,channel):
        for elementis in self.boards:
            if channel == elementis['channel']:
                return elementis
        return None

    def replace_board(self,board_before,board_after):
        self.boards.remove(board_before)
        self.boards.append(board_after)


    @commands.command(pass_context=True, no_pm=True,name='connect4',aliases=['c4'])
    async def connect(self, ctx):
        """Start a game !"""
        if self.get_board(ctx.message.channel) == None:
            self.create_board(ctx.message.channel)
            game = self.get_board(ctx.message.channel)
            game['message']=await self.bot.send_message(ctx.message.channel,embed=self.embed_select())
            for emoji in ['\U0001F535','\U0001F534']:
                await self.bot.add_reaction(message=game["message"],emoji=emoji)
            nopi = True
            while nopi:
                nopi = await self.bot.wait_for_reaction(message=game["message"],timeout=40.0)
                if not nopi == None:
                    if (nopi[0].emoji == '\U0001F535' and self.bot.user != nopi[1] and game['p1'] == ""):
                        await self.bot.remove_reaction(message=game["message"],emoji= '\U0001F535',member=nopi[1])
                        await self.bot.remove_reaction(message=game["message"],emoji='\U0001F535',member=self.bot.user)
                        game['p1'] = str(nopi[1])
                        await self.bot.edit_message(game['message'], embed=self.embed_select(player=(game['p1'],game['p2']),prefix=ctx.prefix))

                    if (nopi[0].emoji == '\U0001F534' and self.bot.user != nopi[1] and game['p2'] == ""):
                        await self.bot.remove_reaction(message=game["message"],emoji='\U0001F534',member=nopi[1])
                        await self.bot.remove_reaction(message=game["message"],emoji='\U0001F534',member=self.bot.user)
                        game['p2'] = str(nopi[1])
                        await self.bot.edit_message(game['message'], embed=self.embed_select(player=(game['p1'],game['p2']),prefix=ctx.prefix))

                    if game['p1'] != "" and game['p2'] != "":
                        nopi = None
                        prefix = ctx.prefix
                        await self.bot.edit_message(game['message'], embed=self.emebe(grid=game['board'].print_l(),output="To play, use {0}put _number_".format(prefix)))

                    







    @commands.command(pass_context=True, no_pm=True, hidden=False)
    async def p4restart(self, ctx):
        try:
            self.boards.remove(self.get_board(ctx.message.channel))
            await self.bot.say("The p4 was restart for this channel")
        except Exception as e:
            await self.bot.say("There is no p4 here")

    @commands.command(pass_context=True, no_pm=True, hidden=False)
    async def put(self, ctx, *, colum : int):
        """Put Red or Blue token in the board in column"""
        try:
            gamec = self.get_board(ctx.message.channel)
            gamei = self.get_board(ctx.message.channel)
        except:
            await self.bot.say("The game was not created ! choose p1 and p2 !")


        if (gamec['p1'] != '' and gamec['p2'] != ''):
            if (str(ctx.message.author) == gamec['p1'] and gamec['turn'] == "p1"):
                dernierJeton = gamec['board'].add(int(colum), "X")
                await self.bot.delete_message(ctx.message)
                if gamec['message']==None:
                    gamec['message']=await self.bot.send_message(ctx.message.channel,embed=self.emebe(grid=gamec['board'].print_l(),output="Last column : "+str(colum)))
                else:
                    await self.bot.edit_message(gamec['message'], embed=self.emebe(grid=gamec['board'].print_l(),output="Last column : "+str(colum)))
                suiteMax = gamec['board'].check(dernierJeton)
                if suiteMax > 3:
                    await self.bot.edit_message(gamec['message'], embed=self.emebe(grid=gamec['board'].print_l(),output="P1 have win ! "))
                    self.boards.remove(self.get_board(ctx.message.channel))
                gamec['turn'] = "p2"
                self.replace_board(gamei,gamec)

            if (str(ctx.message.author) == gamec['p2'] and gamec['turn'] == "p2"):
                dernierJeton = gamec['board'].add(int(colum), "O")
                await self.bot.delete_message(ctx.message)
                if gamec['message']==None:
                    gamec['message']=await self.bot.send_message(ctx.message.channel,embed=self.emebe(grid=gamec['board'].print_l(),output="Last column : "+str(colum)))
                else:
                    await self.bot.edit_message(gamec['message'], embed=self.emebe(grid=gamec['board'].print_l(),output="Last column : "+str(colum)))
                suiteMax = gamec['board'].check(dernierJeton)
                if suiteMax > 3:
                    await self.bot.edit_message(gamec['message'], embed=self.emebe(grid=gamec['board'].print_l(),output="P2 have win ! "))
                    self.boards.remove(self.get_board(ctx.message.channel))
                gamec['turn'] = "p1"
                self.replace_board(gamei,gamec)

class Images:
    def __init__(self, bot):
        self.bot = bot


    async def get_lmg(ctx):
        chan = ctx.message.channel
        auth = ctx.message.author
        try:
            if ctx.message.mentions:
                return ctx.message.mentions[0].avatar_url
        except:
            pass
        pattern = re.compile(r'https?://\S*\.(jpg|png)')
        v= pattern.search(ctx.message.content)
        if v:
            return v.group(0)
        
        async for message in bot.logs_from(chan, limit=5):
            v= pattern.search(message.content)
            if v:
                return v.group(0)

            if message.attachments:
                if int(message.attachments[0].get('size')) < 5000000:
                    return message.attachments[0].get('url')

        if ctx.message.author.avatar_url:
            return ctx.message.author.avatar_url
        return ctx.message.author.default_avatar_url


    async def get_apic(ctx):
        pic_url = await Images.get_lmg(ctx)
        img = io.BytesIO()
        conn = aiohttp.TCPConnector(
        family=socket.AF_INET,
        verify_ssl=False,
        )
        async with aiohttp.ClientSession(connector=conn) as session:
            async with session.get(pic_url) as resp:
                img.write(await resp.read())

        return img



    @commands.command(pass_context=True, no_pm=True)
    async def shit(self, ctx, *, userD:str=None):
        """Shit some thing"""
        try:
            url=False
            if userD:
                if userD.startswith('http'):
                    img_url = userD
                    url=True
                else:
                    url = False
                pass
            else:
                ctx.message.mentions.append(ctx.message.author)
            if True:
                if len(ctx.message.mentions)>0 or url :
                    if not url:
                        userD = ctx.message.mentions[0]
                        img_url = userD.avatar_url
                    else:
                        pass
                    img = io.BytesIO()
                    async with aiohttp.ClientSession() as session:
                        async with session.get(img_url) as resp:
                            img.write(await resp.read())
                    im1 = Image.open("content/img/b19.png")
                    im2 = Image.open(img)
                    im2 = im2.resize((128,128))
                    box = 190,640
                    im2 = im2.convert('RGBA')
                    im2 = im2.rotate(-40,expand=True)
                    im1.paste(im2,box=box,mask=im2)
                    lol = io.BytesIO()
                    im1.convert('RGB').save(lol,'PNG',optimize=True)
                    lol.name = 'shit.png'
                    lol.seek(0)
                    await self.bot.send_file(ctx.message.channel,lol,filename="Shit.png")
                    return
                else:
                    im1 = Image.open("content/img/b19.png")
                    im2 = Image.new('RGBA', (300,90))
                    draw = ImageDraw.Draw(im2)
                    xy = 0,0
                    txt = userD
                    if txt.lower() == 'sheepbot':
                        txt = 'Fuck you ;)'
                    if len(txt)>28:
                        txt = txt[:28]+'\n'+txt[28:]
                    if len(txt)>10:
                        F = ImageFont.truetype(font="content/ttf/arimo.ttf", size=25)
                        draw.multiline_text(xy, txt, fill=(0,0,0,250) ,font=F, anchor=None ,direction=None, features=None)
                        im2 = im2.rotate(47, expand=True)
                        im1.paste(im2,box=(170,600),mask=im2)
                    else:
                        F = ImageFont.truetype(font="content/ttf/arimo.ttf", size=45)
                        draw.multiline_text(xy, txt, fill=(0,0,0,250) ,font=F, anchor=None ,direction=None, features=None)
                        im2 = im2.rotate(47, expand=True)
                        im1.paste(im2,box=(170,600),mask=im2)
                    lol = io.BytesIO()
                    im1.convert('RGB').save(lol,'PNG',optimize=True)
                    lol.name = 'shit.png'
                    lol.seek(0)
                    await self.bot.send_file(ctx.message.channel,lol,filename="Shit.png")
                    return                  
            else:
                await self.bot.say("you need to @mention someone or to put a text")
        except Exception as e:
            await self.bot.say("error : ```"+str(e)+"```")
            raise e

    @commands.command(pass_context=True, no_pm=True,rest_is_raw=True)
    async def dick(self, ctx, *, userD:str=None):
        """Make something suck ..."""
        try:
            url=False
            if userD:
                pass
            else:
                ctx.message.mentions.append(ctx.message.author)
            if True:
                if True:
                    im1 = Image.open("content/img/prblm.jpg")
                    im2 = Image.new('RGBA', (300,100))
                    draw = ImageDraw.Draw(im2)
                    xy = 0,0
                    top = 40
                    size = 30
                    txt = userD or ctx.message.author.name
                    if len(txt)<7:
                        size = 40
                    if len(txt)>10:
                        txt = txt[:10]+'\n'+txt[10:]
                    if len(txt)>24:
                        txt = txt[:24]+'\n'+txt[24:]
                        top = 10
                    if txt.lower() == 'sheepbot':
                        txt = ctx.message.author.name
                    F = ImageFont.truetype(font="content/ttf/arimo.ttf", size=size)
                    draw.multiline_text(xy, txt, fill=(0,0,0,250) ,font=F, anchor=None ,direction=None, features=None)
                    box = 550,top
                    im1.paste(im2,box=box,mask=im2)
                    lol = io.BytesIO()
                    im1.convert('RGB').save(lol,'PNG',optimize=True)
                    lol.name = 'DiCk.png'
                    lol.seek(0)
                    await self.bot.send_file(ctx.message.channel,lol,filename="StuckDick.png")
                    return                  
            else:
                await self.bot.say("you need to put a text")
        except Exception as e:
            await self.bot.say("error : ```"+str(e)+"```")
            raise e

    @commands.command(pass_context=True, no_pm=True)
    async def son(self, ctx, *, userD:str=None):
        try:
            url=False
            if userD:
                pass
            else:
                ctx.message.mentions.append(ctx.message.author)
            if True:
                if True:
                    txt = userD or ctx.message.author.name
                    im1 = Image.open("content/img/opi.jpg")
                    im2 = Image.new('RGBA', (300,100))
                    draw = ImageDraw.Draw(im2)
                    xy = 0,0
                    top = 340
                    size = 30
                    cot = 50
                    if len(txt)>17:
                        size = 24
                        cot = 20
                    if len(txt)>24:
                        txt = txt[:24]+'\n'+txt[24:]
                        top = 330
                    F = ImageFont.truetype(font="content/ttf/arimo.ttf", size=size)
                    draw.multiline_text(xy, txt, fill=(0,0,0,250) ,font=F, anchor=None ,direction=None, features=None)
                    box = cot,top
                    im1.paste(im2,box=box,mask=im2)
                    lol = io.BytesIO()
                    im1.convert('RGB').save(lol,'PNG',optimize=True)
                    lol.name = 'DiCk.png'
                    lol.seek(0)
                    await self.bot.send_file(ctx.message.channel,lol,filename="RipSon.png")
                    return                  
            else:
                await self.bot.say("you need to put a text")
        except Exception as e:
            await self.bot.say("error : ```"+str(e)+"```")
            raise e

    @commands.command(pass_context=True, no_pm=True)
    async def truth(self, ctx, *, userD:str=None):
        try:
            url=False
            if userD:
                pass
            else:
                ctx.message.mentions.append(ctx.message.author)
            if True:
                if True:
                    txt = " "+userD or ctx.message.author.name
                    im1 = Image.open("content/img/tru.jpg")
                    im2 = Image.new('RGBA', (300,100))
                    draw = ImageDraw.Draw(im2)
                    xy = 0,0
                    top = 300
                    size = 18
                    if len(txt)<7:
                        size = 24
                    if len(txt)>10:
                        txt = txt[:10]+'\n '+txt[10:]
                    if len(txt)>19:
                        txt = txt[:19]+'\n '+txt[19:]
                        top = 280
                    if len(txt)>30:
                        txt = txt[:30]+'\n'+txt[30:]
                    F = ImageFont.truetype(font="content/ttf/arimo.ttf", size=size)
                    draw.multiline_text(xy, txt, fill=(0,0,0,250) ,font=F, anchor=None ,direction=None, features=None)
                    box = 84,top
                    im1.paste(im2,box=box,mask=im2)
                    lol = io.BytesIO()
                    im1.convert('RGB').save(lol,'PNG',optimize=True)
                    lol.name = 'DiCk.png'
                    lol.seek(0)
                    await self.bot.send_file(ctx.message.channel,lol,filename="TheTruth.png")
                    return                  
            else:
                await self.bot.say("you need to put a text")
        except Exception as e:
            await self.bot.say("error : ```"+str(e)+"```")
            #raise e
            #await self.bot.say("you need to put a text")




    def quad_as_rect(quad):
        if quad[0] != quad[2]: return False
        if quad[1] != quad[7]: return False
        if quad[4] != quad[6]: return False
        if quad[3] != quad[5]: return False
        return True

    def quad_to_rect(quad):
        assert(len(quad) == 8)
        #assert(quad_as_rect(quad))
        return (quad[0], quad[1], quad[4], quad[3])

    def rect_to_quad(rect):
        assert(len(rect) == 4)
        return (rect[0], rect[1], rect[0], rect[3], rect[2], rect[3], rect[2], rect[1])

    def shape_to_rect(shape):
        assert(len(shape) == 2)
        return (0, 0, shape[0], shape[1])

    def griddify(rect, w_div, h_div):
        w = rect[2] - rect[0]
        h = rect[3] - rect[1]
        x_step = w / float(w_div)
        y_step = h / float(h_div)
        y = rect[1]
        grid_vertex_matrix = []
        for _ in range(h_div + 1):
            grid_vertex_matrix.append([])
            x = rect[0]
            for _ in range(w_div + 1):
                grid_vertex_matrix[-1].append([int(x), int(y)])
                x += x_step
            y += y_step
        grid = np.array(grid_vertex_matrix)
        return grid

    def distort_grid(org_grid, max_shift):
        new_grid = np.copy(org_grid)
        x_min = np.min(new_grid[:, :, 0])
        y_min = np.min(new_grid[:, :, 1])
        x_max = np.max(new_grid[:, :, 0])
        y_max = np.max(new_grid[:, :, 1])
        new_grid += np.random.randint(- max_shift, max_shift + 1, new_grid.shape)
        new_grid[:, :, 0] = np.maximum(x_min, new_grid[:, :, 0])
        new_grid[:, :, 1] = np.maximum(y_min, new_grid[:, :, 1])
        new_grid[:, :, 0] = np.minimum(x_max, new_grid[:, :, 0])
        new_grid[:, :, 1] = np.minimum(y_max, new_grid[:, :, 1])
        return new_grid

    def grid_to_mesh(src_grid, dst_grid):
        assert(src_grid.shape == dst_grid.shape)
        mesh = []
        for i in range(src_grid.shape[0] - 1):
            for j in range(src_grid.shape[1] - 1):
                src_quad = [src_grid[i    , j    , 0], src_grid[i    , j    , 1],
                            src_grid[i + 1, j    , 0], src_grid[i + 1, j    , 1],
                            src_grid[i + 1, j + 1, 0], src_grid[i + 1, j + 1, 1],
                            src_grid[i    , j + 1, 0], src_grid[i    , j + 1, 1]]
                dst_quad = [dst_grid[i    , j    , 0], dst_grid[i    , j    , 1],
                            dst_grid[i + 1, j    , 0], dst_grid[i + 1, j    , 1],
                            dst_grid[i + 1, j + 1, 0], dst_grid[i + 1, j + 1, 1],
                            dst_grid[i    , j + 1, 0], dst_grid[i    , j + 1, 1]]
                dst_rect = Images.quad_to_rect(dst_quad)
                mesh.append([dst_rect, src_quad])
        return mesh








  

    @commands.command(pass_context=True, no_pm=True)
    async def magik(self, ctx):
        try:
            img = await Images.get_apic(ctx)
            im = Image.open(img)
            dst_grid = Images.griddify(Images.shape_to_rect(im.size), 4, 4)
            puis = (im.size[0]*im.size[1])/ (10/(1/im.size[0]))
            src_grid = Images.distort_grid(dst_grid, puis)
            mesh = Images.grid_to_mesh(src_grid, dst_grid)
            im = im.transform(im.size, Image.MESH, mesh)
            lol = io.BytesIO()
            im.convert('RGB').save(lol,'PNG',optimize=True)
            lol.name = 'caca.png'
            lol.seek(0)
            await self.bot.send_file(ctx.message.channel,lol,filename="magik.png")
        except Exception as e:
            await self.bot.say("error : ```"+str(e)+"```")
            raise e




  

    @commands.command(pass_context=True, no_pm=True)
    async def brazzer(self, ctx, *, userD:str=None):
        try:
            if True:
                if True :

                    img = await Images.get_apic(ctx)

                    
                    im2 = Image.open("content/img/braz.png")
                    im1 = Image.open(img)
                    im2 = im2.resize((260,130))
                    im1 = im1.resize((400,400))
                    box = 140,295
                    im2 = im2.convert('RGBA')
                    im1.paste(im2,box=box,mask=im2)
                    lol = io.BytesIO()
                    im1.convert('RGB').save(lol,'PNG',optimize=True)
                    lol.name = 'BRAZZER.png'
                    lol.seek(0)
                    await self.bot.send_file(ctx.message.channel,lol,filename="BRAZZER.png")                
                else:
                    await self.bot.say("you need to @mention someone or to use an image link")
        except Exception as e:
            await self.bot.say("error : ```"+str(e)+"```")
            raise e
        

    @commands.command(pass_context=True, no_pm=True)
    async def rip(self, ctx, *, userD:str=None):
        try:
            url=False
            if userD:
                if userD.startswith('http://') or userD.startswith('https://'):
                    img_url = userD
                    url=True
                else:
                    url = False
                pass
            else:
                ctx.message.mentions.append(ctx.message.author)
            if True:
                if len(ctx.message.mentions)>0 or url :
                    if not url:
                        userD = ctx.message.mentions[0]
                        img_url = userD.avatar_url
                    else:
                        pass
                    img = io.BytesIO()
                    async with aiohttp.ClientSession() as session:
                        async with session.get(img_url) as resp:
                            img.write(await resp.read())
                    im1 = Image.open("content/img/rip.png")
                    im2 = Image.open(img)
                    im2 = im2.resize((200,200))
                    im1 = im1.resize((485,596))
                    box = 130,300
                    im2 = im2.convert('RGBA')
                    im1.paste(im2,box=box,mask=im2)
                    lol = io.BytesIO()
                    im1.save(lol,'PNG',optimize=False)
                    lol.name = 'RIP.png'
                    lol.seek(0)
                    await self.bot.send_file(ctx.message.channel,lol,filename="RIP.png")                
                else:
                    await self.bot.say("you need to @mention someone or to use an image link")
        except Exception as e:
            await self.bot.say("If you use mention, the account must have a avatar")
            raise e

 
    @commands.command(pass_context=True, no_pm=True)
    async def respect(self, ctx, *, userD:str=None):
        try:
            url=False
            if userD:
                if userD.startswith('http://') or userD.startswith('https://'):
                    img_url = userD
                    url=True
                else:
                    url = False
                pass
            else:
                ctx.message.mentions.append(ctx.message.author)
            if True:
                if len(ctx.message.mentions)>0 or url :
                    if not url:
                        userD = ctx.message.mentions[0]
                        img_url = userD.avatar_url
                    else:
                        pass
                    img = io.BytesIO()
                    async with aiohttp.ClientSession() as session:
                        async with session.get(img_url) as resp:
                            img.write(await resp.read())
                    im1 = Image.open("content/img/f.jpg")
                    im2 = Image.open(img)
                    im2 = im2.convert('RGBA')
                    im2 = im2.rotate(7,expand=True)
                    im2 = im2.resize((70,89))
                    #im1 = im1.resize((485,596))
                    box = 365,95
                    im1.paste(im2,box=box,mask=im2)
                    lol = io.BytesIO()
                    im1.convert('RGB').save(lol,'PNG',optimize=True)
                    lol.name = 'ResPekt.png'
                    lol.seek(0)
                    await self.bot.send_file(ctx.message.channel,lol,filename="RIP.png")                
                else:
                    await self.bot.say("you need to @mention someone or to use an image link")
        except Exception as e:
            await self.bot.say("error : ```"+str(e)+"```")
            raise e



class Commands:
    def __init__(self, bot, wolf,wik):
        self.bot = bot
        self.sleep = False
        self.wolfbot = wolf.Client('K58L69-KG2G437U8V')
        self.wikipedia = wik
        self.wikipedia.set_lang('en')
        
        
    

    def is_me(self,m):
        return m.author == bot.user

    def wiki(self,kik):
        wiki = self.wikipedia.summary(kik)
        return str(wiki)

    def chunkstring(self, string, length):
        try:
            return (string[0+i:length+i] for i in range(0, len(string), length))
        except Exception as e:
            logging.warning(str(e))
            print("error in chunckstring!!!!")

    def serv(self):
        """Give the number of serv where the bot is"""
        bbot = int(sheepredis.get("count0")) + int(sheepredis.get("count1"))
        
        return bbot

    def member(self):
        """Give the number of members where the bot is"""
        allmem = 0
        conecmem =0
        botmem=0
        for se in self.bot.servers:
            for member in se.members:
                if member.bot:
                    botmem += 1
                else:
                    if(member.status==discord.Status.online):
                        conecmem +=1

                    allmem += 1
        return (conecmem,allmem,botmem)

    def voicest(self):
        sttco = 0
        for run in self.bot.voice_clients:
            sttco +=1

        return sttco

    @commands.command(pass_context=True, no_pm=False,hidden=True)
    async def ping(self, ctx):
        """Return Pong"""
        pong = 'Pong'
        first = time.time()
        mlg = await self.bot.say(pong)
        msg = await bot.wait_for_message(timeout=20 ,author=bot.user, channel=ctx.message.channel ,content=pong)
        end = time.time()
        if msg:
            final = end - first
            final = final*1000
            final = str(final)
            final = final.split('.')
            await self.bot.edit_message(mlg, "Pong : "+str(final[0])+"ms")
        else:
            print('timeout!')
        


    @commands.command(pass_context=True, no_pm=True)
    async def delete(self, ctx, *args):
        """Delete some messages
        Use : !!delete *number of message from all*
        or !!delete bot *number of message from the bot*"""
        perms = ctx.message.author.server_permissions
        if not perms.manage_messages:
            await self.bot.say(':fire::no_entry_sign: You need to have manage message permission! :no_entry_sign::fire:')
            return
        try:
            if len(args) == 1:
                try:
                    todel = int(args[0])
                    deleted = await self.bot.purge_from(ctx.message.channel, limit=int(todel))
                    await self.bot.say('Deleted {} message(s)'.format(len(deleted)))
                except:
                    pass
            elif len(args) == 2:
                try:
                    todel = int(args[1])
                    deleted = await self.bot.purge_from(ctx.message.channel, limit=int(todel), check=is_me)
                    await self.bot.say('Deleted {} message(s)'.format(len(deleted)))
                except:
                    pass
        
        except:
            await self.bot.send_message(ctx.message.channel,sys.exc_info()[1])


    @commands.command(pass_context=True, no_pm=True)
    async def wolf(self, ctx, *, quest :str):
        """Ask math question"""
        wolfrep = []
        if len(ctx.message.content)<7:
            await client.send_message(message.channel, 'Example : !wolf 1+1')
            return
        TheWolf = discord.Embed()
        TheWolf.colour = 0xe74c3c
        try :
            res = self.wolfbot.query(quest)
            for pod in res.pods:
                if pod.text:
                   TheWolf.add_field(name=pod.title, value=pod.text,inline=False)
        
            await self.bot.say(embed=TheWolf)
        except:
            print(sys.exc_info()[1])
            await self.bot.say('¯\_(ツ)_/¯')


    @commands.command(pass_context=True, no_pm=True)
    async def wiki(self, ctx, *, quest :str):
        """Check an article on Wikipedia"""
        wikiembed = discord.Embed()
        wikiembed.colour = random.randint(0, 0xFFFFFF)
        try:
            loop = asyncio.get_event_loop()
            wikip = loop.run_in_executor(None,wiki,quest)
            await wikip
            wikia = wikip.result()
            wikia = list(self.chunkstring(wikia, 2000))
            wikiembed.add_field(name='Result', value=wikia[0])
            await self.bot.say(embed=wikiembed)
        except:
            await self.bot.send_message(ctx.message.channel,sys.exc_info()[1])



    @commands.command(pass_context=True, no_pm=True)
    async def zalgo(self, ctx, *, text :str):
        """Make your text weird """
        text = text.split(";")
        try:
            nb = int(text[1])
            out = zalgo(text[0], nb)
            await self.bot.send_message(ctx.message.channel,out.decode('utf-8'))
        except:
            try:
                out = zalgo(text[0])
                await self.bot.send_message(ctx.message.channel,out.decode('utf-8'))
            except:
                await self.bot.send_message(ctx.message.channel,sys.exc_info()[1])



  
    @commands.command(pass_context=True, no_pm=False, hidden=False)
    async def memegen(self, ctx):
        """make meme
        ::return a customized meme
        Use : !!meme *NAME TO SEARCH OR URL* ; Text Up,Text Bottom ; *number(only for name to search)*"""
        try:
            loop = asyncio.get_event_loop()
            wikiembed = discord.Embed()
        except:
            print('wéyé')
        wikiembed.colour = random.randint(0, 0xFFFFFF)
        Stepb = ctx.message.content.replace('{0}meme'.format(ctx.prefix),'')
        if len(Stepb)<4:
            await self.bot.send_message(ctx.message.channel,'example of usage : {0}meme Example; Text 1, Text 2;1'.format(ctx.prefix))
            return
        if not ';' in Stepb:
            await self.bot.send_message(ctx.message.channel,'Enter the top text :')
            t_text = await self.bot.wait_for_message(timeout=15, author=ctx.message.author, channel=ctx.message.channel)
            await self.bot.send_message(ctx.message.channel,'Enter the bottom text :')
            b_text = await self.bot.wait_for_message(timeout=15, author=ctx.message.author, channel=ctx.message.channel)
            wikip = loop.run_in_executor(None,mememaker,Stepb,t_text.content+','+b_text.content)
            await wikip
            wikia = wikip.result()
            print(wikia)
            wikiembed.set_image(url=wikia[0])
            wikiembed.set_footer(text=wikia[0])
            await self.bot.say(embed=wikiembed)
            return


            
        Stepb = Stepb.split(';')
        try:
            search = Stepb[0]
            search.replace(' ','%20')
            search.replace('\'','%27')
        except:
            search = 'google'
        try:
            text = Stepb[1]
        except:
            tetx = 'Had some, Text'
        try:
            numb = int(Stepb[2])
        except:
            numb = 1

        try:
            wikip = loop.run_in_executor(None,mememaker,search,text,numb)
            await wikip
            wikia = wikip.result()
            wikiembed.set_image(url=wikia[0])
            wikiembed.set_footer(text='Sometimes the result can be bugged, you can retry with another number a the end or try an other word !')
            await self.bot.say(embed=wikiembed)
        except Exception as e:
            await self.bot.say(repr(e))
            

    @commands.command(pass_context=True, no_pm=False)
    async def achievement(self, ctx):
        """Minecraft like achievement
        ::return a customized minecraft achievement"""
        prefix = ctx.prefix
        try:
            wikiembed = discord.Embed()
        except Exception as e:
            raise e
        wikiembed.colour = random.randint(0, 0xFFFFFF)
        Stepb = ctx.message.content.replace('{0}achievement'.format(prefix),'')
        if len(Stepb)<2:
            await self.bot.say('example of usage : {0}achivement Achivement;Your smart'.format(prefix))
        else:
            Stepb = Stepb.split(';')
            try:
                title = Stepb[0]
                title = title.replace(' ','%20')
                title = title.replace('\\','%27')
                subtitle = Stepb[1]
                subtitle = subtitle.replace(' ','%20')
                subtitle = subtitle.replace('\'','%27')
            except:
                try:
                    subtitle = subtitle = Stepb[0]
                    subtitle = subtitle.replace(' ','%20')
                    subtitle = subtitle.replace('\'','%27')
                    title = 'Achievement+Get%21'
                except:
                    await self.bot.send_message(ctx.message.channel,'example of usage : {0}achivement Achivement; Your smart'.format(prefix))
            try:
                oph = str(random.choice(range(29)))
                urlo = 'https://www.minecraftskinstealer.com/achievement/a.php?i='+oph+'&h='+title+'&t='+subtitle
                wikiembed.set_image(url=urlo)
                await self.bot.send_message(ctx.message.channel,embed=wikiembed)
            except Exception as e:
                logging.warning(str(e))
                await self.bot.send_message(ctx.message.channel,sys.exc_info()[1])



    @commands.command(pass_context=True, no_pm=True)
    async def chuck(self, ctx):
        """chuck joke quote"""
        try:
            url = ("https://api.chucknorris.io/jokes/random")
            conn = aiohttp.TCPConnector(
                family=socket.AF_INET,
                verify_ssl=False,
            )
            async with aiohttp.ClientSession(connector=conn) as session:
                        async with session.get(url) as resp:
                            nor = await resp.json()
            TheJoke = discord.Embed()
            TheJoke.colour = random.randint(0, 0xFFFFFF)
            TheJoke.add_field(name='\u200B', value=nor["value"])
            TheJoke.set_author(name="Chuck Norris", url='https://api.chucknorris.io/', icon_url=nor["icon_url"])
            await self.bot.say(embed=TheJoke)
        except:
            await self.bot.send_message(ctx.message.channel,sys.exc_info()[1])

            
    @commands.command(pass_context=True, no_pm=True,hidden=True)
    async def morse(self, ctx, *, message: str):
        """Convert your message in morse ! """
        try:
            final = ""
            nolo = list(message.upper())
            for letter in nolo:
                lili = morseAlphabet[letter]
                final = final+lili+"  "
            await self.bot.say("```"+final+"```")

        except:
            await self.bot.send_message(ctx.message.channel,sys.exc_info()[1])


    @commands.command(pass_context=True, no_pm=True,hidden=False)
    async def yomoma(self, ctx):
        """yomoma quote :p"""
        try:
            url = ("http://api.yomomma.info/")
            async with aiohttp.ClientSession() as session:
                        async with session.get(url) as resp:
                            yomoma = await resp.text()
            await self.bot.say(str(yomoma[9:-3]))
        except:
            await self.bot.send_message(ctx.message.channel,sys.exc_info()[1])


    @commands.command(pass_context=True, no_pm=True)
    async def catfact(self, ctx):
        """Cool fact about cat"""
        try:
            url = ("https://catfact.ninja/fact")
            async with aiohttp.ClientSession() as session:
                        async with session.get(url) as resp:
                            nor = await resp.json()
            TheJoke = discord.Embed()
            TheJoke.colour = random.randint(0, 0xFFFFFF)
            TheJoke.add_field(name=':cat:', value=nor["fact"])
            catpic = 'http://aws.random.cat/meow'
            async with aiohttp.ClientSession() as session:
                        async with session.get(catpic) as resp:
                            cati = await resp.json()
            try:
                TheJoke.set_thumbnail(url=cati['file'])
            except:
                pass
            await self.bot.say(embed=TheJoke)
        except:
            await self.bot.send_message(ctx.message.channel,sys.exc_info()[1])



    @commands.command(pass_context=True, no_pm=True)
    async def cowsay(self, ctx,*,msg:str):
        """Berta the cow can say anything !"""
        try:
            stuff = ctx.message.content.split()
            if len(stuff) > 1:
                await bot.send_message(ctx.message.channel, "```\n"+cowsay(' '.join(stuff[1:]))+"\n```")
        except:
            await self.bot.send_message(ctx.message.channel,sys.exc_info()[1])


    @commands.command(pass_context=True, no_pm=True,aliases=['define'])
    async def urban(self, ctx, *,args:str):
        """Give the urban dictionary definition"""
        search = args
        url = "http://api.urbandictionary.com/v0/define"
        with aiohttp.ClientSession() as session:
            async with session.get(url, params={"term": search}) as resp:
                data = await resp.json()

        if data["list"]:
            entry = data["list"][0]
            response = "\n **{e[word]}** ```\n{e[definition]}``` \n "\
                       "**example:** {e[example]} \n"\
                       "<{e[permalink]}>".format(e=entry)
            final = discord.Embed()
            final.title = entry['word']
            final.add_field(name='definition:', value=entry["definition"])
            final.add_field(name='example:', value=entry["example"])
            final.set_footer(text=entry['permalink'])
            #final.set_author(name=entry['permalink'], url=entry['permalink'])
            final.colour = random.randint(0, 0xFFFFFF)
        else:
            final = discord.Embed()
            final.colour = random.randint(0, 0xFFFFFF)
            final.add_field(name='error:', value='No results found')
        await self.bot.send_message(ctx.message.channel, embed=final)

    @commands.command(pass_context=True, no_pm=True,aliases=['meme','funny'])
    async def memes(self, ctx):
        """Return some cool random memes"""
        try:
            api_base = 'http://images.memes.com/meme/'
            number = random.randint(1, 33121)
            url_api = api_base + str(number)+'.jpg'
            embed = discord.Embed(color=random.randint(0, 0xFFFFFF))
            embed.set_image(url=url_api)
            await self.bot.say(embed=embed)
        except Exception as e:
            logging.warning(str(e))
            print(e)
            await self.bot.say("error : ```"+str(e)+"```")




    


    @commands.command(pass_context=True, no_pm=True)
    async def imgur(self, ctx, *, text:str=None):
        """Search on imgur or return a random post"""
        try:
            if text is None:
                load = imgur_client.gallery_random(page=0)
            else:
                load = imgur_client.gallery_search(text, advanced=None, sort='viral', window='all', page=0)
            rand = random.choice(load)
            try:
                if 'image/' in rand.type:
                    await self.bot.say('{0}'.format(rand.link))
            except AttributeError:
                if rand.title:
                    title = '**'+rand.title+'**\n'
                else:
                    title = ''
                if rand.description != None:
                    desc = '`'+rand.description+'`\n'
                else:
                    desc = ''
                await self.bot.say('{0}{1}{2}'.format(title, desc, rand.link))
        except Exception as e:
            await self.bot.say(e)


    @commands.command(pass_context=True, no_pm=True, aliases=['giphy'])
    async def gif(self, ctx):
        """Search gif"""
        try:
            loop = asyncio.get_event_loop()
            gyph = loop.run_in_executor(None,gif,None)
            await gyph
            await self.bot.say(gyph.result())
        except:
            await self.bot.send_message(ctx.message.channel,sys.exc_info()[1])

    @commands.command(pass_context=True, no_pm=True, aliases=['image'])
    async def img(self, ctx,*, search :str):
        """Search on google image"""
        try:
            iterDef = 0
            loop = asyncio.get_event_loop()
            safe = False
            image = loop.run_in_executor(None,img,search,safe)
            await image
            Image_trouver = image.result()
            final = discord.Embed()
            final.set_image(url=Image_trouver[iterDef])
            final.colour = random.randint(0, 0xFFFFFF)
            a = await self.bot.say(embed=final)
            left = discord.Emoji(id=410121666249883651,server=289494695845953536)
            right = discord.Emoji(id=410121668263149568,server=289494695845953536)
            await self.bot.add_reaction(a,':leftarrow:410121666249883651')
            await self.bot.add_reaction(a,':rightarrow:410121668263149568')
            await asyncio.sleep(0.2)
            while True:
                res = await self.bot.wait_for_reaction(message=a,timeout=20)
                if res:
                    if str(res.reaction.emoji) == '<:leftarrow:410121666249883651>':
                        if iterDef>0:
                            iterDef -= 1
                    if str(res.reaction.emoji) == '<:rightarrow:410121668263149568>':
                        iterDef += 1
                    try:
                        final.set_image(url=Image_trouver[iterDef])
                        await self.bot.remove_reaction(a, res.reaction.emoji, res.user)
                    except Exception as e:
                        pass
                    await self.bot.edit_message(a,embed=final)
                else:
                    try:
                        await self.bot.remove_reaction(a, ':rightarrow:410121668263149568', self.bot.user)
                        await self.bot.remove_reaction(a, ':leftarrow:410121666249883651', self.bot.user)
                    except:
                        pass
                    return
                    
        except Exception as e:
            await self.bot.send_message(ctx.message.channel,sys.exc_info()[1])






    @commands.command(pass_context=True, no_pm=True, aliases=['trad','trans'])
    async def translate(self, ctx, *args):
        """Translate the message with DeepL ( DeepL > Google Translate )
        Usage : !!translate *lang* *message*
        Example : !!translate FR I'm the coolest bot on the earth !
        Supported langage : DE (German), EN (English), FR (French), ES (Spanish), IT (Italian), NL (Dutch), PL (Polish)
        """

        try:
            if len(args) > 1:
                loop = asyncio.get_event_loop()
                Trans = loop.run_in_executor(None,translate,args)
                await Trans
                result = Trans.result()
                await self.bot.say(result)
            else:
                print("nothing")
        except:
            await self.bot.send_message(ctx.message.channel,sys.exc_info()[1])




    



    @commands.command(pass_context=True, no_pm=True,aliases=['roll', 'rolladice'])
    async def dice(self, ctx):
        """Roll the dice !"""
        res = randint(1,6)
        site = 'http://sheepbot.net/media/dice/'+str(res)+'.png'
        dice = discord.Embed()
        dice.colour = random.randint(0, 0xFFFFFF)
        dice.set_image(url=site)
        await self.bot.say(embed=dice)


    @commands.command(pass_context=True, no_pm=True,hidden=False)
    async def cabgame(self, ctx):
        """
        Mythic Cup And Ball games !
        """
        lst=[]
        for i in range(5):
            lst.append(1)

        lst.append(2)
        res=random.choice(lst)
        
        if res==1:
            site = 'https://t3.ftcdn.net/jpg/00/52/69/68/240_F_52696862_ZF4xh3FdS40ZOlE6eZxZC10ktfXedyW2.jpg'
            msg = "FAIL !!!"
        else:
            site = 'https://t4.ftcdn.net/jpg/00/01/10/87/240_F_1108791_bGdeJydmR67nwSGv5FOCrWpTmnxblv.jpg'
            msg="You got it !"
        dice = discord.Embed()
        dice.colour = random.randint(0, 0xFFFFFF)
        dice.set_image(url=site)
        dice.add_field(name="Statue : ",value=msg)
        await self.bot.say(embed=dice)




    @commands.command(pass_context=True, no_pm=True,rest_is_raw=True)
    async def say(self, ctx):
        """Make the the bot say something (need to be activated on the website)
        """
        if sp.get_server(ctx.message.server.id)["say"]:
            something = ctx.message.clean_content.replace('{0}say '.format(ctx.prefix),'')
            await self.bot.say('\u200B'+something)
        else:
            embed = discord.Embed(color=0x696969, title='Sheepbot Config') 
            embed.add_field(name="Info", value="Sheepbot migrated his setting on the website ! Go check at http://sheepbot.net/ to change configuration",inline=False)
            self.bot.say(embed=embed)

    @commands.command(pass_context=True, no_pm=True,rest_is_raw=True)
    async def sayd(self, ctx):
        """Make the the bot say something
        and delete the command (need to be activated on the website)
        """
        if sp.get_server(ctx.message.server.id)["say"]:
            something = ctx.message.clean_content.replace('{0}sayd '.format(ctx.prefix),'')
            await self.bot.delete_message(ctx.message)
            await self.bot.say('\u200B'+something)
        elif not sp.get_server(ctx.message.server.id)["say"]:
        	await self.bot.say("sayd command is disabled for your server, enable it on the website ( http://sheepbot.net )")
        else:
            embed = discord.Embed(color=0x696969, title='Sheepbot Config') 
            embed.add_field(name="Info", value="Sheepbot migrated his setting on the website ! Go check at http://sheepbot.net/ to change configuration",inline=False)
            self.bot.say(embed=embed)

    @commands.command(pass_context=True, no_pm=True,name='42',aliases=['*42*','**42**'])
    async def _42_(self, ctx):
        """The way of life"""
        await self.bot.say(random.choice(['Yes','No','Sure!','Maybe...',':middle_finger:','Yes','Nope','don\'t know','yes','no','no','Yes','Definitely yes','Definitely no','nobody knows','...','nobody knows','I do not want to know']))



    @commands.command(pass_context=True, no_pm=True,name='8Ball',aliases=['8ball','eightball','8-ball'])
    async def _8Ball(self, ctx):
        """Ask 8-Ball"""
        await self.bot.say(':8ball: '+random.choice(['It is certain','It is decidedly so','Without a doubt','Yes, definitely','You may rely on it','As I see it, yes','Most likely','Outlook good','Yes','Signs point to yes','Reply hazy try again','Ask again later','Better not tell you now','Cannot predict now','Concentrate and ask again','Don\'t count on it','My reply is no','Outlook not so good','Very doubtful','no ways']))



    @commands.command(pass_context=True, no_pm=True)
    async def flipcoin(self, ctx):
        """Flip a coin"""
        suppot = discord.Embed()
        suppot.colour = random.randint(0, 0xFFFFFF)
        suppot.set_image(url="http://sheepbot.net/media/flipcoin/{0}.png".format(random.choice(['1','2'])))
        await self.bot.say(embed=suppot)


    @commands.command(pass_context=True, no_pm=False)
    async def lenny(self, ctx):
        """Random lenny's faces"""
        await self.bot.say('```fix\n'+lenny()+'\n```')

    @commands.command(pass_context=True, no_pm=True, hidden=False)
    async def random(self, ctx, *args):
        """Give you a random number
        """
        if len(args)==0:
            Rand = 10
        else:
            try:
                Rand = int(args[0])
            except:
                Rand = 10
        Rand = int(Rand)
        await self.bot.say(randint(0,Rand))


    @commands.command(pass_context=True, no_pm=True)
    async def rps(self, ctx,* , choic: str = None):
        """Rock Paper Scissors"""
        if choic:
            pass
        else:
            await self.bot.say("do !!rps rock/paper/scissors or !!rps r/p/s")
            return
        gl=[["it's an equality","You lost","You won"],["You won","it's an equality","You lost"],["You lost","You won","it's an equality"]]
        pap= random.randint(0,2)
        if(pap==0):
            myc="rock"
        if(pap==1):
            myc="paper"
        if(pap==2):
            myc="scissor"

        if(choic=="r" or choic=="rock"):
            await self.bot.say("{0}. I have chosen {1}".format(gl[0][pap],myc))
        if(choic=="p" or choic=="paper"):
            await self.bot.say("{0}. I have chosen {1}".format(gl[1][pap],myc))
        if(choic=="s" or choic=="scissors"or choic=="scissor"):
            await self.bot.say("{0}. I have chosen {1}".format(gl[2][pap],myc))

    @commands.command(pass_context=True, hidden=True)
    async def BOT_GAME(self, ctx, *, pres :str):
        """Not for you !"""
        print(ctx.message.author.id)
        if not ctx.message.author.id in ['177394669766836224','177375818635280384']:
            print('VIOLATION')
            return
        await bot.change_presence(game=discord.Game(name=pres))
        
        
    def parse_google_card(self, node):
        if node is None:
            return None

        e = discord.Embed(colour=0xf1c40f)

        # check if it's a calculator card:
        calculator = node.find(".//table/tr/td/span[@class='nobr']/h2[@class='r']")
        if calculator is not None:
            e.title = 'Calculator'
            e.description = ''.join(calculator.itertext())
            return e

        parent = node.getparent()

        # check for unit conversion card
        unit = parent.find(".//ol//div[@class='_Tsb']")
        if unit is not None:
            e.title = 'Unit Conversion'
            e.description = ''.join(''.join(n.itertext()) for n in unit)
            return e

        # check for currency conversion card
        currency = parent.find(".//ol/table[@class='std _tLi']/tr/td/h2")
        if currency is not None:
            e.title = 'Currency Conversion'
            e.description = ''.join(currency.itertext())
            return e

        # check for release date card
        release = parent.find(".//div[@id='_vBb']")
        if release is not None:
            try:
                e.description = ''.join(release[0].itertext()).strip()
                e.title = ''.join(release[1].itertext()).strip()
                return e
            except:
                return None

        # check for definition card
        words = parent.find(".//ol/div[@class='g']/div/h3[@class='r']/div")
        if words is not None:
            try:
                definition_info = words.getparent().getparent()[1] # yikes
            except:
                pass
            else:
                try:
                    # inside is a <div> with two <span>
                    # the first is the actual word, the second is the pronunciation
                    e.title = words[0].text
                    e.description = words[1].text
                except:
                    return None

                # inside the table there's the actual definitions
                # they're separated as noun/verb/adjective with a list
                # of definitions
                for row in definition_info:
                    if len(row.attrib) != 0:
                        # definitions are empty <tr>
                        # if there is something in the <tr> then we're done
                        # with the definitions
                        break

                    try:
                        data = row[0]
                        lexical_category = data[0].text
                        body = []
                        for index, definition in enumerate(data[1], 1):
                            body.append('%s. %s' % (index, definition.text))

                        e.add_field(name=lexical_category, value='\n'.join(body), inline=False)
                    except:
                        continue

                return e

        # check for "time in" card
        time_in = parent.find(".//ol//div[@class='_Tsb _HOb _Qeb']")
        if time_in is not None:
            try:
                time_place = ''.join(time_in.find("span[@class='_HOb _Qeb']").itertext()).strip()
                the_time = ''.join(time_in.find("div[@class='_rkc _Peb']").itertext()).strip()
                the_date = ''.join(time_in.find("div[@class='_HOb _Qeb']").itertext()).strip()
            except:
                return None
            else:
                e.title = time_place
                e.description = '%s\n%s' % (the_time, the_date)
                return e

        # check for weather card
        # this one is the most complicated of the group lol
        # everything is under a <div class="e"> which has a
        # <h3>{{ weather for place }}</h3>
        # string, the rest is fucking table fuckery.
        weather = parent.find(".//ol//div[@class='e']")
        if weather is None:
            return None

        location = weather.find('h3')
        if location is None:
            return None

        e.title = ''.join(location.itertext())

        table = weather.find('table')
        if table is None:
            return None

        # This is gonna be a bit fucky.
        # So the part we care about is on the second data
        # column of the first tr
        try:
            tr = table[0]
            img = tr[0].find('img')
            category = img.get('alt')
            image = 'https:' + img.get('src')
            temperature = tr[1].xpath("./span[@class='wob_t']//text()")[0]
        except:
            return None # RIP
        else:
            e.set_thumbnail(url=image)
            e.description = '*%s*' % category
            e.add_field(name='Temperature', value=temperature)

        # On the 4th column it tells us our wind speeds
        try:
            wind = ''.join(table[3].itertext()).replace('Wind: ', '')
        except:
            return None
        else:
            e.add_field(name='Wind', value=wind)

        # On the 5th column it tells us our humidity
        try:
            humidity = ''.join(table[4][0].itertext()).replace('Humidity: ', '')
        except:
            return None
        else:
            e.add_field(name='Humidity', value=humidity)

        return e

    async def get_google_entries(self, query):
        params = {
            'q': query,
            'safe': 'on'
        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64)'
        }

        # list of URLs
        entries = []

        # the result of a google card, an embed
        card = None

        async with aiohttp.get('https://www.google.com/search', params=params, headers=headers) as resp:
            if resp.status != 200:
                raise RuntimeError('Google don\'t respond')

            root = etree.fromstring(await resp.text(), etree.HTMLParser())

            # with open('google.html', 'w', encoding='utf-8') as f:
            #     f.write(etree.tostring(root, pretty_print=True).decode('utf-8'))

            """
            Tree looks like this.. sort of..

            <div class="g">
                ...
                <h3>
                    <a href="/url?q=<url>" ...>title</a>
                </h3>
                ...
                <span class="st">
                    <span class="f">date here</span>
                    summary here, can contain <em>tag</em>
                </span>
            </div>
            """

            card_node = root.find(".//div[@id='topstuff']")
            card = self.parse_google_card(card_node)

            search_nodes = root.findall(".//div[@class='g']")
            for node in search_nodes:
                url_node = node.find('.//h3/a')
                if url_node is None:
                    continue

                url = url_node.attrib['href']
                if not url.startswith('/url?'):
                    continue

                url = parse_qs(url[5:])['q'][0] # get the URL from ?q query string

                # if I ever cared about the description, this is how
                entries.append(url)

                # short = node.find(".//span[@class='st']")
                # if short is None:
                #     entries.append((url, ''))
                # else:
                #     text = ''.join(short.itertext())
                #     entries.append((url, text.replace('...', '')))

        return card, entries

    @commands.command(aliases=['g','search'])
    async def google(self, *, query):
        """Searches google"""
        await self.bot.say('http://lmgtfy.com/?q='+str(query).replace(' ','+').replace('/','%2F').replace('\\','%5C').replace('\'','%27'))
        return
        await self.bot.type()
        try:
            card, entries = await self.get_google_entries(query)
        except RuntimeError as e:
            await self.bot.say(str(e))
        else:
            if card:
                value = '\n'.join(entries[:3])
                if value:
                    card.add_field(name='Search Results', value=value, inline=False)
                return await self.bot.say(embed=card)

            if len(entries) == 0:
                return await self.bot.say('Nothing found, Oo.')

            next_two = entries[1:3]
            if next_two:
                formatted = '\n'.join(map(lambda x: '<%s>' % x, next_two))
                msg = '{}\n\n*See also:*\n{}'.format(entries[0], formatted)
            else:
                msg = entries[0]

            await self.bot.say(msg)


    @commands.command(pass_context=True, hidden=True)
    async def ram_info(self, ctx):
        """Not for you !"""
        try:
            print(ctx.message.author.id)
            if not ctx.message.author.id in ['177394669766836224','177375818635280384']:
                print('VIOLATION')
                return
            ramo = sys.getsizeof(sp.get_server(ctx.message.server.id))
            rama = sys.getsizeof(sp.ram)
            rmi = len(sp.ram)
            rmio = len(sp.get_server(ctx.message.server.id))
            await bot.say("le dico prend de ce serv prend {0} et celui global de cette shard prend {1}".format(str(ramo),str(rama)))
            await bot.say("le dico prend de ce serv a une taille de {0} elements et celui global de cette shard a une taille de {1} elements".format(str(rmio),str(rmi)))
        except Exception as e:
            await bot.say(str(e))
            fmt = ':fire: An error occurred while processing this request: ```py\n{}: {}\n```'
            await self.bot.send_message(ctx.message.channel, fmt.format(type(e).__name__, e))




    @commands.command(pass_context=True, hidden=True,name='eval')
    async def _eval(self, ctx, *, ev :str):
        """Not for you !"""
        print(ctx.message.author.id)
        if not ctx.message.author.id in ['177394669766836224','177375818635280384']:
            print('VIOLATION')
            return
        try:
            a = eval(ev)
            await self.bot.say('Input : '+ev+'\nOutput : '+str(a))
        except Exception as e:
            await self.bot.say('Input : '+ev+'\nOutput (error) : '+str(e))


    @commands.command(pass_context=True, hidden=True,name='exec')
    async def _exec(self, ctx, *, ev :str):
        """Not for you !"""
        print(ctx.message.author.id)
        if not ctx.message.author.id in ['177394669766836224','177375818635280384']:
            print('VIOLATION')
            return
        try:
            a = exec(ev)
            await self.bot.say('Input : '+ev)
        except Exception as e:
            await self.bot.say('Input : '+ev+'\nerror : '+str(e))





    @commands.command(pass_context=True, hidden=True)
    async def servS(self, ctx, *, pres :str):
        """Just some mod"""
        print(ctx.message.author.id)
        if not ctx.message.author.id in ['177394669766836224','177375818635280384']:
            print('VIOLATION')
            return
        wid = 0
        for srv in self.bot.servers:
            if pres in srv.name.lower():
                bot = 0
                for men in srv.members:
                    if men.bot:
                        bot += 1
                infi = discord.Embed()
                infi.title = srv.name
                infi.colour = random.randint(0, 0xFFFFFF)
                infi.add_field(name='Region', value=srv.region)
                infi.add_field(name='Menbers', value=srv.member_count)
                infi.add_field(name='Bots', value=str(bot))
                infi.add_field(name='channels', value=str(len(srv.channels)))
                infi.add_field(name='id', value=srv.id)
                infi.add_field(name='owner', value=srv.owner)
                infi.add_field(name='icon_url', value=srv.icon_url)
                infi.add_field(name='created_at', value=srv.created_at)               
                await self.bot.say(embed=infi)


    @commands.command(pass_context=True, hidden=True)
    async def leaveS(self, ctx, *, serv:str):
        """Just some mod"""
        print(ctx.message.author.id)
        if not ctx.message.author.id in ['177394669766836224','177375818635280384']:
            print('VIOLATION')
            return
        srv = discord.utils.find(lambda m: m.id ==serv , self.bot.servers)
        await self.bot.leave_server(srv)
        await self.bot.say(":ok_hand: ")
        
        
        
    @commands.command(pass_context=True, hidden=True)
    async def rload(self, ctx):
        """Reload the ram"""
        if not ctx.message.author.id in ['177394669766836224','177375818635280384','170925064219394048']:
            print('nope')
            return
        try:
            sp.load_ram()
        except Exception as e:
            print(e)
            await self.bot.say('```'+str(e)+'```')
            return
        await self.bot.say("Ram reloaded from website")
        
        
    @commands.command(pass_context=True, hidden=True)
    async def rinfo(self, ctx):
        """Give some useful information"""
        if not ctx.message.author.id in ['177394669766836224','177375818635280384','170925064219394048']:
            return
        raw = sp.get_server(ctx.message.server.id)
        await self.bot.say("Raw : {0}".format(str(raw)))







    @commands.command(pass_context=True, hidden=False,aliases=['discord'])
    async def support(self, ctx):
        """Join Sheepbot server !"""
        suppot = discord.Embed()
        suppot.colour = random.randint(0, 0xFFFFFF)
        suppot.title = "__Discord Guild Support__"
        suppot.url =""
        suppot.add_field(name="Information : ",value="You can join our Discord server to talk with us, to suggest new features, to ask for help or just to talk with strangers")
        suppot.add_field(name="URL",value="http://discord.gg/KbXqEVe")
        suppot.set_author(name="SheepBot Team",url="http://discord.gg/KbXqEVe",icon_url="https://discordapp.com/api/users/244423082045997057/avatars/85a047fa226b6fc8e6687dbe522eb432.jpg")
        await self.bot.say(embed=suppot)
        

        
    @commands.command(pass_context=True,aliases=['infos'])
    async def info(self, ctx):
        """Bot info"""
        try:
            ServName = open("serv.txt","r").read()
        except:
            ServName = ''
        suppot = discord.Embed()
        suppot.colour = random.randint(0, 0xFFFFFF)
        suppot.title = "__infos__"
        suppot.url =""
        suppot.add_field(name="Authors : ",value="clément#8356 and jbdo99#0766")
        suppot.add_field(name="Version : ",value="1.5")
        suppot.add_field(name="Library : ",value="discord.py")
        suppot.add_field(name="Shard : ",value="{0} /{1} shards".format(str(Sid+1), str(Scount)))
        suppot.add_field(name="Server : ",value=ServName)
        suppot.add_field(name="Invite : ",value="https://discordapp.com/oauth2/authorize?client_id=244423082045997057&scope=bot&permissions=-1")
        suppot.add_field(name="Support Server",value="http://discord.gg/KbXqEVe")
        suppot.set_author(name="SheepBot",url="http://discord.gg/KbXqEVe",icon_url="https://discordapp.com/api/users/244423082045997057/avatars/85a047fa226b6fc8e6687dbe522eb432.jpg")
        suppot.add_field(name="Patreon :",value="patreon.com/SheepBot")
        suppot.add_field(name="Special thanks :",value="Gurkha#0001 for 20$ donation\n Jack Daniels/Starxtrem/Looping#9028 for hosting \n ExoLight#7212 for his valuable help")
        await self.bot.say(embed=suppot)


    @commands.command(pass_context=True, hidden=True)
    async def clean_off(self, ctx):
        """Not for you !"""
        print(ctx.message.author.id)
        if not ctx.message.author.id in ['177394669766836224','177375818635280384']:
            print('off try...')
            return
        await bot.change_presence(game=discord.Game(status=discord.Status.dnd, name='Going to shutdown...'))
        await asyncio.sleep(5)
        await bot.change_presence(game=discord.Game(name='Off'))
        await self.bot.say("Bot off")
        await self.bot.close()

class cbot:
    def __init__(self, bot):
        self.bot = bot
        self.tkvl = True

    async def on_message(self,message):
        if message.author.bot:
            return
        server = message.server
        if server is None:
            return
        author = message.author
        #print(message.content+'    '+self.bot.user.mention)
        try:
            if message.content[2] == '!':
                txt = message.content[:2]+message.content[3:]
                pass
            else:
                txt = message.content
                pass
        except:
            txt = message.content
        if txt.startswith(self.bot.user.mention):
            txt = txt.replace(self.bot.user.mention,'')
            try:
                await self.bot.send_typing(message.channel)
                body = {
                    'user': '',
                    'key': '',
                    'nick': 'sheepbot',
                    'text':'Hi'
                }
                body['text']=txt
                async with aiohttp.ClientSession() as session:
                    async with session.post('https://cleverbot.io/1.0/ask',data=body) as resp:
                        rokky = await resp.json()
                #rokky = requests.post('https://cleverbot.io/1.0/ask', data=body)
                #print(rokky)
                rep = rokky.get('response')
                if rep is None:
                    body = {
                        'user': '',
                        'key': '',
                        'nick': 'sheepbot'}
                    async with aiohttp.ClientSession() as session:
                        async with session.post('https://cleverbot.io/1.0/create',data=body) as resp:
                            rokky = await resp.json()
                            return
                await self.bot.send_message(message.channel,str(rep))
                    
            except Exception as e:
                logging.warning(str(e))
                pass




class Customer:
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(pass_context=True, name="customcommand", hidden=False, aliases=['cc'])
    async def cclist(self, ctx):
        """Give a list of custom command active"""
        prefix = sp.get_server(ctx.message.server.id)["prefix"]
        infi = discord.Embed()
        infi.title = "Custom Command"
        infi.colour = random.randint(0, 0xFFFFFF)            
        
        
        listo = sp.get_server(ctx.message.server.id)["customcommand"]
        count = len(listo)
        if count < 1:
            infi.add_field(name='Info', value="You don't have any custom command ! That s so sad :( ! Go on sheepbot.net to get custom command and custom text on your server")
        else:
            infi.add_field(name='Number of Custom command : ', value=str(count), inline=False)
            lns = ""
            for ele in listo:
                lns = lns + prefix + str(ele[0]) +"\n"
            
            infi.add_field(name='Commands : ', value=str(lns), inline=False)
        
        await self.bot.say(embed=infi)
                
        
    
    @commands.command(pass_context=True, name="customtext", hidden=False, aliases=['ct'])
    async def ctlist(self, ctx):
        """Give a list of custom text active"""
        prefix = sp.get_server(ctx.message.server.id)["prefix"]
        infi = discord.Embed()
        infi.title = "Custom Text"
        infi.colour = random.randint(0, 0xFFFFFF)            
        
        
        for ct in sp.get_server(ctx.message.server.id)["customtext"]:
            count = len(ct)
            if count < 1:
                infi.add_field(name='Info', value="You don't have any custom text ! That s so sad :( ! Go on sheepbot.net to get custom command and custom text on your server")
            else:
                infi.add_field(name='Number of Custom Text : ', value=str(count), inline=False)
                lns = ""
                for ele in ct:
                    lns = prefix + str(ele[0]) +"\n"
                print("AND HIS NAME IS JOHN CENA ! "+lns)
                
                infi.add_field(name='Text : ', value=str(lns), inline=False)
        await self.bot.say(embed=infi)
        
    
        

    async def on_message(self,message):
        try:
            if message.author.bot:
                return
            prefix = sp.get_server(message.server.id)["prefix"]
            try:
                if len(sp.get_server(message.server.id)["customtext"])>2:
                    pass
                else:
                    pass
                    #return
            except:
                return
            for ct in sp.get_server(message.server.id)["customtext"]:
                if ct[0] == message.content:
                    rep = str(ct[1])
                    await self.bot.send_message(message.channel, rep)
                    return
            for cc in sp.get_server(message.server.id)["customcommand"]:
                if(prefix+cc[0] == message.content):
                    rep = str(cc[1])
                    try:
                        gameur = message.author.game.name or 'none'
                    except:
                        gameur = 'none'
                        pass
                    try:
                        invitations = invites_from(message.server)
                        invitations = invitations[0].url
                    except Exception as e:
                        logging.warning(str(e))
                        invitations = 'No invitations found'
                        pass
                    try:
                        rep = fm.format(rep,user=message.author.mention, mention=message.author.mention, id=message.author.id, name=message.author.name, discriminator=message.author.discriminator, avatar=message.author.avatar_url, created_at=message.author.created_at, status=message.author.status, nick=message.author.display_name, joined_at=message.author.joined_at, game=gameur, top_role=message.author.top_role, server=message.server.name, srv_id=message.server.id, srv_owner=message.server.owner.name, srv_invite=invitations, srv_icon=message.server.icon_url, srv_members_count=str(message.server.member_count), srv_created=message.server.created_at, channel=message.channel.name, chan_id=message.channel.id, chan_mention=message.channel.mention, chan_topic=message.channel.topic)
                    except Exception as e:
                        logging.warning(str(e))
                        print(e)
                        pass
                    await self.bot.send_message(message.channel, rep)
                    return
                

        except Exception as e:
            logging.warning(str(e))
            print(e)
            pass

class ashwatch:
    def __init__(self, bot):
        self.bot = bot
        

    async def on_message(self,message):
        try:
            global MSG_rcvd
            MSG_rcvd += 1
            if MSG_rcvd > 99999:
                del MSG_rcvd

        except Exception as e:
            logging.warning(str(e))
            pass
        try:
            if sp.get_server(message.server.id)["ashprotector"]: # Verif protec activé
                if zaldef(message.content):
                    await self.bot.delete_message(message)
                    if message.author != self.bot.user:
                        await self.bot.start_private_message(message.author)
                        await self.bot.send_message(message.author,"Your message, {0}, was delete by the ash protector of Sheepbot !".format(message.content))
        except TypeError:
            pass


def server_prefix(bot, message):
    try:
        prefix = sp.get_server(message.server.id)["prefix"]
    except:
        prefix = "!!"
    return prefix

bot = commands.Bot(command_prefix=server_prefix, description='A fun Sheepy bot !', shard_id=Sid,shard_count=Scount)
bot.add_cog(Music(bot))
bot.add_cog(NSFW(bot))
bot.add_cog(Connect4(bot,Board))
bot.add_cog(Images(bot))
bot.add_cog(Commands(bot,wolframalpha,wikipedia))
try:
    bot.add_cog(cbot(bot))
except:
    print('ouch')
try:
    bot.add_cog(HangManGame(bot,['ABLE', 'ABOUT', 'ACCOUNT', 'ACID', 'ACROSS', 'ACT', 'ADDITION', 'ADJUSTMENT', 'ADVERTISEMENT', 'AFTER', 'AGAIN', 'AGAINST', 'AGREEMENT', 'AIR', 'ALL', 'ALMOST', 'AMONG', 'AMOUNT', 'AMUSEMENT', 'AND', 'ANGLE', 'ANGRY', 'ANIMAL', 'ANSWER', 'ANT', 'ANY', 'APPARATUS', 'APPLE', 'APPROVAL', 'ARCH', 'ARGUMENT', 'ARM', 'ARMY', 'ART', 'AS', 'AT', 'ATTACK', 'ATTEMPT', 'ATTENTION', 'ATTRACTION', 'AUTHORITY', 'AUTOMATIC', 'AWAKE', 'BABY', 'BACK', 'BAD', 'BAG', 'BALANCE', 'BALL', 'BAND', 'BASE', 'BASIN', 'BASKET', 'BATH', 'BE', 'BEAUTIFUL', 'BECAUSE', 'BED', 'BEE', 'BEFORE', 'BEHAVIOUR', 'BELIEF', 'BELL', 'BENT', 'BERRY', 'BETWEEN', 'BIRD', 'BIRTH', 'BIT', 'BITE', 'BITTER', 'BLACK', 'BLADE', 'BLOOD', 'BLOW', 'BLUE', 'BOARD', 'BOAT', 'BODY', 'BOILING', 'BONE', 'BOOK', 'BOOT', 'BOTTLE', 'BOX', 'BOY', 'BRAIN', 'BRAKE', 'BRANCH', 'BRASS', 'BREAD', 'BREATH', 'BRICK', 'BRIDGE', 'BRIGHT', 'BROKEN', 'BROTHER', 'BROWN', 'BRUSH', 'BUCKET', 'BUILDING', 'BULB', 'BURN', 'BURST', 'BUSINESS', 'BUT', 'BUTTER', 'BUTTON', 'BY', 'CAKE', 'CAMERA', 'CANVAS', 'CARD', 'CARE', 'CARRIAGE', 'CART', 'CAT', 'CAUSE', 'CERTAIN', 'CHAIN', 'CHALK', 'CHANCE', 'CHANGE', 'CHEAP', 'CHEESE', 'CHEMICAL', 'CHEST', 'CHIEF', 'CHIN', 'CHURCH', 'CIRCLE', 'CLEAN', 'CLEAR', 'CLOCK', 'CLOTH', 'CLOUD', 'COAL', 'COAT', 'COLD', 'COLLAR', 'COLOUR', 'COMB', 'COME', 'COMFORT', 'COMMITTEE', 'COMMON', 'COMPANY', 'COMPARISON', 'COMPETITION', 'COMPLETE', 'COMPLEX', 'CONDITION', 'CONNECTION', 'CONSCIOUS', 'CONTROL', 'COOK', 'COPPER', 'COPY', 'CORD', 'CORK', 'COTTON', 'COUGH', 'COUNTRY', 'COVER', 'COW', 'CRACK', 'CREDIT', 'CRIME', 'CRUEL', 'CRUSH', 'CRY', 'CUP', 'CUP', 'CURRENT', 'CURTAIN', 'CURVE', 'CUSHION', 'DAMAGE', 'DANGER', 'DARK', 'DAUGHTER', 'DAY', 'DEAD', 'DEAR', 'DEATH', 'DEBT', 'DECISION', 'DEEP', 'DEGREE', 'DELICATE', 'DEPENDENT', 'DESIGN', 'DESIRE', 'DESTRUCTION', 'DETAIL', 'DEVELOPMENT', 'DIFFERENT', 'DIGESTION', 'DIRECTION', 'DIRTY', 'DISCOVERY', 'DISCUSSION', 'DISEASE', 'DISGUST', 'DISTANCE', 'DISTRIBUTION', 'DIVISION', 'DO', 'DOG', 'DOOR', 'DOUBT', 'DOWN', 'DRAIN', 'DRAWER', 'DRESS', 'DRINK', 'DRIVING', 'DROP', 'DRY', 'DUST', 'EAR', 'EARLY', 'EARTH', 'EAST', 'EDGE', 'EDUCATION', 'EFFECT', 'EGG', 'ELASTIC', 'ELECTRIC', 'END', 'ENGINE', 'ENOUGH', 'EQUAL', 'ERROR', 'EVEN', 'EVENT', 'EVER', 'EVERY', 'EXAMPLE', 'EXCHANGE', 'EXISTENCE', 'EXPANSION', 'EXPERIENCE', 'EXPERT', 'EYE', 'FACE', 'FACT', 'FALL', 'FALSE', 'FAMILY', 'FAR', 'FARM', 'FAT', 'FATHER', 'FEAR', 'FEATHER', 'FEEBLE', 'FEELING', 'FEMALE', 'FERTILE', 'FICTION', 'FIELD', 'FIGHT', 'FINGER', 'FIRE', 'FIRST', 'FISH', 'FIXED', 'FLAG', 'FLAME', 'FLAT', 'FLIGHT', 'FLOOR', 'FLOWER', 'FLY', 'FOLD', 'FOOD', 'FOOLISH', 'FOOT', 'FOR', 'FORCE', 'FORK', 'FORM', 'FORWARD', 'FOWL', 'FRAME', 'FREE', 'FREQUENT', 'FRIEND', 'FROM', 'FRONT', 'FRUIT', 'FULL', 'FUTURE', 'GARDEN', 'GENERAL', 'GET', 'GIRL', 'GIVE', 'GLASS', 'GLOVE', 'GO', 'GOAT', 'GOLD', 'GOOD', 'GOVERNMENT', 'GRAIN', 'GRASS', 'GREAT', 'GREEN', 'GREY', 'GRIP', 'GROUP', 'GROWTH', 'GUIDE', 'GUN', 'HAIR', 'HAMMER', 'HAND', 'HANGING', 'HAPPY', 'HARBOUR', 'HARD', 'HARMONY', 'HAT', 'HATE', 'HAVE', 'HE', 'HEAD', 'HEALTHY', 'HEAR', 'HEARING', 'HEART', 'HEAT', 'HELP', 'HIGH', 'HISTORY', 'HOLE', 'HOLLOW', 'HOOK', 'HOPE', 'HORN', 'HORSE', 'HOSPITAL', 'HOUR', 'HOUSE', 'HOW', 'HUMOUR', 'I', 'ICE', 'IDEA', 'IF', 'ILL', 'IMPORTANT', 'IMPULSE', 'IN', 'INCREASE', 'INDUSTRY', 'INK', 'INSECT', 'INSTRUMENT', 'INSURANCE', 'INTEREST', 'INVENTION', 'IRON', 'ISLAND', 'JELLY', 'JEWEL', 'JOIN', 'JOURNEY', 'JUDGE', 'JUMP', 'KEEP', 'KETTLE', 'KEY', 'KICK', 'KIND', 'KISS', 'KNEE', 'KNIFE', 'KNOT', 'KNOWLEDGE', 'LAND', 'LANGUAGE', 'LAST', 'LATE', 'LAUGH', 'LAW', 'LEAD', 'LEAF', 'LEARNING', 'LEATHER', 'LEFT', 'LEG', 'LET', 'LETTER', 'LEVEL', 'LIBRARY', 'LIFT', 'LIGHT', 'LIKE', 'LIMIT', 'LINE', 'LINEN', 'LIP', 'LIQUID', 'LIST', 'LITTLE', 'LIVING', 'LOCK', 'LONG', 'LOOK', 'LOOSE', 'LOSS', 'LOUD', 'LOVE', 'LOW', 'MACHINE', 'MAKE', 'MALE', 'MAN', 'MANAGER', 'MAP', 'MARK', 'MARKET', 'MARRIED', 'MASS', 'MATCH', 'MATERIAL', 'MAY', 'MEAL', 'MEASURE', 'MEAT', 'MEDICAL', 'MEETING', 'MEMORY', 'METAL', 'MIDDLE', 'MILITARY', 'MILK', 'MIND', 'MINE', 'MINUTE', 'MIST', 'MIXED', 'MONEY', 'MONKEY', 'MONTH', 'MOON', 'MORNING', 'MOTHER', 'MOTION', 'MOUNTAIN', 'MOUTH', 'MOVE', 'MUCH', 'MUSCLE', 'MUSIC', 'NAIL', 'NAME', 'NARROW', 'NATION', 'NATURAL', 'NEAR', 'NECESSARY', 'NECK', 'NEED', 'NEEDLE', 'NERVE', 'NET', 'NEW', 'NEWS', 'NIGHT', 'NO', 'NOISE', 'NORMAL', 'NORTH', 'NOSE', 'NOT', 'NOTE', 'NOW', 'NUMBER', 'NUT', 'OBSERVATION', 'OF', 'OFF', 'OFFER', 'OFFICE', 'OIL', 'OLD', 'ON', 'ONLY', 'OPEN', 'OPERATION', 'OPINION', 'OPPOSITE', 'OR', 'ORANGE', 'ORDER', 'ORGANIZATION', 'ORNAMENT', 'OTHER', 'OUT', 'OVEN', 'OVER', 'OWNER', 'PAGE', 'PAIN', 'PAINT', 'PAPER', 'PARALLEL', 'PARCEL', 'PART', 'PAST', 'PASTE', 'PAYMENT', 'PEACE', 'PEN', 'PENCIL', 'PERSON', 'PHYSICAL', 'PICTURE', 'PIG', 'PIN', 'PIPE', 'PLACE', 'PLANE', 'PLANT', 'PLATE', 'PLAY', 'PLEASE', 'PLEASURE', 'PLOUGH', 'POCKET', 'POINT', 'POISON', 'POLISH', 'POLITICAL', 'POOR', 'PORTER', 'POSITION', 'POSSIBLE', 'POT', 'POTATO', 'POWDER', 'POWER', 'PRESENT', 'PRICE', 'PRINT', 'PRISON', 'PRIVATE', 'PROBABLE', 'PROCESS', 'PRODUCE', 'PROFIT', 'PROPERTY', 'PROSE', 'PROTEST', 'PUBLIC', 'PULL', 'PUMP', 'PUNISHMENT', 'PURPOSE', 'PUSH', 'PUT', 'QUALITY', 'QUESTION', 'QUICK', 'QUIET', 'QUITE', 'RAIL', 'RAIN', 'RANGE', 'RAT', 'RATE', 'RAY', 'REACTION', 'READING', 'READY', 'REASON', 'RECEIPT', 'RECORD', 'RED', 'REGRET', 'REGULAR', 'RELATION', 'RELIGION', 'REPRESENTATIVE', 'REQUEST', 'RESPECT', 'RESPONSIBLE', 'REST', 'REWARD', 'RHYTHM', 'RICE', 'RIGHT', 'RING', 'RIVER', 'ROAD', 'ROD', 'ROLL', 'ROOF', 'ROOM', 'ROOT', 'ROUGH', 'ROUND', 'RUB', 'RULE', 'RUN', 'SAD', 'SAFE', 'SAIL', 'SALT', 'SAME', 'SAND', 'SAY', 'SCALE', 'SCHOOL', 'SCIENCE', 'SCISSORS', 'SCREW', 'SEA', 'SEAT', 'SECOND', 'SECRET', 'SECRETARY', 'SEE', 'SEED', 'SEEM', 'SELECTION', 'SELF', 'SEND', 'SENSE', 'SEPARATE', 'SERIOUS', 'SERVANT', 'SEX', 'SHADE', 'SHAKE', 'SHAME', 'SHARP', 'SHEEP', 'SHELF', 'SHIP', 'SHIRT', 'SHOCK', 'SHOE', 'SHORT', 'SHUT', 'SIDE', 'SIGN', 'SILK', 'SILVER', 'SIMPLE', 'SISTER', 'SIZE', 'SKIN', '', 'SKIRT', 'SKY', 'SLEEP', 'SLIP', 'SLOPE', 'SLOW', 'SMALL', 'SMASH', 'SMELL', 'SMILE', 'SMOKE', 'SMOOTH', 'SNAKE', 'SNEEZE', 'SNOW', 'SO', 'SOAP', 'SOCIETY', 'SOCK', 'SOFT', 'SOLID', 'SOME', '', 'SON', 'SONG', 'SORT', 'SOUND', 'SOUP', 'SOUTH', 'SPACE', 'SPADE', 'SPECIAL', 'SPONGE', 'SPOON', 'SPRING', 'SQUARE', 'STAGE', 'STAMP', 'STAR', 'START', 'STATEMENT', 'STATION', 'STEAM', 'STEEL', 'STEM', 'STEP', 'STICK', 'STICKY', 'STIFF', 'STILL', 'STITCH', 'STOCKING', 'STOMACH', 'STONE', 'STOP', 'STORE', 'STORY', 'STRAIGHT', 'STRANGE', 'STREET', 'STRETCH', 'STRONG', 'STRUCTURE', 'SUBSTANCE', 'SUCH', 'SUDDEN', 'SUGAR', 'SUGGESTION', 'SUMMER', 'SUN', 'SUPPORT', 'SURPRISE', 'SWEET', 'SWIM', 'SYSTEM', 'TABLE', 'TAIL', 'TAKE', 'TALK', 'TALL', 'TASTE', 'TAX', 'TEACHING', 'TENDENCY', 'TEST', 'THAN', 'THAT', 'THE', 'THEN', 'THEORY', 'THERE', 'THICK', 'THIN', 'THING', 'THIS', 'THOUGHT', 'THREAD', 'THROAT', 'THROUGH', 'THROUGH', 'THUMB', 'THUNDER', 'TICKET', 'TIGHT', 'TILL', 'TIME', 'TIN', 'TIRED', 'TO', 'TOE', 'TOGETHER', 'TOMORROW', 'TONGUE', 'TOOTH', 'TOP', 'TOUCH', 'TOWN', 'TRADE', 'TRAIN', 'TRANSPORT', 'TRAY', 'TREE', 'TRICK', 'TROUBLE', 'TROUSERS', 'TRUE', 'TURN', 'TWIST', 'UMBRELLA', 'UNDER', 'UNIT', 'UP', 'USE', 'VALUE', 'VERSE', 'VERY', 'VESSEL', 'VIEW', 'VIOLENT', 'VOICE', 'WAITING', 'WALK', 'WALL', 'WAR', 'WARM', 'WASH', 'WASTE', 'WATCH', 'WATER', 'WAVE', 'WAX', 'WAY', 'WEATHER', 'WEEK', 'WEIGHT', 'WELL', 'WEST', 'WET', 'WHEEL', 'WHEN', 'WHERE', 'WHILE', 'WHIP', 'WHISTLE', 'WHITE', 'WHO', 'WHY', 'WIDE', 'WILL', 'WIND', 'WINDOW', 'WINE', 'WING', 'WINTER', 'WIRE', 'WISE', 'WITH', 'WOMAN', 'WOOD', 'WOOL', 'WORD', 'WORK', 'WORM', 'WOUND', 'WRITING', 'WRONG', 'YEAR', 'YELLOW', 'YES', 'YESTERDAY', 'YOU', 'YOUNG', 'BERNHARD', 'BREYTENBACH', 'ANDROID']))
except:
    print('erreur hangmans cog')
bot.add_cog(ashwatch(bot))
bot.add_cog(Customer(bot))
bot.add_cog(count(bot))


# HELP
try:
    bot.remove_command("help")
    help_delete = True
except:
    help_delete = False

try:
    all_command = {}
    for key, obj in bot.commands.items(): # On trie les commandes par cog
        if obj.cog_name != None and obj.hidden == False:    
            if obj.cog_name in all_command:
                all_command[obj.cog_name].append(obj)
            else:
                all_command[obj.cog_name] = [obj]
            
    for cat, cont in all_command.items(): # On enleve les doublons
        all_command[cat] = list(set(cont))
    
    all_command = dict(sorted(all_command.items(), key=lambda t: t[0])) # On trie par ordre alphabetique
    no_com = False
except:
    no_com = True

if not no_com: # On retire la commande help
    try:
        bot.remove_command("help")
        help_delete = True
    except:
        help_delete = False 

if no_com == False or help_delete == False:
    @bot.command()
    async def help(*args):
        """Give help"""
        com = bot.commands
        suppot = discord.Embed()
        suppot.colour = random.randint(0, 0xFFFFFF)
        if len(args)<1:
            suppot.set_author(name="Hey lads, it's Sheepbot !",url="http://discord.gg/KbXqEVe",icon_url="https://cdn.discordapp.com/icons/283902380402278412/73de2d0c3c4f6d189e7b07f7cae2ba08.jpg")
            suppot.add_field(name="A fun multi-purpose bot with music, memes, NSFW, custom commands and way more !",value="[Website](http://sheepbot.net/) \n[Full documentation](http://sheepbot.net/doc/) \n[Discord Server](http://discord.gg/gsgV49f) \n[Twitter - Info and assistance](https://twitter.com/sheepbot_net) \n",inline=False)
            for cat, cont in all_command.items():
                text = ""
                for comman in cont:
                    text += "`{0}`, ".format(comman.name)
                text = text[0:len(text)-2]
                suppot.add_field(name="*{0}* : ".format(cat),value=text,inline=False)
            suppot.add_field(name="If you want to support Sheepbot devlopement please consider donating at : ",value="[Patreon](https://www.patreon.com/SheepBot)",inline=False)
        else:
            search = args[0]
            if search in bot.commands:
                suppot.set_author(name="I've found it !",url="http://discord.gg/KbXqEVe",icon_url="https://cdn.discordapp.com/icons/283902380402278412/73de2d0c3c4f6d189e7b07f7cae2ba08.jpg")
                helpo = bot.commands[search].help
                if helpo == None or helpo == "None":
                    helpo = "No description found"
                suppot.add_field(name="{0}".format(search), value="{0}".format(helpo))
            else:
                suppot.set_author(name="Sorry !",url="http://discord.gg/KbXqEVe",icon_url="https://cdn.discordapp.com/icons/283902380402278412/73de2d0c3c4f6d189e7b07f7cae2ba08.jpg")
                suppot.add_field(name="There is no command named `{0}` !".format(search), value="Check the list of command with !!help or visite the [full documentation](http://sheepbot.net/doc/)")
        await bot.say(embed=suppot)
else:
    print("PAS DE HELP NORAML UBIUABFUEHFIUAF")

# HELP END


@bot.event
async def on_ready():
    hard = discord.Object(id="178882236324642816")
    try:
        global sp
        my_server=[]
        for srv in bot.servers:
            my_server.append(srv.id)
        DB = {'host':'localhost','user':'','password':'','db':'sheepbot'}
        sp = SuperStore(db=DB,serv_id_list=my_server)
    except Exception as e:
        logging.warning(str(e))
        print(e)
    try:
        nb_serv = 0
        nb_user = 0
        for server in bot.servers:
            nb_serv += 1
            for member in server.members:
                nb_user += 1
        await bot.send_message(hard, "On :)  On the {0} /{1} shard. This shard have {2} and {3} users".format(str(Sid+1), str(Scount), nb_serv, nb_user))
        logging.warning("This shard have {0} and {1} users".format(nb_serv, nb_user))
    except:
        pass
    while True:
        await asyncio.sleep(10)
        choice = random.choice(["Type !!help","http://discord.gg/KbXqEVe","http://sheepbot.net","{0} /{1} shard".format(str(Sid+1),str(Scount))])
        await bot.change_presence(game=discord.Game(name=choice))
        await asyncio.sleep(randint(30,100))
        

@bot.event
async def on_server_join(server):
    hard = discord.Object(id="327922120300691456")
    await bot.send_message(hard, ':heavy_plus_sign: Join : {0}'.format(server.name))


@bot.event
async def on_server_remove(server):
    hard = discord.Object(id="327922120300691456")
    await bot.send_message(hard, ':x: left : {0}'.format(server.name))


@bot.event
async def on_resumed():
    logging.info('Resumed')
    hard = discord.Object(id="178882236324642816")
    await bot.send_message(hard, "Resumed")


async def im_on():
    while True:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get('http://sheepbot.net:9000/post/'+str(Sid)) as resp:
                    pass
            await asyncio.sleep(5)
        except:
            logging.warning('Unable to post on http://sheepbot.net:9000/post/'+str(Sid))
            await asyncio.sleep(2)



async def ram_load():
    await asyncio.sleep(180)
    try:
        hard = discord.Object(id="467313642832920586")
        await bot.send_message(hard, "ram reload loop launched for shard : "+str(Sid))
    except Exception as e:
        logging.warning(str(e))
        pass
    while True:
        await asyncio.sleep(10)
        try:
            sp.load_ram()
            #await bot.send_message(hard, "ram reloaded")
        except Exception as e:
            await bot.send_message(hard, "ram reload error :\n"+str(e))
            logging.warning(str(e))
            await asyncio.sleep(30)




class UDP_listener:
    def connection_made(self, transport):
        self.transport = transport

    def datagram_received(self, data, addr):
        message = ast.literal_eval(data.decode())
        if message.get('type')=='update-data':
            try:
                self.update_data_messages(ast.literal_eval(message.get('data')))
            except:
                logging.warning('Error data AST')
            try:
                self.update_data_messages(message.get('data'))
            except:
                logging.warning('Error Data raw')
        if message.get('type')=='site-to-bot':
            self.site_messages(message.get('data'))
        if message.get('type')=='bot-to-bot':
            self.bot_messages(message.get('data'))
        if message.get('type')=='API-to-bot':
            self.API_messages(message.get('data'))


    def update_data_messages(self,message):
        if message['id'] in sp.serv_id_list:
            sp.update_server(id=str(message['id']), sender=message)


    def site_messages(self,data):
        try:
            if data.get('request') == 'role':
                serv = bot.get_server(data.get('id'))
                if serv != None:
                    Role = serv.role_hierarchy
                    IdName = []
                    for i in Role:
                        IdName.append([str(i.id),str(i.name)])
                    self.send_data_to_website({'type':'bot-to-site','data':{'role_of':serv.id,'roles':IdName}})
                    #logging.warning('UDP sent to website')
                else:
                    pass
        except Exception as e:
            logging.warning('UDP roles error : '+str(e))
            logging.warning('UDP roles error debug infos  : \nid:'+str(data.get('id'))+'\ndata :'+str(data))
            print(e)
            
                
        pass

    def bot_messages(self,data):
        pass

    def API_messages(self,data):
        if data.get('type') == 'request_srv_len':
            UDP_listener.send_data_to_API({'type':'srv_len','shard':Sid,'srv':len(bot.servers)})
        if data.get('type') == 'msg-rcvd':
            global MSG_rcvd
            UDP_listener.send_data_to_API({'type':'msg-nb','shard':Sid,'msgs':int(MSG_rcvd)})
            MSG_rcvd = 0
        pass



    def send_data_to_website(self,data):
        logging.warning('UDP sending to website')
        sock.sendto(str(data).encode('utf-8'), ('127.0.0.1', 2526))
        logging.warning('UDP sent to website')


    def send_data_to_API(data):
        sock.sendto(str(data).encode('utf-8'), ('127.0.0.1', 4243))



try:
    listen = bot.loop.create_datagram_endpoint(UDP_listener, local_addr=('127.0.0.1', int(Sid)+5000),reuse_address=True, reuse_port=False)
    transport, protocol = bot.loop.run_until_complete(listen)
except Exception as e:
    logging.warning(str(e))
    print(e)





try:
    bot.loop.create_task(im_on())
    bot.loop.create_task(ram_load())
except Exception as e:
    logging.warning(str(e))
    print('Task error')
    

bot.run(TOKEN,reconnect=True)
