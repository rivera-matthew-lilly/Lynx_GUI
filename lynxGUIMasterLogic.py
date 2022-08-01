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
#ask user if normalized samples need to be transfer to Echo plate
bCreateEcho = input("Transfer to Echo plate ('yes' or 'no')?: ")
#ask user if files are to bee uploaded (radio button: True/False)
fileBasedNorm = input("Is this a file based normalizaton ('yes' or 'no')?: ")

if fileBasedNorm == "yes":
    targetVol = int(input("Target volume (100-200uL): "))

    targetConc = int(input("Target concentration (1-200ug/mL): "))

    neatVol = int(input("Volume for neat transfers (75-200uL): "))
else:
    #Final Plate concentration (units = ug/mL) (required input)
    targetConc = input("Final plate concentration?")

advancedVariables = input("Would you like to adjust advanced settings ('yes' or 'no)?: ")

if advancedVariables == "yes":
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

##########################################################

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

    aplhaList = ["A", "B", "C", "D", "E", "F", "G", "H"]
    for i in range(0, 8):
        writer("\n")
        writer(aplhaList[i])
        for j in range(i, 96, 8):
            writer("," + lst[j])


def volListCreation(plateNum, targetConc, targetVol, neatVol, supVolList, dilVolList):
    for i in plateNum:
        quantConc = i
        quantConc = float(quantConc)
        supVol = supCalc(targetConc, targetVol, quantConc, neatVol)
        dilVol = targetVol - supVol
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

#trim down the octet output file into 4 plate list
# octetFilePath = "C:\codeBASE\Lynx\octet_results_sheet.csv"
# #"C:\codeBASE\Lynx\octet_report"
# octetPlateCount = 4
# plate1of4 = ["A1", "A3", "A5", "A7", "A9", "A11", "A13", "A15", "A17", "A19", "A21", "A23", "C1", "C3", "C5", "C7", "C9", "C11", "C13", "C15", "C17", "C19", "C21", "C23", "E1", "E3", "E5", "E7", "E9", "E11", "E13", "E15", "E17", "E19", "E21", "E23", "G1", "G3", "G5", "G7", "G9", "G11", "G13", "G15", "G17", "G19", "G21", "G23", "I1", "I3", "I5", "I7", "I9", "I11", "I13", "I15", "I17", "I19", "I21", "I23", "K1", "K3", "K5", "K7", "K9", "K11", "K13", "K15", "K17", "K19", "K21", "K23", "M1", "M3", "M5", "M7", "M9", "M11", "M13", "M15", "M17", "M19", "M21", "M23", "O1", "O3", "O5", "O7", "O9", "O11", "O13", "O15", "O17", "O19", "O21", "O23"]
# plate2of4 = ["A2", "A4", "A6", "A8", "A10", "A12", "A14", "A16", "A18", "A20", "A22", "A24", "C2", "C4", "C6", "C8", "C10", "C12", "C14", "C16", "C18", "C20", "C22", "C24", "E2", "E4", "E6", "E8", "E10", "E12", "E14", "E16", "E18", "E20", "E22", "E24", "G2", "G4", "G6", "G8", "G10", "G12", "G14", "G16", "G18", "G20", "G22", "G24", "I2", "I4", "I6", "I8", "I10", "I12", "I14", "I16", "I18", "I20", "I22", "I24", "K2", "K4", "K6", "K8", "K10", "K12", "K14", "K16", "K18", "K20", "K22", "K24", "M2", "M4", "M6", "M8", "M10", "M12", "M14", "M16", "M18", "M20", "M22", "M24", "O2", "O4", "O6", "O8", "O10", "O12", "O14", "O16", "O18", "O20", "O22", "O24"]
# plate3of4 = ["B1", "B3", "B5", "B7", "B9", "B11", "B13", "B15", "B17", "B19", "B21", "B23", "D1", "D3", "D5", "D7", "D9", "D11", "D13", "D15", "D17", "D19", "D21", "D23", "F1", "F3", "F5", "F7", "F9", "F11", "F13", "F15", "F17", "F19", "F21", "F23", "H1", "H3", "H5", "H7", "H9", "H11", "H13", "H15", "H17", "H19", "H21", "H23", "J1", "J3", "J5", "J7", "J9", "J11", "J13", "J15", "J17", "J19", "J21", "J23", "L1", "L3", "L5", "L7", "L9", "L11", "L13", "L15", "L17", "L19", "L21", "L23", "N1", "N3", "N5", "N7", "N9", "N11", "N13", "N15", "N17", "N19", "N21", "N23", "P1", "P3", "P5", "P7", "P9", "P11", "P13", "P15", "P17", "P19", "P21", "P23"]
# plate4of4 = ["B2", "B4", "B6", "B8", "B10", "B12", "B14", "B16", "B18", "B20", "B22", "B24", "D2", "D4", "D6", "D8", "D10", "D12", "D14", "D16", "D18", "D20", "D22", "D24", "F2", "F4", "F6", "F8", "F10", "F12", "F14", "F16", "F18", "F20", "F22", "F24", "H2", "H4", "H6", "H8", "H10", "H12", "H14", "H16", "H18", "H20", "H22", "H24", "J2", "J4", "J6", "J8", "J10", "J12", "J14", "J16", "J18", "J20", "J22", "J24", "L2", "L4", "L6", "L8", "L10", "L12", "L14", "L16", "L18", "L20", "L22", "L24", "N2", "N4", "N6", "N8", "N10", "N12", "N14", "N16", "N18", "N20", "N22", "N24", "P2", "P4", "P6", "P8", "P10", "P12", "P14", "P16", "P18", "P20", "P22", "P24"]


# octetQuants = []
# with open(octetFilePath, "r") as f:
#     file_reader = reader(f)
#     counter = 0
#     lines = (96 * numberOfPlates) + 1
#     for i in file_reader:
#         if counter != 0 and counter < lines:
#             wellId = i[5]
#             octetConc = i[12]
#             counter = counter + 1
#             if wellId in plate1of4:
#                 octetQuants.append(octetConc)
#         else:
#             counter = counter + 1

# print(octetQuants)

################################################
# #testing a function type for the below quant data sepration - THIS IS TH WORKING NEW FUNCTION
octetFilePath = "C:\codeBASE\Lynx\octet_results_sheet_randomized.csv"

plate1of4 = ["A1", "A3", "A5", "A7", "A9", "A11", "A13", "A15", "A17", "A19", "A21", "A23", "C1", "C3", "C5", "C7", "C9", "C11", "C13", "C15", "C17", "C19", "C21", "C23", "E1", "E3", "E5", "E7", "E9", "E11", "E13", "E15", "E17", "E19", "E21", "E23", "G1", "G3", "G5", "G7", "G9", "G11", "G13", "G15", "G17", "G19", "G21", "G23", "I1", "I3", "I5", "I7", "I9", "I11", "I13", "I15", "I17", "I19", "I21", "I23", "K1", "K3", "K5", "K7", "K9", "K11", "K13", "K15", "K17", "K19", "K21", "K23", "M1", "M3", "M5", "M7", "M9", "M11", "M13", "M15", "M17", "M19", "M21", "M23", "O1", "O3", "O5", "O7", "O9", "O11", "O13", "O15", "O17", "O19", "O21", "O23"]
plate2of4 = ["A2", "A4", "A6", "A8", "A10", "A12", "A14", "A16", "A18", "A20", "A22", "A24", "C2", "C4", "C6", "C8", "C10", "C12", "C14", "C16", "C18", "C20", "C22", "C24", "E2", "E4", "E6", "E8", "E10", "E12", "E14", "E16", "E18", "E20", "E22", "E24", "G2", "G4", "G6", "G8", "G10", "G12", "G14", "G16", "G18", "G20", "G22", "G24", "I2", "I4", "I6", "I8", "I10", "I12", "I14", "I16", "I18", "I20", "I22", "I24", "K2", "K4", "K6", "K8", "K10", "K12", "K14", "K16", "K18", "K20", "K22", "K24", "M2", "M4", "M6", "M8", "M10", "M12", "M14", "M16", "M18", "M20", "M22", "M24", "O2", "O4", "O6", "O8", "O10", "O12", "O14", "O16", "O18", "O20", "O22", "O24"]
plate3of4 = ["B1", "B3", "B5", "B7", "B9", "B11", "B13", "B15", "B17", "B19", "B21", "B23", "D1", "D3", "D5", "D7", "D9", "D11", "D13", "D15", "D17", "D19", "D21", "D23", "F1", "F3", "F5", "F7", "F9", "F11", "F13", "F15", "F17", "F19", "F21", "F23", "H1", "H3", "H5", "H7", "H9", "H11", "H13", "H15", "H17", "H19", "H21", "H23", "J1", "J3", "J5", "J7", "J9", "J11", "J13", "J15", "J17", "J19", "J21", "J23", "L1", "L3", "L5", "L7", "L9", "L11", "L13", "L15", "L17", "L19", "L21", "L23", "N1", "N3", "N5", "N7", "N9", "N11", "N13", "N15", "N17", "N19", "N21", "N23", "P1", "P3", "P5", "P7", "P9", "P11", "P13", "P15", "P17", "P19", "P21", "P23"]
plate4of4 = ["B2", "B4", "B6", "B8", "B10", "B12", "B14", "B16", "B18", "B20", "B22", "B24", "D2", "D4", "D6", "D8", "D10", "D12", "D14", "D16", "D18", "D20", "D22", "D24", "F2", "F4", "F6", "F8", "F10", "F12", "F14", "F16", "F18", "F20", "F22", "F24", "H2", "H4", "H6", "H8", "H10", "H12", "H14", "H16", "H18", "H20", "H22", "H24", "J2", "J4", "J6", "J8", "J10", "J12", "J14", "J16", "J18", "J20", "J22", "J24", "L2", "L4", "L6", "L8", "L10", "L12", "L14", "L16", "L18", "L20", "L22", "L24", "N2", "N4", "N6", "N8", "N10", "N12", "N14", "N16", "N18", "N20", "N22", "N24", "P2", "P4", "P6", "P8", "P10", "P12", "P14", "P16", "P18", "P20", "P22", "P24"]


#dictornary to hold well id and quant value
octetQuantsDict_Quad1 = {}
octetQuantsDict_Quad2 = {}
octetQuantsDict_Quad3 = {}
octetQuantsDict_Quad4 = {}

#reads incoming octet raw file and capture well id and qant value into a dictionary based on the quad of the 384 well plate the well id is in
with open(octetFilePath, "r") as f:
    file_reader = reader(f)
    counter = 0
    lines = (96 * numberOfPlates) + 1
    for i in file_reader:
        if counter != 0: 
            wellID = i[5]
            octetConc = i[12]
            counter = counter + 1
            if wellID in plate1of4:
                octetQuantsDict_Quad1[wellID] = octetConc
            if wellID in plate2of4:
                octetQuantsDict_Quad2[wellID] = octetConc
            if wellID in plate3of4:
                octetQuantsDict_Quad3[wellID] = octetConc
            if wellID in plate4of4:
                octetQuantsDict_Quad4[wellID] = octetConc
        else:
            counter = counter + 1

#adds dictoary values quant value) to the octetQuants_Quad list based on strict order of the plate#of# list struct
def quantListCreator(dict, read_lst, write_lst):
    counter = 0
    while counter < 96:
        for key, value in dict.items():
            if key == read_lst[counter]:
                write_lst.append(value)
                counter += 1

########################################################
########################################################

if numberOfPlates >= 1:

    octetQuants_Quad1 = []
    quantListCreator(octetQuantsDict_Quad1, plate1of4, octetQuants_Quad1)

    supVolListPlate1 = []
    dilVolListPlate1 = []
    volListCreation(octetQuants_Quad1, targetConc, targetVol, neatVol, supVolListPlate1, dilVolListPlate1)

    SupCSVInputP1 = "C:\codeBASE\Lynx\output_Test_files\SupCSVInputP1_" + time + ".csv"
    DilCSVInputP1 =  "C:\codeBASE\Lynx\output_Test_files\DilCSVInputP1_" + time + ".csv"
    inputCSVFileWriter(SupCSVInputP1, DilCSVInputP1, supVolListPlate1, dilVolListPlate1)

if numberOfPlates >= 2:


    octetQuants_Quad2 = []
    quantListCreator(octetQuantsDict_Quad2, plate2of4, octetQuants_Quad2)

    supVolListPlate2 = []
    dilVolListPlate2 = []
    volListCreation(octetQuants_Quad2, targetConc, targetVol, neatVol, supVolListPlate2, dilVolListPlate2)

    SupCSVInputP2 = "C:\codeBASE\Lynx\output_Test_files\SupCSVInputP2_" + time + ".csv"
    DilCSVInputP2 =  "C:\codeBASE\Lynx\output_Test_files\DilCSVInputP2_" + time + ".csv"
    inputCSVFileWriter(SupCSVInputP2, DilCSVInputP2, supVolListPlate2, dilVolListPlate2)

if numberOfPlates >= 3:


    octetQuants_Quad3 = []
    quantListCreator(octetQuantsDict_Quad3, plate3of4, octetQuants_Quad3)

    supVolListPlate3 = []
    dilVolListPlate3 = []
    volListCreation(octetQuants_Quad3, targetConc, targetVol, neatVol, supVolListPlate3, dilVolListPlate3)

    SupCSVInputP3 = "C:\codeBASE\Lynx\output_Test_files\SupCSVInputP3_" + time + ".csv"
    DilCSVInputP3 =  "C:\codeBASE\Lynx\output_Test_files\DilCSVInputP3_" + time + ".csv"
    inputCSVFileWriter(SupCSVInputP3, DilCSVInputP3, supVolListPlate3, dilVolListPlate3)

if numberOfPlates >= 4:

    octetQuants_Quad4 = []
    quantListCreator(octetQuantsDict_Quad4, plate4of4, octetQuants_Quad4)

    supVolListPlate4 = []
    dilVolListPlate4 = []
    volListCreation(octetQuants_Quad4, targetConc, targetVol, neatVol, supVolListPlate4, dilVolListPlate4)

    SupCSVInputP4 = "C:\codeBASE\Lynx\output_Test_files\SupCSVInputP4_" + time + ".csv"
    DilCSVInputP4 =  "C:\codeBASE\Lynx\output_Test_files\DilCSVInputP4_" + time + ".csv"
    inputCSVFileWriter(SupCSVInputP4, DilCSVInputP4, supVolListPlate4, dilVolListPlate4)


#build worktable path
worktableDefaultPath = "C:\MethodManager4\Workspaces\LO507\Methods\Production\Worktables\\"
worktableCustomPath = (worktableDefaultPath + tipTypeSelected + "_" + sourceTypeSelected + "_" + desTypeSelected + ".worktable.Lynx.Left.worktable")

if fileBasedNorm == "yes":
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
        "worktableCustomPath" : worktableCustomPath,
        "normSup1" : SupCSVInputP1,
        "normDil1" : DilCSVInputP1,
        "normSup2" : SupCSVInputP2,
        "normDil2" : DilCSVInputP2,
        "normSup3" : SupCSVInputP3,
        "normDil3" : DilCSVInputP3,
        "normSup4" : SupCSVInputP4,
        "normDil4" : DilCSVInputP4,
        # "normSup5" : SupCSVInputP1,
        # "normDil5" : DilCSVInputP1,
        # "normSup6" : SupCSVInputP2,
        # "normDil6" : DilCSVInputP2,
        # "normSup7" : SupCSVInputP3,
        # "normDil7" : DilCSVInputP3,
        # "normSup8" : SupCSVInputP4,
        # "normDil8" : DilCSVInputP4,
        # "normSup9" : SupCSVInputP1,
        # "normDil9" : DilCSVInputP1,
        # "normSup10" : SupCSVInputP2,
        # "normDil10" : DilCSVInputP2,
        # "normSup11" : SupCSVInputP3,
        # "normDil11" : DilCSVInputP3,
        # "normSup12" : SupCSVInputP4,
        # "normDil12" : DilCSVInputP4,
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


recordInputFile = "C:\codeBASE\Lynx\output_Test_files\ELI_inputFileRecord" + time + ".txt"

with open (recordInputFile, 'w', encoding='UTF8', newline='') as f:
    for key, value in data.items(): 
        f.write('%s:%s\n' % (key, value))


inputEliFile = "C:\codeBASE\Lynx\output_Test_files\ELI_inputFile.txt"

with open (inputEliFile, 'w', encoding='UTF8', newline='') as f:
    for key, value in data.items(): 
        f.write('%s\n' % (value))


#lynxGUIMasterLogic.py