import requests,os
import time,re
from multiprocessing.dummy import Pool as ThreadPool
from colorama import Fore,Style, init
init(autoreset=True)
#Buy Coffee 
#? BITCOIN = 31mtLHqhaXXyCMnT2EU73U8fwYwigiEEU1
#? PERFECT MONEY  = U22270614

def askdns(url):
	try:
		headers = {
		'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36'
		}
		x = requests.get('https://askdns.com/ip/'+url, headers=headers,timeout=30).content
		if 'Domain Name' in x:
			regex = re.findall('<a href="/domain/(.*?)">', x)
			for jan in regex:
				print("GET {} DOMAIN FROM {}".format(len(jan), url))
				open('revip.txt','a').write('http://'+jan+'\n')
			else:
				print("BAD RAP" + url )
	except:
		pass

def rapid(url):
	try:
		headers = {
		'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36'
		}
		x = requests.get('https://rapiddns.io/s/'+url+'?full=1&down=1#result/', headers=headers,timeout=30).content
		if '<th scope="row ">' in x:
			regex = re.findall('<td>(?!\-)(?:[a-zA-Z\d\-]{0,62}[a-zA-Z\d]\.){1,126}(?!\d+)[a-zA-Z]{1,63}</td>', x)
			for jan in regex:
				cok = jan.replace('<td>','').replace('</td>','').replace('ftp.','').replace('images.','').replace('cpanel.','').replace('cpcalendars.','').replace('cpcontacts.','').replace('webmail.','').replace('webdisk.','').replace('hostmaster.','').replace('mail.','').replace('ns1.','').replace('ns2.','').replace('autodiscover.','')
				print("GET {} DOMAIN FROM {}".format(len(cok), url))
				open('revip.txt','a').write('http://'+cok+'\n')
			else:
				print("BAD RAP" + url )
	except:
		pass

def revip(url):
	try:
		rapid(url)
		askdns(url)
	except:
		pass

def Main():
	os.system('cls' if os.name == 'nt' else 'clear')
	print "{} Repip MultiThreading !  | {}Shin Code\n".format(Fore.YELLOW,Fore.CYAN)
	try:
		list = raw_input("UR LIST :~# ")
		url = open(list, 'r').read().splitlines()
		THREAD = raw_input("THREAD :~# ")
		pp = ThreadPool(int(THREAD))
		pr = pp.map(revip,url)
	except:
		pass
if __name__ == '__main__':
	Main()
