#Written By Stefan Strutz for Cisco Web Academy
#The goal of the code is to print the ASCII art for the inputted number
#The inputted number can be multiple digits.
#This code was written before I learned error handling

display = """
 ###   # ### ### # # ### ### ### ### ### 
 # #   #   #   # # # #   #     # # # # # 
 # #   # ### ### ### ### ###   # ### ### 
 # #   # #     #   #   # # #   # # #   # 
 ###   # ### ###   # ### ###   # ### ### 
"""
#The above string is used to hold the ASCII art
# note that each number is 4 characters wide and 5 characters tall

number = input ("Enter an integer:")
for j in range (5):
    # the art is 5 characters tall
    for i in number:
        digit =int (i)
        print (display [1+4*digit+j*42:5+4*digit+j*42],end = "")
        #This piece grabs one line from the corresponding number from above for every loop
        #note that it prints 4 characters for each number entered
    print ()
