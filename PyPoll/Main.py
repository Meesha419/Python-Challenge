#Set modules
import os
import csv

# Set filepath 
PyPollcsv = os.path.join("..", "PyPoll", "Resources","election_data.csv")

# List to store data and initialise
count = 0
candidatelist = []
unique_candidate = []
vote_count = []
vote_percent = []

   # Set path to open the file
with open(PyPollcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

 # Conduct the ask
    for row in csvreader:

        # Total number of vote count
        count = count + 1

        # Set Candidates names in the list
        candidatelist.append(row[2])

        # Create a set from the candidatelist to get the unique candidate names
for x in set(candidatelist):
        unique_candidate.append(x)
        # y = number of votes per candidate
        y = candidatelist.count(x)
        vote_count.append(y)
        # z = total votes per candidate
        z = (y/count)*100
        vote_percent.append(z)
        
winning_vote_count = max(vote_count)
winner = unique_candidate[vote_count.index(winning_vote_count)]
    

print("ELECTION RESULTS")   
print("-------------------------")
print("Total Votes : " + str(count))    
print("-------------------------")

for i in range(len(unique_candidate)):
  
   print(unique_candidate[i] + ": " + str(format(vote_percent[i], ".3f") +"% (" + str(vote_count[i])+ ")"))
    
print("-------------------------")
print("The winner is: " + winner)
print("-------------------------")

with open("Analysis_ElectionPoll.txt", "w") as text:
    text.write("Election Results\n")
    text.write("---------------------------------------\n")
    text.write("Total Vote: " + str(count) + "\n")
    text.write("---------------------------------------\n")
    for i in range(len(set(unique_candidate))):
      text.write(unique_candidate[i] + ": " + str(format(vote_percent[i], ".3f") +"% (" + str(vote_count[i]) + ")\n"))
    text.write("---------------------------------------\n")
    text.write("The winner is: " + winner + "\n")
    text.write("---------------------------------------\n")
      