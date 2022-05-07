import tkinter as Tk
from itertools import count
import matplotlib.pyplot as plt
import serial
import time

arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.1)

ivmex_dosya = open("ivme_x.txt", "w")
ivmey_dosya = open("ivme_y.txt", "w")
ivmez_dosya = open("ivme_z.txt", "w")

gyrox_dosya = open("gyro_x.txt", "w")
gyroy_dosya = open("gyro_y.txt", "w")
gyroz_dosya = open("gyro_z.txt", "w")

ivme_x=[]
ivme_y=[]
ivme_z=[]
gyro_x=[]
gyro_y=[]
gyro_z=[]
counter=0


while True:
    if arduino.in_waiting:
        arduino_data=arduino.readline()
        counter+=1
       # print(arduino_data.decode('utf'))
        if counter>=8 and counter<14:
            splt_data= arduino_data.decode('utf').split('=')
            if counter==8:
                ivmex_dosya.write(str(int(splt_data[1])))
                ivmex_dosya.write("\n")
                ivmex_dosya.flush()
                ivme_x.append(int(splt_data[1]))
                print(ivme_x)

            elif counter==9:
                ivmey_dosya.write(str(int(splt_data[1])))
                ivmey_dosya.write("\n")
                ivmey_dosya.flush()
                ivme_y.append(int(splt_data[1]))
            elif counter==10:
                ivmez_dosya.write(str(int(splt_data[1])))
                ivmez_dosya.write("\n")
                ivmez_dosya.flush()
                ivme_z.append(int(splt_data[1]))
            elif counter == 11:
                gyrox_dosya.write(str(int(splt_data[1])))
                gyrox_dosya.write("\n")
                gyrox_dosya.flush()
                gyro_x.append(int(splt_data[1]))
            elif counter == 12:
                gyroy_dosya.write(str(int(splt_data[1])))
                gyroy_dosya.write("\n")
                gyroy_dosya.flush()
                gyro_y.append(int(splt_data[1]))
            elif counter == 13:
                gyroy_dosya.write(str(int(splt_data[1])))
                gyroy_dosya.write("\n")
                gyroy_dosya.flush()
                gyro_z.append(int(splt_data[1]))

        elif counter==14:
            counter=0

