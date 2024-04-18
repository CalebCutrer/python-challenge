import os
import csv

# Creating variables:
Candidates_Set = set()
Candidates_List = []
Candidate1 = [] 
Candidate2 = [] 
Candidate3 = [] 
Winner = []

Total_Votes = 0
Total_Votes_Stockham = 0
Total_Votes_DeGette = 0
Total_Votes_Doane = 0

Percentage_Votes_Stockham = 0
Percentage_Votes_DeGette = 0
Percentage_Votes_Doane = 0

# Create file path for data
election_csv =os.path.join('Resources', 'election_data.csv')
#-------------------------------------------------

# Read in data to determine candidates, skip header row 
with open(election_csv) as csvfile: 
    csv_reader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csv_reader)
    
#Getting a set of candidates who received votes 
    for row in csv_reader:
        Candidates_Set.add(row[2])

#create a break in the code to stop it from reassigning each time code is ran?
#Assigning Candidates
    Candidates_List = list(Candidates_Set) #Complete list of candidates
    #Candidate1 = Candidates_List[0]
    #Candidate2 = Candidates_List[1]
    #Candidate3 = Candidates_List[2]
    print(Candidates_List)
    
#------------------------------------------------    

# Read in data again, skip header row 
with open(election_csv) as csvfile: 
    csv_reader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csv_reader)

# Total Votes:   
    for row in csv_reader:
        Total_Votes +=1
        
# Votes per candidate:    
        if row[2] == "Diana DeGette":
            Total_Votes_DeGette = Total_Votes_DeGette +1
        elif row[2] == "Raymon Anthony Doane":
            Total_Votes_Doane = Total_Votes_Doane +1
        else:
            Total_Votes_Stockham = Total_Votes_Stockham + 1
            
#Percent votes per candidate       
        Percentage_Votes_DeGette = (Total_Votes_DeGette/Total_Votes)*100
        Percentage_Votes_Doane = (Total_Votes_Doane/Total_Votes)*100
        Percentage_Votes_Stockham = (Total_Votes_Stockham/Total_Votes)*100

#Winner:
        if (Total_Votes_Doane > Total_Votes_DeGette) & (Total_Votes_Doane > Total_Votes_Stockham):
            Winner = "Raymon Anthony Doane"
        elif (Total_Votes_DeGette > Total_Votes_Doane) & (Total_Votes_DeGette > Total_Votes_Stockham):
            Winner = "Diana DeGette"
        else:
            Winner = "Charles Casper Stockham"

#
#------------------------------------------------
#
   
# Creating output summary and writing it into a text file
outputpy = os.path.join('analysis', 'ElectionResults') #Creating path to folder
with open(outputpy, "w", newline = '') as textfile:
        writer = csv.writer(textfile)

        print("Election Results: ", file= textfile)
        print("\n----------------------------------\n", file = textfile) 
        print(f"Total Votes: {Total_Votes}", file = textfile)
        print("\n----------------------------------\n", file = textfile)
        print(f"Charles Casper Stockham: {round(Percentage_Votes_Stockham, ndigits =3)}% ({Total_Votes_Stockham})", file = textfile)
        print(f"\nDiana DeGette: {round(Percentage_Votes_DeGette, ndigits =3)}% ({Total_Votes_DeGette})", file = textfile)
        print(f"\nRaymon Anthony Doane: {round(Percentage_Votes_Doane, ndigits =3)}% ({Total_Votes_Doane})", file = textfile)
        print("\n----------------------------------\n", file = textfile)
        print(f"Winner: {Winner}\n", file= textfile)








# Sources: 
# https://stackoverflow.com/questions/70551174/python-add-unique-values-from-a-csv-column-to-list (Used as guide to make list of candidates using a set)