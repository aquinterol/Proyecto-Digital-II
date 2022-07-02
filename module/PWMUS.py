from migen import *
from migen.genlib.cdc import MultiReg
from litex.soc.interconnect.csr import *
from litex.soc.interconnect.csr_eventmanager import *

class servoUS(Module, AutoCSR):
    def __init__(self, servo1, servo2, servo3):
            self.clk = ClockSignal()
            self.pos1 = CSRStorage(2)
            self.servo1 = servo1
            self.pos2 = CSRStorage(2)
            self.servo2 = servo2
            self.pos3 = CSRStorage(2)
            self.servo3 = servo3

            self.specials += Instance("PWMUS",
                i_clk = self.clk,
                i_pos1 = self.pos1.storage,
                o_servo1 = self.servo1,
                i_pos2 = self.pos2.storage,
                o_servo2 = self.servo2,
                i_pos3 = self.pos3.storage,
                o_servo3 = self.servo3)
