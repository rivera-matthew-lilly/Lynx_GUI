import tkinter as tk
from tkinter import ttk, StringVar
from turtle import st

master = tk.Tk()
master.geometry("750x750")
master.title("E.L.I. | Enhanced Lynx Interface")
master.config(background="#a3a3c2")

run_variables_Dict = {}
paddingX = 5
paddingY = 5


q1_frame = tk.Frame(background="#a3a3c2")
question_1_label = tk.Label(master=q1_frame, text="Select source plate type:", font=("Monospace", 12), background="#a3a3c2")
question_1_label.grid(row=1,column=1, sticky="w")
question_1_combo = ttk.Combobox(master=q1_frame, values=["96 MasterBlock", "96 DeepWell", "96 FlatBottom", "96 PCR"])
question_1_combo.grid(row=2, column=1, sticky="w")
q1_frame.grid(row=1,column=1, padx=paddingX, pady=paddingY,sticky="w")

q2_frame = tk.Frame(background="#a3a3c2")
question_2_label = tk.Label(master=q2_frame, text="Select destinaton plate type:", font=("Monospace", 12), background="#a3a3c2")
question_2_label.grid(row=1,column=1, padx=paddingX, pady=paddingY,sticky="w")
#change upon source selection
question_2_combo = ttk.Combobox(master=q2_frame, values=["96 MasterBlock", "96 DeepWell", "96 FlatBottom", "96 PCR"])
question_2_combo.grid(row=2, column=1, sticky="w")
q2_frame.grid(row=2, column=1, padx=paddingX, pady=paddingY,sticky="w")

q3_frame = tk.Frame(background="#a3a3c2")
question_3_label = tk.Label(master=q3_frame, text="Select tip type:", font=("Monospace", 12), background="#a3a3c2")
question_3_label.grid(row=1,column=1, sticky="w")
question_3_combo = ttk.Combobox(master=q3_frame, values=["60F", "340F", "1250F"])
question_3_combo.grid(row=2, column=1, sticky="w")
q3_frame.grid(row=3, column=1, padx=paddingX, pady=paddingY,sticky="w")

q4_frame = tk.Frame(background="#a3a3c2")
question_4_label = tk.Label(master=q4_frame, text="Transfer to echo plate?", font=("Monospace", 12), background="#a3a3c2")
question_4_label.grid(row=1, column=1, sticky="w")
question_4_answer = tk.IntVar()
tk.Radiobutton(master=q4_frame, text="Yes", variable=question_4_answer, value=1, font=("Monospace", 12), background="#a3a3c2").grid(row=1, column=2, sticky="w")
tk.Radiobutton(master=q4_frame, text="No", variable=question_4_answer, value=0, font=("Monospace", 12), background="#a3a3c2").grid(row=1, column=3, sticky="w")
q4_frame.grid(row=4, column=1, padx=paddingX, pady=paddingY,sticky="w")

q5_frame = tk.Frame(background="#a3a3c2")
question_5_label = tk.Label(master=q5_frame, text="Mix plates (8 cycles) after normalization?", font=("Monospace", 12), background="#a3a3c2")
question_5_label.grid(row=1, column=1, sticky="w")
question_5_answer = tk.IntVar()
tk.Radiobutton(master=q5_frame, text="Yes", variable=question_5_answer, value=1, font=("Monospace", 12), background="#a3a3c2").grid(row=1, column=2, sticky="w")
tk.Radiobutton(master=q5_frame, text="No", variable=question_5_answer, value=0, font=("Monospace", 12), background="#a3a3c2").grid(row=1, column=3, sticky="w")
q5_frame.grid(row=5, column=1, padx=paddingX, pady=paddingY,sticky="w")

q6_frame = tk.Frame(background="#a3a3c2")
question_6_label = tk.Label(master=q6_frame, text="Mixing height offset (Recommended 1mm)?", font=("Monospace", 12), background="#a3a3c2")
question_6_label.grid(row=1,column=1, sticky="w")
intMixHeightOffset = StringVar()
question_6_combo = tk.Entry(master=q6_frame, textvariable=intMixHeightOffset, relief="sunken").grid(row=1, column=2, sticky="w")
q6_frame.grid(row=6, column=1, padx=paddingX, pady=paddingY,sticky="w")

q7_frame = tk.Frame(background="#a3a3c2")
question_7_label = tk.Label(master=q7_frame, text="Mix Volume (Recommended 100ul)?", font=("Monospace", 12), background="#a3a3c2")
question_7_label.grid(row=10,column=1, padx=paddingX, pady=paddingY,sticky="w")
mixVol = StringVar()
question_7_combo = tk.Entry(master=q7_frame, textvariable=mixVol, relief="sunken").grid(row=10, column=2, sticky="w")
q7_frame.grid(row=7, column=1, padx=paddingX, pady=paddingY,sticky="w")

def submitForum():
    run_variables_Dict["sourceTypeSelected"] = question_1_combo.get()
    run_variables_Dict["desTypeSelected"] = question_2_combo.get()
    run_variables_Dict["tipTypeSelected"] = question_3_combo.get()
    if question_4_answer.get() == 1:
        run_variables_Dict["bCreateEcho"] = "yes"
    else:
        run_variables_Dict["bCreateEcho"] = "no"
    if question_5_answer.get() == 1:
        run_variables_Dict["bMix"] = "yes"
    else:
        run_variables_Dict["bMix"] = "no"
    run_variables_Dict["intMixHeightOffset"] = intMixHeightOffset.get()
    run_variables_Dict["mixVol"] = mixVol.get()
    
    master.destroy()
 
bSubmit = tk.Button(master ,text="OK",command=submitForum)
bSubmit.grid(row=25, column=1, padx=10,pady=10,ipadx=15,ipady=5)

master.mainloop()

print(run_variables_Dict)

#run_variable_capture.py