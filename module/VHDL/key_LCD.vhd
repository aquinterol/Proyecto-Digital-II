----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 20.01.2022 13:08:40
-- Design Name: 
-- Module Name: key_LCD - Behavioral
-- Project Name: 
-- Target Devices: 
-- Tool Versions: 
-- Description: 
-- 
-- Dependencies: 
-- 
-- Revision:
-- Revision 0.01 - File Created
-- Additional Comments:
-- 
----------------------------------------------------------------------------------


library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity LCD is
  Port (
    data_entry:in std_logic_vector(3 downto 0):=b"0000";
    puntos  :   in std_logic_vector(3 downto 0);
    clk 		  : IN  STD_LOGIC; 				   --RELOJ FPGA
	lcd_e  : out std_logic;
    lcd_rs : out std_logic;
    lcd_rw : out std_logic;
    lcd_db4 : out std_logic;
    lcd_db5 : out std_logic;
    lcd_db6 : out std_logic;
    lcd_db7 : out std_logic);
    
end LCD;

architecture Behavioral of LCD is
signal lcd_db:std_logic_vector(7 downto 4);
begin


lcd: entity work.logica_usuario
port map(clk => clk,
lcd_e =>lcd_e,
lcd_rs => lcd_rs,
lcd_rw => lcd_rw,
lcd_db(4)  => lcd_db4,
lcd_db(5)  => lcd_db5,
lcd_db(6)  => lcd_db6,
lcd_db(7)  => lcd_db7,
data_entry => data_entry,
puntos => puntos);




end behavioral;
