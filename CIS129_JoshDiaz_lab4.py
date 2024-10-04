#The main function
def main():
    #declare local variables
    monthlySales = getSales(storeAmount) #call to get sales
    salesIncrease = getIncrease(empAmount) #call to getIncrease
    storeAmount = calcStoreBonus(monthlySales) #call to calcStoreBonus
    empAmount = calcEmpBonus(salesIncrease) #call to calcEmpBonus
    printBouns = (storeAmount, empAmount) #call to printBonus
#This function gets the monthly sales
def getSales(storeAmount):
    monthlySales = float(input(storeAmount)) 
    return monthlySales
#This function gets the percent of increase in sales
def getIncrease(empAmount):
    salesIncrease = float(input(empAmount))
    salesIncrease = salesIncrease / 100
    return salesIncrease
#This function determines the storeAmount bonus
def calcStoreBonus(monthlySales):
    if monthySales >= 110000:
        storeAmount = 6000
    elif monthlySales >= 100000:
        storeAmount = 5000
    elif monthlySales >= 90000:
        storeAmount = 4000
    elif monthlySales >= 80000:
        storeAmount = 3000
    else:
        storeAmount = 0
    return storeAmount
    #This function determines the empAmount bonus
    def calcEmpBonus(salesIncrease):
        if salesIncrease >= .05:
            empAmount = 75
        elif salesIncrease >= .04:
            empAmount = 50
        elif salesIncrease >= .03:
            empAmount = 40
        else:
            empAmount = 0
        return empAmount
#This function prints the bonus information
def printBonus(storeAmount, empAmount):
    print("The store bonus amount is $", storeAmount)
    print("The employee bonus amount is $", empAmount)
    if (storeAmount == 6000) or (empAmount == 75):
        print('Congrats! You have reached the highest bonus amounts possible! ')
#calls main
main()      
