PORTB = $7ff0
PORTA = $7ff1
DDRB  = $7ff2
DDRA  = $7ff3

E     = %10000000
RW    = %01000000
RS    = %00100000


        .org $8000

reset:
        ldx #$ff        ; stack initialize
        txs

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


        lda #"H"
        jsr print

        lda #"e"
        jsr print

        lda #"l"
        jsr print

        lda #"l"
        jsr print

        lda #"o"
        jsr print

        lda #","
        jsr print

        lda #" "
        jsr print

        lda #"W"
        jsr print

        lda #"o"
        jsr print

        lda #"r"
        jsr print

        lda #"l"
        jsr print

        lda #"d"
        jsr print

        lda #"!"
        jsr print

loop:
        jmp loop


lcd:
        sta PORTB

        lda #0          ; Clear RS/RW/E bits
        sta PORTA

        lda #E          ; Set E bit to send instruction
        sta PORTA

        lda #0
        sta PORTA

        rts


print:
        sta PORTB

        lda #RS         ; Set RS, clear RW/E bit
        sta PORTA

        lda #(RS | E)   ; Set RS and E bit
        sta PORTA

        lda #RS         ; Clear E bit
        sta PORTA

        rts


        .org $fffc
        .word reset
        .word $0000
