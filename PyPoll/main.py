import os
import csv

# Creating variables:
Total_Votes = 0
Candidates_Set = set()
Candidates_Set2 = set()
Candidates_List = []
Candidate1 = [] #Degette
Candidate2 = [] #Stockham
Candidate3 = [] #Doane
Winner = []

Percentage_Votes_Stockham = 0
Percentage_Votes_DeGette = 0
Percentage_Votes_Doane = 0

Total_Votes_Stockham = 0
Total_Votes_DeGette = 0
Total_Votes_Doane = 0

# Create file path for data
election_csv =os.path.join('Resources', 'election_data.csv')


    

# Read in data, skip header row 
with open(election_csv) as csvfile: 
    csv_reader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csv_reader)

# Total Votes:   
    for row in csv_reader:
        Total_Votes +=1
    print(Total_Votes)

# Read in data, skip header row 
with open(election_csv) as csvfile: 
    csv_reader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csv_reader)
    
#Getting a set of candidates who received votes 
    for row in csv_reader:
        Candidates_Set.add(row[2])

#Assigning Candidates
    Candidates_List = list(Candidates_Set)
    Candidate1 = Candidates_List[0]
    Candidate2 = Candidates_List[1]
    Candidate3 = Candidates_List[2]
    print(Candidates_List)
    print(Candidate1)
    print(Candidate2)
    print(Candidate3)

    









# Sources: 
# https://stackoverflow.com/questions/70551174/python-add-unique-values-from-a-csv-column-to-list (Used as guide to make list of candidates)