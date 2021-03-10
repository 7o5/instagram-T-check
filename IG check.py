reaper = input ("Enter Password : ")
if reaper == "EYE" :
        print ("Thanks..."*4)
else :
        print ("ERROR... ENTER PASSWORD...")
        os.system("exit")
import requests
import time
import sys
import os
from colorama import init,Fore
import random

green=""
red=""
white=""
blue=""
db_1 = ("1")
db_2 = ("2")
db_3 = ("3")
print("loding")
time.sleep(0.3)
print("10%■□□□□□□□□□")
time.sleep(0.3)
print("20%■■□□□□□□□□")
time.sleep(0.3)
print("30%■■■□□□□□□□")
time.sleep(0.3)
print("40%■■■■□□□□□□")
time.sleep(0.3)
print("50%■■■■■□□□□□")
time.sleep(0.3)
print("60%■■■■■■□□□□")
time.sleep(0.3)
print("70%■■■■■■■□□□")
time.sleep(0.3)
print("80%■■■■■■■■□□")
time.sleep(0.3)
print("90%■■■■■■■■■□")
time.sleep(0.3)
print("100%■■■■■■■■■")
time.sleep(0.4)
os.system("clear")
print("""

    __________   ________  ________________ __ ____ 
   /  _/ ____/  / ____/ / / / ____/ ____/ //_// __ \
   / // / __   / /   / /_/ / __/ / /   / ,<  / /_/ /
 _/ // /_/ /  / /___/ __  / /___/ /___/ /| |/ _, _/ 
/___/\____/   \____/_/ /_/_____/\____/_/ |_/_/ |_|  
                                                    

""")
print ("[1] user maker")
print ("[2] Checker")
print("[3]Turbo")
reaper=input("choose: ")
def Bot(data):
    listusers=[]
    for userId ,status in zip(data.profile.userId,data.profile.status):
       if status!=9 and status !=10:
           listusers.append(userId)
    return listusers

if reaper== db_1:
	print("_"*70)
	Users = int(input("[?] Enter How Many User Do You Want : "))


Letters = int(input("[?] Enter How Long Do You Want Letter : "))


def Make_users(data):


  Leeter = (Letters)


  User = ""


  while len(User) != Leeter:


    The_Choice = random.choice(data)


    User += The_Choice


  return User


Choose = 'qwertyuioplkjhgfdsaxzcvbnm1234576890___'


num = 0


for Make in range(Users):


   Done_User=Make_users(Choose)


   with open('users.txt', 'a+') as Type:


      Type.write(f"{Done_User}\n")


      num += 1


      print(f"\r[+] Successfully Make >> [{num}] [{Done_User}]", end="")


print("\n"+"-"*70)


print("[!] All Users Was Saved In [ users.txt ] File")

if reaper== db_2:
	from colorama import init,Fore
import requests, multiprocessing
import time

class Start:
    run = True
    a = []
    b = []
    SPACING = 23
    start_time = time.time()
    URL = f"https://www.instagram.com/"
    def link(self):
        start_time = time.time()
        
        # self.file_name = input("Eneter your list name/path: ")
        start = time.perf_counter()
        with open("users.txt",'r') as f:
            try:
                while True:
                    self.lines = f.readline().strip()
                    self.req = requests.get(f"https://www.instagram.com/{self.lines}")
                    if self.lines == '':
                        f.strip('\n')
                        f.close()
                    if self.req.status_code == 200:
                        print('\033[1;31;40m',' '*self.SPACING, self.lines , '    not avalible')
                        self.b.append(self.lines)
                    elif 404:
                        print(Fore.GREEN, ' '*self.SPACING ,self.lines,'    is Availble')
                        self.a.append(self.lines)
                    else:
                        print('\033[1;36;40m',' '*self.SPACING, self.lines , '    unknown')
            except Exception as e:
                print(Fore.CYAN,  "\n", ' '*12,"ALL USER HAVE BEEN CHECKED SUCCESSFULY \n",' '*18 ,"AND SAVED TO AVALIBLE.TXT",Fore.RESET)
                finish = time.perf_counter()
            except KeyboardInterrupt:
                print('\033[1;31;40m',' '*24,len(self.b),"users unavalible",Fore.RESET)
                print(Fore.GREEN, ' '*25,len(self.a),"users avalible",Fore.RESET)
                print('\033[1;31;40m',' '*27," Aborted.",Fore.RESET)
        self.avalible()
        finish = time.perf_counter()
        print(' '*25,'\033[95m','Finished in ' + str(round(finish-start, 2)))

    def avalible(self):
        with open("avalible.txt",'w') as f:
            for user in self.a:
                f.write("%s\n" % user)
                
checker = Start()
checker.link()

if reaper== db_3:
	import requests
from colorama import Fore

username_login = input('[+] Enter Username To Login in Instagram ==> : ')
password_login = input('[+] Enter Password ==> : ')
url_login = 'https://www.instagram.com/accounts/login/ajax/'
headers_login = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'content-length': '291',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'ig_did=3E70DB93-4A27-43EB-8463-E0BFC9B02AE1; mid=YCAadAALAAH35g_7e7h0SwBbFzBt; ig_nrcb=1; csrftoken=COmXgzKurrq8awSnRS1xf3u9rL6QsGZI',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent':'Mozilla/5.0 (Linux; Android 11; SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36',
    'x-csrftoken': 'COmXgzKurrq8awSnRS1xf3u9rL6QsGZI',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': '0',
    'x-instagram-ajax': '1cb44f68ffec',
    'x-requested-with': 'XMLHttpRequest'
}
data_login = {
    'username': username_login,
    'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1613414957:{password_login}',
    'queryParams': '{}',
    'optIntoOneTap': 'false'
}
req_login = requests.post(url_login, data=data_login, headers=headers_login)
if '"authenticated":false' in req_login.text:
    print('[!] Username Or Password Is Error - Try Agin')
    exit(0)
elif '"authenticated":true' in req_login.text:
    print('[+] Done Login')
    sessd = req_login.cookies['sessionid']
    username = input('[+] Enter Name File ==> : ')
    ff = username
    file = open(ff).read().splitlines()
    for file in file:
        url_checker = 'https://www.instagram.com/accounts/login/ajax/'
        headers_checker = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
            'content-length': '291',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': 'ig_did=3E70DB93-4A27-43EB-8463-E0BFC9B02AE1; mid=YCAadAALAAH35g_7e7h0SwBbFzBt; ig_nrcb=1; csrftoken=COmXgzKurrq8awSnRS1xf3u9rL6QsGZI',
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Linux; Android 11; SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36',
            'x-csrftoken': 'COmXgzKurrq8awSnRS1xf3u9rL6QsGZI',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': '0',
            'x-instagram-ajax': '1cb44f68ffec',
            'x-requested-with': 'XMLHttpRequest'
        }
        data_checker = {
            'username': file,
            'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1613414957:dsbvhdbvdsvbsdh',
            'queryParams': '{}',
            'optIntoOneTap': 'false'
        }
        req = requests.post(url_checker, data=data_checker, headers=headers_checker).text
        if '"user":false' in req:
            url_get_info = 'https://www.instagram.com/accounts/edit/?__a=1'
            headers_get_info = {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
                'cookie': f'ig_did=3E70DB93-4A27-43EB-8463-E0BFC9B02AE1; mid=YCAadAALAAH35g_7e7h0SwBbFzBt; ig_nrcb=1; csrftoken=Zc4tm5D7QNL1hiMGJ1caLT7DNPTYHqH0; ds_user_id=45334757205; sessionid={sessd}; rur=VLL',
                'referer': 'https://www.instagram.com/accounts/edit/',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
                'x-ig-app-id': '936619743392459',
                'x-ig-www-claim': 'hmac.AR3P8eA45g5ELL3lqdIm-DHKY2MSY_kGWkN0tGEwG2Ks9Ncl',
                'x-requested-with': 'XMLHttpRequest'
            }
            data_get_info = {
                '__a': '1'
            }
            req_get_info = requests.get(url_get_info, data=data_get_info, headers=headers_get_info)
            email = str(req_get_info.json()['form_data']['email'])
            first_name = str(req_get_info.json()['form_data']['first_name'])
            phone_number = str(req_get_info.json()['form_data']['phone_number'])
            biography = str(req_get_info.json()['form_data']['biography'])
            external_url = str(req_get_info.json()['form_data']['external_url'])
            url_swap = 'https://www.instagram.com/accounts/edit/'
            headers_swap = {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
                'content-length': '130',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': f'ig_did=3E70DB93-4A27-43EB-8463-E0BFC9B02AE1; mid=YCAadAALAAH35g_7e7h0SwBbFzBt; ig_nrcb=1; csrftoken=UeJJwEB0TKAL0cEYl3dsep58FFYKH0Nc; ds_user_id=45334757205; sessionid={sessd}; rur=VLL',
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/accounts/edit/',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
                'x-csrftoken': 'UeJJwEB0TKAL0cEYl3dsep58FFYKH0Nc',
                'x-ig-app-id': '936619743392459',
                'x-ig-www-claim': 'hmac.AR3P8eA45g5ELL3lqdIm-DHKY2MSY_kGWkN0tGEwG2Ks9Ncl',
                'x-instagram-ajax': '1cb44f68ffec',
                'x-requested-with': 'XMLHttpRequest',
            }
            data_swap = {
                'first_name': first_name,
                'email': email,
                'username': file,
                'phone_number': phone_number,
                'biography': biography,
                'external_url': external_url,
                'chaining_enabled': 'on'
            }
            req_swap = requests.post(url_swap, data=data_swap, headers=headers_swap).text
            if '{"status":"ok"' in req_swap:
                print(Fore.RED+f'[+] {Fore.BLUE}*{Fore.BLUE}************************************** {Fore.RED}[+]')
                print(Fore.RED+f' {Fore.YELLOW}    Username Found ==> : {Fore.GREEN}{file}')
                print(Fore.RED+f' {Fore.YELLOW}    Username Done Swap ==> : {Fore.GREEN}{file}')
                print(Fore.RED+f'[+] {Fore.BLUE}*{Fore.BLUE}************************************** {Fore.RED}[+]')
            else:
                print(f'[-] Error Swap The Username ==> : {file}')
        elif '"user":true' in req:
            print(Fore.RED+f'[=] Username Taken ==> : {file}')