module tb;
    reg clk, rstn;
    wire [1:0] light;

    initial begin
        clk = 1;
        forever #5 clk = ~clk;  
    end

    initial begin
        rstn = 1;
        #10 rstn = 0;
        #20 rstn = 1;
    end

    traffic_light u_light(clk, rstn, light);

    initial begin
        $dumpfile("wave.vcd");
        $dumpvars(0, tb);
        #700 $finish;
    end

endmodule