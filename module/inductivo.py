from migen import *
from migen.genlib.cdc import MultiReg
from litex.soc.interconnect.csr import *
from litex.soc.interconnect.csr_eventmanager import *

class inductivo(Module, AutoCSR):
   def __init__(self, ind):
            
            self.ind = ind;

#Mapeo de memoria
            self.data_in = CSRStatus(1)
 
            self.specials += Instance("inductivo",
                i_ind = self.ind,
                o_data_in = self.data_in.status)
