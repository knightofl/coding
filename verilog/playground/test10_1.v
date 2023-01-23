module watch(
    input clk, rstn,
    output reg [3:0] hour,
    output reg [5:0] minute
);

    always @(posedge clk, negedge rstn)
        if (!rstn) minute <= 0;
        else if (minute == 59) minute <= 0;
        else       minute <= minute + 1;

    always @(posedge clk, negedge rstn)
        if (!rstn) hour <= 0;
        else begin
            if (hour == 11 && minute == 59) hour <= 0; 
            else if (minute == 59) hour <= hour + 1;
        end

endmodule