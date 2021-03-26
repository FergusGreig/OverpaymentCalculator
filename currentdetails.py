# These are the the numbers used for the calculations in MOPcalc edit them to fit 
# your detatils
mortValue = 194000 
mortInt = 1.5
mortTerm = 35
mortPaym = 597

def displayNums():
    print("This calculation was computed using: ")
    print("A mortgage of £" + str(mortValue) + ".")
    print("With an interest rate of "+ str(mortInt) +"%.")
    print("Being paid at £"+str(mortPaym)+" per month.")
    print("Over a " + str(mortTerm) + " year term.")

if (__name__ == '__main__'):
    displayNums()
