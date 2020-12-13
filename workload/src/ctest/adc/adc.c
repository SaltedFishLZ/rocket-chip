#include "stdlib.h"
#include "stdint.h"

#include "util.h"

#define ITERS 1000

volatile uint8_t * sensor_in = (volatile uint8_t *)0x81000000; 
volatile uint8_t * driver_out = (volatile uint8_t *)0x82000000; 

volatile uint32_t * magic = (volatile uint32_t *)0x8FFF0000; 

float data;

int main()
{
    // setStats(1);
    for (int i = 0; i < ITERS; i++) {
        *magic = 0x149a;
        // begin
        data = (float)(*sensor_in) / 256.0;
        if (data > 0.5) {
            *driver_out = 100;
        }
        else
        {
            *driver_out = 50;
        }
        // end
        *magic = 0x249a;
    }
    // setStats(0);
    return 0;
}