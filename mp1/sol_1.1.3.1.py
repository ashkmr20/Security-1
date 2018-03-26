
import sys
from Crypto import Random
from Crypto.Cipher import AES
import os
import binascii
import hashlib

f1_f=sys.argv[1]
f2_f =sys.argv[2]
outp_f=sys.argv[3]

with open(f1_f) as f:
    f1_content= f.read().strip()
with open(f2_f) as f:
    f2_content= f.read().strip()

result=""
hash1 =(hashlib.sha256(f1_content))
hash2= (hashlib.sha256(f2_content))
hex_dig1 = hash1.hexdigest()
hex_dig2= hash2.hexdigest()

intc1 = int(hex_dig1,16)
intc2 = int(hex_dig2,16)
bin_1 =bin(intc1)[2:]
bin_2 =bin(intc2)[2:]

hamm=0
for ch1, ch2 in zip(bin_1, bin_2):
    if ch1 != ch2:
    	hamm += 1
    
res=hex(hamm)[2:]
res.replace("L","")
print(res)
#result=plaintext
with open(outp_f, "w") as outp:
    outp.write(res)


