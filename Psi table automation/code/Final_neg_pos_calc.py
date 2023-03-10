#Program to calculate the negative Calibration Data

CM_dict = {0: 0.02,1: 0.01,2: 0.005} #Defining dictionaries to retrieve the values.

CM = input ('Enter the CM module value (0/1/2):') #Taking input for the module number.
CM_str_to_int = int(CM)
CM_module = (CM_dict[CM_str_to_int])
#print(CM_module)


final = [] #Defining the final list where the acceptable difference will be stored.

psi_range = [10,15,30,50,100,150,300,500,1000,1500,2000,2500,3000] #Defining the psi ranges in a list.
x = input('Enter psi full scale range:') #FS is full scale range.
FS_psi = int(x) #Convert the str to int.
#print(FS_psi)

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

        1:{10: [0.000,1.9757,3.9674,5.9590,7.9930,9.9846,4.9844,0.000], #psi table is calculated
           15: [0.000,2.9928,5.95895,8.96755,11.97615,14.98465,7.48445,0.000], #psi table is calculated
           30: [0.0000,5.9033,11.96734,17.92976,23.97652,29.93896,14.92674,0], #psi table is calculated
           50: [0.000,9.9294,19.9191,29.9081,39.8977,49.8871,24.9981,0.000], #psi table is calculated
           100: [0.000,19.919,39.898,59.876,79.855,99.833,49.887,0.000], #psi table is calculated
           150: [0.000,29.908,59.876,89.844,119.981,149.9495,74.945,0.000], #psi table is calculated
           300: [0.000,59.36067,119.4726667,179.588,239.702,299.814,149.955,0.000], #psi table is calculated
           500: [0.000,99.17,199.944,299.872,399.799,499.725,249.909,0.000], #psi table is calculated
           1000: [0.000,199.6,399.465,599.345,799.215,999.085,499.41,0.000], #psi table is calculated
           1500: [0.000,299.32,599.63,899.94,1199.25,1499.58,749.78,0.000], #psi table is calculated
           2000: [0.000,399.41,799.8,1199.2,1599.61,1999.02,999,0.000], #psi table is calculated
           2500: [0.000,499.53,999.05,1499.58,1999.10,2499.62,1249.30,0.000], #psi table is calculated
           3000: [0.000,599.625,1199.24,1799.875,2399.495,2999.095,1499.555,0.000] #psi table is calculated
        },

        2:{10: [0.000,1.98576,3.83432,5.86617,7.89755,9.92938,4.85003,0.000], #psi table is calculated
           15: [0.000,2.98105,5.98849,8.99607,11.96118,14.96852,7.47105,0.000], #psi table is calculated
           30: [0.0000,5.9590,11.9763,17.9933,23.9681,29.9852,14.9848,0.000], #psi table is calculated
           50: [0.000,9.882,19.876,29.869,39.863,49.856,24.957,0.000], #psi table is calculated
           100: [0.000,19.9119,39.89188333,59.87176667,79.85185,99.8601,49.88186667,0.000], #psi table is calculated
           150: [0.000,29.908,59.87595,89.84355,119.98055,149.94915,74.9445,0.000], #psi table is calculated
           300: [0.000,59.009,119.993,179.280,238.555,299.538,148.786,0.000], #psi table is calculated
           500: [0.000,99.17,199.944,299.872,399.799,499.725,249.909,0.000], #psi table is calculated
           1000: [0.000,199.831,399.561,599.29,799.863,999.593,499.425,0.000], #psi table is calculated
           1500: [0.000,299.325,599.631,899.942,1199.256,1499.579,749.785,0.000],  #psi table is calculated
           2000: [0.000,399.42,799.8225,1199.2325,1649.705,1999.0725,999.0275,0.000], #psi table is calculated
           2500: [0.000,499.530,999.047,1499.579,1999.107,2499.627,1249.303,0.000], #psi table is calculated
           3000: [0.000,599.62,1199.236667,1799.873333,2399.49,2999.096667,1499.556667,0.000] #psi table is calculated
        }
        }

    RDG = RDG_dict[CM_str_to_int][FS_psi]

    for i in RDG: #The RDG_xyz should be fetched here.

        #formula = CM_module*0.01*(FS_psi + RDG)
        formula_value = CM_module*0.01*(FS_psi+i)
        final.append(round(formula_value,4))
    print(final)

elif FS_psi == -14:

    y = input('Enter full scale range [for negative]:') #FS is full scale range.
    FS_neg_psi = int(y) #Convert the str to int.


    #code for negative calculation here.
    RDG_dict = {0:{
           10: [0.000,1.9604,3.9939,5.985,7.9762,9.9675,4.96820,0.000], #psi table is calculated
           15: [0.000,2.7808,5.5777,8.3749,11.1722,13.9697,6.9763,0.000], #psi table is calculated
           30: [0.0000,2.7742,5.5698,8.3661,11.1623,13.9585,6.9680,0.000], #psi table is calculated
           50: [0.000,2.781,5.578,8.375,11.172,13.969,6.976,0.000], #psi table is calculated
           100: [0.000,2.781,5.578,8.375,11.172,13.97,6.976,0.000], #psi table is calculated
           150: [0.000,2.781,5.578,8.375,11.172,13.97,6.976,0.000], #psi table is calculated
           300:[0.000,2.781,5.578,8.375,11.172,13.97,6.976,0.000], #psi table is calculated
           500: [0.000,2.781,5.578,8.375,11.172,13.97,6.976,0.000], #psi table is calculated
           1000: [0.000,2.781,5.578,8.375,11.172,13.97,6.976,0.000], #psi table is calculated
           1500: [0.000,2.781,5.578,8.375,11.172,13.97,6.976,0.000], #psi table is calculated
           2000: [0.000,2.781,5.578,8.375,11.172,13.97,6.976,0.000], #psi table is calculated
           2500: [0.000,2.781,5.578,8.375,11.172,13.97,6.976,0.000], #psi table is calculated
           3000: [0.000,2.781,5.578,8.375,11.172,13.97,6.976,0.000] #psi table is calculated
        },

        1:{10: [0], # we do not calibrate these.
           15: [0.000,2.7808,5.57775,8.37505,11.17235,13.96985,6.97635,0.000], #psi table is calculated
           30: [0.0000,2.7219,5.55255,8.3059,11.144325,13.982775,6.929275,0.000], #psi table is calculated
           50: [0.000,2.663,5.5274,8.2368,11.1163,13.9956,6.8822,0.000], #psi table is calculated
           100: [0.000,2.7808,5.57775,8.37505,11.17235,13.9700,6.97635,0.000], #psi table is calculated
           150: [0.000,29.908,59.876,89.844,119.981,149.9495,74.945,0.000], #
           300: [0.000,2.7825,5.579,8.3755,11.172,13.9695,6.977,0.000], #psi table is calculated
           500: [0.000,2.781,5.578,8.375,11.172,13.97,6.976,0.000], #psi table is calculated
           1000: [0.000,2.77,5.57,8.37,11.16,13.96,6.97,0.000], #psi table is calculated
           1500: [0.000,2.77,5.57,8.37,11.16,13.96,6.97,0.000], #psi table is calculated
           2000: [0.000,2.77,5.57,8.37,11.16,13.96,6.97,0.000], #psi table is calculated
           2500: [0.000,2.77,5.57,8.37,11.16,13.96,6.97,0.000], #psi table is calculated
           3000: [0.000,2.77,5.57097,8.3711,11.1638,13.9620,6.9742,0.000] #psi table is calculated
        },

        2:{10: [0.000,1.97553,3.96732,5.95916,7.99346,9.98545,4.9844,0.000], #psi table is calculated
           15: [0.000,2.98117,5.98892,8.99699,11.96275,14.97095,7.47169,0.000], #psi table is calculated
           30: [0.0000,2.7742,5.5699,8.3662,11.1624,13.9586,6.9681,0.000], #psi table is calculated
           50: [0.000,2.65635,5.4705,8.34935,11.0595,13.93855,6.90995,0.000], #psi table is calculated
           100: [0.000,2.76955,5.56535,8.38295,11.179,13.9751,6.9634,0.000], #psi table is calculated
           150: [0.000,2.7809,5.5778,8.37505,11.17225,13.96975,6.97635,0.000], #psi table is calculated
           300: [0.000,2.741666667,5.561,8.329,11.15333333,13.97866667,6.9446666670,0.000], #psi table is calculated
           500: [0.000,2.765,5.561,8.4001-11.196-13.992-6.959,0.000], #psi table is calculated
           1000: [0.000,2.781,5.578,8.375,11.172,13.97,6.976,0.000], #psi table is calculated
           1500: [0.000,2.774,5.570,8.366,11.162,13.959,6.968,0.000], #psi table is calculated
           2000: [0.000,2.76955,5.56535,8.38295,11.179,13.9751,6.9634,0.000], #psi table is calculated
           2500: [0.000,2.774,5.570,8.366,11.162,13.959,6.968,0.000], #psi table is calculated
           3000: [0.000,2.76955,5.56535,8.38295,11.179,13.9751,6.9634,0.000], #psi table is calculated
        }


        }

    #code for range calculation below

    RDG = RDG_dict[CM_str_to_int][FS_neg_psi]

    for i in RDG: #The RDG_xyz should be fetched here.

        #formula = CM_module*0.01*(FS_psi + RDG)
        formula_value = CM_module*0.01*(FS_neg_psi+i)
        final.append(round(formula_value,4))
    print(final)

else:
    print('Incorrect range')



