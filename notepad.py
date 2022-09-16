import tkinter
from PIL import ImageTk,Image
from tkinter import StringVar,IntVar,scrolledtext,END,messagebox,filedialog
"""
import tkinter
from tkinter impo
root=tkinter.Tk()
fonts=font.families()
print(fonts)"""

root=tkinter.Tk()
root.title("Notepad")
root.iconbitmap("")
root.geometry("600x600")
root.resizable(0,0)

###########################
text_colour="#fffacd" 
menu_colour="#dbd9db"
root_colour="#6c809a"
root.config(bg=root_colour)

###############################
def change_font(event):
   # print("hello")
  if font_option.get()=="none":
      my_font=(font_family.get(),font_size.get())
  else:
      my_font=(font_family.get(),font_size.get(),font_option.get())

  input_text.config(font=my_font)

  ##############################################
def new_note():
      question=messagebox.askyesno("New Note","Are you sure you want to start a new note?")
      if question==1:
          input_text.delete("1.0",END)

##############################################################################
def close_note():
    question=messagebox.askyesnocancel("Close Note","Are you sure you want close your note?")
    if question==1:
        root.destroy()

        ###########################################################################
def save_note():
    save_name=filedialog.asksaveasfilename(initialdir="./",title="Save Note",filetypes=(("Text Files","*.txt"),("All Files","*.*")))

    with open(save_name,"w") as f:
        f.write(font_family.get()+"\n")
        f.write(str(font_size.get())+"\n")
        f.write(font_option.get()+"\n")

        f.write(input_text.get("1.0",END))

###########################################################
def open_note():
    open_name=filedialog.askopenfilename(initialdir="./",title="Open Note",filetypes=(("Text Files","*.txt"),("All Files","*.*")))

    with open(open_name,"r") as f:
        input_text.delete("1.0",END)

        font_family.set(f.readline().strip())
        font_size.set(int(f.readline().strip()))
        font_option.set(f.readline().strip())

        '''(f.readline().strip())
        (int(f.readline().strip()))
        (f.readline().strip())'''


        change_font(1)

        text=f.read()
        input_text.insert("5.0",text)



      


menu_frame=tkinter.Frame(root,bg=menu_colour)
text_frame=tkinter.Frame(root,bg=text_colour)
menu_frame.pack(padx=5,pady=5)
text_frame.pack(padx=5,pady=5)

######################################
#new_image=ImageTk.PhotoImage(Image.open("pad.png"))
new_button=tkinter.Button(menu_frame,#image=new_image,
text="add",command=new_note)
new_button.grid(row=0,column=0,padx=5,pady=5)

#save_image=ImageTk.PhotoImage(Image.open("pad.png"))
save_button=tkinter.Button(menu_frame,#image=save_image#,
text="save",command=save_note)
save_button.grid(row=0,column=1,padx=5,pady=5)

#open_image=ImageTk.PhotoImage(Image.open("pad.png"))
open_button=tkinter.Button(menu_frame,#image=open_image,
text="open",command=open_note)
open_button.grid(row=0,column=2,padx=5,pady=5)

#close_image=ImageTk.PhotoImage(Image.open("pad.png"))
close_button=tkinter.Button(menu_frame,#image=close_image,
text="close",command=close_note)
close_button.grid(row=0,column=3,padx=5,pady=5)

#################################################
families=["Terminal","Modern","Script","Courier","Calibri","Cambria","Georgia","Ms Gothic","SimSun","Talhoma","Times New Roman","Verdana","Wingdings"]

font_family=StringVar()
font_family_drop=tkinter.OptionMenu(menu_frame,font_family,*families,command=change_font)
font_family.set("Terminal")
font_family_drop.grid(row=0,column=4,padx=5,pady=5)
font_family_drop.config(width=16)

sizes=["8","10","12","14","16","20","24","32",'"48',"64","72","96"]
font_size=IntVar()
font_size_drop=tkinter.OptionMenu(menu_frame,font_size,*sizes,command=change_font)
font_size.set("12")
font_size_drop.grid(row=0,column=5,padx=5,pady=5)
font_size_drop.config(width=2)

options=["none","bold","italic"]
font_option=StringVar()
font_option_drop=tkinter.OptionMenu(menu_frame,font_option,*options,command=change_font)
font_option.set("none")
font_option_drop.grid(row=0,column=6,padx=5,pady=5)
font_option_drop.config(width=5)

###############################################
my_font=(font_family.get(),font_size.get())
input_text=tkinter.scrolledtext.ScrolledText(text_frame,width=1000,height=100,bg=text_colour,font=my_font,)
input_text.pack()










root.mainloop()