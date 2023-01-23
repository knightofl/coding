module counter(
    input clk, rstn,
    output reg [3:0] cnt
);

    always @(posedge clk, negedge rstn)
        if (!rstn) cnt <= 0;
        else       cnt <= cnt + 1;

endmodule