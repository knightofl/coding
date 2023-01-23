module hello;
  int test = 0;
  
  initial begin
    #10 $display("time : %t, hello world : %d", $time, test++);
    #10 $display("time : %t, hello world : %d", $time, test++);
    $display("time : %t, hello world : %d", $time, test++);
  end
  
  initial begin
    $monitor("monitor test : %d", test);
  end
  
endmodule