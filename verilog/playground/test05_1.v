// 2bit full adder
module fulladder_gatelevel (
    input   [1:0] a, b,
    output  [1:0] sum,
    output  carry
);

    wire and_1;
    wire xor_3;
    wire and_2, and_3;

    xor(sum[0], a[0], b[0]);
    and(and_1, a[0], b[0]);
    xor(xor_3, a[1], b[1]);
    
    and(and_2, and_1, xor_3);
    and(and_3, a[1], b[1]);

    xor(sum[1], and_1, xor_3);
    or(carry, and_2, and_3);

endmodule


module fulladder_dataflow (
    input   [1:0] a, b,
    output  [1:0] sum,
    output  carry
);

    wire [2:0] sum_3bit;

    assign sum_3bit = a + b;
    assign sum = sum_3bit[1:0];
    assign carry = sum_3bit[2];

    //assign {carry, sum} = a + b;

endmodule


module fulladder_behavioral (
    input   [1:0] a, b,
    output  reg [1:0] sum,
    output  reg carry
);

    always @* begin
        {carry, sum} = a + b;
    end

endmodule