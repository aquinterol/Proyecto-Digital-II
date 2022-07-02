#!/usr/bin/env python3

from migen import *
from migen.genlib.io import CRG
from migen.genlib.cdc import MultiReg

#import nexys4 as tarjeta
import nexys4ddr as tarjeta
#import c4e6e10 as tarjeta

from litex.soc.integration.soc_core import *
from litex.soc.integration.builder import *
from litex.soc.interconnect.csr import *

from litex.soc.cores import gpio
from module import rgbled
from module import sevensegment
from module import vgacontroller
from module import ultrasonido
from module import PWMUS
from module import infraRed
from module import RFID
from module import lcd
from module import inductivo 
from module import Boton
from module import ultraSound
from litex.soc.cores import uart

# BaseSoC ------------------------------------------------------------------------------------------

class BaseSoC(SoCCore):
	def __init__(self):
		platform = tarjeta.Platform()
		
		# add Here verilog sources

		#Perifericos
		platform.add_source("module/VHDL/INTESC_LIB_ULTRASONICO_RevC.vhd")
		platform.add_source("module/VHDL/DIVISION_ULTRASONICO_RevA.vhd")
		platform.add_source("module/verilog/PWMUS.v")
		platform.add_source("module/verilog/infraRed.v")
		platform.add_source("module/verilog/inductivo.v")
		platform.add_source("module/verilog/boton.v")
		platform.add_source("module/verilog/spi_controller.v")
		platform.add_source("module/verilog/ultraSound.v")
		platform.add_source("module/verilog/divFreq.v")
		platform.add_source("module/VHDL/key_LCD.vhd")
		platform.add_source("module/VHDL/logica_usuario.vhd")
		platform.add_source("module/VHDL/controlador.vhd")
		
		
		# SoC with CPU
		SoCCore.__init__(self, platform,
 			cpu_type="picorv32",
#			cpu_type="vexriscv",
			clk_freq=100e6,
			integrated_rom_size=0x6000,
			integrated_main_ram_size=16*1024)

		# Clock Reset Generation
		self.submodules.crg = CRG(platform.request("clk"), ~platform.request("cpu_reset"))

		# Leds
		SoCCore.add_csr(self,"leds")
		user_leds = Cat(*[platform.request("led", i) for i in range(10)])
		self.submodules.leds = gpio.GPIOOut(user_leds)
		
		# Switchs
		SoCCore.add_csr(self,"switchs")
		user_switchs = Cat(*[platform.request("sw", i) for i in range(8)])
		self.submodules.switchs = gpio.GPIOIn(user_switchs)
		
		# Buttons
		SoCCore.add_csr(self,"buttons")
		user_buttons = Cat(*[platform.request("btn%c" %c) for c in ['c','r','l']])
		self.submodules.buttons = gpio.GPIOIn(user_buttons)
		
		# 7segments Display
		SoCCore.add_csr(self,"display")
		display_segments = Cat(*[platform.request("display_segment", i) for i in range(8)])
		display_digits = Cat(*[platform.request("display_digit", i) for i in range(8)])
		self.submodules.display = sevensegment.SevenSegment(display_segments,display_digits)

		# RGB leds
		SoCCore.add_csr(self,"ledRGB_1")
		self.submodules.ledRGB_1 = rgbled.RGBLed(platform.request("ledRGB",1))
		
		SoCCore.add_csr(self,"ledRGB_2")
		self.submodules.ledRGB_2 = rgbled.RGBLed(platform.request("ledRGB",2))
		
		
		#ultraSound
		#SoCCore.add_csr(self,"ultrasonido_cntrl")
		#self.submodules.ultrasonido_cntrl = ultrasonido.INTESC_LIB_ULTRASONICO_RevC(platform.request("ECO"), 	platform.request("TRIGGER"))
		
		
		#ultraSound
		SoCCore.add_csr(self,"ultraSound_cntrl")
		self.submodules.ultraSound_cntrl = ultraSound.US(platform.request("echo"), 	platform.request("trig"))
		
     
		#infraRed    
		SoCCore.add_csr(self,"IR_cntrl")	
		self.submodules.IR_cntrl = infraRed.infraRed(platform.request("ir"))
		
		#inductivo  
		SoCCore.add_csr(self,"IN_cntrl")	
		self.submodules.IN_cntrl = inductivo.inductivo(platform.request("ind"))
		
			
		#BTONES
		SoCCore.add_csr(self,"Boton_cntrl")
		self.submodules.Boton_cntrl = Boton.boton(platform.request("b1"), platform.request("b2"))
		
		#("btnr", 0, Pins("M17"), IOStandard("LVCMOS33")),
       # ("btnl", 0, Pins("P17"), IOStandard("LVCMOS33")),
		
					
		#PWMUS
		SoCCore.add_csr(self,"PWMUS_cntrl")
		self.submodules.PWMUS_cntrl = PWMUS.servoUS(platform.request("servo1"),platform.request("servo2"),platform.request("servo3"))
		
				
	    #UART BLUETHOOT
		self.submodules.uart1_phy = uart.UARTPHY(
			pads     = platform.request("uart1"),
			clk_freq = self.sys_clk_freq,
			baudrate = 9600)
		self.submodules.uart1 = ResetInserter()(uart.UART(self.uart1_phy,
			tx_fifo_depth = 16,
			rx_fifo_depth = 16))
		self.csr.add("uart1_phy", use_loc_if_exists=True)
		self.csr.add("uart1", use_loc_if_exists=True)
		if hasattr(self.cpu, "interrupt"):
			self.irq.add("uart1", use_loc_if_exists=True)
		else:
			self.add_constant("UART_POLLING")
		
		
		#Control LCD
		SoCCore.add_csr(self,"lcd")
		lcd_e=platform.request("lcd_e",0)
		lcd_rs=platform.request("lcd_rs",0)
		lcd_rw=platform.request("lcd_rw",0)
		lcd_db7=platform.request("lcd_db7",0)
		lcd_db6=platform.request("lcd_db6",0)
		lcd_db5=platform.request("lcd_db5",0)
		lcd_db4=platform.request("lcd_db4",0)

		self.submodules.lcd = lcd.LCD(lcd_e,lcd_rs,lcd_rw,lcd_db7,lcd_db6,lcd_db5,lcd_db4)


# Build --------------------------------------------------------------------------------------------

if __name__ == "__main__":
	builder = Builder(BaseSoC(),csr_csv="Soc_MemoryMap.csv")
	builder.build()
