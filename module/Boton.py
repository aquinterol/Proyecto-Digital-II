from migen import *
from migen.genlib.cdc import MultiReg
from litex.soc.interconnect.csr import *
from litex.soc.interconnect.csr_eventmanager import *

class boton(Module, AutoCSR):
    def __init__(self, b1, b2):

            self.b1 = b1
            self.b2 = b2

#Mapeo de memoria
            self.data_b1 = CSRStatus(1)
            self.data_b2 = CSRStatus(1)
 
            self.specials += Instance("boton",
                i_b1 = self.b1,
                o_data_b1 = self.data_b1.status,
                i_b2 = self.b2,
                o_data_b2 = self.data_b2.status)

