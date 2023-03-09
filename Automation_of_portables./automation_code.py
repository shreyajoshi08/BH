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

    wb['AutoCAL']['L3'] = "gauge_Adjustment"
    
    if wb['AutoCAL']['D3'].value == "PM620":
        SN = input("Please enter the serial number of the PM620: ")
    elif wb['AutoCAL']['D3'].value == "UPM":
        SN = input("Please enter the serial number of the UPM: ")
    elif wb['AutoCAL']['D3'].value == "PACE1000":
        SN = input("Please choose range of the PACE1000 (1 or 2 or 3): ")
        wb['AutoCAL']['S7'] = Pace1000sensor
    elif wb['AutoCAL']['D3'].value == "DPI610":
        rc = input("Is it external sensor? (Y/N)")
        if rc == 'Y':
            wb['AutoCAL']['M1'] = 1
    elif wb['AutoCAL']['M1'].value == 1:
        SN = input("Please enter the serial number of external sensor: ")
        wb['AutoCAL']['S7'] = SN
    elif wb['AutoCAL']['D3'].value == "DPI705E":
        rc = input("Are there Negative pressure option? (Y/N)")
        if rc == 'Y':
            option705E = 0
        else:
            option705E = 1
    elif wb['AutoCAL']['D3'].value == "DPI800":
        rc = input("Which is range of DPI800? If P1, please select Y. P2 is N.")
        if rc == 'Y':
            range_800 = 2
        else:
            range_800 = 3
    
    rc = input("Do you perform pre-check? (Y/N)")
    if rc == 'Y':
        precheck = 0
    else:
        precheck = 1
    
    if wb['AutoCAL']['E3'].value == "CM":
        CMlimitcheckg()
    
    rc = input("Have you checked Limit and FS? (Y/N)")
    if rc == 'Y':
        print("Start process.")
    else:
        print("Stop process.")
        return
