.global your_asm_fn
.section .text

your_asm_fn:

push	%ebp
mov	%esp,%ebp
subl    $12, %esp
movl    $0xc001f00d, 8(%esp)
movl    $0xc105ed, 4(%esp)
movl    $0xacce55ed, (%esp)

call practice

leave
ret