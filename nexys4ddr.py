from litex.build.generic_platform import *
from litex.build.xilinx import XilinxPlatform, VivadoProgrammer

# IOs ----------------------------------------------------------------------------------------------

_io = [
    ("led",  0, Pins("H17"), IOStandard("LVCMOS33")),
    ("led",  1, Pins("K15"), IOStandard("LVCMOS33")),
    ("led",  2, Pins("J13"), IOStandard("LVCMOS33")),
    ("led",  3, Pins("N14"), IOStandard("LVCMOS33")),
    ("led",  4, Pins("R18"), IOStandard("LVCMOS33")),
    ("led",  5, Pins("V17"), IOStandard("LVCMOS33")),
    ("led",  6, Pins("U17"), IOStandard("LVCMOS33")),
    ("led",  7, Pins("U16"), IOStandard("LVCMOS33")),
    ("led",  8, Pins("V16"), IOStandard("LVCMOS33")),
    ("led",  9, Pins("T15"), IOStandard("LVCMOS33")),
    ("led", 10, Pins("U14"), IOStandard("LVCMOS33")),
    ("led", 11, Pins("T16"), IOStandard("LVCMOS33")),
    ("led", 12, Pins("V15"), IOStandard("LVCMOS33")),
    ("led", 13, Pins("V14"), IOStandard("LVCMOS33")),
    ("led", 14, Pins("V12"), IOStandard("LVCMOS33")),
    ("led", 15, Pins("V11"), IOStandard("LVCMOS33")),

    ("sw",  0, Pins("J15"), IOStandard("LVCMOS33")),
    ("sw",  1, Pins("L16"), IOStandard("LVCMOS33")),
    ("sw",  2, Pins("M13"), IOStandard("LVCMOS33")),
    ("sw",  3, Pins("R15"), IOStandard("LVCMOS33")),
    ("sw",  4, Pins("R17"), IOStandard("LVCMOS33")),
    ("sw",  5, Pins("T18"), IOStandard("LVCMOS33")),
    ("sw",  6, Pins("U18"), IOStandard("LVCMOS33")),
    ("sw",  7, Pins("R13"), IOStandard("LVCMOS33")),
    ("sw",  8, Pins("T8"), IOStandard("LVCMOS33")),
    ("sw",  9, Pins("U8"), IOStandard("LVCMOS33")),
    ("sw", 10, Pins("R16"), IOStandard("LVCMOS33")),
    ("sw", 11, Pins("T13"), IOStandard("LVCMOS33")),
    ("sw", 12, Pins("H6"), IOStandard("LVCMOS33")),
    ("sw", 13, Pins("U12"), IOStandard("LVCMOS33")),
    ("sw", 14, Pins("U11"), IOStandard("LVCMOS33")),
    ("sw", 15, Pins("V10"), IOStandard("LVCMOS33")),
    
    ("btnc", 0, Pins("N17"), IOStandard("LVCMOS33")),
    ("btnd", 0, Pins("P18"), IOStandard("LVCMOS33")),
    ("btnu", 0, Pins("M18"), IOStandard("LVCMOS33")),
    ("btnr", 0, Pins("M17"), IOStandard("LVCMOS33")),
    ("btnl", 0, Pins("P17"), IOStandard("LVCMOS33")),

    ("ledRGB", 1,
        Subsignal("r", Pins("N15")),
        Subsignal("g", Pins("M16")),
        Subsignal("b", Pins("R12")),
        IOStandard("LVCMOS33")),

    ("ledRGB", 2,
        Subsignal("r", Pins("N16")),
        Subsignal("g", Pins("R11")),
        Subsignal("b", Pins("G14")),
        IOStandard("LVCMOS33")),
       
    ("display_digit",  0, Pins("J17"), IOStandard("LVCMOS33")),
    ("display_digit",  1, Pins("J18"), IOStandard("LVCMOS33")),
    ("display_digit",  2, Pins("T9"), IOStandard("LVCMOS33")),
    ("display_digit",  3, Pins("J14"), IOStandard("LVCMOS33")),
    ("display_digit",  4, Pins("P14"), IOStandard("LVCMOS33")),
    ("display_digit",  5, Pins("T14"), IOStandard("LVCMOS33")),
    ("display_digit",  6, Pins("K2"), IOStandard("LVCMOS33")),
    ("display_digit",  7, Pins("U13"), IOStandard("LVCMOS33")),
    ("display_segment", 0, Pins("T10"), IOStandard("LVCMOS33")),
    ("display_segment", 1, Pins("R10"), IOStandard("LVCMOS33")),
    ("display_segment", 2, Pins("K16"), IOStandard("LVCMOS33")),
    ("display_segment", 3, Pins("K13"), IOStandard("LVCMOS33")),
    ("display_segment", 4, Pins("P15"), IOStandard("LVCMOS33")),
    ("display_segment", 5, Pins("T11"), IOStandard("LVCMOS33")),
    ("display_segment", 6, Pins("L18"), IOStandard("LVCMOS33")),
    ("display_segment", 7, Pins("H15"), IOStandard("LVCMOS33")),
    
  	
    ("vga_red", 0, Pins("A3"), IOStandard("LVCMOS33")),
    ("vga_red", 1, Pins("B4"), IOStandard("LVCMOS33")),
    ("vga_red", 2, Pins("C5"), IOStandard("LVCMOS33")),
    ("vga_red", 3, Pins("A4"), IOStandard("LVCMOS33")),
    ("vga_green", 0, Pins("C6"), IOStandard("LVCMOS33")),
    ("vga_green", 1, Pins("A5"), IOStandard("LVCMOS33")),
    ("vga_green", 2, Pins("B6"), IOStandard("LVCMOS33")),
    ("vga_green", 3, Pins("A6"), IOStandard("LVCMOS33")),
    ("vga_blue", 0, Pins("B7"), IOStandard("LVCMOS33")),
    ("vga_blue", 1, Pins("C7"), IOStandard("LVCMOS33")),
    ("vga_blue", 2, Pins("D7"), IOStandard("LVCMOS33")),
    ("vga_blue", 3, Pins("D8"), IOStandard("LVCMOS33")),
    ("hsync", 0, Pins("B11"), IOStandard("LVCMOS33")),
    ("vsync", 0, Pins("B12"), IOStandard("LVCMOS33")),
    
    ("cpu_reset", 0, Pins("C12"), IOStandard("LVCMOS33")),
    
    ("clk", 0, Pins("E3"), IOStandard("LVCMOS33")),

    ("serial", 0,
        Subsignal("tx", Pins("D4")),
        Subsignal("rx", Pins("C4")),
        IOStandard("LVCMOS33"),
    ),

    ("ddram", 0,
        Subsignal("a", Pins(
            "M4 P4 M6 T1 L3 P5 M2 N1",
            "L4 N5 R2 K5 N6"),
            IOStandard("SSTL18_II")),
        Subsignal("ba", Pins("P2 P3 R1"), IOStandard("SSTL18_II")),
        Subsignal("ras_n", Pins("N4"), IOStandard("SSTL18_II")),
        Subsignal("cas_n", Pins("L1"), IOStandard("SSTL18_II")),
        Subsignal("we_n", Pins("N2"), IOStandard("SSTL18_II")),
        Subsignal("dm", Pins("T6 U1"), IOStandard("SSTL18_II")),
        Subsignal("dq", Pins(
            "R7 V6 R8 U7 V7 R6 U6 R5",
            "T5 U3 V5 U4 V4 T4 V1 T3"),
            IOStandard("SSTL18_II"),
            Misc("IN_TERM=UNTUNED_SPLIT_50")),
        Subsignal("dqs_p", Pins("U9 U2"), IOStandard("DIFF_SSTL18_II")),
        Subsignal("dqs_n", Pins("V9 V2"), IOStandard("DIFF_SSTL18_II")),
        Subsignal("clk_p", Pins("L6"), IOStandard("DIFF_SSTL18_II")),
        Subsignal("clk_n", Pins("L5"), IOStandard("DIFF_SSTL18_II")),
        Subsignal("cke", Pins("M1"), IOStandard("SSTL18_II")),
        Subsignal("odt", Pins("M3"), IOStandard("SSTL18_II")),
        Subsignal("cs_n", Pins("K6"), IOStandard("SSTL18_II")),
        Misc("SLEW=FAST"),
    ),

    ("eth_clocks", 0,
        Subsignal("ref_clk", Pins("D5")),
        IOStandard("LVCMOS33"),
    ),

    ("eth", 0,
        Subsignal("rst_n", Pins("B3")),
        Subsignal("rx_data", Pins("C11 D10")),
        Subsignal("crs_dv", Pins("D9")),
        Subsignal("tx_en", Pins("B9")),
        Subsignal("tx_data", Pins("A10 A8")),
        Subsignal("mdc", Pins("C9")),
        Subsignal("mdio", Pins("A9")),
        Subsignal("rx_er", Pins("C10")),
        Subsignal("int_n", Pins("D8")),
        IOStandard("LVCMOS33")
     ),
    

##Pmod Headers


##Pmod Header JA

  ("echo",  0, Pins("D17"), IOStandard("LVCMOS33")), 
  ("trig",  0, Pins("E17"), IOStandard("LVCMOS33")),  
  ("ir",  0, Pins("E18"), IOStandard("LVCMOS33")), 
  ("ind",  0, Pins("G17"), IOStandard("LVCMOS33")),  
  
#set_property -dict { PACKAGE_PIN D17   IOSTANDARD LVCMOS33 } [get_ports { JA[7] }]; #IO_L16N_T2_A27_15 Sch=ja[7]
#set_property -dict { PACKAGE_PIN E17   IOSTANDARD LVCMOS33 } [get_ports { JA[8] }]; #IO_L16P_T2_A28_15 Sch=ja[8]
#set_property -dict { PACKAGE_PIN F18   IOSTANDARD LVCMOS33 } [get_ports { JA[9] }]; #IO_L22N_T3_A16_15 Sch=ja[9]
#set_property -dict { PACKAGE_PIN G18   IOSTANDARD LVCMOS33 } [get_ports { JA[10] }]; #IO_L22P_T3_A17_15 Sch=ja[10]


##Pmod Header JC

      #Pines LCD
    ("lcd_e",0,Pins("E7"),IOStandard("LVCMOS33")), 
    ("lcd_rw",0,Pins("J3"),IOStandard("LVCMOS33")),
    ("lcd_rs",0,Pins("J4"),IOStandard("LVCMOS33")),

    ("lcd_db7",0,Pins("K1"),IOStandard("LVCMOS33")), 
    ("lcd_db6",0,Pins("F6"),IOStandard("LVCMOS33")),
    ("lcd_db5",0,Pins("J2"),IOStandard("LVCMOS33")),
    ("lcd_db4",0,Pins("G6"),IOStandard("LVCMOS33")),

#set_property -dict { PACKAGE_PIN K1    IOSTANDARD LVCMOS33 } [get_ports { JC[1] }]; #IO_L23N_T3_35 Sch=jc[1]
#set_property -dict { PACKAGE_PIN F6    IOSTANDARD LVCMOS33 } [get_ports { JC[2] }]; #IO_L19N_T3_VREF_35 Sch=jc[2]
#set_property -dict { PACKAGE_PIN J2    IOSTANDARD LVCMOS33 } [get_ports { JC[3] }]; #IO_L22N_T3_35 Sch=jc[3]
#set_property -dict { PACKAGE_PIN G6    IOSTANDARD LVCMOS33 } [get_ports { JC[4] }]; #IO_L19P_T3_35 Sch=jc[4]
#set_property -dict { PACKAGE_PIN E7    IOSTANDARD LVCMOS33 } [get_ports { JC[7] }]; #IO_L6P_T0_35 Sch=jc[7]
#set_property -dict { PACKAGE_PIN J3    IOSTANDARD LVCMOS33 } [get_ports { JC[8] }]; #IO_L22P_T3_35 Sch=jc[8]
#set_property -dict { PACKAGE_PIN J4    IOSTANDARD LVCMOS33 } [get_ports { JC[9] }]; #IO_L21P_T3_DQS_35 Sch=jc[9]
#set_property -dict { PACKAGE_PIN E6    IOSTANDARD LVCMOS33 } [get_ports { JC[10] }]; #IO_L5P_T0_AD13P_35 Sch=jc[10]



##Pmod Header JB

  # ("b1",  0, Pins("D14"), IOStandard("LVCMOS33")),
  # ("b2",  0, Pins("F16"), IOStandard("LVCMOS33")),
   ("servo1",  0, Pins("E16"), IOStandard("LVCMOS33")),
   ("servo2",  0, Pins("F13"), IOStandard("LVCMOS33")),
   ("servo3",  0, Pins("G13"), IOStandard("LVCMOS33")),
   
     ("uart1", 0,
        Subsignal("tx", Pins("G16")),
        Subsignal("rx", Pins("H14")),
        IOStandard("LVCMOS33"),
    ),
   

#set_property -dict { PACKAGE_PIN D14   IOSTANDARD LVCMOS33 } [get_ports { JB[1] }]; #IO_L1P_T0_AD0P_15 Sch=jb[1]
#set_property -dict { PACKAGE_PIN F16   IOSTANDARD LVCMOS33 } [get_ports { JB[2] }]; #IO_L14N_T2_SRCC_15 Sch=jb[2]
#set_property -dict { PACKAGE_PIN G16   IOSTANDARD LVCMOS33 } [get_ports { JB[3] }]; #IO_L13N_T2_MRCC_15 Sch=jb[3]
#set_property -dict { PACKAGE_PIN H14   IOSTANDARD LVCMOS33 } [get_ports { JB[4] }]; #IO_L15P_T2_DQS_15 Sch=jb[4]
#set_property -dict { PACKAGE_PIN E16   IOSTANDARD LVCMOS33 } [get_ports { JB[7] }]; #IO_L11N_T1_SRCC_15 Sch=jb[7]
#set_property -dict { PACKAGE_PIN F13   IOSTANDARD LVCMOS33 } [get_ports { JB[8] }]; #IO_L5P_T0_AD9P_15 Sch=jb[8]
#set_property -dict { PACKAGE_PIN G13   IOSTANDARD LVCMOS33 } [get_ports { JB[9] }]; #IO_0_15 Sch=jb[9]
#set_property -dict { PACKAGE_PIN H16   IOSTANDARD LVCMOS33 } [get_ports { JB[10] }]; #IO_L13P_T2_MRCC_15 Sch=jb[10]



##Pmod Header JD

   ("b1",  0, Pins("H4"), IOStandard("LVCMOS33")),
   ("b2",  0, Pins("H1"), IOStandard("LVCMOS33")),

#set_property -dict { PACKAGE_PIN H4    IOSTANDARD LVCMOS33 } [get_ports { JD[1] }]; #IO_L21N_T3_DQS_35 Sch=jd[1]
#set_property -dict { PACKAGE_PIN H1    IOSTANDARD LVCMOS33 } [get_ports { JD[2] }]; #IO_L17P_T2_35 Sch=jd[2]
#set_property -dict { PACKAGE_PIN G1    IOSTANDARD LVCMOS33 } [get_ports { JD[3] }]; #IO_L17N_T2_35 Sch=jd[3]
#set_property -dict { PACKAGE_PIN G3    IOSTANDARD LVCMOS33 } [get_ports { JD[4] }]; #IO_L20N_T3_35 Sch=jd[4]
#set_property -dict { PACKAGE_PIN H2    IOSTANDARD LVCMOS33 } [get_ports { JD[7] }]; #IO_L15P_T2_DQS_35 Sch=jd[7]
#set_property -dict { PACKAGE_PIN G4    IOSTANDARD LVCMOS33 } [get_ports { JD[8] }]; #IO_L20P_T3_35 Sch=jd[8]
#set_property -dict { PACKAGE_PIN G2    IOSTANDARD LVCMOS33 } [get_ports { JD[9] }]; #IO_L15N_T2_DQS_35 Sch=jd[9]
#set_property -dict { PACKAGE_PIN F3    IOSTANDARD LVCMOS33 } [get_ports { JD[10] }]; #IO_L13N_T2_MRCC_35 Sch=jd[10]


##Pmod Header JXADC

#set_property -dict { PACKAGE_PIN A14   IOSTANDARD LVDS     } [get_ports { XA_N[1] }]; #IO_L9N_T1_DQS_AD3N_15 Sch=xa_n[1]
#set_property -dict { PACKAGE_PIN A13   IOSTANDARD LVDS     } [get_ports { XA_P[1] }]; #IO_L9P_T1_DQS_AD3P_15 Sch=xa_p[1]
#set_property -dict { PACKAGE_PIN A16   IOSTANDARD LVDS     } [get_ports { XA_N[2] }]; #IO_L8N_T1_AD10N_15 Sch=xa_n[2]
#set_property -dict { PACKAGE_PIN A15   IOSTANDARD LVDS     } [get_ports { XA_P[2] }]; #IO_L8P_T1_AD10P_15 Sch=xa_p[2]
#set_property -dict { PACKAGE_PIN B17   IOSTANDARD LVDS     } [get_ports { XA_N[3] }]; #IO_L7N_T1_AD2N_15 Sch=xa_n[3]
#set_property -dict { PACKAGE_PIN B16   IOSTANDARD LVDS     } [get_ports { XA_P[3] }]; #IO_L7P_T1_AD2P_15 Sch=xa_p[3]
#set_property -dict { PACKAGE_PIN A18   IOSTANDARD LVDS     } [get_ports { XA_N[4] }]; #IO_L10N_T1_AD11N_15 Sch=xa_n[4]
#set_property -dict { PACKAGE_PIN B18   IOSTANDARD LVDS     } [get_ports { XA_P[4] }]; #IO_L10P_T1_AD11P_15 Sch=xa_p[4]

    
    
    
]

# Platform -----------------------------------------------------------------------------------------

class Platform(XilinxPlatform):
    default_clk_name = "clk"
    default_clk_period = 1e9/100e6

    def __init__(self):
        XilinxPlatform.__init__(self, "xc7a100t-CSG324-1", _io, toolchain="vivado")
        self.add_platform_command("set_property INTERNAL_VREF 0.750 [get_iobanks 34]")

    def create_programmer(self):
        return VivadoProgrammer()

    def do_finalize(self, fragment):
        XilinxPlatform.do_finalize(self, fragment)
