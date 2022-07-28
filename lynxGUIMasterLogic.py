from csv import reader
import csv
from datetime import datetime

#time management
time = str(datetime.now())
time = time.replace(" ", "_")
time = time.replace("-", ".")
time = time.replace(":", ".")

################################################################

#get user parameters for run
sourceTypeSelected = input("Select source plate type: ")
#destination plate (drop down choices: "96Flatbottom", "96PCR", "96MasterBlock") (required input)
desTypeSelected = input("Select destination plate type: ")
#tip type (drop down choices: "340F", "1250F") (required input)
tipTypeSelected = input("Select tip type: ")
#number of plates to be ran (numerical choices: 1-4) (required input)
numberOfPlates = int(input("Enter Number of source plates to normalize: "))
#ask user if files are to bee uploaded (radio button: True/False)
fileBasedNorm = bool(input("Is this a file based normalizaton ('True' or 'False')?: "))
#ask user if normalized samples need to be transfer to Echo plate
bCreateEcho = bool(input("Transfer to Echo plate ('True' or 'False')?: "))
advancedVariables = bool(input("Would you like to adjust advanced settings ('True' or 'False)?: "))

#build worktable path
worktableDefaultPath = "C:\MethodManager4\Workspaces\LO507\Methods\Production\Worktables\\"
worktableCustomPath = (worktableDefaultPath + tipTypeSelected + "_" + sourceTypeSelected + "_" + desTypeSelected + ".worktable.Lynx.Left.worktable")

if advancedVariables == True:
    #ask user if they want to mix (defualt = yes/true)
    bMix = input("Mix plates (8 cycles) after normalization ('yes' or 'no')?: ")
    #ask user to dded mix height offset variable - numerical choice (default = 1.0 mm) (min = 0.0 mm max=5.0 mm) (increment by 0.1 mm)
    intMixHeightOffset = int(input("Mixing height offset (Default 1mm)?: "))
    #ask user for mix volume (min = 0uL max = 150uL)
    mixVol = int(input("Mix Volume (Defualt 100ul)?: "))
else:
    bMix = 'yes'
    intMixHeightOffset = 1
    mixVol = 100

if fileBasedNorm == True:
    targetVol = int(input("Target volume (100-200uL): "))

    targetConc = int(input("Target concentration (1-200ug/mL): "))

    neatVol = int(input("Volume for neat transfers (75-200uL): "))

    inputFile = "C:\codeBASE\Lynx\input_for_dil_sol_files.csv"
else:
    #Final Plate concentration (units = ug/mL) (required input)
    targetConc = input("Final plate concentration?")

##########################################################


#trim down the octet output file into 4 plate list
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

for i in range(0,96):
    myQuant = octetQuants[i]
    plate1.append(myQuant)
for i in range(96,192):
    myQuant = octetQuants[i]
    plate2.append(myQuant)
for i in range(192,288):
    myQuant = octetQuants[i]
    plate3.append(myQuant)
for i in range(288,384):
    myQuant = octetQuants[i]
    plate4.append(myQuant)
################################################


#functions to handel data inflow and parameters entered by user
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

def volListCreation(plateNum, targetConc, targetVol, neatVol, supVolList, dilVolList):
    for i in plateNum:
        quantConc = i
        quantConc = float(quantConc)
        supVol = supCalc(targetConc, targetVol, quantConc, neatVol)
        dilVol = 100 - supVol
        dilVol = round(dilVol, 2)
        supVolList.append(str(supVol))
        dilVolList.append(str(dilVol))

def inputCSVFileWriter(supWriteToLocation, dilWriteToLocation, supLst, dilLst):
    with open(supWriteToLocation, "w") as SUP:
        writer = SUP.write
        plateFormatFileWriter(writer, supLst)

    with open(dilWriteToLocation, "w") as DIL:
        writer = DIL.write
        plateFormatFileWriter(writer, dilLst)
################################################

#edited from orginal to no longer look at file but rather consume list made via python
supVolListPlate1 = []
dilVolListPlate1 = []
supVolListPlate2 = []
dilVolListPlate2 = []
supVolListPlate3 = []
dilVolListPlate3 = []
supVolListPlate4 = []
dilVolListPlate4 = []

volListCreation(plate1, targetConc, targetVol, neatVol, supVolListPlate1, dilVolListPlate1)
volListCreation(plate2, targetConc, targetVol, neatVol, supVolListPlate2, dilVolListPlate2)
volListCreation(plate3, targetConc, targetVol, neatVol, supVolListPlate3, dilVolListPlate3)
volListCreation(plate4, targetConc, targetVol, neatVol, supVolListPlate4, dilVolListPlate4)

# print(len(supVolListPlate1))
# print(len(dilVolListPlate1))
# print(len(supVolListPlate2))
# print(len(dilVolListPlate2))
# print(len(supVolListPlate3))
# print(len(dilVolListPlate3))
# print(len(supVolListPlate4))
# print(len(dilVolListPlate4))

SupCSVInputP1 = "C:\codeBASE\Lynx\output_Test_files\SupCSVInputP1_" + time + ".csv"
DilCSVInputP1 =  "C:\codeBASE\Lynx\output_Test_files\DilCSVInputP1_" + time + ".csv"
SupCSVInputP2 = "C:\codeBASE\Lynx\output_Test_files\SupCSVInputP2_" + time + ".csv"
DilCSVInputP2 =  "C:\codeBASE\Lynx\output_Test_files\DilCSVInputP2_" + time + ".csv"
SupCSVInputP3 = "C:\codeBASE\Lynx\output_Test_files\SupCSVInputP3_" + time + ".csv"
DilCSVInputP3 =  "C:\codeBASE\Lynx\output_Test_files\DilCSVInputP3_" + time + ".csv"
SupCSVInputP4 = "C:\codeBASE\Lynx\output_Test_files\SupCSVInputP4_" + time + ".csv"
DilCSVInputP4 =  "C:\codeBASE\Lynx\output_Test_files\DilCSVInputP4_" + time + ".csv"

inputCSVFileWriter(SupCSVInputP1, DilCSVInputP1, supVolListPlate1, dilVolListPlate1)
inputCSVFileWriter(SupCSVInputP2, DilCSVInputP2, supVolListPlate2, dilVolListPlate2)
inputCSVFileWriter(SupCSVInputP3, DilCSVInputP3, supVolListPlate3, dilVolListPlate3)
inputCSVFileWriter(SupCSVInputP4, DilCSVInputP4, supVolListPlate4, dilVolListPlate4)

if fileBasedNorm == True:
    data = {
        "sourceTypeSelected" : sourceTypeSelected,
        "desTypeSelected" : desTypeSelected,
        "tipTypeSelected" : tipTypeSelected,
        "numberOfPlates" : numberOfPlates,
        "fileBasedNorm" : fileBasedNorm,
        "normSup1" : SupCSVInputP1,
        "normDil1" : DilCSVInputP1,
        "normSup2" : SupCSVInputP2,
        "normDil2" : DilCSVInputP2,
        "normSup3" : SupCSVInputP3,
        "normDil3" : DilCSVInputP3,
        "normSup4" : SupCSVInputP4,
        "normDil4" : DilCSVInputP4,
        "targetConc" : targetConc,
        "bCreateEcho" : bCreateEcho,
        "bMix" : bMix,
        "intMixHeightOffset" : intMixHeightOffset,
        "mixVol" : mixVol,
        "worktableCustomPath" : worktableCustomPath
    }

else:
    data = {
        "sourceTypeSelected" : sourceTypeSelected,
        "desTypeSelected" : desTypeSelected,
        "tipTypeSelected" : tipTypeSelected,
        "numberOfPlates" : numberOfPlates,
        "fileBasedNorm" : fileBasedNorm,
        "targetConc" : targetConc,
        "bCreateEcho" : bCreateEcho,
        "bMix" : bMix,
        "intMixHeightOffset" : intMixHeightOffset,
        "mixVol" : mixVol,
        "worktableCustomPath" : worktableCustomPath
    }


csvOutputFilePath = "C:\codeBASE\Lynx\output_Test_files\inputForMachine_" + time + ".csv"

print(csvOutputFilePath)

with open (csvOutputFilePath, 'w', encoding='UTF8', newline='') as f:
    w = csv.DictWriter(f, data.keys())
    w.writeheader()
    w.writerow(data)

#lynxGUIMasterLogic.py