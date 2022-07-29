using System;
using System.Linq;
using System.Windows.Forms;
using System.Xml;
using System.Data;
using System.Data.DataSetExtensions;
using System.Drawing;
using System.Collections;
using System.Collections.Generic;
using System.Text;
using System.IO;
using MethodManager.Core;
using MMScriptObjects;
using MethodManager.Interop;
using MMScriptObjects.ScriptUtils;
/* 
** The script entry point will be the method Execute() in a unique instance of a class that implements IMMScriptExecutor.
*/
public class MMScriptExecutor : IMMScriptExecutor
{
	// This is the first method that gets executed.
	public void Execute(IMMApp app)
	{

        string sourceTypeSelected = "";
        string desTypeSelected = "";
        string tipTypeSelected = "";
        int k = 0;
        string fileBasedNorm = "";
        int targetConc = 0;
        string bCreateEcho = "";
        string bMix = "";
        int intMixHeightOffset = 0;
        int mixVol = 0;
        string worktableCustomPath = "";
        string normSup1 = "";
        string normDil1 = "";
        string normSup2 = "";
        string normDil2 = "";
        string normSup3 = "";
        string normDil3 = "";
        string normSup4 = "";
        string normDil4 = "";
 
        
        //string ELI_inputFile = "C:\\codeBASE\\Lynx\\output_Test_files\\ELI_inputFile.txt";
		string ELI_inputFile = "C:\\MethodManager4\\Workspaces\\LO507\\ForMatthew\\ELI_inputFile.txt";
		List<string> lines = new List<string>();
		

		int counter = 0;
		foreach (string line in System.IO.File.ReadLines(ELI_inputFile)){  
            if (counter == 0){
                sourceTypeSelected = line;
            }
            if (counter == 1){
                desTypeSelected = line;
            }
            if (counter == 2){
                tipTypeSelected = line;
            }
            if (counter == 3){
                k = Convert.ToInt32(line);
            }
            if (counter == 4){
                fileBasedNorm = line;
            }
            if (counter == 5){
                targetConc = Convert.ToInt32(line);
            }
            if (counter == 6){
                bCreateEcho = line;
            }
            if (counter == 7){
                bMix = line;
            }
            if (counter == 8){
                intMixHeightOffset = Convert.ToInt32(line);
            }
            if (counter == 9){
                mixVol = Convert.ToInt32(line);
            }
            if (counter == 10){
                worktableCustomPath = line;
            }
            if (counter == 11){
                normSup1 = line;
            }
            if (counter == 12){
                normDil1 = line;
			}
			if (counter == 13){
                normSup2 = line;
            }
            if (counter == 14){
                normDil2 = line;
            }
            if (counter == 15){
                normSup3 = line;
            }
            if (counter == 16){
                normDil3 = line;
            }
            if (counter == 17){
                normSup4 = line;
            }
            if (counter == 18){
                normDil4 = line;
            }
			counter = counter + 1;
		}
			
		MMScriptDialog HomeWindow = new MMScriptDialog();{
			HomeWindow.AddMessage("TO AVOID A TRAGEDY, DO NOT EDIT ANY FEILD BELOW");
			HomeWindow.AddEdit("Source Plate Type: ", sourceTypeSelected, false, "sourceTypeSelected");
			HomeWindow.AddEdit("Destination Plate Type: ", desTypeSelected, false, "desTypeSelected");
			HomeWindow.AddEdit("Tip type: ", tipTypeSelected, false, "tipTypeSelected");
			HomeWindow.AddNumerical("Number of plates to be normalized: ", "Source plates", 1,4,1,0,k, "k"); 
			HomeWindow.AddEdit("Input files recieved: ", fileBasedNorm, false, "fileBasedNorm");
			HomeWindow.AddNumerical("Target concentration: ", "mg/uL", 1.0,500.0,0.1,2,targetConc, "targetConc");
			HomeWindow.AddEdit("Transfer to echo?: ", bCreateEcho, false, "bCreateEcho");
			HomeWindow.AddEdit("Mix samples?: ", bMix, false, "bMix");
			HomeWindow.AddNumerical("Mixing height offset: ", "mm", 1.0,5.0,0.1,2,intMixHeightOffset, "intMixHeightOffset");
			HomeWindow.AddNumerical("Mixing volume: ", "uL",1,150,1,0,mixVol, "mixVol");
			HomeWindow.AddOpenFileDlg("Worktable path: ", worktableCustomPath, "txt", false, "worktableCustomPath");
			
				
			bool bValid = HomeWindow.Show(app,"Imported Variables",false,false);
		}
		MMScriptDialog NextWindow = new MMScriptDialog();{
			NextWindow.AddMessage("TO AVOID A TRAGEDY, DO NOT EDIT ANY FEILD BELOW");
			NextWindow.AddOpenFileDlg("Plate 1 Diluent file",normDil1,"csv",false,"normDil1");
			NextWindow.AddOpenFileDlg("Plate 1 Supernatant file",normSup1,"csv",false,"normSup1");
			NextWindow.AddOpenFileDlg("Plate 2 Diluent file",normDil2,"csv",false,"normDil2");
			NextWindow.AddOpenFileDlg("Plate 2 Supernatant file",normSup2,"csv",false,"normSup2");	
			NextWindow.AddOpenFileDlg("Plate 3 Diluent file",normDil3,"csv",false,"normDil3");
			NextWindow.AddOpenFileDlg("Plate 3 Supernatant file",normSup3,"csv",false,"normSup3");
			NextWindow.AddOpenFileDlg("Plate 4 Diluent file",normDil4,"csv",false,"normDil4");
			NextWindow.AddOpenFileDlg("Plate 4 Supernatant file",normSup4,"csv",false,"normSup4");
			
			bool bValid = NextWindow.Show(app,"Input Files",false,false);
		}
	}
}
		