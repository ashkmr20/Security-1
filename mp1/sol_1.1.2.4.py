import sys
from Crypto.Cipher import AES
import math
ciph_f=sys.argv[1]
key_f =sys.argv[2]
mod_f =sys.argv[3]
outp_f=sys.argv[4]


with open(ciph_f) as f:
    ciph_content= f.read().strip()
with open(key_f) as f:
    key_content= f.read().strip()
with open(mod_f) as f:
    mod_content= f.read().strip()
result=""
ciph = int(ciph_content,16)
key = int(key_content,16)
mod = int(mod_content,16)
interm =	ciph**key
result = interm% mod


with open(outp_f, "w") as outp:
    outp.write(hex(result)[2:-1])