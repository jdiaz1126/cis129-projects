#Module 5 Lab 
#Declaring variables 
totalBottles = 0          
counter = 1             
todayBottles = 0         
totalPayout = 0          
keepGoing = "y"          
#Loop to run program again
While keepGoing == "y"
    #Code to set value of variables 
    totalBottles = 0  
    totalPayout = 0    
    call getBottles()   
    call calcPayout()    
    call printInfo()     
    Display "Do you want to enter another week’s worth of data?"
    Display "(Enter y or n)"
    Input keepGoing
End While	
#Get Bottles code
NBR_OF_DAYS = 7
totalBottles = 0
todayBottles = 0
counter = 1
While counter <= NBR_OF_DAYS
    Display "Enter number of bottles returned for day #", counter, ":"
    Input todayBottles
    totalBottles = totalBottles + todayBottles  
    counter = counter + 1  
End While
#Calculate payout code
PAYOUT_PER_BOTTLE = .10
totalPayout = 0 
totalPayout = totalBottles * PAYOUT_PER_BOTTLE  
#Print information code
Display "Total bottles collected: ", totalBottles
Display "Total payout for the week: $", totalPayout
