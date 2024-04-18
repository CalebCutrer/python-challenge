# I got assistance from Melissa from class on the formatting of my variables and for loops, we collaborated on this assignment over zoom. 

#Import os module to create file paths
import os

#Import csv module to read in csv
import csv

#Specify path to csv file in resources folder
csvpath = os.path.join('Resources', 'budget_data.csv')

#Reading in file
with open(csvpath) as csvfile: 
        csv_reader = csv.reader(csvfile, delimiter = ',')
        print(csv_reader)
        
        #Checking for header
        csv_header = next(csv_reader)
        print(f"Header: {csv_header}")

        #Looking at subsequent rows
        for row in csv_reader:
               print(row)

# Creating the variables we need:
TotalMonths = 0
NetTotalProfit = 0
LastMonthProfit = 0
ThisMonthProfit = 0
TotalProfitChange = 0
AverageProfitChange = 0

# The following variables were the ones Melissa helped me format correctly:
GreatestIncrease = float('-inf')
GreatestDecrease = float('inf')
MonthIncrease = None 
MonthDecrease = None
FirstMonth = True 

#Reading in file again, making sure to skip header:
with open(csvpath) as csvfile: 
        csv_reader = csv.reader(csvfile, delimiter = ',')
        print(csv_reader)
        csv_header = next(csv_reader)

 #Finding the total number of months, as well as the total profits/losses over this period
        for row in csv_reader:
                LastMonthProfit = ThisMonthProfit
                TotalMonths += 1
                ThisMonthProfit = float(row[1])
                NetTotalProfit += ThisMonthProfit
                
                Date = row[0] #will be used later to determine the MonthIncrease and MonthDecrease values
                ProfitChange = ThisMonthProfit - LastMonthProfit #Tracks monthly profit fluctuations
                
                #Skipping first row because there is no change yet given there is no data on the previous month
                if not FirstMonth: 
                        TotalProfitChange += ProfitChange
                else:
                        FirstMonth = False

                #Greatest profit increase and corresponding month
                if ProfitChange > GreatestIncrease:
                        GreatestIncrease = ProfitChange
                        MonthIncrease = Date
                
                Date = row[0] #Reset date value to begin at the first row/month once we find greatest increase
                
                #Greatest profit decrease and corresponding month
                if ProfitChange < GreatestDecrease:
                        GreatestDecrease = ProfitChange
                        MonthDecrease = Date
        
        #Finding average profit change over time period using  
        AverageProfitChange = TotalProfitChange/(TotalMonths-1) 
                
# Creating output summary and writing it into a text file
output = os.path.join('analysis', 'BankAnalysis') #Creating path to folder
with open(output, "w", newline = '') as textfile:
        writer = csv.writer(textfile)

        print("\nFinancial Analysis", file = textfile)
        print("\n--------------------------------------------\n", file = textfile) 
        print(f"Total Months: {TotalMonths}",file = textfile)
        print(f"\nTotal: ${round(NetTotalProfit)}", file = textfile) 
        print(f"\nAverage Change: ${round(AverageProfitChange, ndigits=2)}", file = textfile)
        print(f"\nGreatest Increase in Profits: {MonthIncrease} (${round(GreatestIncrease)})", file = textfile)
        print(f"\nGreatest Decrease in Profits: {MonthDecrease} (${round(GreatestDecrease)})\n", file = textfile)
        
#Learned the print setting "file =" on stack overflow: https://stackoverflow.com/questions/36571560/directing-print-output-to-a-txt-file 


















