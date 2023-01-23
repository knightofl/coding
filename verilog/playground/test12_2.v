module tb;
    reg clk, rstn;
    event timer_start;
    reg enable;
    wire done_a, done_b, done_c;

    timer #(.N(10)) timer_a(clk, rstn, enable, done_a);
    timer #(.N(15)) timer_b(clk, rstn, enable, done_b);
    timer #(.N(20)) timer_c(clk, rstn, enable, done_c);

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
        #50 -> timer_start;
        $display("%3t : timer start", $time);
    end

    initial begin
        enable = 0;
        @(timer_start)
        enable = 1;

        fork
            begin
                wait (done_a == 1)
                $display("%3t : done_a", $time);
            end
            begin
                wait (done_b == 1)
                $display("%3t : done_b", $time);
            end
            begin
                wait (done_c == 1)
                $display("%3t : done_c", $time);
            end
        join_any

        $finish;
    end

endmodule