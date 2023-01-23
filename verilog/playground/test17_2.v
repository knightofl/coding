module tb_fifo;
    parameter DEPTH = 16, WIDTH = 8;

    reg clk, rstn;
    reg push, pop;
    wire full, empty;

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

    initial begin
        push <= 0;
        pop <= 0;
        @(negedge rstn);
        @(posedge rstn);
        repeat(5) @(posedge clk);

        for (int i=0; i<DEPTH; i++) write(i);
        for (int i=0; i<DEPTH; i++) read();
    end

    task write(
        input [WIDTH-1:0] task_wd
    );
        push <= 1;
        wd <= task_wd;
        @(posedge clk);
        push <= 0;
    endtask

    task read();
        pop <= 1;
        @(posedge clk);
        pop <= 0;
    endtask

    fifo #(.DEPTH(16), .WIDTH(8))
         u_fifo(clk, rstn, push, pop, wd, rd, full, empty);

    initial begin
        $dumpfile("wave.vcd");
        $dumpvars(0, tb_fifo);
        #500 $finish;
    end

endmodule