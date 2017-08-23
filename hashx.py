import hashlib
from platform import system
import os , sys

if system() == 'Linux':
    os.system('clear')
elif system() == 'Windows':
    os.system('cls')
os.system('color a')

print ('''
FOR HELPING YOU ..

                               ___TYPE_HASH___


SHA512
SHA1
md4
ecdsa-with-SHA1
SHA
sha224
RIPEMD160
SHA224
SHA256
sha256
MD5
whirlpool
DSA-SHA
dsaWithSHA
ripemd160
sha
DSA
sha512
sha1
SHA384
MD4
dsaEncryption
sha384
md5



      ___           ___           ___           ___           ___      
     /\  \         /\  \         /\__\         /\  \         /|  |     
     \:\  \       /::\  \       /:/ _/_        \:\  \       |:|  |     
      \:\  \     /:/\:\  \     /:/ /\  \        \:\  \      |:|  |     
  ___ /::\  \   /:/ /::\  \   /:/ /::\  \   ___ /::\  \   __|:|__|     
 /\  /:/\:\__\ /:/_/:/\:\__\ /:/_/:/\:\__\ /\  /:/\:\__\ /::::\__\_____
 \:\/:/  \/__/ \:\/:/  \/__/ \:\/:/ /:/  / \:\/:/  \/__/ ~~~~\::::/___/
  \::/__/       \::/__/       \::/ /:/  /   \::/__/          |:|~~|    
   \:\  \        \:\  \        \/_/:/  /     \:\  \          |:|  |    
    \:\__\        \:\__\         /:/  /       \:\__\         |:|__|    
     \/__/         \/__/         \/__/         \/__/         |/__/     



''')
  
class amr:
    def van (self,text,type_hash):
        text = text.encode('utf-8')
        x = hashlib.new(type_hash)
        x.update(text)
        return x.hexdigest()
while True:
    text= input('enter the text > :')
    type_hash= input('enter the hash_type > : ')
    g= amr()
    print (g.van (text ,type_hash))


        
     
