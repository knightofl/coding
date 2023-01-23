module adder_test;
  
  reg [1:0] a[2:0], b[2:0];
  wire [1:0] sum[2:0];
  wire carry[2:0];
  
  fulladder_gatelevel adder_gl(a[0], b[0], sum[0], carry[0]);
  fulladder_dataflow adder_df(a[1], b[1], sum[1], carry[1]);
  fulladder_behavioral adder_be(a[2], b[2], sum[2], carry[2]);
  
  initial begin
    a[0] = 1; b[0] = 0;
    a[1] = 2; b[1] = 2;
    a[2] = 3; b[2] = 1;
  end
  
  initial begin
    $monitor("gate level a:%d, b:%d, sum:%d, carry:%d",
             a[0], b[0], sum[0], carry[0]);
    $monitor("data flow  a:%d, b:%d, sum:%d, carry:%d",
             a[1], b[1], sum[1], carry[1]);
    $monitor("behavioral a:%d, b:%d, sum:%d, carry:%d",
             a[2], b[2], sum[2], carry[2]);
  end
  
endmodule