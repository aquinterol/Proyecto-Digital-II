from migen import *
from migen.genlib.cdc import MultiReg
from litex.soc.interconnect.csr import *
from litex.soc.interconnect.csr_eventmanager import *

# Modulo Principal
class LCD(Module,AutoCSR):
    def __init__(self, lcd_e, lcd_rs, lcd_rw, lcd_db7,lcd_db6,lcd_db5,lcd_db4):
        self.clk = ClockSignal()
        self.data_entry = CSRStorage(4)
        self.puntos = CSRStorage(4)
        self.lcd_e = lcd_e
        self.lcd_rs = lcd_rs
        self.lcd_rw = lcd_rw  
        self.lcd_db7 = lcd_db7
        self.lcd_db6 = lcd_db6
        self.lcd_db5 = lcd_db5
        self.lcd_db4 = lcd_db4



        self.specials +=Instance("LCD",
            i_clk = self.clk,
            i_data_entry = self.data_entry.storage,
            i_puntos = self.puntos.storage,
            o_lcd_e = self.lcd_e,
            o_lcd_rs = self.lcd_rs,
            o_lcd_rw = self.lcd_rw,
            o_lcd_db7 = self.lcd_db7,
            o_lcd_db6 = self.lcd_db6,
            o_lcd_db5 = self.lcd_db5,
            o_lcd_db4 = self.lcd_db4,
        )

