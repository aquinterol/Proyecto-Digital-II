`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 25.06.2021 21:11:04
// Design Name: 
// Module Name: PWM
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////

module PWMUS(clk, servo1, servo2, servo3, pos1, pos2,pos3);
input clk;
input [1:0]pos1;
input [1:0]pos2;
input [1:0]pos3;
output reg servo1;
output reg servo2;
output reg servo3;

reg [20:0]contador = 0;

always@(posedge clk)begin
	contador = contador + 1;
	if(contador =='d1_000_000) begin
	   contador = 0;
	end
	
	case(pos1)
        2'b00:  servo1 = (contador < 'd50_000) ? 1:0;
        
        2'b01:  servo1 = (contador < 'd150_000) ? 1:0;
        
        2'b10:  servo1 = (contador < 'd250_000) ? 1:0;
        
        default:servo1 = (contador < 'd50_000) ? 1:0;
    endcase
    
    case(pos2)
        2'b00:  servo2 = (contador < 'd50_000) ? 1:0;
        
        2'b01:  servo2 = (contador < 'd150_000) ? 1:0;
        
        2'b10:  servo2 = (contador < 'd250_000) ? 1:0;
        
        default:servo2 = (contador < 'd50_000) ? 1:0;
    endcase
    
    case(pos3)
        2'b00:  servo3 = (contador < 'd50_000) ? 1:0;
        
        2'b01:  servo3 = (contador < 'd150_000) ? 1:0;
        
        2'b10:  servo3 = (contador < 'd250_000) ? 1:0;
        
        default:servo3 = (contador < 'd50_000) ? 1:0;
    endcase

end
endmodule
