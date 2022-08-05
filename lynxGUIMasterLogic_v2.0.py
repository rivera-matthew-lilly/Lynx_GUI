from csv import reader
import csv
from datetime import datetime
from testingPlatesAsObjects import NormPlate, QuantPlate
from lynxGUIFunctions import userInputForNorm, userInputForQuant
import os

#time management
current_datetime = datetime.now()
time = current_datetime.strftime("%d.%m.%Y %H.%M.%S")
time = time.replace(" ", "_")
time = str(time)

#final write to path creation
if not os.path.isdir("C:\codeBASE\Lynx\output_Test_files\Lynx_Input_" + time):
    os.mkdir("C:\codeBASE\Lynx\output_Test_files\Lynx_Input_" + time)

#run user input functions
octetPlateCount, octetFilePath1, numberOfQuads_fromOctetPlate1, octetFilePath2, numberOfQuads_fromOctetPlate2, octetFilePath3, numberOfQuads_fromOctetPlate3 = userInputForQuant()
sourceTypeSelected, desTypeSelected, tipTypeSelected, numberOfPlates, bCreateEcho, fileBasedNorm, targetVol, targetConc, neatVol, bMix, intMixHeightOffset, mixVol = userInputForNorm()
#build worktable path  
worktableDefaultPath = "C:\MethodManager4\Workspaces\LO507\Methods\Production\Worktables\\"
worktableCustomPath = (worktableDefaultPath + "ManualNorm" + "_" + tipTypeSelected + "_" + sourceTypeSelected + "_" + desTypeSelected + ".worktable.Lynx.Left.worktable")
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
    quantPlate1 = QuantPlate("QuantPlate1", octetFilePath1, numberOfQuads_fromOctetPlate1)
    quantPlateObjectList.append(quantPlate1)
    quantPlate1.masterQuantParser()

    if numberOfQuads_fromOctetPlate1 >= 1:
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
        normSup1_Barcode = quantPlate1.octetBarcode + "_Sup_1"
        normDil1_Barcode = quantPlate1.octetBarcode + "_Dil_1"
        lynxParametersDict["normSup1_Barcode"] = normSup1_Barcode
        lynxParametersDict["normDil1_Barcode"] = normDil1_Barcode

    if numberOfQuads_fromOctetPlate1 >= 2:
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
        normSup2_Barcode = quantPlate1.octetBarcode + "_Sup_2"
        normDil2_Barcode = quantPlate1.octetBarcode + "_Dil_2"
        lynxParametersDict["normSup2_Barcode"] = normSup2_Barcode
        lynxParametersDict["normDil2_Barcode"] = normDil2_Barcode

    if numberOfQuads_fromOctetPlate1 >= 3:
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
        normSup3_Barcode = quantPlate1.octetBarcode + "_Sup_3"
        normDil3_Barcode = quantPlate1.octetBarcode + "_Dil_3"
        lynxParametersDict["normSup3_Barcode"] = normSup3_Barcode
        lynxParametersDict["normDil3_Barcode"] = normDil3_Barcode

    if numberOfQuads_fromOctetPlate1 >= 4:
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
        normSup4_Barcode = quantPlate1.octetBarcode + "_Sup_4"
        normDil4_Barcode = quantPlate1.octetBarcode + "_Dil_4"
        lynxParametersDict["normSup4_Barcode"] = normSup4_Barcode
        lynxParametersDict["normDil4_Barcode"] = normDil4_Barcode

if octetPlateCount >= 2:
    quantPlate2 = QuantPlate("QuantPlate2", octetFilePath2,numberOfQuads_fromOctetPlate2)
    quantPlateObjectList.append(quantPlate2)
    quantPlate2.masterQuantParser()

    if numberOfQuads_fromOctetPlate2 >= 1:
        #quant plat 2 & norm plate 1
        quantsPlate2_Quad1 = quantPlate2.getOctetQuants_Quad1()
        normPlate5 = NormPlate("NormPlate5", targetConc, targetVol, neatVol)
        normPlateObjectList.append(normPlate5)
        normPlate5.volListCreation(quantsPlate2_Quad1)
        normPlate5.inputCSVFileWriter()
        normPlate5_CSVSupFilePath = normPlate5.getSupCSVInput()
        normPlate5_CSVDilFilePath = normPlate5.getDilCSVInput()
        lynxParametersDict["normSup5"] = normPlate5_CSVSupFilePath
        lynxParametersDict["normDil5"] = normPlate5_CSVDilFilePath
        normSup5_Barcode = quantPlate2.octetBarcode + "_Sup_1"
        normDil5_Barcode = quantPlate2.octetBarcode + "_Dil_1"
        lynxParametersDict["normSup5_Barcode"] = normSup5_Barcode
        lynxParametersDict["normDil5_Barcode"] = normDil5_Barcode

    if numberOfQuads_fromOctetPlate2 >= 2:
        #quant plat 2 & norm plate 2
        quantsPlate2_Quad2 = quantPlate2.getOctetQuants_Quad2()
        normPlate6 = NormPlate("NormPlate6", targetConc, targetVol, neatVol)
        normPlateObjectList.append(normPlate6)
        normPlate6.volListCreation(quantsPlate2_Quad2)
        normPlate6.inputCSVFileWriter()
        normPlate6_CSVSupFilePath = normPlate6.getSupCSVInput()
        normPlate6_CSVDilFilePath = normPlate6.getDilCSVInput() 
        lynxParametersDict["normSup6"] = normPlate6_CSVSupFilePath
        lynxParametersDict["normDil6"] = normPlate6_CSVDilFilePath
        normSup6_Barcode = quantPlate2.octetBarcode + "_Sup_2"
        normDil6_Barcode = quantPlate2.octetBarcode + "_Dil_2"
        lynxParametersDict["normSup6_Barcode"] = normSup6_Barcode
        lynxParametersDict["normDil6_Barcode"] = normDil6_Barcode

    if numberOfQuads_fromOctetPlate2 >= 3:
        #quant plat 2 & norm plate 3
        quantsPlate2_Quad3 = quantPlate2.getOctetQuants_Quad3()
        normPlate7 = NormPlate("NormPlate7", targetConc, targetVol, neatVol)
        normPlateObjectList.append(normPlate7)
        normPlate7.volListCreation(quantsPlate2_Quad3)
        normPlate7.inputCSVFileWriter()
        normPlate7_CSVSupFilePath = normPlate7.getSupCSVInput()
        normPlate7_CSVDilFilePath = normPlate7.getDilCSVInput()
        lynxParametersDict["normSup7"] = normPlate7_CSVSupFilePath
        lynxParametersDict["normDil7"] = normPlate7_CSVDilFilePath
        normSup7_Barcode = quantPlate2.octetBarcode + "_Sup_3"
        normDil7_Barcode = quantPlate2.octetBarcode + "_Dil_3"
        lynxParametersDict["normSup7_Barcode"] = normSup7_Barcode
        lynxParametersDict["normDil7_Barcode"] = normDil7_Barcode

    if numberOfQuads_fromOctetPlate2 >= 4:
        #quant plat 2 & norm plate 4
        quantsPlate2_Quad4 = quantPlate2.getOctetQuants_Quad4()
        normPlate8 = NormPlate("NormPlate8", targetConc, targetVol, neatVol)
        normPlateObjectList.append(normPlate8)
        normPlate8.volListCreation(quantsPlate2_Quad4)
        normPlate8.inputCSVFileWriter()
        normPlate8_CSVSupFilePath = normPlate8.getSupCSVInput()
        normPlate8_CSVDilFilePath = normPlate8.getDilCSVInput()  
        lynxParametersDict["normSup8"] = normPlate8_CSVSupFilePath
        lynxParametersDict["normDil8"] = normPlate8_CSVDilFilePath
        normSup8_Barcode = quantPlate2.octetBarcode + "_Sup_4"
        normDil8_Barcode = quantPlate2.octetBarcode + "_Dil_4"
        lynxParametersDict["normSup8_Barcode"] = normSup8_Barcode
        lynxParametersDict["normDil8_Barcode"] = normDil8_Barcode

if octetPlateCount >=3:
    quantPlate3 = QuantPlate("QuantPlate3", octetFilePath3, numberOfQuads_fromOctetPlate3)
    quantPlateObjectList.append(quantPlate3)
    quantPlate3.masterQuantParser()

    if numberOfQuads_fromOctetPlate3 >= 1:
        #quant plat 3 & norm plate 1
        quantsPlate3_Quad1 = quantPlate3.getOctetQuants_Quad1()
        normPlate9 = NormPlate("NormPlate9", targetConc, targetVol, neatVol)
        normPlateObjectList.append(normPlate9)
        normPlate9.volListCreation(quantsPlate3_Quad1)
        normPlate9.inputCSVFileWriter()
        normPlate9_CSVSupFilePath = normPlate9.getSupCSVInput()
        normPlate9_CSVDilFilePath = normPlate9.getDilCSVInput()
        lynxParametersDict["normSup9"] = normPlate9_CSVSupFilePath
        lynxParametersDict["normDil9"] = normPlate9_CSVDilFilePath
        normSup9_Barcode = quantPlate3.octetBarcode + "_Sup_1"
        normDil9_Barcode = quantPlate3.octetBarcode + "_Dil_1"
        lynxParametersDict["normSup9_Barcode"] = normSup9_Barcode
        lynxParametersDict["normDil9_Barcode"] = normDil9_Barcode

    if numberOfQuads_fromOctetPlate3 >= 2:
        #quant plat 3 & norm plate 2
        quantsPlate3_Quad2 = quantPlate3.getOctetQuants_Quad2()
        normPlate10 = NormPlate("NormPlate10", targetConc, targetVol, neatVol)
        normPlateObjectList.append(normPlate10)
        normPlate10.volListCreation(quantsPlate3_Quad2)
        normPlate10.inputCSVFileWriter()
        normPlate10_CSVSupFilePath = normPlate10.getSupCSVInput()
        normPlate10_CSVDilFilePath = normPlate10.getDilCSVInput()
        lynxParametersDict["normSup10"] = normPlate10_CSVSupFilePath
        lynxParametersDict["normDil10"] = normPlate10_CSVDilFilePath
        normSup10_Barcode = quantPlate3.octetBarcode + "_Sup_2"
        normDil10_Barcode = quantPlate3.octetBarcode + "_Dil_2"
        lynxParametersDict["normSup10_Barcode"] = normSup10_Barcode
        lynxParametersDict["normDil10_Barcode"] = normDil10_Barcode

    if numberOfQuads_fromOctetPlate3 >= 3:
        #quant plat 3 & norm plate 3
        quantsPlate3_Quad3 = quantPlate3.getOctetQuants_Quad3()
        normPlate11 = NormPlate("NormPlate11", targetConc, targetVol, neatVol)
        normPlateObjectList.append(normPlate11)
        normPlate11.volListCreation(quantsPlate3_Quad3)
        normPlate11.inputCSVFileWriter()
        normPlate11_CSVSupFilePath = normPlate11.getSupCSVInput()
        normPlate11_CSVDilFilePath = normPlate11.getDilCSVInput()
        lynxParametersDict["normSup11"] = normPlate11_CSVSupFilePath
        lynxParametersDict["normDil11"] = normPlate11_CSVDilFilePath
        normSup11_Barcode = quantPlate3.octetBarcode + "_Sup_3"
        normDil11_Barcode = quantPlate3.octetBarcode + "_Dil_3"
        lynxParametersDict["normSup11_Barcode"] = normSup11_Barcode
        lynxParametersDict["normDil11_Barcode"] = normDil11_Barcode
        

    if numberOfQuads_fromOctetPlate3 >= 4:
        #quant plat 3 & norm plate 4
        quantsPlate3_Quad4 = quantPlate3.getOctetQuants_Quad4()
        normPlate12 = NormPlate("NormPlate12", targetConc, targetVol, neatVol)
        normPlateObjectList.append(normPlate12)
        normPlate12.volListCreation(quantsPlate3_Quad4)
        normPlate12.inputCSVFileWriter()
        normPlate12_CSVSupFilePath = normPlate12.getSupCSVInput()
        normPlate12_CSVDilFilePath = normPlate12.getDilCSVInput()
        lynxParametersDict["normSup12"] = normPlate12_CSVSupFilePath
        lynxParametersDict["normDil12"] = normPlate12_CSVDilFilePath
        normSup12_Barcode = quantPlate3.octetBarcode + "_Sup_4"
        normDil12_Barcode = quantPlate3.octetBarcode + "_Dil_4"
        lynxParametersDict["normSup12_Barcode"] = normSup12_Barcode
        lynxParametersDict["normDil12_Barcode"] = normDil12_Barcode

for key, item in lynxParametersDict.items():
    print(key + ": " + str(item))



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
