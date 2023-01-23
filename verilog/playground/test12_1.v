module  timer #(
    parameter  N = 10
)(
    input clk, rstn,
    input enable,
    output done
);
    reg [4:0] cnt;

    always @(posedge clk, negedge rstn)
        if (!rstn) cnt <= N;
        else if (enable) cnt <= cnt - 1;

    assign done = cnt == 0;

endmodule