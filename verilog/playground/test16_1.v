module sram #(
    parameter DEPTH = 16,
              WIDTH = 8,
              DEPTH_B = $clog2(DEPTH)
)(
    input clk,
    input cs, we,
    input [DEPTH_B-1:0] ad,
    input [WIDTH-1:0] wd,
    output reg [WIDTH-1:0] rd
);
    reg [WIDTH-1:0] mem[DEPTH-1:0];

    always @(posedge clk)
        if (cs & we) mem[ad] <= wd;

    always @(posedge clk)
        if (cs & ~we) rd <= mem[ad];

endmodule