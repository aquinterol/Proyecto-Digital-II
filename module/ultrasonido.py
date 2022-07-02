from migen import *
from migen.genlib.cdc import MultiReg
from litex.soc.interconnect.csr import *
from litex.soc.interconnect.csr_eventmanager import *

class INTESC_LIB_ULTRASONICO_RevC(Module, AutoCSR):
    def __init__(self, ECO, TRIGGER):
        #entradas
        self.CLK = ClockSignal()
        self.ECO = ECO
        self.TRIGGER = TRIGGER
        
        #Registros de memoria - mapeados
        self.DISTANCIA_CM = CSRStatus(9)
        self.DATO_LISTO = CSRStatus(1)

        self.specials += Instance("INTESC_LIB_ULTRASONICO_RevC",
            i_clk = self.CLK,
            i_ECO = self.ECO,
            o_TRIGGER = self.TRIGGER,
            o_DISTANCIA_CM = self.DISTANCIA_CM.status,
            o_DATO_LISTO = self.DATO_LISTO.status)
        
