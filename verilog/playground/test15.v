module  tb;
    reg clk;
    reg [3:0] blk_a, blk_b, nbk_a, nbk_b;

    initial begin
        clk = 1;
        forever #5 clk = ~clk;
    end

    initial task_blk(1, 2, blk_a, blk_b);
    initial task_nbk(1, 2, nbk_a, nbk_b);

    task task_blk(
        input [3:0] in_a, in_b,
        output [3:0] out_a, out_b
    );
        out_a = in_a + 1;
        #1 out_b = in_b + 1;

        @(posedge clk)
            out_a = out_a + 1;
            out_b = out_b + 1;

        @(posedge clk)
            out_a = out_a + 1;
            out_b = out_b + 1;
    endtask

    task task_nbk(
        input [3:0] in_a, in_b,
        output [3:0] out_a, out_b
    );
        out_a <= in_a + 1;
        #1 out_b <= in_b + 1;

        @(posedge clk)
            out_a <= out_a + 1;
            out_b <= out_b + 1;

        @(posedge clk)
            out_a <= out_a + 1;
            out_b <= out_b + 1;
    endtask

    initial begin
        $dumpfile("wave.vcd");
        $dumpvars(0, tb);
        #50 $finish;
    end
    
endmodule