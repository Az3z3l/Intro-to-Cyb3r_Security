BITS 32

extern printf

section .rodata
    no: db "%d",10,0

section .text

    global main

    main:
    push ebp
    mov ebp, esp

    loooop:
        inc ebx
        push ebx
        push no
        call printf
        cmp ebx, 10
        jl loooop
    leave
    ret