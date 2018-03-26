import sys
ciph_f=sys.argv[1]
key_f =sys.argv[2]
outp_f=sys.argv[3]


with open(ciph_f) as f:
    ciph_content= f.read().strip()
with open(key_f) as f:
    key_content= f.read().strip()
result=""
for char in ciph_content:
	if char.isalpha():
		resultind= key_content.index(char)
		result=result + chr(resultind+65)
	else:
		result=result+ char
with open(outp_f, "w") as outp:
    outp.write(result)

