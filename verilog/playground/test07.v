module always_test;
    reg [2:0] blk_a, blk_b, blk_c, blk_d, blk_e;
    reg [2:0] nbk_a, nbk_b, nbk_c, nbk_d, nbk_e;

    initial begin
        blk_a = 0; nbk_a = 0;
        #10;
        blk_a = 1; nbk_a = 1;
        #10;
    end

    //always @* begin
    always @(blk_a) begin
        blk_b = blk_a + 1;
        blk_c = blk_b + 1;
        blk_d = blk_c + 1;
        blk_e = blk_d + 1;
    end

    //always @* begin
    always @(nbk_a) begin
        nbk_b <= nbk_a + 1;
        nbk_c <= nbk_b + 1;
        nbk_d <= nbk_c + 1;
        nbk_e <= nbk_d + 1;
    end

    initial begin
        $dumpfile("wave.vcd");
        $dumpvars(0, always_test);
    end
    
endmodule