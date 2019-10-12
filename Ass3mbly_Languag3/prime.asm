BITS 32

extern printf
extern scanf

section .data 
    no: db "%d",0
    true:db "is a prime number",10,0
    false:db "is not a prime number",10,0

section .text

    global main

    main:
    push ebp
    mov ebp,esp

    lea eax, [ebp-0x4]
	push eax
	push no
	call scanf
    mov edx,0
    mov eax,[ebp-0x4] 
    mov ecx,2  
    cmp eax,1
    je fin

    looop:
        cmp ecx,[ebp-0x4]
        je tr   
        div ecx
        cmp edx,0
        je fin
        mov edx,0
        mov eax,[ebp-0x4]
        inc ecx
        jmp looop
        

    fin:
        push false
        call printf
        leave
        ret

    tr:
        push true
        call printf
        leave
        ret