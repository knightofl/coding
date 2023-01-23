module  tb;
    initial #10 disp_a();
    initial #10 disp_a();
    initial #10 disp_a();

    initial #20 auto_disp();
    initial #20 auto_disp();
    initial #20 auto_disp();
    
    task disp_a;
        int i = 0;
        $display("static int i = %2d", i++);
    endtask

    task automatic auto_disp;
        int i = 0;
        $display("automatic int i = %2d", i++);
        disp_b();
    endtask  
    
    task disp_b;
        int j = 0;
        $display("static int j = %2d", j++);
    endtask

endmodule