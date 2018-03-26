from pymd5 import md5, padding
import sys
import urllib
query_f=sys.argv[1]
cmd_f =sys.argv[2]
outp_f=sys.argv[3]

with open(query_f) as f:
    query= f.read().strip()
with open(cmd_f) as f:
    cmd= f.read().strip()
token=query[6:38]
#print(query[6:38],query[38:])
new_h= md5(state=token.decode('hex'),count=512)
x=cmd
new_h.update(x)
output="http://ece422.org/project1/api?token="

padding= urllib.quote(padding((len(query[39:])+8)*8))
#print(padding)
output=output+new_h.hexdigest()+ query[38:] + padding + cmd
#print new_h.hexdigest()
#padstring= (padding.encode('hex'))


with open(outp_f, "w") as outp:
    outp.write(output)