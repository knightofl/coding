module swap;
    reg blk_a, blk_b;
    reg nbk_a, nbk_b;

    initial begin
        blk_a = 0; blk_b = 1;
        #10
        blk_a = blk_b;
        blk_b = blk_a;
        #10;
    end

    initial begin
        nbk_a = 0; nbk_b = 1;
        #10
        nbk_a <= nbk_b;
        nbk_b <= nbk_a;
        #10;
    end

    initial begin
        $dumpfile("wave.vcd");
        $dumpvars(0, swap);
    end

endmodule