import currentdetails

mortVal = [0,0]
mortVal.pop()
mortVal[0] =currentdetails.mortValue
intSum = 0

years = range(0,currentdetails.mortTerm,1)
for n in years:
    intPaid = mortVal[n]*(currentdetails.mortInt/100)
    mortPaid = 12*currentdetails.mortPaym - intPaid
    mortVal.append( mortVal[n]-mortPaid)
    intSum += intPaid


def showResult():
    print(intSum)
    for n in mortVal:
        print(n)

if(__name__ == '__main__'):
    showResult()