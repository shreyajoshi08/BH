import time
import openpyxl

Pace1000sensor = 0
chassis = 0
starttime = 0.0
stoptime = 0.0
wb = openpyxl.load_workbook('your_workbook.xlsx')
option705E = 0
leakdo = 0
range_800 = 0
precheck = 0
caldue800 = ''
waitr = 0
gauge_range = ''

def gauge_AdjustmentCAL():
    global Pace1000sensor, starttime, stoptime, option705E, range_800, precheck, caldue800
    
    x = wb['AutoCAL']['J4'].value
    temp = float(input("Enter current temperature: "))
    wb['AutoCAL']['B12'] = temp
    hum = float(input("Enter current humidity: "))
    wb['AutoCAL']['B13'] = hum
    p1 = wb['AutoCAL']['D4'].value  # CAL port for DUT
    p2 = wb['AutoCAL']['E4'].value  # CAL port for STD
    POR1 = p1
    POR2 = p2
    FS = wb['AutoCAL']['C4'].value
    Unit = wb['AutoCAL']['B4'].value
    ec_WAITmS = 100
    path = wb.path
