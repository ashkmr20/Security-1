.global your_asm_fn
.section .text

your_asm_fn:

push	%ebp
mov	%esp,%ebp
subl    $12, %esp
movl    $0xc105ed, 4(%esp)
movl    $0xacce55ed, (%esp)

movl    $myval, 8(%esp)
call practice

leave
ret

myval:
.long 0xc001f00d