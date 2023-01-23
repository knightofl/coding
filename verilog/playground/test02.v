module dump_example;
  reg a, b;
  
  initial begin
    a = 0; b = 0;
    #10 a = 1; b = 0;
    #10 a = 0; b = 1;
    #10 a = 1; b = 1;
    #10 $finish;
  end
  
  initial begin
    $dumpfile("dump.vcd");
    $dumpvars(1, dump_example);
    $display("dump test");
  end
  
endmodule