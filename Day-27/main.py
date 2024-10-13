import tkinter
window = tkinter.Tk()
window.title("Mile to KM Convertor")
window.minsize(width=100, height=190)
window.config(padx=20, pady=20)


input_miles = tkinter.Entry(width=10)
input_miles.grid(column=1, row=0)
my_label_miles = tkinter.Label(text="Miles",font=("Arial",10, "bold"))
my_label_miles.grid(column=2, row=0)
my_label = tkinter.Label(text="is equal to",font=("Arial",10, "bold"))
my_label.grid(column=0, row=1)
my_label_ans = tkinter.Label(text="0",font=("Arial", 10, "bold"))
my_label_ans.grid(column=1, row=1)
my_label_km = tkinter.Label(text="KM", font=("Arial", 10, "bold"))
my_label_km.grid(column=2, row=1)


def mile_to_km():
    miles = input_miles.get()
    km = round(float(miles) * 1.609344, ndigits=2)
    my_label_ans.config(text=f"{km}")


button = tkinter.Button(text="Calculate", command=mile_to_km)
button.grid(column=1, row=2)

window.mainloop()
