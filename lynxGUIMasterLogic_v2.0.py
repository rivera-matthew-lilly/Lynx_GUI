from csv import reader
import csv
from datetime import datetime
from testingPlatesAsObjects import NormPlate, QuantPlate
from lynxGUIFunctions import userInputForNorm, userInputForQuant
import os

#time management
time = str(datetime.now())
time = time.replace(" ", "_")
time = time.replace("-", ".")
time = time.replace(":", ".")

#final write to path creation
if not os.path.isdir("C:\codeBASE\Lynx\output_Test_files\Lynx_Input_" + time):
    os.mkdir("C:\codeBASE\Lynx\output_Test_files\Lynx_Input_" + time)

#run user input functions
octetPlateCount, octetFilePath1, octetFilePath2, octetFilePath3 = userInputForQuant()
sourceTypeSelected, desTypeSelected, tipTypeSelected, numberOfPlates, bCreateEcho, fileBasedNorm, targetVol, targetConc, neatVol, bMix, intMixHeightOffset, mixVol = userInputForNorm()
#build worktable path  
worktableDefaultPath = "C:\MethodManager4\Workspaces\LO507\Methods\Production\Worktables\\"
worktableCustomPath = (worktableDefaultPath + tipTypeSelected + "_" + sourceTypeSelected + "_" + desTypeSelected + ".worktable.Lynx.Left.worktable")
print(worktableCustomPath)

lynxParametersDict = {
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

#QuantPlate Object --->__init__(self, plateNum, octetFilePath):
quantPlateObjectList = []
normPlateObjectList = []
if octetPlateCount >= 1:
    quantPlate1 = QuantPlate("QuantPlate1", octetFilePath1)
    quantPlateObjectList.append(quantPlate1)
    quantPlate1.masterQuantParser()

    #quant plat 1 & norm plate 1
    quantsPlate1_Quad1 = quantPlate1.getOctetQuants_Quad1()
    normPlate1 = NormPlate("NormPlate1", targetConc, targetVol, neatVol)
    normPlateObjectList.append(normPlate1)
    normPlate1.volListCreation(quantsPlate1_Quad1)
    normPlate1.inputCSVFileWriter()
    normPlate1_CSVSupFilePath = normPlate1.getSupCSVInput()
    normPlate1_CSVDilFilePath = normPlate1.getDilCSVInput()
    lynxParametersDict["normSup1"] = normPlate1_CSVSupFilePath
    lynxParametersDict["normDil1"] = normPlate1_CSVDilFilePath

    #quant plat 1 & norm plate 2
    quantsPlate1_Quad2 = quantPlate1.getOctetQuants_Quad2()
    normPlate2 = NormPlate("NormPlate2", targetConc, targetVol, neatVol)
    normPlateObjectList.append(normPlate2)
    normPlate2.volListCreation(quantsPlate1_Quad2)
    normPlate2.inputCSVFileWriter()
    normPlate2_CSVSupFilePath = normPlate2.getSupCSVInput()
    normPlate2_CSVDilFilePath = normPlate2.getDilCSVInput()
    lynxParametersDict["normSup2"] = normPlate2_CSVSupFilePath
    lynxParametersDict["normDil2"] = normPlate2_CSVDilFilePath

    #quant plat 1 & norm plate 3
    quantsPlate1_Quad3 = quantPlate1.getOctetQuants_Quad3()
    normPlate3 = NormPlate("NormPlate3", targetConc, targetVol, neatVol)
    normPlateObjectList.append(normPlate3)
    normPlate3.volListCreation(quantsPlate1_Quad3)
    normPlate3.inputCSVFileWriter()
    normPlate3_CSVSupFilePath = normPlate3.getSupCSVInput()
    normPlate3_CSVDilFilePath = normPlate3.getDilCSVInput()
    lynxParametersDict["normSup3"] = normPlate3_CSVSupFilePath
    lynxParametersDict["normDil3"] = normPlate3_CSVDilFilePath

    #quant plat 1 & norm plate 4
    quantsPlate1_Quad4 = quantPlate1.getOctetQuants_Quad4()
    normPlate4 = NormPlate("NormPlate4", targetConc, targetVol, neatVol)
    normPlateObjectList.append(normPlate4)
    normPlate4.volListCreation(quantsPlate1_Quad4)
    normPlate4.inputCSVFileWriter()
    normPlate4_CSVSupFilePath = normPlate4.getSupCSVInput()
    normPlate4_CSVDilFilePath = normPlate4.getDilCSVInput()
    lynxParametersDict["normSup4"] = normPlate4_CSVSupFilePath
    lynxParametersDict["normDil4"] = normPlate4_CSVDilFilePath

if octetPlateCount >= 2:
    plate2 = QuantPlate("QuantPlate2", octetFilePath2)
    quantPlateObjectList.append(plate2)
    plate2.masterQuantParser()

    #quant plat 2 & norm plate 1
    quantsPlate2_Quad1 = plate2.getOctetQuants_Quad1()
    normPlate5 = NormPlate("NormPlate5", targetConc, targetVol, neatVol)
    normPlateObjectList.append(normPlate5)
    normPlate5.volListCreation(quantsPlate2_Quad1)
    normPlate5.inputCSVFileWriter()
    normPlate5_CSVSupFilePath = normPlate5.getSupCSVInput()
    normPlate5_CSVDilFilePath = normPlate5.getDilCSVInput()
    lynxParametersDict["normSup5"] = normPlate5_CSVSupFilePath
    lynxParametersDict["normDil5"] = normPlate5_CSVDilFilePath

    #quant plat 2 & norm plate 2
    quantsPlate2_Quad2 = plate2.getOctetQuants_Quad2()
    normPlate6 = NormPlate("NormPlate6", targetConc, targetVol, neatVol)
    normPlateObjectList.append(normPlate6)
    normPlate6.volListCreation(quantsPlate2_Quad2)
    normPlate6.inputCSVFileWriter()
    normPlate6_CSVSupFilePath = normPlate6.getSupCSVInput()
    normPlate6_CSVDilFilePath = normPlate6.getDilCSVInput() 
    lynxParametersDict["normSup6"] = normPlate6_CSVSupFilePath
    lynxParametersDict["normDil6"] = normPlate6_CSVDilFilePath

    #quant plat 2 & norm plate 3
    quantsPlate2_Quad3 = plate2.getOctetQuants_Quad3()
    normPlate7 = NormPlate("NormPlate7", targetConc, targetVol, neatVol)
    normPlateObjectList.append(normPlate7)
    normPlate7.volListCreation(quantsPlate2_Quad3)
    normPlate7.inputCSVFileWriter()
    normPlate7_CSVSupFilePath = normPlate7.getSupCSVInput()
    normPlate7_CSVDilFilePath = normPlate7.getDilCSVInput()
    lynxParametersDict["normSup7"] = normPlate7_CSVSupFilePath
    lynxParametersDict["normDil7"] = normPlate7_CSVDilFilePath

    #quant plat 2 & norm plate 4
    quantsPlate2_Quad4 = plate2.getOctetQuants_Quad4()
    normPlate8 = NormPlate("NormPlate8", targetConc, targetVol, neatVol)
    normPlateObjectList.append(normPlate8)
    normPlate8.volListCreation(quantsPlate2_Quad4)
    normPlate8.inputCSVFileWriter()
    normPlate8_CSVSupFilePath = normPlate8.getSupCSVInput()
    normPlate8_CSVDilFilePath = normPlate8.getDilCSVInput()  
    lynxParametersDict["normSup8"] = normPlate8_CSVSupFilePath
    lynxParametersDict["normDil8"] = normPlate8_CSVDilFilePath  

if octetPlateCount >=3:
    plate3 = QuantPlate("QuantPlate3", octetFilePath3)
    quantPlateObjectList.append(plate3)
    plate3.masterQuantParser()

    #quant plat 3 & norm plate 1
    quantsPlate3_Quad1 = plate3.getOctetQuants_Quad1()
    normPlate9 = NormPlate("NormPlate9", targetConc, targetVol, neatVol)
    normPlateObjectList.append(normPlate9)
    normPlate9.volListCreation(quantsPlate3_Quad1)
    normPlate9.inputCSVFileWriter()
    normPlate9_CSVSupFilePath = normPlate9.getSupCSVInput()
    normPlate9_CSVDilFilePath = normPlate9.getDilCSVInput()
    lynxParametersDict["normSup9"] = normPlate9_CSVSupFilePath
    lynxParametersDict["normDil9"] = normPlate9_CSVDilFilePath

    #quant plat 3 & norm plate 2
    quantsPlate3_Quad2 = plate3.getOctetQuants_Quad2()
    normPlate10 = NormPlate("NormPlate10", targetConc, targetVol, neatVol)
    normPlateObjectList.append(normPlate10)
    normPlate10.volListCreation(quantsPlate3_Quad2)
    normPlate10.inputCSVFileWriter()
    normPlate10_CSVSupFilePath = normPlate10.getSupCSVInput()
    normPlate10_CSVDilFilePath = normPlate10.getDilCSVInput()
    lynxParametersDict["normSup10"] = normPlate10_CSVSupFilePath
    lynxParametersDict["normDil10"] = normPlate10_CSVDilFilePath

    #quant plat 3 & norm plate 3
    quantsPlate3_Quad3 = plate3.getOctetQuants_Quad3()
    normPlate11 = NormPlate("NormPlate11", targetConc, targetVol, neatVol)
    normPlateObjectList.append(normPlate11)
    normPlate11.volListCreation(quantsPlate3_Quad3)
    normPlate11.inputCSVFileWriter()
    normPlate11_CSVSupFilePath = normPlate11.getSupCSVInput()
    normPlate11_CSVDilFilePath = normPlate11.getDilCSVInput()
    lynxParametersDict["normSup11"] = normPlate11_CSVSupFilePath
    lynxParametersDict["normDil11"] = normPlate11_CSVDilFilePath

    #quant plat 3 & norm plate 4
    quantsPlate3_Quad4 = plate3.getOctetQuants_Quad4()
    normPlate12 = NormPlate("NormPlate12", targetConc, targetVol, neatVol)
    normPlateObjectList.append(normPlate12)
    normPlate12.volListCreation(quantsPlate3_Quad4)
    normPlate12.inputCSVFileWriter()
    normPlate12_CSVSupFilePath = normPlate12.getSupCSVInput()
    normPlate12_CSVDilFilePath = normPlate12.getDilCSVInput()
    lynxParametersDict["normSup12"] = normPlate12_CSVSupFilePath
    lynxParametersDict["normDil12"] = normPlate12_CSVDilFilePath

# for key, item in lynxParametersDict.items():
#     print(key + ": " + str(item))



recordInputFile = "C:\codeBASE\Lynx\output_Test_files\Lynx_Input_" + time + "\ELI_inputFileRecord" + time + ".txt"

with open (recordInputFile, 'w', encoding='UTF8', newline='') as f:
    for key, value in lynxParametersDict.items(): 
        f.write('%s:%s\n' % (key, value))


inputEliFile = "C:\codeBASE\Lynx\output_Test_files\Lynx_Input_" + time + "\ELI_inputFile.txt"

with open (inputEliFile, 'w', encoding='UTF8', newline='') as f:
    for key, value in lynxParametersDict.items(): 
        f.write('%s\n' % (value))


# print(len(normPlateObjectList))
#C:\codeBASE\Lynx\octet_results_sheet.csv
#"C:\codeBASE\Lynx\octet_results_sheet_4plate_testable.csv"
#lynxGUIMasterLogic_v2.0.py
