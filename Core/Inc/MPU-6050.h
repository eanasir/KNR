// MPU6050.h KNR 2024
#include "main.h"
#include "i2c.h"

#define MPU6050_PORT hi2c1
extern I2C_HandleTypeDef MPU6050_PORT;
#define WHO_AM_I 0x75 // rejestr kontrolny

#define PWR_MGMT_1 0x6B // zarzadzanie zasilaniem

#define TEMP_OUT_L    0X42
#define TEMP_OUT_H	  0x41 //czujnik temperatury

#define MPU6050_ADDRESS 0xD0
#define timeout 1000

int16_t MPU6050_TEMP_Read();
uint8_t MPU6050_Init(void);
float MPU6050_TEMP_Read_Celsius();


