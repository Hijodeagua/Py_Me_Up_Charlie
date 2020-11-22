import os
import csv


#Define Variables
votes = []
county = []
cand = []
Khan = []
Correy = []
Li = []
Tooley = []


poll_path=os.path.join('..','PyPoll','election.csv')
with open(poll_path, newline='') as csvfile:
    poll_reader = csv.reader(csvfile, delimiter=',')
    print(poll_reader)
    poll_header = next(poll_reader)
    
    for row in poll_reader:
        votes.append(int(row[0]))
        county.append(row[1])
        cand.append(row[2])
        
    Vote_Count = len(votes)
    
    for candidate in cand:
        if candidate == "Khan":
            Khan.append(cand)
            votes_for_k = len(Khan)
        elif candidate == "Correy":
            Correy.append(cand)
            votes_for_C = len(Correy) 
        elif candidate == "Li":
            Li.append(cand)
            votes_for_Li = len(Li) 
        else: 
            Tooley.append(cand)
            votes_for_OT = len(Tooley) 
    
    percent_k = round((votes_for_k/Vote_Count)*100)   
    percent_c = round((votes_for_C/Vote_Count)*100)
    percent_li = round((votes_for_Li/Vote_Count)*100)
    percent_OT = round((votes_for_OT/Vote_Count)*100)
    
    if percent_k > max(percent_c, percent_li, percent_OT):
        winner = "Khan"
    elif percent_c > max(percent_k, percent_li, percent_OT):
        winner = "Correy"  
    elif percent_li > max(percent_k, percent_c, percent_OT):
        winner = "Li"
    else:
        winner = "O'Tooley"
        
Analysis = (
f"Election Results\n"
f"---------------------------- \n"
f"Total Votes: {Vote_Count} \n"
f"---------------------------- \n"
f"Votes for Khan, (Total, Percentage): {votes_for_k}, {percent_k}% \n"
f"Votes for Correy: {votes_for_C}, {percent_c}% \n"
f"Votes for Li: {votes_for_Li}, {percent_li}% \n"
f"Votes for O'Tooley: {votes_for_OT}, {percent_OT}% \n"
f"---------------------------- \n"
f"Ganador: {winner} \n"
f"---------------------------- \n")

print(Analysis)

polls_output = os.path.join('Polls Analysis.txt')

with open(polls_output, 'w') as txtfile:
    
    Analysis_Output = txtfile.write(Analysis)
        
