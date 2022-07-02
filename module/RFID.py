from migen import *
from migen.genlib.cdc import MultiReg
from litex.soc.interconnect.csr import *
from litex.soc.interconnect.csr_eventmanager import *

class spi_controller(Module, AutoCSR):
    def __init__(self, miso, mosi, sck, ss):
        #entradas
        self.clk = ClockSignal()
        self.rst = ResetSignal()
        self.miso = miso
        self.mosi = mosi
        self.ss = ss
        self.sck = sck
        
        
        #Registros de memoria - mapeados
        self.start = CSRStorage(1)
        self.busy = CSRStatus(1)
        self.new_data = CSRStatus(1)
        self.data_in = CSRStorage(16)
        self.data_out = CSRStatus(16)


        self.specials += Instance("spi_controller",
            i_clk = self.clk,
            i_rst = self.rst,
            i_miso = self.miso,
            o_mosi = self.mosi,
            o_sck = self.sck,
            o_ss = self.ss,
            i_start = self.start.storage,
            i_data_in = self.data_in.storage,
            o_data_out = self.data_out.status,
            o_busy = self.busy.status,
            o_new_data = self.new_data.status)
        
