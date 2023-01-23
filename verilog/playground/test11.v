module tb;
event event_a; 

initial begin
    #20 -> event_a;
    $display("%3t : event_a", $time);
end

initial begin
    $display("%3t : before event_a", $time);
    @(event_a)
    $display("%3t : after event_a", $time);
end

endmodule