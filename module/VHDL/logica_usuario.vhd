----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 20.01.2022 13:08:40
-- Design Name: 
-- Module Name: logica_usuario - Behavioral
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

library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use ieee.std_logic_arith.all;
use IEEE.std_logic_unsigned.all;
use IEEE.STD_LOGIC_1164.ALL;-------------------------------------------------------------------------------

entity logica_usuario is
  port (

    clk    : in  std_logic;
    lcd_e  : out std_logic;
    lcd_rs : out std_logic;
    lcd_rw : out std_logic;
    lcd_db : out std_logic_vector(7 downto 4);
    data_entry : in std_logic_vector (3 DOWNTO 0);
    puntos  :   in std_logic_vector(3 downto 0)); 

end entity logica_usuario;

-------------------------------------------------------------------------------

architecture behavior of logica_usuario is

  -- 
  signal timer : natural range 0 to 100000000 := 0;
  signal switch_lines : std_logic := '0';
  signal line1 : std_logic_vector(127 downto 0); --16 POSICIONES, CADA UNA DE 8 BITS
  signal line2 : std_logic_vector(127 downto 0); --16 POSICIONES, CADA UNA DE 8 BITS
  signal count : integer range 0 to 10:= 0;

  -- component generics
  constant CLK_PERIOD_NS : positive := 8;  -- 125 Mhz

  -- component ports
  signal rst          : std_logic;
  signal line1_buffer : std_logic_vector(127 downto 0) := (others => '0');--SE�ALES: TRANSPORTAN EL MENSAJE
  signal line2_buffer : std_logic_vector(127 downto 0) := x"3E202020202020202020202020202020";

  -- Componentes m�quina de estados
  type states is (s0,s1,s2,s3,s4,s5,s6,s7,s8,s9);
  signal present_state, next_state: states;
      
         
      
begin  -- architecture behavior

  -- component instantiation
  DUT : entity work.controlador 
    generic map (
      CLK_PERIOD_NS => CLK_PERIOD_NS)
    port map (
      clk          => clk,
      rst          => rst,
      lcd_e        => lcd_e,
      lcd_rs       => lcd_rs,
      lcd_rw       => lcd_rw,
      lcd_db       => lcd_db,
      line1_buffer => line1_buffer,
      line2_buffer => line2_buffer);

  rst <= '0';

  -- see the display's datasheet for the character map
  
--===================
-- Present State
--===================
process(clk)
  begin
    present_state <= s0;
  if ((clk'event and clk='1')) then
	   present_state <= next_state;
    else		
	   present_state <= present_state;
  end if;
end process;

--===================
-- Next state logic
--===================
process(present_state)
  begin 
  case present_state is 
    when s0 =>
	   if (data_entry = "0001") then
		   next_state <= s1;
       elsif (data_entry = "0010") then 
            next_state <= s2;
       else
		   next_state <= s0;
		end if;

    when s1 =>
	    if (data_entry = "0011") then
		   next_state <= s3;
		else 
		   next_state <= s1;
		end if;
		
	when s2 =>
	   if (data_entry = "0011") then
		   next_state <= s3;
		   
		else 
		   next_state <= s2;
		end if;

    when s3 =>
	    if (data_entry = "0100") then
		   next_state <= s4;
		else 
		   next_state <= s3;
		end if;
		
	when s4 =>
	   if (data_entry = "0101") then
		   next_state <= s5;
       elsif (data_entry = "0110") then 
            next_state <= s6;
       elsif (data_entry = "0111") then 
            next_state <= s7;     
       else
		   next_state <= s4;
		end if;

    when s5 =>
	    if (data_entry = "1000") then
		   next_state <= s8;
		else 
		   next_state <= s5;
		end if;
	when s6 =>
	   if (data_entry = "1000") then
		   next_state <= s8;
		   
		else 
		   next_state <= s6;
		end if;

    when s7 =>
	    if (data_entry = "1000") then
		   next_state <= s8;
		else 
		   next_state <= s7;
		end if;	
		
    when s8 =>
	    if (data_entry = "1001") then
		   next_state <= s4;
		elsif (data_entry = "1010") then 
            next_state <= s9;   
		else 
		   next_state <= s8;
		end if;
	when s9 =>
	   if (data_entry = "1011") then
		   next_state <= s0;
		   
		else 
		   next_state <= s9;
		end if;

  end case;
end process;

--===================	
-- Output logic
--===================
process(present_state, clk)
  begin
  case present_state is
    when s0 =>   
    --Acerque su 
    line1 <= x"20204163657271756520737520202020";
    line1_buffer <= line1;
    -- tarjeta:
    line2 <= x"20202020207461726a65746120202020";
    line2_buffer <= line2;
    
    when s1 =>
	--Bienvenido
	line1 <= x"202020204269656e76656e69646f2020";
    line1_buffer <= line1;
	  --  Diana 
    line2 <= x"20202020204469616e61202020202020";  
    line2_buffer <= line2;   
    
    when s2 =>
	-- Bienvenido
	line1 <= x"202020204269656e76656e69646f2020";
    line1_buffer <= line1;
	  -- Ana Maria  
    line2 <= x"20202020416e61204d61726961202020";  
    line2_buffer <= line2; 
    
     when s3 =>   
    -- 1. Para
    line1 <= x"20202020312e20506172612020202020";
    line1_buffer <= line1;
    --  detectar
    line2 <= x"20202020446574656374617220202020";
    line2_buffer <= line2;
    
    when s4 =>
	--Procesando ...
	line1 <= x"50726f636573616e646f202e2e2e2020";
    line1_buffer <= line1;
	  -- Blanco   
    line2 <= x"20202020202020202020202020202020";  
    line2_buffer <= line2;   
    
    when s5 =>
	-- Plastico
	line1 <= x"20202020506c61737469636f20202020";
    line1_buffer <= line1;
	  -- + 3 puntos   
	 line2 <= x"2020202b20332050756e746f73202020";  
    line2_buffer <= line2;
    
     when s6 =>   
    -- Metal
    line1 <= x"20202020204d6574616c202020202020";
    line1_buffer <= line1;
    -- 2
    line2 <= x"2020202b20322050756e746f73202020";
    line2_buffer <= line2;
    
    when s7 =>
	-- Papel
	line1 <= x"2020202020506170656c202020202020";
    line1_buffer <= line1;
	  -- 1   
	 line2 <= x"2020202b20312050756e746f73202020";  
    line2_buffer <= line2; 
    
    when s8 =>
	--1. Detectar
	line1 <= x"312e2044657465637461722020202020";
    line1_buffer <= line1;
	  --  2. Terminar
	 line2 <= x"322e205465726d696e61722020202020";  
    line2_buffer <= line2;   
    
     when s9 =>
	--Diana 
	line1 <= x"2020202020" & x"3" & puntos(3 downto 0)& x"2050756e746f73202020";
    line1_buffer <= line1;
	  --  Diana 
	 line2 <= x"20202020202020202020202020202020";  
    line2_buffer <= line2;   
    
    
  end case;
end process;


end architecture behavior;

