from operator import invert
from pwn import *
from sage import *
from Crypto.Util.number import bytes_to_long, getPrime, long_to_bytes
from gmpy import invert


flag = 49364843843516391046524858268527194975796465451738728838358032889241583861681330662767392725024498128283428237150126842155134747862768281794100146644762400911056367438565918807838022537636139082681255925833425278781968862019514751174859831833535384067616751710444808458127047852149547554804396254364290625686
flag = 1383267881415754384761584821237495877696649322415291415115286645195619073381462292999464927996391147913482468851071078001359267525978080374044197506996867123714733496719096089378963153914346503639801329908547994849412904416650762397904239913368400506600031425890740026601275815000227565394224244102210288111
flag = 1519579176762631193459775938985477977407160163691778453249498992479840564257314191794900660927224933425057451227048385230727023930907257743930890225666299447966367616361578716141573484847718831863944399631844272299122579650519163342974424904814893805994319116220695473077100212351047128480919112710173644145
flag = 1519579176762631193459775938985477977407160163691778453249498992479840564257314191808811284775725779785737966841460666216843488772556234048949970361287574788499511878008737988121888005562650140590424353042984690060537862777614080769894438371268877745152383172097525337811247644386550766803886329552977731627
flag = 49364843843516391046524858268527194975796465451738728838358032889241583861681330662805744384643615080783736466263862424627957295396965989818562735100345397897204476911811494476051886042402287885624633447864215372696967903925688430695026280061407762981113772713153260689367626604780512215178462682026543537136
print("Flag : ",long_to_bytes(flag)) 