module design_d(
  input		clk,
  input		rstn,
  input 	[3:0] in,
  output	[3:0] out
);

  wire	[3:0] a;
  reg	[3:0] b;
  
  assign a = in + 1;
  
  always @(posedge clk, negedge rstn) begin
    if (!rstn) b <= 0;
    else b <= a;
  end
  
  assign out = b;
 
endmodule