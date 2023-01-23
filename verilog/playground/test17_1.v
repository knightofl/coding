module fifo #(
    parameter DEPTH = 16,
              WIDTH = 8,
              DEPTH_B = $clog2(DEPTH)
)(
    input clk, rstn,
    input push, pop,
    input [WIDTH-1:0] wd,
    output [WIDTH-1:0] rd,
    output full, empty
);
    reg [WIDTH-1:0] mem[DEPTH-1:0];
    reg [DEPTH_B-1:0] push_ad, pop_ad;
    reg [WIDTH-1:0] rd_reg;
    reg [DEPTH_B:0] diff_ad;

    always @(posedge clk, negedge rstn)
        if (!rstn) for (int i=0; i<DEPTH; i++) mem[i] <= 0;
        else if (push) mem[push_ad] <= wd;

    always @(posedge clk, negedge rstn)
        if (!rstn) push_ad <= 0;
        else if (push) push_ad <= push_ad + 1;

    always @(posedge clk, negedge rstn)
        if (!rstn) rd_reg <= 0;
        else if (pop) rd_reg <= mem[pop_ad];

    always @(posedge clk, negedge rstn)
        if (!rstn) pop_ad <= 0;
        else if (pop) pop_ad <= pop_ad + 1;

    assign rd = pop ? mem[pop_ad] : rd_reg;

    always @(posedge clk, negedge rstn)
        if (!rstn) diff_ad <= 0;
        else if (push & pop) diff_ad <= diff_ad;
        else if (push) diff_ad <= diff_ad + 1;
        else if (pop) diff_ad <= diff_ad - 1;

    assign full = (diff_ad + push - pop) >= DEPTH;
    assign empty = (diff_ad + push - pop) == 0;

endmodule