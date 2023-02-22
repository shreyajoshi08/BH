#Program to calculate the Calibration Data

CM_dict = {0: 0.02,1: 0.01,2: 0.005} #Defining dictionaries to retrieve the values.

CM = input ('Enter the CM module value (0/1/2):') #Taking input for the module number.
CM_str_to_int = int(CM)
CM_module = (CM_dict[CM_str_to_int])
#print(CM_module)


final = [] #Defining the final list where the acceptable difference will be stored.

psi_range = [10,15,30,50,100,150,300,500,1000,1500,2000,2500,3000] #Defining the psi ranges in a list.
x = input('Enter psi range:') #FS is full scale range.
FS_psi = int(x) #Convert the str to int.
print(FS_psi)

if FS_psi in psi_range:
    
    #Enter the code for the actual reading table here.
    #RDG = probably run a for loop through the values in the table.
    
    RDG_dict = {0:{
           10: [0.000,1.9604,3.9937,5.9846,7.9755,9.9666,4.9679,0.000], #psi table is calculated 
           15: [0.000,2.8322,5.8662,8.9137,11.9614,14.8397,7.3898,0.000], #psi table is calculated 
           30: [0.0000,5.9260,11.9382,17.8655,23.9612,29.8887,14.9635,0.000], #psi table is calculated
           50: [0.000,9.929,19.919,29.907,39.897,49.886,24.997,0.000], #psi table is calculated 
           100: [0.000,19.919,39.898,59.8765,79.855,99.834,49.887,0.000], #psi table is calculated 
           150: [0.000,29.729,59.368,89.855,119.492,149.981,74.612,0.000], #psi table is calculated 
           300: [0.000,59.3683,119.4921714,179.6191857,239.7450143,299.8687143,149.9804714,0], #psi table is calculated
           500: [0.000,99.17,199.945,299.875,399.8,499.725,249.91,0.000], #psi table is calculated
           1000: [0.000,199.94,399.8,599.65,799.505,999.355,499.69,0.000], #psi table is calculated
           1500: [0.000,299.32,599.63,899.94,1199.25,1499.58,749.78,0.000], #psi table is calculated
           2000: [0.000,399.43,799.84,1199.25,1599.68,1999.10,999.05,0.000], #psi table is calculated
           2500: [0.000,499.53,999.05,1499.58,1999.10,2499.62,1249.30,0.000], #psi table is calculated
           3000: [0.000,599.63,1199.24,1799.88,2399.5,2999.11,1499.56,0.000] #psi table is calculated
        },
                
        1:{10: [0.000,5.9585,11.9149,17.8435,23.9402,29.8693],
           15: [0.000,2.9928,5.95895,8.96755,11.97615,14.98465,7.48445,0.000], #psi table is calculated
           30: [0.0000,5.9033,11.96734,17.92976,23.97652,29.93896,14.92674,0], #psi table is calculated
           50: [0.000,9.9294,19.9191,29.9081,39.8977,49.8871,24.9981,0.000], #psi table is calculated
           100: [0.000,19.919,39.898,59.876,79.855,99.833,49.887,0.000], #psi table is calculated
           150: [0.000,29.908,59.876,89.844,119.981,149.9495,74.945,0.000], #psi table is calculated
           300: [0.000,59.36067,119.4726667,179.588,239.702,299.814,149.955,0.000], #psi table is calculated
           500: [0.000,99.17,199.944,299.872,399.799,499.725,249.909,0.000], #psi table is calculated
           1000: [0.000,199.6,399.465,599.345,799.215,999.085,499.41,0.000], #psi table is calculated
           1500: [0.000,5.9585,11.9149,17.8435,23.9402,29.8693],
           2000: [0.000,399.41,799.8,1199.2,1599.61,1999.02,999,0.000], #psi table is calculated
           2500: [0.000,5.9585,11.9149,17.8435,23.9402,29.8693],
           3000: [0.000,599.625,1199.24,1799.875,2399.495,2999.095,1499.555,0.000] #psi table is calculated
        },
                
        2:{10: [0.000,1.98576,3.83432,5.86617,7.89755,9.92938,4.85003,0.000], #psi table is calculated
           15: [0.000,2.98105,5.98849,8.99607,11.96118,14.96852,7.47105,0.000], #psi table is calculated
           30: [0.0000,5.9260,11.9382,17.8655,23.9612,29.8887],
           50: [0.000,09.869366667,19.8583,29.84623333,39.9476,49.93633333,24.9367,0.000], #psi table is calculated
           100: [0.000,19.9119,39.89188333,59.87176667,79.85185,99.8601,49.88186667,0.000], #psi table is calculated
           150: [0.000,29.908,59.87595,89.84355,119.98055,149.94915,74.9445,0.000], #psi table is calculated
           300: [0.000,50.88014286,102.405,153.9324286,205.4584286,256.9825714,128.5324286,0.000], #psi table is calculated
           500: [0.000,99.17,199.944,299.872,399.799,499.725,249.909,0.000], #psi table is calculated
           1000: [0.000,199.831,399.561,599.29,799.863,999.593,499.425,0.000], #psi table is calculated
           1500: [0.000,5.9585,11.9149,17.8435,23.9402,29.8693], 
           2000: [0.000,399.42,799.8225,1199.2325,1649.705,1999.0725,999.0275,0.000], #psi table is calculated
           2500: [0.000,5.9585,11.9149,17.8435,23.9402,29.8693],
           3000: [0.000,599.62,1199.236667,1799.873333,2399.49,2999.096667,1499.556667,0.000] #psi table is calculated
        }
        }

    RDG = RDG_dict[CM_str_to_int][FS_psi]
    
    for i in RDG: #The RDG_xyz should be fetched here.

        #formula = CM_module*0.01*(FS_psi + RDG)
        formula_value = CM_module*0.01*(FS_psi+i)
        final.append(round(formula_value,4))
    print(final)
    
    
else:
    print('Incorrect range')
