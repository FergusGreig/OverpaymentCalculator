import currentdetails

mortVal = [currentdetails.mortValue]
intSum = 0
mortRem = mortVal[0]
months = 0
years = 0

while (mortRem >= 0):
    intAnnual = mortRem*(currentdetails.mortInt/100)
    intMonth = intAnnual/12
    mortPaid = currentdetails.mortPaym - intMonth
    mortRem -= mortPaid
    intSum += intMonth
    months += 1
    if (months == 12):
        months = 0
        years += 1
        mortVal.append(mortRem)
    


def showResult():
    print("Total Interest paid = £"+ str(intSum))
    print("Time taken = "+ str(years)+" years and " + str(months)+" months.")
    for n in mortVal:
        print(n)

if(__name__ == '__main__'):
    showResult()