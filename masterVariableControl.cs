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
 
        
        string ELI_inputFile = "C:\\codeBASE\\Lynx\\output_Test_files\\ELI_inputFile.txt";
		List<string> lines = new List<string>();
		

		int counter = 0;
		foreach (string line in System.IO.File.ReadLines(ELI_inputFile)){  
            if (counter == 0){
                sourceTypeSelected = line;
                counter = counter + 1;
            }
            if (counter == 1){
                desTypeSelected = line;
                counter = counter + 1;
            }
            if (counter == 2){
                tipTypeSelected = line;
                counter = counter + 1;
            }
            if (counter == 3){
                k = Convert.ToInt32(line);
                counter = counter + 1;
            }
            if (counter == 4){
                fileBasedNorm = line;
                counter = counter + 1;
            }
            if (counter == 5){
                targetConc = Convert.ToInt32(line);
                counter = counter + 1;
            }
            if (counter == 6){
                bCreateEcho = line;
                counter = counter + 1;
            }
            if (counter == 7){
                bMix = line;
                counter = counter + 1;
            }
            if (counter == 8){
                intMixHeightOffset = Convert.ToInt32(line);
                counter = counter + 1;
            }
            if (counter == 9){
                mixVol = Convert.ToInt32(line);
                counter = counter + 1;
            }
            if (counter == 10){
                worktableCustomPath = line;
                counter = counter + 1;
            }
            if (k >= 1){
                if (counter == 11){
                    normSup1 = line;
                    counter = counter + 1;
                    }
                if (counter == 12){
                    normDil1 = line;
                    counter = counter + 1;
                    }
            }
            if (k >=2){
                if (counter == 13){
                    normSup2 = line;
                    counter = counter + 1;
                }
                if (counter == 14){
                    normDil2 = line;
                    counter = counter + 1;
                }
            }
            if (k >=3){
                if (counter == 15){
                    normSup3 = line;
                    counter = counter + 1;
                }
                if (counter == 16){
                    normDil3 = line;
                    counter = counter + 1;
                }
            }
            if (k >=4){
                if (counter == 17){
                    normSup4 = line;
                    counter = counter + 1;
                }
                if (counter == 18){
                    normDil4 = line;
                    counter = counter + 1;
                }
            }
		} 
    }
}
		