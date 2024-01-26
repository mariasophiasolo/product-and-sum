# calculating the product and sum of two numbers

# calculate the product of the two numbers
def product_or_sum (number1,number2):
    product = number1 * number2

# check if the product is less than 1000
    if product <= 1000:
        return product
# if the product is greater than 1000 then calculate for its sum
    else: 
        return number1 + number2

# first given 
first_number_given1 = 20
second_number_given1 = 30 
result1 = product_or_sum (first_number_given1,second_number_given1)
print ("The result is: ", result1)

# second given
first_number_given2 = 40
second_number_given2 = 30
result2 = product_or_sum (first_number_given2, second_number_given2)
print ("The result is: ", result2)