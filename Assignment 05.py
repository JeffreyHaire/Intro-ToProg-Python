# Jeffrey Haire
# IT FDN 100
# Prof Root
# Assignment 5
# 10/28/17
# Because the file doesn't exist on your computer, I have to make it like assgn 3
objF = open("c:\PythonClass\Module05\ToDo.txt", "w") # Write file if it doesn't exist
objF.write("Task,Priority \nClean, Low\nPay Bills, High") # Write what I want the list to look like
objF.close() # Close file b/c done w/it for now and maybe ever
# Read from the text file
objFile = open("C:\PythonClass\Module05\ToDo.txt", "r")#see page 193
strData = objFile.readline() # Read what's in the text file
dicRow1 = {(strData.split(",")[0]).strip():(strData.split(",")[1]).strip()} # divide the data into 2 elements
lstTable = [dicRow1] # This is a table of dictionaries

# values()
# Now, get all of the other rows
for line in objFile: # Scan each line
 strData = line # readline() reads a line of the data
 dicRow = {(strData.split(",")[0]).strip(): (strData.split(",")[1]).strip()}  # divide the data into 2 elements
 lstTable.append(dicRow), # now add the row to the table
objFile.close()
# That completes the setup. Now for the loop
choice = None
while choice != "0": # So if the choice is zero then skip the rest of the loop
    print( # Here is my menu displayed for the user
        """
        Please select one of the following options:

        0 - Quit
        1 - Show all tasks and priority levels
        2 - Add a task and priority level for it
        3 - Remove an existing item
        4 - Save to text file
        """
    )# End of menu
    choice = input("Choice: ") # Pauses for user input
    print()
    # exit
    if choice == "0": # 0 is equal to 0, so exit the loop
        print("Good-bye.")
        break # Start again
    # Show all entries
    elif choice == "1": # Display option
        print("Here are your current tasks and priority levels\n")
        for row in lstTable: # Prints the rows of the table
            print(row)
    elif choice == "2": # Add to list option
        strTask = input("What task do you want to add to the list?: ")
        strPriority = input(str("What priority level is it?: "))
        dicRow = {strTask:strPriority}  # divide the data into 2 elements
        lstTable.append(dicRow) # Used append to add the data to existing to do list
        continue # back to menu
        # Ask to save their inputs to text file
    elif choice == "3": # Removing an entry from the list
        strData = input("What term do you want me to delete?: ") # Get item from user
        for row in lstTable: # Search every row of the list
            if strData in row: # If the input is found
                lstTable.remove(row) # Take out the whole row it was found in
                print("\nOkay, I deleted", strData) # Show what was deleted
                break # Back to the larger loop
        else: # In case the user typed something that wasn't on the list
            print("\nI can't do that!", strData, "doesn't exist in the dictionary.") # Friendly error message
    elif choice == "4": # Saving to text file
        strSaveToFile = input("Type 'yes' to save to text file or any key to exit: ") # Get input
        if (strSaveToFile.lower() == "yes"): # If they want to save it
            objF = open("c:\PythonClass\Module05\ToDo.txt", "w") # Open the file created in the beginning
            objF.write(str(lstTable)) # Write the new list
            objF.close() # Close out the text file
            print("The following data was saved to a file:\n\r", lstTable) # Display for user
            continue # Back to the menu
    else:
        print("Continue") # Oops
objF = open("c:\PythonClass\Module05\ToDo.txt", "w")  # Open the file created in the beginning
objF.write(str(lstTable))  # Write the new list
objF.close()  # Close out the text file
print("The following data was saved to a file:\n\r", lstTable)  # Display for user

        # Ask if they want to save to a file when they exit the loop if they say yes

input("\n\nPress the enter key to exit.")

