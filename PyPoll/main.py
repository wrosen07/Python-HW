import os
import csv

total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)

    for row in csvreader:
        total_votes += 1
        if(row[2] == "Khan"):
            khan_votes += 1
        elif(row[2] == "Correy"):
            correy_votes += 1
        elif(row[2] == "Li"):
            li_votes += 1
        else:
            otooley_votes += 1

khan_percent = khan_votes / total_votes
correy_percent = correy_votes / total_votes
li_percent = li_votes / total_votes
otooley_percent = otooley_votes / total_votes

winner = max(khan_votes, correy_votes, li_votes, otooley_votes)

if winner == khan_votes:
    winner_name = "Khan"
elif winner == correy_votes:
    winner_name = "Correy"
elif winner == li_votes:
    winner_name = "Li"
else:
    winner_name = "O'Tooley"

print(f"Election Results")
print(f"-----------------------------")
print(f"Total Votes: {total_votes}")
print(f"-----------------------------")
print(f"Khan: {khan_percent:.3%}({khan_votes})")
print(f"Correy: {correy_percent:.3%}({correy_votes})")
print(f"Li: {li_percent:.3%}({li_votes})")
print(f"O'Tooley: {otooley_percent:.3%}({otooley_votes})")
print(f"-----------------------------")
print(f"Winner: {winner_name}")
print(f"-----------------------------")

output_file = os.path.join('Analysis', 'election_date_revised.txt')
with open(output_file, 'w',) as txtfile:

    txtfile.write(f"Election Results\n")
    txtfile.write(f"------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}")
    txtfile.write(f"------------------------\n")
    txtfile.write(f"Khan: {khan_percent:.3%}({khan_votes})\n")
    txtfile.write(f"Correy: {correy_percent:.3%}({correy_votes})\n")
    txtfile.write(f"Li: {li_percent:.3%}({li_votes})\n")
    txtfile.write(f"O'Tooley: {otooley_percent:.3%}({otooley_votes})\n")
    txtfile.write(f"------------------------\n")
    txtfile.write(f"Winner: {winner_name}\n")
    txtfile.write(f"------------------------\n")
    