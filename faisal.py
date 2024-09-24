import pyshorteners

#Jav Code
X = "\033[0;37;40m"
DG = "\033[1;30;40m"
R = "\033[1;31;40m"
Y = "\033[1;33;40m"
W = "\033[1;37;40m"
shortme = pyshorteners.Shortener()

print(W+"    ["+R+"+"+W+"]     LINK PHISHING    ["+R+"+"+W+"]")
print(W+"    ["+R+"+"+W+"] ANAK CIREBON TIMUR "+Y+"Muhammad Arif Faisal"+W+" ["+R+"+"+W+"]\n")
url = input("Your URL "+R+"> "+W)
fake = input("Fake URL "+R+"> "+W)
print("Contoh "+R+":"+W+" how-to-get-free-coin")
rantai = input("Rantai url "+R+"> "+W)
hasil = (url)
tanpahttp = hasil[7:]
print("Your link "+R+": "+Y+fake+"-"+rantai+"@"+tanpahttp+X)
