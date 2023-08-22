from tkinter import *
from tkinter import ttk

units = ["Bananas", "cm", "Meters", "Kilometers", "Inches", "Feet", "Yards", "Miles"]

def banana_convert():
    from_unit = from_unit_combo.get()
    to_unit = to_unit_combo.get()
    amount_unit = convers_entry.get()

    #Banana/cm
    if from_unit == "Bananas" and to_unit == "cm":
        banaconv = 17.78
        result = banaconv * float(amount_unit)
        result_label.config(text=result)
    elif from_unit == "cm" and to_unit == "Bananas":
        banaconv = 0.056
        result = banaconv * float(amount_unit)
        result_label.config(text=result)

    #Banana/meter
    elif from_unit == "Bananas" and to_unit == "Meters":
        banaconv = 0.178
        result = banaconv * float(amount_unit)
        result_label.config(text=result)
    elif from_unit == "Meters" and to_unit == "Bananas":
        banaconv = 5.618
        result = banaconv * float(amount_unit)
        result_label.config(text=result)

    #Banana/kilometer
    elif from_unit == "Bananas" and to_unit == "Kilometers":
        banaconv = 0.000178
        result = banaconv * float(amount_unit)
        result_label.config(text=result)
    elif from_unit == "Kilometers" and to_unit == "Bananas":
        banaconv = 5617.977
        result = banaconv * float(amount_unit)
        result_label.config(text=result)

    #Banana/inch
    elif from_unit == "Bananas" and to_unit == "Inches":
        banaconv = 7
        result = banaconv * float(amount_unit)
        result_label.config(text=result)
    elif from_unit == "Inches" and to_unit == "Bananas":
        banaconv = 0.143
        result = banaconv * float(amount_unit)
        result_label.config(text=result)

    #Banana/feet
    elif from_unit == "Bananas" and to_unit == "Feet":
        banaconv = 0.583
        result = banaconv * float(amount_unit)
        result_label.config(text=result)
    elif from_unit == "Feet" and to_unit == "Bananas":
        banaconv = 1.715
        result = banaconv * float(amount_unit)
        result_label.config(text=result)
        
    #Banana/yard
    elif from_unit == "Bananas" and to_unit == "Yards":
        banaconv = 0.194
        result = banaconv * float(amount_unit)
        result_label.config(text=result)
    elif from_unit == "Yards" and to_unit == "Bananas":
        banaconv = 5.143
        result = banaconv * float(amount_unit)
        result_label.config(text=result)

    #Banana/miles
    elif from_unit == "Bananas" and to_unit == "Miles":
        banaconv = 0.000110
        result = banaconv * float(amount_unit)
        result_label.config(text=result)
    elif from_unit == "Miles" and to_unit == "Bananas":
        banaconv = 9090.909
        result = banaconv * float(amount_unit)
        result_label.config(text=result)

    #cm/meter
    elif from_unit == "cm" and to_unit == "Meters":
        banaconv = 0.010
        result = banaconv * float(amount_unit)
        result_label.config(text=result)
    elif from_unit == "Meters" and to_unit == "cm":
        banaconv = 100
        result = banaconv * float(amount_unit)
        result_label.config(text=result)

    #cm/kilometer
    elif from_unit == "cm" and to_unit == "Kilometers":
        banaconv = 0.000010
        result = banaconv * float(amount_unit)
        result_label.config(text=result)
    elif from_unit == "Kilometers" and to_unit == "cm":
        banaconv = 100000
        result = banaconv * float(amount_unit)
        result_label.config(text=result)
        
    #cm/inch
    elif from_unit == "cm" and to_unit == "Inches":
        banaconv = 0.39
        result = banaconv * float(amount_unit)
        result_label.config(text=result)
    elif from_unit == "Inches" and to_unit == "cm":
        banaconv = 2.54
        result = banaconv * float(amount_unit)
        result_label.config(text=result)

    #cm/feet
    elif from_unit == "cm" and to_unit == "Feet":
        banaconv = 0.033
        result = banaconv * float(amount_unit)
        result_label.config(text=result)
    elif from_unit == "Feet" and to_unit == "cm":
        banaconv = 30
        result = banaconv * float(amount_unit)
        result_label.config(text=result)

    #cm/yard
    elif from_unit == "cm" and to_unit == "Yards":
        banaconv = 0.011
        result = banaconv * float(amount_unit)
        result_label.config(text=result)
    elif from_unit == "Yards" and to_unit == "cm":
        banaconv = 91
        result = banaconv * float(amount_unit)
        result_label.config(text=result)

    #cm/miles
    elif from_unit == "cm" and to_unit == "Miles":
        banaconv = 0.000006
        result = banaconv * float(amount_unit)
        result_label.config(text=result)
    elif from_unit == "Miles" and to_unit == "cm":
        banaconv = 160935
        result = banaconv * float(amount_unit)
        result_label.config(text=result)

    #meter/kilometer
    elif from_unit == "Meters" and to_unit == "Kilometers":
        banaconv = 0.00100
        result = banaconv * float(amount_unit)
        result_label.config(text=result)
    elif from_unit == "Kilometers" and to_unit == "Meters":
        banaconv = 1000
        result = banaconv * float(amount_unit)
        result_label.config(text=result)

    #meter/inch
    elif from_unit == "Meters" and to_unit == "Inches":
        banaconv = 39.37
        result = banaconv * float(amount_unit)
        result_label.config(text=result)
    elif from_unit == "Inches" and to_unit == "Meters":
        banaconv = 0.025
        result = banaconv * float(amount_unit)
        result_label.config(text=result)

    #meter/feet
    elif from_unit == "Meters" and to_unit == "Feet":
        banaconv = 3.28
        result = banaconv * float(amount_unit)
        result_label.config(text=result)
    elif from_unit == "Feet" and to_unit == "Meters":
        banaconv = 0.30
        result = banaconv * float(amount_unit)
        result_label.config(text=result)

    #meter/yard
    elif from_unit == "Meters" and to_unit == "Yards":
        banaconv = 1.09
        result = banaconv * float(amount_unit)
        result_label.config(text=result)
    elif from_unit == "Yards" and to_unit == "Meters":
        banaconv = 0.91
        result = banaconv * float(amount_unit)
        result_label.config(text=result)

    #meter/miles
    elif from_unit == "Meters" and to_unit == "Miles":
        banaconv = 0.00062
        result = banaconv * float(amount_unit)
        result_label.config(text=result)
    elif from_unit == "Miles" and to_unit == "Meters":
        banaconv = 1609
        result = banaconv * float(amount_unit)
        result_label.config(text=result)

    #kilometer/inch
    elif from_unit == "Kilometers" and to_unit == "Inches":
        banaconv = 39370
        result = banaconv * float(amount_unit)
        result_label.config(text=result)
    elif from_unit == "Inches" and to_unit == "Kilometers":
        banaconv = 0.000025
        result = banaconv * float(amount_unit)
        result_label.config(text=result)

    #kilometer/feet
    elif from_unit == "Kilometers" and to_unit == "Feet":
        banaconv = 3281
        result = banaconv * float(amount_unit)
        result_label.config(text=result)
    elif from_unit == "Feet" and to_unit == "Kilometers":
        banaconv = 0.00030
        result = banaconv * float(amount_unit)
        result_label.config(text=result)

    #kilometer/yard
    elif from_unit == "Kilometers" and to_unit == "Yards":
        banaconv = 1094
        result = banaconv * float(amount_unit)
        result_label.config(text=result)
    elif from_unit == "Yards" and to_unit == "Kilometers":
        banaconv = 0.00091
        result = banaconv * float(amount_unit)
        result_label.config(text=result)

    #kilometer/miles
    elif from_unit == "Kilometers" and to_unit == "Miles":
        banaconv = 0.62
        result = banaconv * float(amount_unit)
        result_label.config(text=result)
    elif from_unit == "Miles" and to_unit == "Kilometers":
        banaconv = 1.61
        result = banaconv * float(amount_unit)
        result_label.config(text=result)

    #inch/feet
    elif from_unit == "Inches" and to_unit == "Feet":
        banaconv = 0.083
        result = banaconv * float(amount_unit)
        result_label.config(text=result)
    elif from_unit == "Feet" and to_unit == "Inches":
        banaconv = 12.00
        result = banaconv * float(amount_unit)
        result_label.config(text=result)

    #inch/yard
    elif from_unit == "Inches" and to_unit == "Yards":
        banaconv = 0.028
        result = banaconv * float(amount_unit)
        result_label.config(text=result)
    elif from_unit == "Yards" and to_unit == "Inches":
        banaconv = 36
        result = banaconv * float(amount_unit)
        result_label.config(text=result)

    #inch/miles
    elif from_unit == "Inches" and to_unit == "Miles":
        banaconv = 0.000016
        result = banaconv * float(amount_unit)
        result_label.config(text=result)
    elif from_unit == "Miles" and to_unit == "Inches":
        banaconv = 63360
        result = banaconv * float(amount_unit)
        result_label.config(text=result)

    #feet/yard
    elif from_unit == "Feet" and to_unit == "Yards":
        banaconv = 0.33
        result = banaconv * float(amount_unit)
        result_label.config(text=result)
    elif from_unit == "Yards" and to_unit == "Feet":
        banaconv = 3
        result = banaconv * float(amount_unit)
        result_label.config(text=result)

    #feet/miles
    elif from_unit == "Feet" and to_unit == "Miles":
        banaconv = 0.00019
        result = banaconv * float(amount_unit)
        result_label.config(text=result)
    elif from_unit == "Miles" and to_unit == "Feet":
        banaconv = 5280
        result = banaconv * float(amount_unit)
        result_label.config(text=result)

    #yard/miles
    elif from_unit == "Yards" and to_unit == "Miles":
        banaconv = 0.00057
        result = banaconv * float(amount_unit)
        result_label.config(text=result)
    elif from_unit == "Miles" and to_unit == "Yards":
        banaconv = 1760
        result = banaconv * float(amount_unit)
        result_label.config(text=result)

window = Tk()
window.geometry('310x340+500+200')
window.title('Banana Converter')
window.resizable(height=FALSE, width=FALSE)
banana_header = '#ffe135'
convert_btn_bg = '#F6BE00'
white = '#FFFFFF'

top_frame = Frame(window, bg=banana_header, width=300, height=80)
top_frame.grid(row=0, column=0)
bottom_frame = Frame(window, width=300, height=250)
bottom_frame.grid(row=1, column=0)

name_label = Label(top_frame, text='Banana Converter', bg=banana_header, fg=white, pady=20, padx=35, justify=CENTER, font=('Poppins 20 bold'))
name_label.grid(row=0, column=0)

from_banana_label = Label(bottom_frame, text='From:', font=('Poppins 10 bold'), justify=LEFT)
from_banana_label.place(x=5, y=10)
to_banana_label = Label(bottom_frame, text='To:', font=('Poppins 10 bold'), justify=RIGHT)
to_banana_label.place(x=160, y=10)

from_unit_combo = ttk.Combobox(bottom_frame, values=list(units), width=14, font=('Poppins 10 bold'))
from_unit_combo.place(x=5, y=30)
to_unit_combo = ttk.Combobox(bottom_frame, values=list(units), width=14, font=('Poppins 10 bold'))
to_unit_combo.place(x=160, y=30)

convers_label = Label(bottom_frame, text='To Convert:', font=('Poppins 10 bold'))
convers_label.place(x=5, y=55)
convers_entry = Entry(bottom_frame, width=25, font=('Poppins 15 bold'))
convers_entry.place(x=5, y=80)

result_label = Label(bottom_frame, text='', font=('Poppins 10 bold'))
result_label.place(x=5, y=115)

convert_button = Button(bottom_frame, text="Convert", bg=convert_btn_bg, fg=white, font=('Poppins 10 bold'), command=banana_convert)
convert_button.place(x=5, y=165)

window.mainloop()