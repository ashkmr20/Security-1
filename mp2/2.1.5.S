.global _main
.section .text

_main:

push	%ebp
mov	%esp,%ebp
subl $4, %esp
movl $0, (%esp)
movl $11, %eax                      # sys_execve
movl $shell_file, %ebx
leal (%esp), %ecx
movl $0, %edx
int  $0x80
leave
ret


shell_file:
.asciz       "/bin/sh"