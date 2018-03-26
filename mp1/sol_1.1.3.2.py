
import sys
from Crypto import Random
from Crypto.Cipher import AES
import os
import binascii
import hashlib

f1_f=sys.argv[1]
outp_f=sys.argv[2]

with open(f1_f) as f:
    f1_content= f.read().strip()

#f1_content="DEAHING TOUSH ROMF WASHIGNTON CD I OG YB THIS VIRGINIA CITY WHERE GEORGE WASHINGTON ONCE DRILLED TROOPS"
Mask= 0x3FFFFFFF
outHash=0
result=""
for byte in f1_content:
	intermediate_value = ((ord(byte) ^ 0xCC) << 24) | ((ord(byte) ^ 0x33) << 16) | ((ord(byte) ^ 0xAA) << 8) | (ord(byte) ^ 0x55)
	outHash = (outHash & Mask) + (intermediate_value & Mask)
	#print(intermediate_value & Mask)
result=(hex(outHash))

with open(outp_f, "w") as outp:
    outp.write(result)


