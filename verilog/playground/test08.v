module always_test;
    reg [2:0] blk_a, blk_b, blk_c, blk_d, blk_e;
    reg [2:0] nbk_a, nbk_b, nbk_c, nbk_d, nbk_e;

    reg clk, rstn;

    initial begin
        clk = 0;
        forever begin
             #5 clk = ~clk;
        end
    end

    initial begin
        rstn = 1;
        #10 rstn = 0;
        #20 rstn = 1;
    end

    initial begin
        #100 $finish;
    end

    always @(posedge clk, negedge rstn)
        if (!rstn) {blk_a, blk_b, blk_c, blk_d, blk_e} = 0;
        else begin
            blk_a = 1;
            blk_b = blk_a + 1;
            blk_c = blk_b + 1;
            blk_d = blk_c + 1;
            blk_e = blk_d + 1;
        end
    
    always @(posedge clk, negedge rstn)
        if (!rstn) {nbk_a, nbk_b, nbk_c, nbk_d, nbk_e} = 0;
        else begin
            nbk_a <= 1;
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