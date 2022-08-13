
def userInputForNorm():
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

    return (sourceTypeSelected, desTypeSelected, tipTypeSelected, numberOfPlates, bCreateEcho, fileBasedNorm, targetVol, targetConc, neatVol, bMix, intMixHeightOffset, mixVol)

def userInputForQuant():
    octetPlateCount = int(input("How many octet file need parsed? (Max: 3): "))
    octetFilePath1 = ""
    octetFilePath2 = ""
    octetFilePath3 = ""
    numberOfQuads_fromOctetPlate1 = 0
    numberOfQuads_fromOctetPlate2 = 0
    numberOfQuads_fromOctetPlate3 = 0
    if octetPlateCount >=1:
        octetFilePath1 = input("Input first octet quant file: ")
        numberOfQuads_fromOctetPlate1 = int(input("How many 96 well plate have quants in this file? (Max 4): "))
    if octetPlateCount >=2:
        octetFilePath2 = input("Input second octet quant file: ")
        numberOfQuads_fromOctetPlate2 = int(input("How many 96 well plate have quants in this file? (Max 4): "))
    if octetPlateCount >=3:
        octetFilePath3 = input("Input third octet quant file: ")
        numberOfQuads_fromOctetPlate3 = int(input("How many 96 well plate have quants in this file? (Max 4): "))

    return (octetPlateCount, octetFilePath1, numberOfQuads_fromOctetPlate1, octetFilePath2, numberOfQuads_fromOctetPlate2, octetFilePath3, numberOfQuads_fromOctetPlate3)



#lynxGUIFunctions.py