import csv

# f = open("Resources\election_data.csv")
# reader = csv.reader(f)
# hdr = next(reader)
# This is printing out the rows
# for row in reader:
    # This is runnig the code
#   print(row)

# using with statement
# The open() function opens a file, and returns it as a file object
f = open("Resources/election_data.csv")
reader = csv.reader(f)
 # This is skipping the header
hdr = next(reader)
 # This is printing out the length
totalLines = len(list(reader))
 # This is runnig the code
print(totalLines)
#  #--------------------------------------------------------------------------------------------------

# Useing with statement
# The open() function opens a file, and returns it as a file object
with open("Resources/election_data.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    # This line tells your fuction not read/count any titles for columns
    csv_header = next(csv_reader)

# The total number of votes each candidate won
    
   # made variable for each candidate, Khan = 0
    Khan = 0
    Correy = 0
    Li = 0
    O_Tooley = 0
    # made a for  Loop, looping through row [2] which is Candidate in the excel sheet
    for row in csv_reader:
     # operator == sign mean that "comparatively equal"
        # if Statement
     if row[2] == "Khan":
            Khan = Khan + 1
    
  
print("Khan has ", Khan, " Votes")

#-------------------------------------------------------------------------------------------------------

with open("Resources/election_data.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    # This line tells your fuction not read/count any titles for columns
    csv_header = next(csv_reader)
   
    # made variable for each candidate,  Correy = 0
    # made a for Loop, looping looping through row [2] which is Candidate in the excel sheet
    Correy = 0
    for row in csv_reader:
        # operator == sign mean that "comparatively equal"
        #  if Statement
        if row[2] == "Correy":
            Correy = Correy + 1

print("Correy has ", Correy, " Votes")

#-----------------------------------------------------------------------------------------------------------------------

with open("Resources/election_data.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    # This line tells your fuction not read/count any titles for columns
    csv_header = next(csv_reader)
   
    # made variable for each candidate,  Li = 0
    # made a for Loop, looping looping through row [2] which is Candidate in the excel sheet
    Li = 0
    for row in csv_reader:
      # operator == sign mean that "comparatively equal"
        # if Statement
        if row[2] == "Li":
            Li = Li + 1

print("Li has ", Li, " Votes")

#------------------------------------------------------------------------------------------------------------------

with open("Resources/election_data.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    # This line tells your fuction not read/count any titles for columns
    csv_header = next(csv_reader)
   
    # made variable for each candidate,  Correy = 0
    # made a for Loop, looping looping through row [2] which is Candidate in the excel sheet
    OTooley = 0
    for row in csv_reader:
        # operator == sign mean that "comparatively equal"
        #  if Statement
        if row[2] == "O\'Tooley":
            OTooley = OTooley + 1

print("OTooley ", OTooley, " Votes")



# number of votes canitdites /(divided) total number of votes 
#  OTooley  /(divided) total numbers number of votes will give the precentage

percentage = OTooley/totalLines
percentage_K = Khan/totalLines
percentage_C = Correy/totalLines
percentage_L = Li/totalLines

#print("{:.2%}".format(percentage))

print((Khan/totalLines)*100)
print("Khan ", Khan, "{:.3%}".format(percentage_K))
#-----------------------------------------------------------------------------------

print((Correy/totalLines)*100)
print("Correy ", Correy, "{:.3%}".format(percentage_C))

#---------------------------------------------------------------------------------

print((Li/totalLines)*100)
print("Li ", Li, "{:.3%}".format(percentage_L))

#---------------------------------------------------------------------------------

# print(f'OTooley {OTooley} Votes')
print((OTooley/totalLines)*100)
print("OTooley ", OTooley, "{:.3%}".format(percentage))

#---------------------------------------------------------------------------------
             # dictionary  
candidates = {'Khan':Khan, 'Correy':Correy, "Li":Li, 'OTooley':OTooley}

print(max([percentage, percentage, percentage_K, percentage_C, percentage_L]))

# Given variable name
keyGreatest = ''
valueGreatest = 0

# for loop
for x in candidates.items():
    print(x[0], x[1])
    print('--------------------------')
    if(valueGreatest < x[1]):
        valueGreatest = x[1]
        keyGreatest = x[0]

print(f"Winner: {keyGreatest}, {valueGreatest}")



    f = open("analysis/test.txt","w")
f.write("\n Election Results")
f.write("\n ------------------------")
f.write("\n Total Votes: 3521001 ")
f.write("\n Khan: 63.000% (2218231)")
f.write("\n Correy: 20.000% (704200) ")
f.write("\n Li: 14.000% (492940 ")
f.write("\n O'Tooley: 3.000% (105630) ")
f.write("\n ---------------------------")
f.write("\n Winner: Khan) ")
f.write("\n ---------------------------")
#f.write(" without newline")