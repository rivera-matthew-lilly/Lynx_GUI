
import tkinter as tk
from tkinter.font import ITALIC
from tkinter import filedialog



submissin_Dict = {}

master = tk.Tk()
master.geometry("750x750")
master.title("E.L.I. | Enhanced Lynx Interface")
master.config(background="#a3a3c2")
paddingX = 5
paddingY = 5

frame_intro = tk.Frame()
intro_label = tk.Label(master=frame_intro, text="E.L.I. | Enhanced Lynx Interface", font=("Monospace", 16), background="#a3a3c2")
intro_label.pack()
frame_intro.pack(padx=20, pady=20)

frame_directions = tk.Frame()
intro_directions = tk.Label(master=frame_directions, text="Hello, I am ELI! Please answer the questions below and I will take care of the rest.", font=("Monospace", 12, ITALIC), background="#a3a3c2")
intro_directions.pack()
frame_directions.pack(anchor=tk.W, padx=paddingX, pady=paddingY)

######################### QUESTION #1 ################################

def open_fileInput():
    new_window = tk.Toplevel(master)
    new_window.title("Input Octet Files")
    new_window.config(background="#a3a3c2")

    def question_1_selected():

        def browse_file_1():
            filename_1 = filedialog.askopenfilename(initialdir="C:/", title="Select a File", filetypes=(("CSV files","*.csv"),("All files","*.*")))
            ent1.configure(text=filename_1, font=10)
            print("filename: " + filename_1)
            submissin_Dict["octetFile_1"] = filename_1
        
        def browse_file_2():
            filename_2 = filedialog.askopenfilename(initialdir="C:/", title="Select a File", filetypes=(("CSV files","*.csv"),("All files","*.*")))
            ent2.configure(text=filename_2, font=10)
            print("filename: " + filename_2)
            submissin_Dict["octetFile_2"] = filename_2

        def browse_file_3():
            filename_3 = filedialog.askopenfilename(initialdir="C:/", title="Select a File", filetypes=(("CSV files","*.csv"),("All files","*.*")))
            ent3.configure(text=filename_3, font=10)
            print("filename: " + filename_3)
            submissin_Dict["octetFile_3"] = filename_3

        def ok_button(row_place):
            bOK = tk.Button(new_window ,text="OK",command=new_window.destroy)
            bOK.grid(row=row_place,column=2, padx=10,pady=10,ipadx=15,ipady=5)

        choice = question_1_answer.get()

        if choice == 1:
            new_window.geometry("800x150")
            question_2_label_1 = tk.Label(new_window)
            question_2_label_1.grid(row=1,column=1,padx=20,pady=10,sticky="w")
            question_2_label_1.config(text="Select first octet quant file: ",  font=("Monospace", 12), background="#a3a3c2")
            ent1=tk.Label(new_window, font=12, text="                                                             ", background="white", borderwidth=3, relief="sunken")
            ent1.grid(row=1, column=2, padx=10)
            b1 = tk.Button(new_window ,background="white", text="Browse",command=browse_file_1)
            b1.grid(row=1,column=3, padx=10,pady=10,ipadx=15,ipady=5)
            ok_button(2)

        elif choice == 2:
            new_window.geometry("900x200")
            question_2_label_1 = tk.Label(new_window)
            question_2_label_2 = tk.Label(new_window)
            question_2_label_1.grid(row=1,column=1,padx=25,pady=2,sticky="w")
            question_2_label_2.grid(row=2,column=1,padx=25,pady=2,sticky="w")
            question_2_label_1.config(text="Select first octet quant file: ",  font=("Monospace", 14), background="#a3a3c2")
            question_2_label_2.config(text="Select second octet quant file: ",  font=("Monospace", 14), background="#a3a3c2")
            ent1=tk.Label(new_window, font=12, text="                                                             ", background="white", borderwidth=3, relief="sunken")
            ent1.grid(row=1, column=2, padx=10)
            b1 = tk.Button(new_window ,background="white", text="Browse",command=browse_file_1)
            b1.grid(row=1,column=3, padx=10,pady=10,ipadx=15,ipady=5)
            ent2=tk.Label(new_window, font=12, text="                                                             ", background="white", borderwidth=3, relief="sunken")
            ent2.grid(row=2, column=2, padx=10)
            b2 = tk.Button(new_window ,background="white", text="Browse",command=browse_file_2)
            b2.grid(row=2,column=3, padx=10,pady=10,ipadx=15,ipady=5)
            ok_button(3)

        elif choice == 3:
            new_window.geometry("900x250")
            question_2_label_1 = tk.Label(new_window)
            question_2_label_2 = tk.Label(new_window)
            question_2_label_3 = tk.Label(new_window)
            question_2_label_1.grid(row=1,column=1,padx=25,pady=5,sticky="w")
            question_2_label_2.grid(row=2,column=1,padx=25,pady=0,sticky="w")
            question_2_label_3.grid(row=3,column=1,padx=25,pady=5,sticky="w")
            question_2_label_1.config(text="Select first octet quant file: ",  font=("Monospace", 14), background="#a3a3c2")
            question_2_label_2.config(text="Select second octet quant file: ",  font=("Monospace", 14), background="#a3a3c2")
            question_2_label_3.config(text="Select third octet quant file: ",  font=("Monospace", 14), background="#a3a3c2")
            ent1=tk.Label(new_window, font=12, text="                                                             ", background="white", borderwidth=3, relief="sunken")
            ent1.grid(row=1, column=2, padx=10)
            b1 = tk.Button(new_window ,background="white", text="Browse",command=browse_file_1)
            b1.grid(row=1,column=3, padx=10,pady=10,ipadx=15,ipady=5)
            ent2=tk.Label(new_window, font=12, text="                                                             ", background="white", borderwidth=3, relief="sunken")
            ent2.grid(row=2, column=2, padx=10)
            b2 = tk.Button(new_window ,background="white", text="Browse",command=browse_file_2)
            b2.grid(row=2,column=3, padx=10,pady=10,ipadx=15,ipady=5)
            ent3=tk.Label(new_window, font=12, text="                                                             ", background="white", borderwidth=3, relief="sunken")
            ent3.grid(row=3, column=2, padx=10)
            b3 = tk.Button(new_window ,background="white", text="Browse",command=browse_file_3)
            b3.grid(row=3,column=3, padx=10,pady=10,ipadx=15,ipady=5)
            ok_button(4)

    question_1_selected()
    


frame_1a = tk.Frame()
question_1_label = tk.Label(master=frame_1a, text="How many octet files need parsed (Max 3 files)?", font=("Monospace", 12), background="#a3a3c2")
question_1_label.pack()#grid(column=1, row=1)
frame_1b = tk.Frame()
frame_1c = tk.Frame()
frame_1d = tk.Frame()
question_1_answer = tk.IntVar()
tk.Radiobutton(master=frame_1b, text="1", variable=question_1_answer, value=1, font=("Monospace", 12), background="#a3a3c2", command=open_fileInput).pack()#grid(column=1, row=2)
tk.Radiobutton(master=frame_1c, text="2", variable=question_1_answer, value=2, font=("Monospace", 12), background="#a3a3c2", command=open_fileInput).pack()#.grid(column=2, row=2)
tk.Radiobutton(master=frame_1d, text="3", variable=question_1_answer, value=3, font=("Monospace", 12), background="#a3a3c2", command=open_fileInput).pack()#.grid(column=3, row=2)
frame_1a.pack(anchor=tk.W, padx=paddingX, pady=paddingY)
frame_1b.pack(anchor=tk.NW, side=tk.LEFT, padx=paddingX, pady=paddingY)
frame_1c.pack(anchor=tk.NW, side=tk.LEFT, padx=paddingX, pady=paddingY)
frame_1d.pack(anchor=tk.NW, side=tk.LEFT, padx=paddingX, pady=paddingY)



bOK = tk.Button(master ,text="OK",command=master.destroy)
bOK.pack(anchor=tk.SW, side=tk.LEFT, padx=10,pady=10,ipadx=15,ipady=5)

master.mainloop()


print(submissin_Dict)

#tkinter_gui_test.py