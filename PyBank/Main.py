# Set modules
from decimal import ROUND_05UP, ROUND_UP, Rounded
from operator import length_hint
import os
import csv
from unicodedata import decimal

# Set filepath 
PyBankcsv = os.path.join("..","PyBank", "Resources", "budget_data.csv")

# Open and read CSV file
with open(PyBankcsv, newline="") as csvfile:
    
# Read header row 
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    
 
# Declare variables 
    Months = []
    Profit_Loss = []
    Differences = []
    Greatest_Increase_Date = ""
    Greatest_Decrease_Date = ""
    
# total number of months 
    for row in csvreader:
        Months.append(row[0])   
        Profit_Loss.append(int(row[1]))
      
# Print final analysed data
    print("Financial Analysis")
    print(".............................................")
    print("Total Months: ", len(Months))
    print("Total: $", sum(Profit_Loss))
    
    for i in range(1, len(Profit_Loss)):
        
    # Average difference between months
        Differences.append(Profit_Loss[i] - Profit_Loss[i-1])
        
    # Find average of values
        Average_Change = sum(Differences) / len(Differences)
       
    # Find greatest increase and date
        Greatest_Increase = max(Differences)
        Greatest_Increase_Date = str(Months[Differences.index(max(Differences))])
        
        
     # Find greatest decrease and date
        Greatest_Decrease = min(Differences)
        Greatest_Decrease_Date = str(Months[Differences.index(min(Differences))])
        
    # Print Analysis
    print("Average Change: $", round(Average_Change, 2))
    print("Greatest Increase in Profits: ", Greatest_Increase_Date, "($", Greatest_Increase,")")
    print("Greatest Decrease in Profits: ", Greatest_Decrease_Date, "($", Greatest_Decrease,")")
        
    
    with open("Analysis_Bank.txt", "w") as text:
        text.write("Financial Analysis\n")
        text.write("...........................\n")
        text.write("Total Months:", str(Months)) 
        text.write("Total: $", sum(Profit_Loss))
for i in range(1, len(Profit_Loss)):
    text.write("Average Change: $", round(Average_Change, 2))
    text.write("Greatest Increase in Profits: ", Greatest_Increase_Date, "($", Greatest_Increase,")") + "\n"
    text.write("Greatest Decrease in Profits: ", Greatest_Decrease_Date, "($", Greatest_Decrease,")") +"\n"
    text.write("...........................\n")