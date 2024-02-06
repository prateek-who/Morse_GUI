import ast
import customtkinter as ct
import morseguiback as ms


ct.set_appearance_mode("dark")
ct.set_default_color_theme("dark-blue")


def encr():
    plaintxt = entry1.get()
    cyphertxt, case_info = ms.encode(plaintxt)
    txt_field1_1.delete(0.0, "end")
    txt_field1_1.insert(0.0, cyphertxt)
    txt_field1_2.delete(0.0, "end")
    txt_field1_2.insert(0.0, case_info)


def decr():
    cyfrtxt = entry2_1.get()
    infodict_str = entry2_2.get()
    if not infodict_str:
        infodict_str = "{"
        for i in range(round(cyfrtxt.__len__()/2)):
            infodict_str += f"{i}: 0, "
        infodict_str += "}"
    infodict = ast.literal_eval(infodict_str)
    final_txt = ms.decode(cyfrtxt, infodict)
    txt_field2.delete(0.0, "end")
    txt_field2.insert(0.0, final_txt)


root = ct.CTk()
root.geometry("800x600")
root.minsize(800, 600)
root.title("Morseeee...")
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)


frame1 = ct.CTkFrame(master=root)
frame1.grid(pady=5, padx=15, row=0, column=0)

label1 = ct.CTkLabel(master=frame1, text="Encoder", font=("normal", 28))
label1.pack(pady=12, padx=10)

entry1 = ct.CTkEntry(master=frame1, placeholder_text="Enter plain text", height=50, width=200, justify="center")
entry1.pack(pady=12, padx=10)

button1 = ct.CTkButton(master=frame1, text="Encrypt", height=50, width=200, command=encr)
button1.pack(pady=12, padx=10)

txt_field1_1 = ct.CTkTextbox(master=frame1, state="normal", width=350, height=170, font=("normal", 18))
txt_field1_1.pack(pady=12, padx=10)
txt_field1_2 = ct.CTkTextbox(master=frame1, state="normal", width=350, height=200, font=("normal", 18))
txt_field1_2.pack(pady=12, padx=10)


frame2 = ct.CTkFrame(master=root)
frame2.grid(pady=5, padx=15, row=0, column=1)

label2 = ct.CTkLabel(master=frame2, text="Decoder", font=("normal", 28))
label2.pack(pady=12, padx=10)

entry2_1 = ct.CTkEntry(master=frame2, placeholder_text="Enter cypher text", height=50, width=200, justify="center")
entry2_1.pack(pady=12, padx=10)
entry2_2 = ct.CTkEntry(master=frame2, placeholder_text="Enter case information dictionary if you have it!", height=50, width=280, justify="center")
entry2_2.pack(pady=12, padx=10)

button2 = ct.CTkButton(master=frame2, text="Decrypt", height=50, width=200, command=decr)
button2.pack(pady=12, padx=10)

txt_field2 = ct.CTkTextbox(master=frame2, state="normal", width=350, height=310, font=("normal", 18))
txt_field2.pack(pady=12, padx=10)

root.mainloop()
