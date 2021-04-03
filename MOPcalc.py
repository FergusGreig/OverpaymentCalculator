import currentdetails

mortVal = [currentdetails.mortValue]

def mortgageCount(payments):
    intSum = 0
    mortRem = mortVal[0]
    months = 0
    years = 0
    while (mortRem >= 0):
        intAnnual = mortRem*(currentdetails.mortInt/100)
        intMonth = intAnnual/12
        mortPaid = payments - intMonth
        mortRem -= mortPaid
        intSum += intMonth
        months += 1
        if (months == 12):
            months = 0
            years += 1
            mortVal.append(mortRem)
    
    return [years,months, intSum]

def showResult(overpayment=0):
    time = mortgageCount(currentdetails.mortPaym + overpayment)
    print("For an overpayment of £" + str(overpayment))
    print("The total interest paid is £"+ str(time[2]))
    print("The time taken is "+ str(time[0])+" years and " + str(time[1])+" months.")
#    for n in mortVal:
#        print(n)

if(__name__ == '__main__'):
    showResult()