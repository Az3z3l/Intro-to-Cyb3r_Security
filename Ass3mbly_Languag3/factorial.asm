BITS 32

extern printf
extern scanf

section .data 
    no: db "%d",0
    
    section .text

    global main

    main:
    push ebp
    mov ebp,esp

    push eax
    mov eax,1
    lea ebx, [ebp-0x4]
	push ebx
	push no
	call scanf
    push eax
    mov eax,1

    looopy:
        cmp ebx,1
        je done
        mul ebx
        dec ebx
        jmp looopy

    done:
        push eax
        call printf
        leave
        ret