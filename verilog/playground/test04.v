module design_d(
  input			clk,
  input			rstn,
  input			[3:0] in,
  output reg	[3:0] out
);

  wire	[3:0] a;
  
  assign a = in + 1;
  
  always @(posedge clk, negedge rstn)
  if (!rstn) out <= 0;
  else out <= a;
 
endmodule