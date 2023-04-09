PORTB = $7ff0
PORTA = $7ff1
DDRB  = $7ff2
DDRA  = $7ff3
PCR   = $7ffc
IFR   = $7ffd
IER   = $7ffe

value = $7200           ; 2 bytes
mod10 = $7202           ; 2 bytes
message = $7204         ; 6 bytes
counter = $720a         ; 2 bytes

E     = %10000000
RW    = %01000000
RS    = %00100000


        .org $8000

reset:
        ldx #$ff        ; stack initialize
        txs
        cli             ; Clear interrupt disable bit

        lda #$82        ; Set CA1 Negative Edge
        sta IER         ; Interrupt Enable Resgister
        lda #$00
        sta PCR


        lda #%11111111  ; Set all pins on port B to output
        sta DDRB

        lda #%11100000  ; Set top 3 pins on port A to output
        sta DDRA


        lda #%00111000  ; Set 8bit mode ; 2 line mode ; 5x8 font
        jsr lcd

        lda #%00001110  ; Set display on ; cursor on ; blink off
        jsr lcd

        lda #%00000110  ; Set increment and shift cursor
        jsr lcd

        lda #%00000001  ; Clear display
        jsr lcd


        lda #0
        sta counter
        sta counter + 1

loop:
        lda #%00000010  ; Cursor to Home
        jsr lcd

decimal:
        lda #0
        sta message

        ; Initialize value to be the number to convert
        sei
        lda counter
        sta value
        lda counter + 1
        sta value + 1
        cli

divide:
        ; Initialize the remainder to zero
        lda #0
        sta mod10
        sta mod10 + 1

        clc
        ldx #16
divloop:
        ; Rotate quotient and remainder
        rol value
        rol value + 1
        rol mod10
        rol mod10 + 1

        ; a and y, devidened - devisor
        sec
        lda mod10
        sbc #10
        tay             ; save loe byte to y
        lda mod10 + 1
        sbc #0
        bcc ignore_result
        sty mod10
        sta mod10 + 1

ignore_result:
        dex
        bne divloop
        rol value       ; shift in the last bit of quotient
        rol value + 1   ; 

        lda mod10
        clc
        adc #"0"
        jsr push

        ; if value != 0 then continue to divide
        lda value
        ora value + 1
        bne divide


        ldx #0
msgprt:
        lda message, x
        beq loop
        jsr print
        inx
        jmp msgprt


        ; Add the character in the A resgister to the beginning
        ; of the null-terminated string 'message'
push:
        pha             ; Push new first char onto the stack
        ldy #0

push_loop:
        lda message, y  ; Get char on string and put into X
        tax
        pla
        sta message, y  ; Pull char off stack and add it to the string
        iny
        txa
        pha
        bne push_loop

        pla
        sta message, y  ; Pull the null off the stack and add to the end of the string

        rts        


wait:
        pha

        lda #%00000000  ; Set port B to input
        sta DDRB

busy:
        lda #RW
        sta PORTA

        lda #(RW | E)
        sta PORTA

        lda PORTB
        and #%10000000
        bne busy

        lda #RW
        sta PORTA

        lda #%11111111 ; Set Port B to output
        sta DDRB

        pla
        rts


lcd:
        jsr wait
        sta PORTB

        lda #0          ; Clear RS/RW/E bits
        sta PORTA

        lda #E          ; Set E bit to send instruction
        sta PORTA

        lda #0
        sta PORTA

        rts


print:
        jsr wait
        sta PORTB

        lda #RS         ; Set RS, clear RW/E bit
        sta PORTA

        lda #(RS | E)   ; Set RS and E bit
        sta PORTA

        lda #RS         ; Clear E bit
        sta PORTA

        rts


nmi:
        rti

irq:
        inc counter
        bne exit_irq
        inc counter + 1
exit_irq:
        bit PORTA       ; read, wrtie ora to clear CA1
        rti

        .org $fffa
        .word nmi
        .word reset
        .word irq
