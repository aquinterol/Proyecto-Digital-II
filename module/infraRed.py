from migen import *
from migen.genlib.cdc import MultiReg
from litex.soc.interconnect.csr import *
from litex.soc.interconnect.csr_eventmanager import *

class infraRed(Module, AutoCSR):
    def __init__(self, ir):

            self.ir = ir

#Mapeo de memoria
            self.data_ir = CSRStatus(1)
 
            self.specials += Instance("infraRed",
                i_ir = self.ir,
                o_data_ir = self.data_ir.status)
