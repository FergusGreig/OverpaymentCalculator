import currentdetails

def compInt(payment, time , rate):
    total = 0
    profit = 0
    months = 0
    while (months < time):
        months+=1
        interest = total*rate/12
        total+=payment + interest
        profit += interest
    return [total, profit]


def mortgageCount(payments):
    mortVal = [currentdetails.mortValue]
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
    results = mortgageCount(currentdetails.mortPaym + overpayment)
    savings = compInt(overpayment,currentdetails.mortTerm*12,0.01)
    print("For a monthly overpayment of £" + str(overpayment))
    print("The total interest paid is £"+ str(results[2]))
    print("The time taken to pay off the debt is "+ str(results[0])+" years and " + str(results[1])+" months.")
    print("""A savings account at 1% interest over 35 years would yeild £""" +str(savings[1]))
#    for n in mortVal:
#        print(n)

def overpayLoop():
    currentdetails.displayNums()
    for x in range(0,2500,500):
        showResult(x)


if(__name__ == '__main__'):
    overpayLoop()