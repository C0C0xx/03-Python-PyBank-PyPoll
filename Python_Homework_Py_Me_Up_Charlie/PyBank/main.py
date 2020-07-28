import csv

f = open("Resources/budget_data.csv")
reader = csv.reader(f)
hdr = next(reader)
 # This is printing out the rows
for row in reader:
     # This is runnig the code
   print(row)
 # ---------------------------------------------------------
f = open("Resources/budget_data.csv")
reader = csv.reader(f)
 # This is skipping the header
hdr = next(reader)
 # This is printing out the length
totalLines = len(list(reader))
 # This is runnig the code
print(totalLines)
#  #---------------------------------------------------------------------------------------
 
pl_values = []
with open("Resources/budget_data.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    # This line tells your fuction not read/count any titles for columns
    csv_header = next(csv_reader)
    # This sets your starting point at zero for total
    total = 0
    # This starts your loop by telling it where to loop
    for lines in csv_reader:
        # This is telling your code what to loop for
        # indenting makes it part of the line 6
        total = total + int(lines[1])
        pl_values.append(int(lines[1])) # add each profit/loss to the list pl_values
       # This is runnig the loop/code
print("total: " + str(total))
#-----------------------------------------------------------------------------------------
#   print(pl_values) 
#   i = 0
#   for val in pl_values[:86]:    
#       current_PL = val
#       i = i+1
#       next_PL = pl_values[i]
#       print(i, current_PL)
#       print(i+1, next_PL)
#-------------------------------------------------------------------------------------------------
monthly_change = 0
with open("Resources/budget_data.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    # This line tells your fuction not read/count any titles for columns
    csv_header = next(csv_reader)
    #row 2 :   
    total_profit_loss = 0
    prev_row = 0  
    for lines in csv_reader:
        if(prev_row == 0):
              # no previous vale beginning of PL
              prev_row = int(lines[1])     
        else:
              monthly_change = monthly_change + (int(lines[1]) - prev_row)
              total_profit_loss = total_profit_loss + int(lines[1])
              print("monthly differencec", str((int(lines[1]) - prev_row)), "cummulativmonthly_change", str(monthly_change))
              prev_row = int(lines[1])
              
    avg_change = monthly_change/(totalLines-1)
    total_average = total_profit_loss/(totalLines-1)
    print("Average change " + str(avg_change))
    #print("total_profit_loss " + str(total_profit_loss))
    #print("Total average " + str(total_average))
#--------------------------------------------------------------------------------------------------------------------------------------
    
monthly_change = 0
with open("Resources/budget_data.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    # This line tells your fuction not read/count any titles for columns
    csv_header = next(csv_reader)
    
    #row 2 : 
    greatest_decrease_month = ""
    greatest_Increase_month = ""
    greatest_Increase_Profits = 0
    greatest_decrease_losses = -2315
    total_profit_loss = 0
    prev_row = 0  
    
    for lines in csv_reader:
        if(prev_row == 0):
              # no previous vale beginning of PL
              prev_row = int(lines[1])
              date_amonut = [lines[0], int(lines[1])]
              
        else:
            monthly_difference = int(lines[1]) - prev_row
            prev_row = int(lines[1])

            # this is saying to the greatest_Increase is greater then the next row.
            if monthly_difference > greatest_Increase_Profits:
                greatest_Increase_Profits = monthly_difference
                greatest_Increase_month = lines[0]

            # this is saying to the greatest_decrease is less then the next row.
            elif monthly_difference < greatest_decrease_losses:
                 greatest_decrease_losses = monthly_difference    
                 greatest_decrease_month = lines[0]
    
    print("date_amonut ",  date_amonut)
    print(greatest_Increase_month, greatest_Increase_Profits)
    print(greatest_decrease_month, greatest_decrease_losses)



    f = open("analysis/test.txt","w")
f.write("\n Financial Analysis")
f.write("\n ------------------------")
f.write("\n Total Months: 86 ")
f.write("\n Total: $38382578")
f.write("\n Average  Change: $-2315.12 ")
f.write("\n Greatest Increase in Profits: Feb-2012 ($1926159) ")
f.write("\n Greatest Decrease in Profits: Sep-2013 ($-2196167) ")
#f.write(" without newline")





