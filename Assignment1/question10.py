# Q10. Take a decimal number as input (like ) and output its: 
# 45.78 
# • integer part - 
# 45 
# • fractional part - 
# .78 
a = float(input("Enter a decimal number: "))
integer_part = int(a)   
fractional_part = a - integer_part
print("Integer part:", integer_part)
print("Fractional part:", fractional_part)