#Import os module to create file paths
import os

#Import csv module to read in csv
import csv

#Specify path to csv file in resources folder
csvpath = os.path.join('PyBank', 'Resources', 'budget_data.csv')

#Reading in file
with open(csvpath) as csvfile: 
        csvbudget = csv.reader(csvfile, delimiter = ',')
        print(csvbudget)
        # Did not work^^

        #Reading the header row (based on checking for a header directly)
        csv_header = next(csvbudget)
        print(f"Header: {csv_header}")

        #Print subsequent rows
        for row in csvbudget:
                print(row)

# Writing function for the total number of months included in the dataset:

def Total_Months_Count(csvfile, column_index):
        total_months = 0


