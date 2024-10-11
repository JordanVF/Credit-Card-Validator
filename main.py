# Luhns algorithm
# Sum of all odd index numbers
# Double all the values of the numbers at even indexes (e.g. 9 becomes 18)
# For all double digit numbers, split the numbers and sum them into single digits (e.g. 18 becomes 1 + 8 = 9)
# Sum all the new values of the even indexes
# Sum value of odd and even indexes
# Divide sum by 10
# If remainder is 0, the credit card number is valid (modulus)

cc_number = "5610591081018250"
odd_sum = 0
double_list = []
even_sum = 0

number = list(cc_number)
for (idx,val) in enumerate(number):
    if idx % 2 !=0: # Odd Number
        odd_sum += int(val)
    else:           # Even Number
        double_list.append(int(val)*2)


# Converting list into string
double_string = ""
for x in double_list:
    double_string += str(x)

# Converting string back into list
double_list = list(double_string)
for x in double_list:
    even_sum += int(x)

net_sum = odd_sum + even_sum
if net_sum%10 ==0:
    print("Valid Card")
else:
    print("Invalid Card")