module tb;
    reg clk, rstn;
    wire [3:0] hour;
    wire [5:0] minute;

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
        #30000 $finish;
    end

    watch u_watch (clk, rstn, hour, minute);

    initial begin
        $dumpfile("wave.vcd");
        $dumpvars(1, tb);
    end

endmodule