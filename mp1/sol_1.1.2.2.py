# -*- coding: utf-8 -*-

import sys
from Crypto import Random
from Crypto.Cipher import AES
import os
import binascii

ciph_f=sys.argv[1]
key_f =sys.argv[2]
iv_f=sys.argv[3]
outp_f=sys.argv[4]

with open(ciph_f) as f:
    ciph_content= f.read().strip()
with open(key_f) as f:
    key_content= f.read().strip()
with open(iv_f) as f:
    iv_content= f.read().strip()
result=""
ciph = ciph_content.decode('hex')
iv= iv_content.decode('hex')
key= key_content.decode('hex')
#print(len(iv))
#print(iv)
cipher = AES.new(key, AES.MODE_CBC, iv)
plaintext = cipher.decrypt(ciph[0:])
result=plaintext
with open(outp_f, "w") as outp:
    outp.write(result)


