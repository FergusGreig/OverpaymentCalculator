# These are the the numbers used for the calculations in MOPcalc edit them to fit 
# your detatils
mortValue = 193400 
mortInt = 1.5
mortTerm = 35

def displayNums():
    print("This calculation was computed using: ")
    print("A mortgage of £" + str(mortValue) + ",")
    print("With interest of "+ str(mortInt) +"%,")
    print("Over a " + str(mortTerm) + " year term.")

if (__name__ == '__main__'):
    displayNums()
