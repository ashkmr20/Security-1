.global your_asm_fn
.section .text

your_asm_fn:

push	%ebp
mov	%esp,%ebp
subl    $12, %esp
movl    $myval, 4(%esp)
movl    $0xacce55ed, (%esp)

movl    $coolval, 8(%esp)
call practice

leave
ret

myval:
.long 0xc105ed

coolval:
.long  0x6c6f6f63
.long 0x646f6f66
.short 0x0000
