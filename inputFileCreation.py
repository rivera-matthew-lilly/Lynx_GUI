from csv import reader
import csv
from datetime import datetime
#import pandas as pd

time = str(datetime.now())
time = time.replace(" ", "_")
time = time.replace("-", ".")
time = time.replace(":", ".")
#user parameters selection, id

targetVol = int(input("Target volume (100-200uL): "))

targetConc = int(input("Target concentration (1-200ug/mL): "))

neatVol = int(input("Volume for neat transfers (75-200uL): "))

inputFile = "C:\codeBASE\Lynx\input_for_dil_sol_files.csv" #input("Select file: ")
#C:\codeBASE\Lynx\input_for_dil_sol_files.csv
#(targetConc/quantConc) * targetVol

def supCalc(targetConc, targetVol, quantConc, neatVol):
    supVol = (targetConc/quantConc) * targetVol
    if supVol > targetVol:
        finalSupVol = neatVol
    else:
        finalSupVol = supVol
    finalSupVol = round(finalSupVol, 2)
    return finalSupVol
    

def plateFormatFileWriter(writer, lst):
        writer("VI;12;8")
        for i in range(1, 13):
            writer("," + str(i))
        writer("\n")
        writer("A")
        for i in range(0, 96, 8):
            writer("," + lst[i])
        writer("\n")
        writer("B")
        for i in range(1, 96, 8):
            writer("," + lst[i])
        writer("\n")
        writer("C")
        for i in range(2,96, 8):
            writer("," + lst[i])
        writer("\n")
        writer("D")
        for i in range(3, 96, 8):
            writer("," + lst[i])
        writer("\n")
        writer("E")
        for i in range(4, 96, 8):
            writer("," + lst[i])
        writer("\n")
        writer("F")
        for i in range(5, 96, 8):
            writer("," + lst[i])
        writer("\n")
        writer("G")
        for i in range(6, 96, 8):
            writer("," + lst[i])
        writer("\n")
        writer("H")
        for i in range(7, 96, 8):
            writer("," + lst[i])

supVolList = []
dilVolList = []

with open(inputFile, "r") as f:
    file_reader = reader(f)
    counter = 0
    for i in file_reader:
        if counter != 0:
            quantConc = i[1]
            quantConc = float(quantConc)
            supVol = supCalc(targetConc, targetVol, quantConc, neatVol)
            dilVol = 100 - supVol
            dilVol = round(dilVol, 2)
            #print("Sup" + str(counter) + " " + str(supVol))
            #print("Dil" + str(counter) + " " + str((dilVol)))
            counter = counter + 1
            supVolList.append(str(supVol))
            dilVolList.append(str(dilVol))
        else:
            counter = counter + 1

# csvSupOutputFilePath = "C:\codeBASE\Lynx\output_Test_files\SupCSV" + time + ".csv"
# csvDilOutputFilePath = "C:\codeBASE\Lynx\output_Test_files\DilCSV" + time + ".csv"

# with open(csvSupOutputFilePath, "w") as SUP:
#     for line in supVolList:
#         SUP.write(str(line))
#         SUP.write("\n")

# with open(csvDilOutputFilePath, "w") as DIL:
#     for line in dilVolList:
#         DIL.write(str(line))
#         DIL.write("\n")

SupCSVInput = "C:\codeBASE\Lynx\output_Test_files\SupCSVInput" + time + ".csv"
DilCSVInput =  "C:\codeBASE\Lynx\output_Test_files\DilCSVInput" + time + ".csv"


with open(SupCSVInput, "w") as SUP:
    writer = SUP.write
    plateFormatFileWriter(writer, supVolList)

with open(DilCSVInput, "w") as DIL:
    writer = DIL.write
    plateFormatFileWriter(writer, dilVolList)

#inputFileCreation.py

#./dL