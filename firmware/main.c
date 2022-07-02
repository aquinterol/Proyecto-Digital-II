#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#include <irq.h>
#include <uart.h>
#include <console.h>
#include <generated/csr.h>

#include "delay.h"
#include "display.h"
#include "spi0.c" 
#include <uart.h>
#include "uart1.h"
#include "uart1.c"


static char *readstr(void)
{
	char c[2];
	static char s[64];
	static int ptr = 0;

	if(readchar_nonblock()) {
		c[0] = readchar();
		c[1] = 0;
		switch(c[0]) {
			case 0x7f:
			case 0x08:
				if(ptr > 0) {
					ptr--;
					putsnonl("\x08 \x08");
				}
				break;
			case 0x07:
				break;
			case '\r':
			case '\n':
				s[ptr] = 0x00;
				putsnonl("\n");
				ptr = 0;
				return s;
			default:
				if(ptr >= (sizeof(s) - 1))
					break;
				putsnonl(c);
				s[ptr] = c[0];
				ptr++;
				break;
		}
	}
	return NULL;
}

static char *get_token(char **str)
{
	char *c, *d;

	c = (char *)strchr(*str, ' ');
	if(c == NULL) {
		d = *str;
		*str = *str+strlen(*str);
		return d;
	}
	*c = 0;
	d = *str;
	*str = c+1;
	return d;
}

static void prompt(void)
{
	printf("RUNTIME>");
}

static void help(void)
{
	puts("Available commands:");
	puts("help                            - this command");
	puts("reboot                          - reboot CPU");
	puts("led                             - led test");
	puts("switch                          - switch test");
	puts("display                         - display test");
    puts("us				              - ultraSound test");
	puts("IR				              - IR test");
 //   puts("PWM				              - PWM test");
    puts("LCD				              - LCD test");
	puts("rgbled                          - rgb led test");
	puts("vga                             - vga test");
    puts("demo                            - demo test");
}

static void reboot(void)
{
	ctrl_reset_write(1);
}

static void display_test(void)
{
	int i;
	signed char defill = 0;	//1->left, -1->right, 0->.
	
	char txtToDisplay[40] = {0, DISPLAY_0, DISPLAY_1,DISPLAY_2,DISPLAY_3,DISPLAY_4,DISPLAY_5,DISPLAY_6,DISPLAY_7,DISPLAY_8,DISPLAY_9,DISPLAY_A,DISPLAY_B,DISPLAY_C,DISPLAY_D,DISPLAY_E,DISPLAY_F,DISPLAY_G,DISPLAY_H,DISPLAY_I,DISPLAY_J,DISPLAY_K,DISPLAY_L,DISPLAY_M,DISPLAY_N,DISPLAY_O,DISPLAY_P,DISPLAY_Q,DISPLAY_R,DISPLAY_S,DISPLAY_T,DISPLAY_U,DISPLAY_V,DISPLAY_W,DISPLAY_X,DISPLAY_Y,DISPLAY_Z,DISPLAY_DP,DISPLAY_TR,DISPLAY_UR};
	
	printf("Test del los display de 7 segmentos... se interrumpe con el botton 1\n");

	while(!(buttons_in_read()&1)) {
		display(txtToDisplay);
		if(buttons_in_read()&(1<<1)) defill = ((defill<=-1) ? -1 : defill-1);
		if(buttons_in_read()&(1<<2)) defill = ((defill>=1) ? 1 : defill+1);
		if (defill > 0) {
			char tmp = txtToDisplay[0];
			for(i=0; i<sizeof(txtToDisplay)/sizeof(txtToDisplay[i]); i++) {
				txtToDisplay[i] = ((i==sizeof(txtToDisplay)/sizeof(txtToDisplay[i])-1) ? tmp : txtToDisplay[i+1]);
			}
		}
		else if(defill < 0) {
			char tmp = txtToDisplay[sizeof(txtToDisplay)/sizeof(txtToDisplay[0])-1];
			for(i=sizeof(txtToDisplay)/sizeof(txtToDisplay[i])-1; i>=0; i--) {
				txtToDisplay[i] = ((i==0) ? tmp : txtToDisplay[i-1]);
			}
		}
		delay_ms(500);
	}
}

static void led_test(void)
{
	unsigned int i;
	printf("Test del los leds... se interrumpe con el botton 1\n");
	while(!(buttons_in_read()&1)) {

	for(i=1; i<65536; i=i*2) {
		leds_out_write(i);
		delay_ms(50);
	}
	for(i=32768;i>1; i=i/2) {
		leds_out_write(i);
		delay_ms(50);
	}
	}
	
}


static void switch_test(void)
{
	unsigned short temp2 =0;
	printf("Test del los interruptores... se interrumpe con el botton 1\n");
	while(!(buttons_in_read()&1)) {
		unsigned short temp = switchs_in_read();
		if (temp2 != temp){
			printf("switch bus : %i\n", temp);
			leds_out_write(temp);
			temp2 = temp;
		}
	}
}


/*static int ultrasonido_test(void)
{
	// Se esperan 2 ms para dar tiempo a que el registro done se actualice
	delay_ms(2);
	while(1){
		if(ultrasonido_cntrl_DATO_LISTO_read() == 1){
			int d = ultrasonido_cntrl_DISTANCIA_CM_read();
            printf("Dato sensor = %d", d);
            printf("\n");
	//		return d;
		}
	}
}



static int ultrasonido(void)
{
	// Se esperan 2 ms para dar tiempo a que el registro done se actualice
	delay_ms(2);
	while(1){
		if(ultrasonido_cntrl_DATO_LISTO_read() == 1){
			int d = ultrasonido_cntrl_DISTANCIA_CM_read();
            printf("Dato sensor = %d", d);
            printf("\n");
			return d;
		}
	}
}*/

static int ultraSound_test(void)
{
	ultraSound_cntrl_init_write(1);
	// Se esperan 2 ms para dar tiempo a que el registro done se actualice
	delay_ms(2);
	while(true){
		if(ultraSound_cntrl_done_read() == 1){
			int d = ultraSound_cntrl_distance_read();
            printf("Dato sensor = %d", d);
            printf("\n");
			ultraSound_cntrl_init_write(0);
			return d;
		}
	}
}


static void lcd_test(void)
{
            int d;
            delay_ms(1000);
            lcd_data_entry_write(0x01);
            delay_ms(1200);
            d = lcd_data_entry_read();
            printf("Prueba digital %d",d);
            printf("\n");
            lcd_data_entry_write(0x02);
            delay_ms(2000);
            d = lcd_data_entry_read();
            printf("Prueba digital %d",d);
            printf("\n");
}



/*static void PWMUS_test(void){
	PWMUS_cntrl_pos_write(0);
	delay_ms(1000);
	PWMUS_cntrl_pos_write(1);
	delay_ms(1000);
	PWMUS_cntrl_pos_write(2);
	delay_ms(1000);
	PWMUS_cntrl_pos_write(3);
}*/


static void IR_test(void)
{
	printf("Test del infra rojo... se interrumpe con el botton 1\n");
	while(!(buttons_in_read()&1)){
		int data_ir = IR_cntrl_data_ir_read();
        delay_ms(2);
		//unsigned short IR = data_ir;
		printf("Dato senso =  %d", data_ir); 
		printf("\n");
	}
}




static void rgbled_test(void)
{
	unsigned int T = 128;
	
	ledRGB_1_r_period_write(T);
	ledRGB_1_g_period_write(T);
	ledRGB_1_b_period_write(T);

	ledRGB_1_r_enable_write(1);
	ledRGB_1_g_enable_write(1);
	ledRGB_1_b_enable_write(1);

	
	ledRGB_2_r_period_write(T);
	ledRGB_2_g_period_write(T);
	ledRGB_2_b_period_write(T);
	
	
	ledRGB_2_r_enable_write(1);
	ledRGB_2_g_enable_write(1);
	ledRGB_2_b_enable_write(1);

	for (unsigned int j=0; j<100; j++){
		ledRGB_1_g_width_write(j);
		for (unsigned int i=0; i<100; i++){
			ledRGB_1_r_width_write(100-i);
			ledRGB_1_b_width_write(i);	
			delay_ms(20);

		}	
	}
	
}






static void console_service(void)
{
	char *str;
	char *token;

	str = readstr();
	if(str == NULL) return;
	token = get_token(&str);
	if(strcmp(token, "help") == 0)
		help();
	else if(strcmp(token, "reboot") == 0)
		reboot();
	else if(strcmp(token, "led") == 0)
		led_test();
	else if(strcmp(token, "switch") == 0)
		switch_test();
	else if(strcmp(token, "display") == 0)
		display_test();
	else if(strcmp(token, "rgbled") == 0)
		rgbled_test();
	//else if(strcmp(token, "vga") == 0)
		//vga_test();
    else if(strcmp(token, "us") == 0)
		ultraSound_test();
  //  else if(strcmp(token, "PWM") == 0)
//		PWMUS_test();
    else if(strcmp(token, "IR") == 0)
		IR_test();
    else if(strcmp(token, "demo") == 0)
		lcd_test(); 
	prompt();
}





int main(void)
{
	irq_setmask(0);
	irq_setie(1);
    uart_init();
	uart1_init();
    
    
	//timer_init_irq(1000);
    
    
    puts("\n                     Prueba Inicial para Proyecto                  \n");
	puts("\nSoC - RiscV project UNAL 2022-1-- CPU testing software built "__DATE__" "__TIME__"\n");
	help();
	prompt();
    int state;
    int data_b1;
    int data_b2;
    int data_b3;
    int data_b4;
    int data_b5;
    int data_b6;
    int data_b7;
    int data_b8;
    int ultra;
    int y;
    int puntos;
    int dato;
    int ptD = 1;
    int ptA = 2;
    
    int usuario;
    usuario = uart11_read();
    printf("Dato usuario rfid = %d", usuario);
    printf("\n");
    
    switch(usuario){
        case 0:
            break;
        case 1:
            state = 0;
             puntos = 1;
           break;
        case 2:
            state = 1;
            puntos = 2;
           break; 
    }

   while(true){    
		switch(state){
			case 0: 
				delay_ms(3000);
                lcd_data_entry_write(1);
                delay_ms(4000);
                lcd_data_entry_write(3);
                printf("CASE 0"); 
				state = 2;
				break;
			case 1: 
				delay_ms(3000);
                lcd_data_entry_write(2);
                delay_ms(4000);
                lcd_data_entry_write(3);
                printf("CASE 1"); 
				state = 2;
				break;
			case 2: 
                 printf("CASE 2"); 
                 data_b1 = Boton_cntrl_data_b1_read();
                 delay_ms(100);
                 printf("Boton1 =  %d", data_b1); 
                 printf("\n");
                 data_b2 = Boton_cntrl_data_b2_read();
                 delay_ms(100);
                 printf("Boton2 =  %d", data_b2); 
                 printf("\n");
                 delay_ms(100);
              /*   ultraSound_cntrl_init_write(1);
                 int init = ultraSound_cntrl_done_read();
                 printf("Dato sensor ultrasonido done = %d", init);
                 printf("\n");
	            while(true){
	         	if(ultraSound_cntrl_done_read() == 0){
		     	 dato = ultraSound_cntrl_distance_read();
		    	 ultraSound_cntrl_init_write(0);
                 printf("Dato sensor ultrasonido read = %d", dato);
                 printf("\n");
                }}*/
                 delay_ms(2000);
				 if(data_b1 == 0){
                 lcd_data_entry_write(4);
                 delay_ms(2000);
                 int y = lcd_data_entry_read();
                 printf("Dato LCD =  %d", y); 
                 printf("\n");
                 int data_IR = IR_cntrl_data_ir_read();
                 printf("Dato sensor IR =  %d", data_IR); 
                 printf("\n");
                 int data_IN = IN_cntrl_data_in_read();
                 printf("Dato sensor IN =  %d", data_IN); 
                 printf("\n"); 
              // Cero detecta 
                 if (data_IR == 0 && data_IN == 1){
                     state = 3;
                     break;
                  }
               if (data_IR == 1 && data_IN == 0){
                    state = 4;
                    break;
                }
              if (data_IR == 1 && data_IN == 1){
                    state = 5;
                    break;
               }
				break; 
		      }
		      break;
            case 3: 
             //Plastico   
               printf("PLastico"); 
               printf("\n");  
               printf("PLastico"); 
               printf("\n");
               data_b3 = Boton_cntrl_data_b1_read();
                 delay_ms(100);
                 printf("Boton1 =  %d", data_b3); 
                 printf("\n");
               data_b4 = Boton_cntrl_data_b2_read();
                 delay_ms(100);
                 printf("Boton2 =  %d", data_b4); 
                 printf("\n");
               lcd_data_entry_write(5);
               delay_ms(4000);
               PWMUS_cntrl_pos1_write(1);
	           delay_ms(5000);
               PWMUS_cntrl_pos1_write(0);
               delay_ms(4000);
               lcd_data_entry_write(8);
               delay_ms(5000);
               int y = lcd_data_entry_read();
               printf("Dato LCD  botones =  %d", y); 
               printf("\n");
               puntos = puntos + 3;
               if(data_b3 == 0){
                   lcd_data_entry_write(9);
                   state = 2;
				break; }
			   if(data_b4 == 0){ //data_b2
                   state = 6;
				break; }
				break;
            case 4:
                //Metal
               printf("Metal"); 
               printf("\n");  
               lcd_data_entry_write(6);
               delay_ms(4000);
               data_b5 = Boton_cntrl_data_b1_read();
                 delay_ms(100);
                 printf("Boton1 =  %d", data_b5); 
                 printf("\n");
               data_b6 = Boton_cntrl_data_b2_read();
                 delay_ms(100);
                 printf("Boton2 =  %d", data_b6); 
                 printf("\n");
               PWMUS_cntrl_pos2_write(1);
	           delay_ms(5000);
               PWMUS_cntrl_pos1_write(1);
	           delay_ms(5000);
                PWMUS_cntrl_pos2_write(0);
               delay_ms(4000);
               PWMUS_cntrl_pos1_write(0);
               delay_ms(4000);
               lcd_data_entry_write(8);
               delay_ms(1000);
               puntos = puntos + 2;
               if(data_b5 == 0){
                   lcd_data_entry_write(9);
                   state = 2;
				break; }
			   if(data_b6 == 0){
                   state = 6;
				break; }	
               break;   
			case 5: 
                //Papel
               printf("Papel"); 
               printf("\n");
               delay_ms(2000);
               lcd_data_entry_write(7);
               delay_ms(4000);
               PWMUS_cntrl_pos3_write(1);
	           delay_ms(5000);
               PWMUS_cntrl_pos1_write(1);
	           delay_ms(5000);
               PWMUS_cntrl_pos3_write(0);
               delay_ms(4000);
               PWMUS_cntrl_pos1_write(0);
               delay_ms(4000);
               lcd_data_entry_write(8);
               delay_ms(1000);
               data_b7 = Boton_cntrl_data_b1_read();
                 delay_ms(100);
                 printf("Boton1_papel =  %d", data_b7); 
                 printf("\n");
              data_b8 = Boton_cntrl_data_b2_read();
                 delay_ms(100);
                 printf("Boton2_papel =  %d", data_b8); 
                 printf("\n");
                 puntos = puntos + 1;
               if(data_b7 == 0){
                   lcd_data_entry_write(9);
                   state = 2;
				break; }
			   if(data_b8 == 0){
                   state = 6;
				break; }	
               break;   
             case 6: 
                lcd_puntos_write(puntos);
                 printf("Puntos =  %d", puntos); 
                 printf("\n");
                lcd_data_entry_write(10);
                delay_ms(8000);
				lcd_data_entry_write(11);
				state = 0;
				break;    
	} } 
    
	while(1) {
		console_service();
	}

	return 0;
} 


