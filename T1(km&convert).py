#take number input from user in km & convert it into yard and meters

meter = 6 # Length in Meter
yard =  23 # Length in Yard

# converting Meter to Yard
meter_to_yard = meter * 1.09361

# converting Yard to meter
yard_to_meter = yard / 1.09361

# printing the output
print("%d Meter in Yard = %.4f " % (meter, meter_to_yard))
print("%d Yard in Meter = %.4f " % (yard, yard_to_meter))
