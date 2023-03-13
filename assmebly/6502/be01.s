PORTB = $7ff0
PORTA = $7ff1
DDRB  = $7ff2
DDRA  = $7ff3
	
E     = %10000000
RW    = %01000000
RS    = %00100000


	.org $8000

reset:
	lda #%11111111  ; Set all pins on port B to output
	sta DDRB

	lda #%11100000  ; Set top 3 pins on port A to output
	sta DDRA
	
	lda #%00111000  ; Set 8bit mode ; 2 line mode ; 5x8 font
	sta PORTB

	lda #0          ; Clear RS/RW/E bits
	sta PORTA

	lda #E          ; Set E bit to send instruction
	sta PORTA

	lda #0
	sta PORTA


        lda #%00001110  ; Set display on ; cursor on ; blink off
        sta PORTB

        lda #0          ; Clear RS/RW/E bits
        sta PORTA

        lda #E          ; Set E bit to send instruction
        sta PORTA

        lda #0
        sta PORTA


        lda #%00000110  ; Set increment and shift cursor
        sta PORTB

        lda #0          ; Clear RS/RW/E bits
        sta PORTA

        lda #E          ; Set E bit to send instruction
        sta PORTA

        lda #0
        sta PORTA


        lda #"H"
        sta PORTB

        lda #RS         ; Set RS, clear RW/E bit
        sta PORTA

        lda #(RS | E)   ; Set RS and E bit
        sta PORTA

        lda #RS         ; Clear E bit
        sta PORTA

	lda #"e"
        sta PORTB

        lda #RS         ; Set RS, clear RW/E bit
        sta PORTA

        lda #(RS | E)   ; Set RS and E bit
        sta PORTA

        lda #RS         ; Clear E bit
        sta PORTA

        lda #"l"
        sta PORTB

        lda #RS         ; Set RS, clear RW/E bit
        sta PORTA

        lda #(RS | E)   ; Set RS and E bit
        sta PORTA

        lda #RS         ; Clear E bit
        sta PORTA

        lda #"l"
        sta PORTB

        lda #RS         ; Set RS, clear RW/E bit
        sta PORTA

        lda #(RS | E)   ; Set RS and E bit
        sta PORTA

        lda #RS         ; Clear E bit
        sta PORTA

        lda #"o"
        sta PORTB

        lda #RS         ; Set RS, clear RW/E bit
        sta PORTA

        lda #(RS | E)   ; Set RS and E bit
        sta PORTA

        lda #RS         ; Clear E bit
        sta PORTA

	lda #","
        sta PORTB

        lda #RS         ; Set RS, clear RW/E bit
        sta PORTA

        lda #(RS | E)   ; Set RS and E bit
        sta PORTA

        lda #RS         ; Clear E bit
        sta PORTA

	lda #" "
        sta PORTB

        lda #RS         ; Set RS, clear RW/E bit
        sta PORTA

        lda #(RS | E)   ; Set RS and E bit
        sta PORTA

        lda #RS         ; Clear E bit
        sta PORTA

        lda #"W"
        sta PORTB

        lda #RS         ; Set RS, clear RW/E bit
        sta PORTA

        lda #(RS | E)   ; Set RS and E bit
        sta PORTA

        lda #RS         ; Clear E bit
        sta PORTA

        lda #"o"
        sta PORTB

        lda #RS         ; Set RS, clear RW/E bit
        sta PORTA

        lda #(RS | E)   ; Set RS and E bit
        sta PORTA

        lda #RS         ; Clear E bit
        sta PORTA

        lda #"r"
        sta PORTB

        lda #RS         ; Set RS, clear RW/E bit
        sta PORTA

        lda #(RS | E)   ; Set RS and E bit
        sta PORTA

        lda #RS         ; Clear E bit
        sta PORTA

	lda #"l"
        sta PORTB

        lda #RS         ; Set RS, clear RW/E bit
        sta PORTA

        lda #(RS | E)   ; Set RS and E bit
        sta PORTA

        lda #RS         ; Clear E bit
        sta PORTA

	lda #"d"
        sta PORTB

        lda #RS         ; Set RS, clear RW/E bit
        sta PORTA

        lda #(RS | E)   ; Set RS and E bit
        sta PORTA

        lda #RS         ; Clear E bit
        sta PORTA

        lda #"!"
        sta PORTB

        lda #RS         ; Set RS, clear RW/E bit
        sta PORTA

        lda #(RS | E)   ; Set RS and E bit
        sta PORTA

        lda #RS         ; Clear E bit
        sta PORTA

loop:
        jmp loop

	.org $fffc
	.word reset
	.word $0000
