#include "delay.h"
#include <generated/csr.h>
#define SPI_START  0x01                    // spi Start
#define SPI_BUSY   0x02                    // spi busy
#define SPI_NEWDATA  0x04                    // spi newData

typedef struct{
	volatile uint32_t ucr;
	volatile uint32_t data_in;
	volatile uint32_t data_out;
} spi_t;

void spi_start();
unsigned char spi_read(char reg);
void spi_write(char reg, char value);

/***************************************************************************
 * Pointer to actual components
 */

extern spi_t   *spi0;
spi_t   *spi0   = (spi_t *)    0x50000000;



/*spi_controller  spi0 (
	.clk( clk ),
	.reset( ~rst ),
	//
	.wb_adr_i( spi0_adr ),
	.wb_dat_i( spi0_dat_w ),
	.wb_dat_o( spi0_dat_r ),
	.wb_stb_i( spi0_stb ),
	.wb_cyc_i( spi0_cyc ),
	.wb_we_i(  spi0_we ),
	.wb_sel_i( spi0_sel ),
	.wb_ack_o( spi0_ack ),
	.mosi( mosi ),
	.miso( miso ),
	.sck(sck),
	.ss(ss)
);


spi_controller spi0(
    .clk (clk),
    .rst (~rst),
    .miso (miso),
    .mosi (mosi),
    .sck (sck),
    .ss (ss),
    .start(start)
  ); */

