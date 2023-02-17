#Program to calculate the Calibration Data

CM_dict = {"0": 0.02,"1": 0.01,"2": 0.005} #Defining dictionaries to retrieve the values.
CM = input ('Enter the CM module value (0/1/2):') #Taking input for the module number.
CM_module = CM_dict[CM]#Storing it in CM_module
CM_module

final = [] #Defining the final list where the acceptable difference will be stored.

psi_range = [10,15,30,50,100,150,300,500,1000,1500,2000,2500,3000] #Defining the psi ranges in a list.
x = input('Enter psi range:') #FS is full scale range.
FS_psi = int(x) #Convert the str to int.
print(FS_psi)

if FS_psi in psi_range:
    #Enter the code for the actual reading table here.
    #RDG = probably run a for loop through the values in the table.
    #EG:
    RDG = [0.000,5.9585,11.9149,17.8435,23.9402,29.8693]


    for i in RDG:
        #formula = CM_module*0.01*(FS_psi + RDG)
        formula_value = CM_module*0.01*(FS_psi+i)
        final.append(round(formula_value,4))

    print(final)

else:
    print('Incorrect range')
