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
        
        #Reading the header row (based on checking for a header directly)
        csv_header = next(csv_reader)
        print(f"Header: {csv_header}")

        #Print subsequent rows
        for row in csv_reader:
               print(row)
   
# Total Months:
MonthCount = []
with open(csvpath, 'r') as csv_file: 
        csv_reader = csv.DictReader(csv_file, delimiter = ',')
        for row in csv_reader:
                MonthCount.append(row['Date'])
                Count = len(MonthCount)
print(Count)
       
# Total Profit/Losses

netprofit = 0

with open(csvpath, 'r') as csv_file: 
        csv_reader = csv.reader(csv_file, delimiter = ',')
        for row in csv_reader:
                value = int(row[1])
                netprofit += value
        print(netprofit) 




        

#create path to file, another with open with a w for write, file.write 
