PORTB = $7ff0
PORTA = $7ff1
DDRB  = $7ff2
DDRA  = $7ff3
	
E     = %10000000
RW    = %01000000
RS    = %00100000


	.org $8000

reset:
	lda #%11111111	; Set all pins on port B to output
	sta DDRB

	lda #%11100000	; Set top 3 pins on port A to output
	sta DDRA
	
	lda #%00111000	; Set 8bit mode ; 2 line mode ; 5x8 font
	jsr lcd_instruct

        lda #%00001110  ; Set display on ; cursor on ; blink off
        jsr lcd_instruct

        lda #%00000110  ; Set increment and shift cursor, don't shift display
        jsr lcd_instruct


        lda #"H"	; Set increment and shift cursor
        jsr lcd_instruct

	lda #"e"        ; Set increment and shift cursor
        sta PORTB

        lda #RS         ; Set RS, clear RW/E bit
        sta PORTA

        lda #(RS | E)   ; Set RS and E bit
        sta PORTA

        lda #RS         ; Clear E bit
        sta PORTA

        lda #"l"        ; Set increment and shift cursor
        sta PORTB

        lda #RS         ; Set RS, clear RW/E bit
        sta PORTA

        lda #(RS | E)   ; Set RS and E bit
        sta PORTA

        lda #RS         ; Clear E bit
        sta PORTA

        lda #"l"        ; Set increment and shift cursor
        sta PORTB

        lda #RS         ; Set RS, clear RW/E bit
        sta PORTA

        lda #(RS | E)   ; Set RS and E bit
        sta PORTA

        lda #RS         ; Clear E bit
        sta PORTA

        lda #"o"
        jsr lcd_instruct

	lda #","
        jsr lcd_instruct

	lda #" "
        jsr lcd_instruct

        lda #"W"
        jsr lcd_instruct

        lda #"o"
        jsr lcd_instruct

        lda #"r"
        jsr lcd_instruct

	lda #"l"
        jsr lcd_instruct

	lda #"d"
	jsr lcd_instruct

        lda #"!"
	jsr lcd_instruct

loop:
	jmp loop

lcd_instruct:
        sta PORTB

        lda #0          ; Clear RS/RW/E bits
        sta PORTA

        lda #E          ; Set E bit to send instruction
        sta PORTA

        lda #0
        sta PORTA

	rts


	.org $fffc
	.word reset
	.word $0000
