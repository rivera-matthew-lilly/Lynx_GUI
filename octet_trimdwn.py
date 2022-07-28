from csv import reader  


octetFilePath = "C:\codeBASE\Lynx\octet_results_sheet.csv"
#"C:\codeBASE\Lynx\octet_report"

octetQuants = []
with open(octetFilePath, "r") as f:
    file_reader = reader(f)
    counter = 0
    for i in file_reader:
        if counter != 0 and counter < 385:
            octetConc = i[12]
            counter = counter + 1
            octetQuants.append(octetConc)
        else:
            counter = counter + 1


plate1 = []
plate2 = []
plate3 = []
plate4 = []

for i in range(0,95):
    myQuant = octetQuants[i]
    plate1.append(myQuant)
for i in range(96,191):
    myQuant = octetQuants[i]
    plate2.append(myQuant)
for i in range(192,287):
    myQuant = octetQuants[i]
    plate3.append(myQuant)
for i in range(288,384):
    myQuant = octetQuants[i]
    plate4.append(myQuant)



#octet_trimdwn.py

#./dL