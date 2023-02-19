#!/bin/python
# import tamper.securesphere as securesphere
import multipleespacio as multipleespacio
import tamper.apostrophemask as apostrophemask
import tamper.apostrophenullencode as apostrophenullencode
import tamper.base64encode as base64encode
import tamper.appendnullbyte as appendnullbyte
import tamper.between as between
import tamper.bluecoat as bluecoat
import tamper.chardoubleencode as chardoubleencode
import tamper.charencode as charencode
import tamper.charunicodeencode as charunicodeencode
import tamper.charunicodeescape as charunicodeescape
import tamper.commalesslimit as commalesslimit
import tamper.commalessmid as commalessmid
import tamper.commentbeforeparentheses as commentbeforeparentheses
import tamper.concat2concatws as concat2concatws
import tamper.equaltolike as equaltolike
import tamper.escapequotes as escapequotes
import tamper.greatest as greatest
import tamper.halfversionedmorekeywords as halfversionedmorekeywords
import tamper.hex2char as hex2char
import tamper.htmlencode as htmlencode
import tamper.ifnull2casewhenisnull as ifnull2casewhenisnull
import tamper.ifnull2ifisnull as ifnull2ifisnull
import tamper.informationschemacomment as informationschemacomment
import tamper.least as least
import tamper.lowercase as lowercase
import tamper.luanginx as luanginx
import tamper.modsecurityversioned as modsecurityversioned
import tamper.modsecurityzeroversioned as modsecurityzeroversioned
import tamper.multiplespaces as multiplespaces
import tamper.overlongutf8 as overlongutf8
import tamper.overlongutf8more as overlongutf8more
import tamper.percentage as percentage
import tamper.plus2concat as plus2concat
import tamper.plus2fnconcat as plus2fnconcat
import tamper.randomcase as randomcase
import tamper.randomcomments as randomcomments
import tamper.space2comment as space2comment
import tamper.space2dash as space2dash
import tamper.space2hash as space2hash
import tamper.space2morecomment as space2morecomment
import tamper.space2morehash as space2morehash
import tamper.space2mssqlblank as space2mssqlblank
import tamper.space2mssqlhash as space2mssqlhash
import tamper.space2mysqlblank as space2mysqlblank
import tamper.space2mysqldash as space2mysqldash
import tamper.space2plus as space2plus
import tamper.space2randomblank as space2randomblank
import tamper.sp_password as sp_password
import tamper.substring2leftright as substring2leftright
import tamper.symboliclogical as symboliclogical
import tamper.unionalltounion as unionalltounion
import tamper.unmagicquotes as unmagicquotes
import tamper.uppercase as uppercase
import tamper.varnish as varnish
import tamper.versionedkeywords as versionedkeywords
import tamper.versionedmorekeywords as versionedmorekeywords
import tamper.xforwardedfor as xforwardedfor
import time
import discord
from discord.ext import commands
import logging
# import file

print("\n[+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+]\n")

print('''
                       _       __ __      ___  _          _
 ___ ._ _  ___  ___  _| | ___ |  \  \ ___|_ _|| |_  ___ _| |_
/ ._>| ' |/ | '/ . \/ . |/ ._>|     |/ ._>| | | . |<_> | | |
\___.|_|_|\_|_.\___/\___|\___.|_|_|_|\___.|_| |_|_|<___| |_|
''')
print(" Payload encoder using sqlmap tampers.\n")
print("\n[+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+]\n")

# Configurar el objeto Logger
logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)

# Configurar el formateo del mensaje
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Configurar el manejador para enviar mensajes a la consola
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# Configurar el manejador para enviar mensajes a un archivo de texto
file_handler = logging.FileHandler('encoder-bot.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

listMSSQL = {between,charencode,charunicodeencode,equaltolike,greatest,multipleespacio,percentage,sp_password,space2comment,space2dash,space2mssqlblank,space2mysqldash,space2plus,space2randomblank,unionalltounion,unmagicquotes}
listMYSQL = {between,bluecoat,charencode,charunicodeencode,concat2concatws,equaltolike,greatest,ifnull2ifisnull,modsecurityversioned,modsecurityzeroversioned,multiplespaces,percentage,randomcase,space2comment,space2hash,space2morehash,space2mysqldash,space2plus,space2randomblank,unionalltounion,unmagicquotes,versionedkeywords,versionedmorekeywords,xforwardedfor}
listGeneric = {apostrophemask,apostrophenullencode,base64encode,between,chardoubleencode,charencode,charunicodeencode,equaltolike,greatest,ifnull2ifisnull,multiplespaces,percentage,randomcase,space2comment,space2plus,space2randomblank,unionalltounion,unmagicquotes}

named_tuple = time.localtime() # get struct_time
time_string = time.strftime("%m%d%Y-%H:%M", named_tuple)

bot = commands.Bot(command_prefix='!')

@bot.command()
async def encode(ctx, encoding_type, *, text):
    print("Let's encode: "+text)
    if encoding_type is "mysql":
        print("[+] You are using mysql default encoding options")
        logger.info('[+] You are using mysql default encoding options')
        payList = listMYSQL
        pass
    if encoding_type is "mssql":
        print("[+] You are using mssql default encoding options")
        logger.info('[+] You are using mssql default encoding options')
        payList = listMSSQL
        pass
    if encoding_type is "random-encode":
        result_dict = set().union(listMSSQL, listMYSQL, listGeneric)
        print("[+] Using random-encode default encoding options")   
        logger.info('[+] You are using random-encode default encoding options')
        selected_items = random.sample(result_dict, 7)
        payList = selected_items
    if encoding_type is "massive":
        print("[+] Using massive default encoding options")     
        logger.info('[+] You are using massive default encoding options')
        for lst in [listMSSQL, listMYSQL, listGeneric]:
            for item in lst:
                unique_dict[item] = True
                unique_list = list(unique_dict.keys())
        
    for payloadEncoder in payList:   
        try:
            print(payloadEncoder.tamper(sqlinjPayload))
            response = f'```{payloadEncoder.tamper(sqlinjPayload)}```'           
            pass
        except KeyError as e:
            logger.error(e)
            pass
            raise

    logger.debug('Sended response ')
    await ctx.send(response)


bot.run('DISCORD-BOT-TOKEN') 
