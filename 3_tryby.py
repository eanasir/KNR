import os
import time

if os.name == 'nt':
    import msvcrt
    def getch():
        return msvcrt.getch().decode()
else:
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    def getch():
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


from dynamixel_sdk import *                    # Uses Dynamixel SDK library
#AX12A
# Control table address
ADDR_MX_TORQUE_ENABLE      = 24    #1b          # Control table address is different in Dynamixel model
ADDR_MX_GOAL_POSITION      = 30    #2b
ADDR_MX_PRESENT_POSITION   = 36
ADDR_MX_PRESENT_SPEED      = 38
ADDR_MX_PRESENT_LOAD       = 40
ADDR_MX_CW_ANGLE_LIMIT    = 6
ADDR_MX_CCW_ANGLE_LIMIT    = 8
ADDR_MX_MOVING_STATUS      = 46
ADDR_MX_MOVING_SPEED      = 32

# Protocol version
PROTOCOL_VERSION            = 1.0               # See which protocol version is used in the Dynamixel

# Default setting
DXL_ID                      = 14                 # Dynamixel ID : 1
BAUDRATE                    = 1000000             # Dynamixel default baudrate : 57600
DEVICENAME                  = "com5"    # Check which port is being used on your controller
                                                # ex) Windows: "COM1"   Linux: "/dev/ttyUSB0" Mac: "/dev/tty.usbserial-*"

TORQUE_ENABLE               = 1                 # Value for enabling the torque
TORQUE_DISABLE              = 0                 # Value for disabling the torque

DXL_MAX_TORQUE              = 1023
DXL_MINIMUM_POSITION_VALUE  = 0         # Dynamixel will rotate between this value
DXL_MAXIMUM_POSITION_VALUE_JOINT  = 1024 
DXL_MAXIMUM_POSITION_VALUE_WHEEL_MODE = 2047    # and this value (note that the Dynamixel would not move when the position value is out of movable range. Check e-manual about the range of the Dynamixel you use.)
DXL_MOVING_STATUS_THRESHOLD = 20                # Dynamixel moving status threshold
DXL_CCW_ANGLE_LIMIT_JOINT_MODE = 1023
DXL_CW_ANGLE_LIMIT_JOINT_MODE = 0
DXL_CCW_ANGLE_LIMIT_WHEEL_MODE = 0
DXL_CW_ANGLE_LIMIT_WHEEL_MODE = 0





portHandler = PortHandler(DEVICENAME)

packetHandler = PacketHandler(PROTOCOL_VERSION)



def jointMode():    
            dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL_ID, ADDR_MX_TORQUE_ENABLE, TORQUE_DISABLE)
            if dxl_comm_result != COMM_SUCCESS:
                 print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
            elif dxl_error != 0:
                print("%s" % packetHandler.getRxPacketError(dxl_error))
            dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_ID, ADDR_MX_CCW_ANGLE_LIMIT, DXL_CCW_ANGLE_LIMIT_JOINT_MODE)
            if dxl_comm_result != COMM_SUCCESS:
                print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
            elif dxl_error != 0:
                print("%s" % packetHandler.getRxPacketError(dxl_error)) #przelacza ccw angle limit na rozne od 0, jesli cw i ccw = 0 => joint mode
            
            dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_ID, ADDR_MX_CW_ANGLE_LIMIT, DXL_CW_ANGLE_LIMIT_JOINT_MODE)
            if dxl_comm_result != COMM_SUCCESS:
                print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
            elif dxl_error != 0:
                print("%s" % packetHandler.getRxPacketError(dxl_error)) #przelacza ccw angle limit na rozne od 0, jesli cw i ccw != 0 => joint mode
            dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL_ID, ADDR_MX_TORQUE_ENABLE, TORQUE_ENABLE)
            if dxl_comm_result != COMM_SUCCESS:
                 print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
            elif dxl_error != 0:
                print("%s" % packetHandler.getRxPacketError(dxl_error)) 
def wheelMode():    
            dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL_ID, ADDR_MX_TORQUE_ENABLE, TORQUE_DISABLE)
            if dxl_comm_result != COMM_SUCCESS:
                 print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
            elif dxl_error != 0:
                print("%s" % packetHandler.getRxPacketError(dxl_error))
            
            
            dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_ID, ADDR_MX_CCW_ANGLE_LIMIT, DXL_CCW_ANGLE_LIMIT_WHEEL_MODE)
            if dxl_comm_result != COMM_SUCCESS:
                print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
            elif dxl_error != 0:
                print("%s" % packetHandler.getRxPacketError(dxl_error)) #przelacza ccw angle limit na 0, jesli cw i ccw = 0 => wheel mode
            
            dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_ID, ADDR_MX_CW_ANGLE_LIMIT, DXL_CW_ANGLE_LIMIT_WHEEL_MODE)
            if dxl_comm_result != COMM_SUCCESS:
                print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
            elif dxl_error != 0:
                print("%s" % packetHandler.getRxPacketError(dxl_error)) #przelacza ccw angle limit na 0, jesli cw i ccw = 0 => wheel mode
             

              
            dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL_ID, ADDR_MX_TORQUE_ENABLE, TORQUE_ENABLE)
            if dxl_comm_result != COMM_SUCCESS:
                 print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
            elif dxl_error != 0:
                print("%s" % packetHandler.getRxPacketError(dxl_error)) 
def writePosition(dxl_goal_position):
    dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_ID, ADDR_MX_GOAL_POSITION, dxl_goal_position)
    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("%s" % packetHandler.getRxPacketError(dxl_error))
def writeMovingSpeed(dxl_goal_moving_speed):
    dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_ID, ADDR_MX_MOVING_SPEED, dxl_goal_moving_speed)
    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("%s" % packetHandler.getRxPacketError(dxl_error))
def writeTorqueLimit(dxl_torque_limit):
    dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_ID, ADDR_MX_MOVING_SPEED, dxl_torque_limit)
    if dxl_comm_result != COMM_SUCCESS:
       print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
       print("%s" % packetHandler.getRxPacketError(dxl_error))
def write3rdMode(dxl_torque_limit,dxl_goal_position):
    dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_ID, ADDR_MX_MOVING_SPEED, dxl_torque_limit)
    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("%s" % packetHandler.getRxPacketError(dxl_error))
    dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_ID, ADDR_MX_GOAL_POSITION, dxl_goal_position)
    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("%s" % packetHandler.getRxPacketError(dxl_error))
def openPort():
    # Open port
    if portHandler.openPort():
        print("Succeeded to open the port")
    else:
        print("Failed to open the port")
        print("Press any key to terminate...")
        getch()
        quit()


    # Set port baudrate
    if portHandler.setBaudRate(BAUDRATE):
        print("Succeeded to change the baudrate")
    else:
        print("Failed to change the baudrate")
        print("Press any key to terminate...")
        getch()
        quit()
def torqueEnable():
        # Enable Dynamixel Torque
    dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL_ID, ADDR_MX_TORQUE_ENABLE, TORQUE_ENABLE)
    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("%s" % packetHandler.getRxPacketError(dxl_error))
    else:
        print("Dynamixel has been successfully connected")
def torqueDisable():
    #Disable Dynamixel Torque
    dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL_ID, ADDR_MX_TORQUE_ENABLE, TORQUE_DISABLE)
    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("%s" % packetHandler.getRxPacketError(dxl_error))
    else:
        print("Dynamixel has been successfully connected")

openPort()
torqueEnable()

while True:    
    mode = int(input("podaj tryb (1 JOINT 2 WHEEL 4 Moment ): "))

    match mode:
        case 1:
            
       
            jointMode()
            writeTorqueLimit(DXL_MAX_TORQUE)
            n = 0
            while n != 1:
                print("podaj pozycje docelowa\n ")
                dxl_goal_position = int(input("podaj pozycje od 0 do 1023, napisz 9999 by wyjsc z tego trybu:"))
                if dxl_goal_position == 9999:
                    n = 1
                elif dxl_goal_position <= DXL_MAXIMUM_POSITION_VALUE_JOINT and dxl_goal_position >=DXL_MINIMUM_POSITION_VALUE : 
                    #zadana pozycja musi byc mniejsza od maksymalnej i wieksza od minimalnej
                    writePosition(dxl_goal_position)
                elif dxl_goal_position > DXL_MAXIMUM_POSITION_VALUE_JOINT or dxl_goal_position < DXL_MINIMUM_POSITION_VALUE and dxl_goal_position != 9999:
                     #zadana pozycja nie moze byc wieksza od maskymalnej i mniejsza od minimalnej
                    print("pozycja wykracza poza dozwolony zakres\n")
               
        case 2:
            wheelMode()
           
            n = 0
            while n != 1:
                print("podaj wartosc predkosci od 0 do 2047\nwartosc od do 1023 spowoduje obrot w lewo\nod 1024 do 2047 powoduje obrot w prawo")
                dxl_goal_moving_speed, czas = int(input("podaj wartosc: ")), int(input("podaj czas:"))
                if  dxl_goal_moving_speed or czas == 9999:
                    n = 1
                
                elif dxl_goal_moving_speed > DXL_MAXIMUM_POSITION_VALUE_WHEEL_MODE or dxl_goal_moving_speed < DXL_MINIMUM_POSITION_VALUE and dxl_goal_moving_speed != 9999: 
                    #zadana predkosc nie moze byc wieksza od maskymalnej i mniejsza od minimalnej
                    print("pozycja wykracza poza dozwolony zakres\n")
               
                if dxl_goal_moving_speed <= DXL_MAXIMUM_POSITION_VALUE_JOINT and dxl_goal_moving_speed >=DXL_MINIMUM_POSITION_VALUE and czas != 9999: #
                    writeMovingSpeed(dxl_goal_moving_speed)
                    time.sleep(czas)
                    print("\nkoniec ruchu")
                    dxl_goal_moving_speed = 0 #stop
                    writeMovingSpeed(dxl_goal_moving_speed)
                
                    #RUCH LEWO
                    
                        
                elif dxl_goal_moving_speed <= DXL_MAXIMUM_POSITION_VALUE_WHEEL_MODE and dxl_goal_moving_speed >DXL_MAXIMUM_POSITION_VALUE_JOINT and czas != 9999:
                    writeMovingSpeed(dxl_goal_moving_speed)
                    time.sleep(czas)
                    print("\nkoniec ruchu")
                    dxl_goal_moving_speed = 1024 #stop
                    writeMovingSpeed(dxl_goal_moving_speed)
                        #RUCH PRAWO
                        
                

        case 3:
            jointMode()
            n = 0
            while n != 1:
                
                dxl_torque_limit = int(input("podaj wartosc od 0 do 1023, napisz 9999 by wyjsc z tego trybu: "))
                if  dxl_torque_limit == 9999 :
                    n = 1
                elif dxl_torque_limit < DXL_MAX_TORQUE and dxl_torque_limit > 0: #
                    writeTorqueLimit(dxl_torque_limit)
                elif  dxl_torque_limit > DXL_MAX_TORQUE or dxl_torque_limit <= 0 and dxl_torque_limit != 9999: #zadana pozycja nie moze byc wieksza od maskymalnej i mniejsza od minimalnej
                    print("pozycja wykracza poza dozwolony zakres\n")    
                

                dxl_goal_position = int(input("podaj wartosc od 0 do 1023, napisz 9999 by wyjsc z tego trybu: "))
                if dxl_torque_limit == 9999:
                    n = 1

                elif dxl_goal_position <= DXL_MAXIMUM_POSITION_VALUE_JOINT and dxl_goal_position >=DXL_MINIMUM_POSITION_VALUE : #zadana pozycja musi byc mniejsza od maksymalnej i wieksza od minimalnej
                    writePosition(dxl_goal_position)
                elif dxl_goal_position > DXL_MAXIMUM_POSITION_VALUE_JOINT or dxl_goal_position < DXL_MINIMUM_POSITION_VALUE and dxl_goal_position != 9999 or dxl_torque_limit > DXL_MAX_TORQUE or dxl_torque_limit < 0: #zadana pozycja nie moze byc wieksza od maskymalnej i mniejsza od minimalnej
                    print("pozycja wykracza poza dozwolony zakres\n")    
        case 4:
            jointMode()
            n = 0
            while n != 1:
                
                dxl_torque_limit, dxl_goal_position = int(input("podaj wartosc momentu wieksza od 0 do 1023 , napisz 9999  by wyjsc z tego trybu:")), int(input("\npodaj wartosc pozycji od 0 do 1023 , napisz 9999  by wyjsc z tego trybu:"))
                if  dxl_torque_limit and dxl_goal_position == 9999 :
                    n = 1
                elif dxl_torque_limit <= DXL_MAX_TORQUE and dxl_torque_limit >0 and dxl_goal_position <= DXL_MAXIMUM_POSITION_VALUE_JOINT and dxl_goal_position >=0 : #
                    write3rdMode(dxl_torque_limit, dxl_goal_position)
                elif  dxl_torque_limit > DXL_MAX_TORQUE or dxl_torque_limit <= 0 and dxl_torque_limit != 9999: #zadana pozycja nie moze byc wieksza od maskymalnej i mniejsza od minimalnej
                    print("moment wykracza poza dozwolony zakres\n")    
                elif dxl_goal_position > DXL_MAXIMUM_POSITION_VALUE_JOINT or dxl_goal_position < DXL_MINIMUM_POSITION_VALUE and dxl_goal_position != 9999 : #zadana pozycja nie moze byc wieksza od maskymalnej i mniejsza od minimalnej
                    print("pozycja wykracza poza dozwolony zakres\n")  
        case 5:
            wheelMode()
            torqueDisable()
            n = 0
            while n != 1:
                
                dxl_torque_limit, dxl_goal_moving_speed, czas = int(input("podaj wartosc momentu wieksza od 0 do 1023 , napisz 9999  by wyjsc z tego trybu:")), int(input("\npodaj wartosc proskosci od 0 do 1023 lub 1024 do 2047 , napisz 9999  by wyjsc z tego trybu:")), int(input("podaj czas:"))
                if  dxl_torque_limit and dxl_goal_moving_speed == 9999 :
                    n = 1
                elif dxl_torque_limit <= DXL_MAX_TORQUE and dxl_torque_limit > 0  and dxl_goal_moving_speed <= DXL_MAXIMUM_POSITION_VALUE_JOINT and dxl_goal_moving_speed >=DXL_MINIMUM_POSITION_VALUE: #
                    writeMovingSpeed(dxl_goal_moving_speed)
                    time.sleep(czas)
                    dxl_goal_moving_speed = 0 #stop
                    print("\nkoniec ruchu")
                    writeMovingSpeed(dxl_goal_moving_speed)
                    #ruch lewo
                elif dxl_torque_limit <= DXL_MAX_TORQUE and dxl_torque_limit > 0  and dxl_goal_moving_speed <= DXL_MAXIMUM_POSITION_VALUE_WHEEL_MODE and dxl_goal_moving_speed >DXL_MAXIMUM_POSITION_VALUE_JOINT:
                    writeMovingSpeed(dxl_goal_moving_speed)
                    time.sleep(czas)
                    print("\nkoniec ruchu")
                    dxl_goal_moving_speed = 1024 #stop
                    writeMovingSpeed(dxl_goal_moving_speed)
                        #RUCH PRAWO
                elif  dxl_torque_limit > DXL_MAX_TORQUE or dxl_torque_limit <= 0 and dxl_torque_limit != 9999: #zadana pozycja nie moze byc wieksza od maskymalnej i mniejsza od minimalnej
                    print("moment wykracza poza dozwolony zakres\n")    
                elif dxl_goal_position > DXL_MAXIMUM_POSITION_VALUE_WHEEL_MODE or dxl_goal_position < DXL_MINIMUM_POSITION_VALUE and dxl_goal_position != 9999 : #zadana pozycja nie moze byc wieksza od maskymalnej i mniejsza od minimalnej
                    print("pozycja wykracza poza dozwolony zakres\n")  
        

                
               

