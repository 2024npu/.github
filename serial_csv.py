import serial
import csv
import time

def read_serial_data(serial,baud_rate,output_csv):
    #open the serial port
    ser = serial.Serial(serial_port)