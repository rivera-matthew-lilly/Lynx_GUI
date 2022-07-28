from datetime import datetime
import csv

time = str(datetime.now())
time = time.replace(" ", "_")
time = time.replace("-", ".")
time = time.replace(":", ".")
#user parameters selection, ideally a drop down with select choices
#source plate (drop down choices: "96MasterBlock", "96PCR") (required input)
sourceTypeSelected = input("Select source plate type: ")
#destination plate (drop down choices: "96Flatbottom", "96PCR", "96MasterBlock") (required input)
desTypeSelected = input("Select destination plate type: ")
#tip type (drop down choices: "340F", "1250F") (required input)
tipTypeSelected = input("Select tip type: ")
#number of plates to be ran (numerical choices: 1-4) (required input)
numberOfPlates = int(input("Enter Number of source plates to normalize: "))
#numberOfPlates = int(numberOfPlates)
#ask user if files are to bee uploaded (radio button: True/False)
fileBasedNorm = bool(input("Is this a file based normalizaton ('true' or 'false')?: "))
#fileBasedNorm = bool(fileBasedNorm)

#intializing variables
normDil1 = ""
normSup1 = ""
normDil2 = ""
normSup2 = ""
normDil3 = ""
normSup3 = ""
normDil4 = ""
normSup4 = ""
targetConc = ""
#if file based normalization:
#csv file input (string open dialoge) (required input)
if fileBasedNorm:
    if numberOfPlates == 1:
        normDil1 = input("Select Plate 1 Diluent file: ")
        normSup1 = input("Select Plate 1 Supernatant file: ")
    elif numberOfPlates == 2:
        normDil1 = input("Select Plate 1 Diluent file: ")
        normSup1 = input("Select Plate 1 Supernatant file: ")
        normDil2 = input("Select Plate 2 Diluent file: ")
        normSup2 = input("Select Plate 2 Supernatant file: ")
    elif numberOfPlates == 3:
        normDil1 = input("Select Plate 1 Diluent file: ")
        normSup1 = input("Select Plate 1 Supernatant file: ")
        normDil2 = input("Select Plate 2 Diluent file: ")
        normSup2 = input("Select Plate 2 Supernatant file: ")
        normDil3 = input("Select Plate 3 Diluent file: ")
        normSup3 = input("Select Plate 3 Supernatant file: ")
    else:
        normDil1 = input("Select Plate 1 Diluent file: ")
        normSup1 = input("Select Plate 1 Supernatant file: ")
        normDil2 = input("Select Plate 2 Diluent file: ")
        normSup2 = input("Select Plate 2 Supernatant file: ")
        normDil3 = input("Select Plate 3 Diluent file: ")
        normSup3 = input("Select Plate 3 Supernatant file: ")
        normDil4 = input("Select Plate 4 Diluent file: ")
        normSup4 = input("Select Plate 4 Supernatant file: ")
else:
    #if not file based normalization:
    #Final Plate concentration (units = ug/mL) (required input)
    targetConc = input("Final plate concentration?")

#ask user if normalized samples need to be transfer to Echo plate
bCreateEcho = bool(input("Transfer to Echo plate ('true' or 'false')?: "))

#advanced settings
#ask user if they want to mix (defualt = yes/true)
bMix = input("Mix plates (8 cycles) after normalization ('yes' or 'no')?: ")


#ask user to dded mix height offset variable - numerical choice (default = 1.0 mm) (min = 0.0 mm max=5.0 mm) (increment by 0.1 mm)
intMixHeightOffset = int(input("Mixing height offset (Default 1mm)?: "))
#intMixHeightOffset = int(intMixHeightOffset)

#ask user for mix volume (min = 0uL max = 150uL)
mixVol = int(input("Mix Volume (Defualt 100ul)?: "))

#build worktable path
worktableDefaultPath = "C:\MethodManager4\Workspaces\LO507\Methods\Production\Worktables\\"
worktableCustomPath = (worktableDefaultPath + tipTypeSelected + "_" + sourceTypeSelected + "_" + desTypeSelected + ".worktable.Lynx.Left.worktable")

print(worktableCustomPath)

data = {
    "sourceTypeSelected" : sourceTypeSelected,
    "desTypeSelected" : desTypeSelected,
    "tipTypeSelected" : tipTypeSelected,
    "numberOfPlates" : numberOfPlates,
    "fileBasedNorm" : fileBasedNorm,
    "normDil1" : normDil1,
    "normSup1" : normSup1,
    "normDil2" : normDil2,
    "normSup2" : normSup2,
    "normDil3" : normDil3,
    "normSup3" : normSup3,
    "normDil4" : normDil4,
    "normSup4" : normSup4,
    "targetConc" : targetConc,
    "bCreateEcho" : bCreateEcho,
    "bMix" : bMix,
    "intMixHeightOffset" : intMixHeightOffset,
    "mixVol" : mixVol,
    "worktableCustomPath" : worktableCustomPath
}
#build outputfile path
csvOutputFilePath = "C:\codeBASE\output_Test_files\output_" + time + ".csv"

print(csvOutputFilePath)

with open (csvOutputFilePath, 'w', encoding='UTF8', newline='') as f:
    w = csv.DictWriter(f, data.keys())
    w.writeheader()
    w.writerow(data)

    
