#range_of_number_counter

#create variables
range_1_10 = 0
range_11_20 = 0
range_21_30 = 0
range_31_40 = 0
range_41_50 = 0

#create loop
while True:

#ask user for input
    user_input = input("Please input a number ranging from 1 up to 50: ")
#check if input is valid
    try:
        number = int(user_input)
#determine the range of the input 
        if 1 <= number <= 50:
            if 1 <= number <= 10:
                range_1_10 += 1
            elif 11 <= number <= 20:
                range_11_20 += 1
            elif 21 <= number <= 30:
                range_21_30 += 1
            elif 31 <= number <= 40:
                range_31_40 += 1
            elif 41 <= number <= 50:
                range_41_50 += 1
        else:
            break

    except:
        break

#print the inputs
print("Summary of inputs by range: ")
print("Numbers 1 - 10 =", range_1_10)
print("Numbers 11 - 20 =", range_11_20)
print("Numbers 21 - 30 =", range_21_30)
print("Numbers 31 - 40 =", range_31_40)
print("Numbers 41 - 50 =", range_41_50)
