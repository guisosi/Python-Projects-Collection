import tkinter

button_values = [
["AC", "+/-", "%", "÷"], 
["7", "8", "9", "×"], 
["4", "5", "6", "-"],
["1", "2", "3", "+"],
["0", ".", "√", "="]    

]

right_symbols = ["÷", "×", "-", "+", "="]
top_symbols = ["AC", "+/-", "%"]

row_count = len(button_values)
column_count = len(button_values[0])


color_light_gray = "#D4D4D2"
color_dark_gray = "#505050"
color_black = "#1C1C1C"
color_orange = "#FF9500"
color_white = "white"


#window setup
window = tkinter.Tk()
window.title("Calculator")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text="0", font=("Arial", 45), background=color_black,
                      foreground=color_white)

label.grid(row=0, column=0)

for row in range(row_count):
  for column in range(column_count):
    value = button_values[row][column]
    button = tkinter.Button(frame,  text=value, font=("Arial", 30),
                            width=column_count-1, height=1,
                            command=lambda value=value: button_clicked(value))  
    button.grid(row=row+1, column=column)

frame.pack()

def button_clicked():
  pass

window.mainloop()


