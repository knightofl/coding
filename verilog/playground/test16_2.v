module tb_sram;
    parameter DEPTH = 16, WIDTH = 8;
    parameter DEPTH_B = $clog2(DEPTH);

    reg clk, rstn;
    reg cs, we;
    reg [DEPTH_B-1:0] ad;
    reg [WIDTH-1:0] wd;
    wire [WIDTH-1:0] rd;

    initial begin
        clk = 0;
        forever #5 clk = ~clk;
    end

    initial begin
        rstn = 1;
        #10 rstn = 0;
        #20 rstn = 1;
    end

    sram #(.DEPTH(DEPTH), .WIDTH(WIDTH))
        u_sram(clk, cs, we, ad, wd, rd);

    initial begin
        cs <= 0;
        we <= 0;
        @(negedge rstn);
        @(posedge rstn);
        repeat(5) @(posedge clk);

        for (int i=0; i<DEPTH; i++) write(i, i);
        for (int i=0; i<DEPTH; i++) read(i);
    end

    task write(
        input [DEPTH_B-1:0] task_ad,
        input [WIDTH-1:0] task_wd
    );
        cs <= 1;
        we <= 1;
        ad <= task_ad;
        wd <= task_wd;

        @(posedge clk);
        cs <= 0;
        we <= 0;
    endtask

    task read(
        input [DEPTH_B-1:0] task_ad
    );
        cs <= 1;
        we <= 0;
        ad <= task_ad;

        @(posedge clk);
        cs <= 0;
        we <= 0;
    endtask

    initial begin
        $dumpfile("wave.vcd");
        $dumpvars(0, tb_sram);
        #500 $finish;
    end

endmodule