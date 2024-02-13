//MPU6050.c KNR 2024

#include "MPU-6050.h"
#include <stdint.h>
#include <stdio.h>
#include <math.h>
int16_t MPU6050_TEMP_Read(){
	uint8_t TEMP_OUT[2];
	int16_t TEMP_Signed;
	float Temperature_C;
	HAL_I2C_Mem_Read(&MPU6050_PORT, MPU6050_ADDRESS, TEMP_OUT_H, 1, TEMP_OUT, 2, timeout);

    TEMP_Signed = (int16_t)(TEMP_OUT[0] << 8 | TEMP_OUT[1]);
    return TEMP_Signed;
}

float MPU6050_TEMP_Read_Celsius(){
	float temp_C;
	temp_C = (float)(((int16_t)MPU6050_TEMP_Read()/340.0)+36.53);
	return temp_C;
}
uint8_t MPU6050_Init(void){
	uint8_t Who_Am_I;
	HAL_I2C_Mem_Read(&MPU6050_PORT, MPU6050_ADDRESS, WHO_AM_I, 1, &Who_Am_I, 1, timeout);
	//debilu to jest rejestr do odczytu

	if(Who_Am_I == 104){
		//adres WHO_AM_I powinien zwrocic 0x68 wg danych producenta
		uint8_t Pwr_Mgmt = 0;
		HAL_I2C_Mem_Write(&MPU6050_PORT, MPU6050_ADDRESS, PWR_MGMT_1, 1, &Pwr_Mgmt, 1, timeout);
		// zapisanie tego rejestru zerami włącza czujnik w normalnym trybie pracy
		return 1;
	}
	else{
		return 0;
	}

}
