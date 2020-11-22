import os
import csv

#Create path for csv
budget_csvpath = os.path.join('..','/PyBank', 'budget_data.csv')

#Define Variables
Months = 0
Total_Rev = 0
past_rev = 0
High_Inc = 0
Low_Dec = 99999999999
Rev_Change = []

#read in csv
with open(budget_csvpath, newline='') as csvfile:
    
    budget_csvreader = csv.reader(csvfile, delimiter=',')
    
    next(budget_csvreader, None)
    
    for row in budget_csvreader:
    
        #Count of Months
        Months = Months + 1
        
        #Total Revenue
        Total_Rev = Total_Rev + (int(row[1]))
        
        #Change in Months
        mthch = int(row[1]) - past_rev
        past_rev = int(row[1])
        
        #Put change in rev in New List
        Rev_Change.append(mthch)
        
        #Find Average Change of Rev
        Averev= round(sum(Rev_Change)/Months)
        
        #Find greatest increase
        if (mthch > High_Inc):
            High_Inc_Month = row[0]
            High_Inc = mthch 
            
        #Find the greatest decrease
        if (mthch < Low_Dec):
            Low_Dec_Month = row[0]
            Low_Dec = mthch

#Print Analysis
Analysis = (
f"Analysis\n"
f"---------------------------- \n"
f"Total Months: {Months} \n"
f"Total Revenue: ${Total_Rev} \n"
f"Average Revenue Change: ${Averev} \n"
f"Greatest Increase in Revenue: {High_Inc_Month} (${High_Inc}) \n"
f"Greatest Decrease in Revenue: {Low_Dec_Month} (${Low_Dec}) \n")
print(Analysis)

budget_output = os.path.join('Budget_Analysis.txt')

with open(budget_output, 'w') as txtfile:
    
    Analysis_Output = txtfile.write(Analysis)

