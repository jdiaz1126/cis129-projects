# Function to calculate total hot dogs required
def getTotalHotDogs():
    # Ask for the number of attendees and the number of hot dogs per person
    attendees = int(input("Enter the number of attendees: "))
    hotDogsPerPerson = int(input("Enter the number of hot dogs per person: "))
    
    # Calculate total number of hot dogs needed
    totalHotDogs = attendees * hotDogsPerPerson
    return totalHotDogs

# Function to calculate and display the results
def showResults(totalHotDogs):
    # Constants for the number of hot dogs and buns per package
    DOGS_PER_PACKAGE = 10
    BUNS_PER_PACKAGE = 8
    
    # Calculate the minimum number of packages required and leftovers
    minHotDogPackages = (totalHotDogs + DOGS_PER_PACKAGE - 1) // DOGS_PER_PACKAGE
    minBunPackages = (totalHotDogs + BUNS_PER_PACKAGE - 1) // BUNS_PER_PACKAGE
    
    # Calculate the leftovers
    hotDogsLeftOver = (minHotDogPackages * DOGS_PER_PACKAGE) - totalHotDogs
    bunsLeftOver = (minBunPackages * BUNS_PER_PACKAGE) - totalHotDogs
    
    # Display the results
    print("Minimum packages of hot dogs needed:", minHotDogPackages)
    print("Minimum packages of hot dog buns needed:", minBunPackages)
    print("Hot dogs remaining:", hotDogsLeftOver)
    print("Hot dog buns remaining:", bunsLeftOver)

# Main program
def main():
    # Get total number of hot dogs required
    totalHotDogs = getTotalHotDogs()
    
    # Show the results
    showResults(totalHotDogs)

# Call the main function to start the program
if __name__ == "__main__":
    main()
