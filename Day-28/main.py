import math
import tkinter

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    check_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    if reps % 2 != 0:
        count_down(WORK_MIN*60)
        timer_label.config(text="Work", fg=GREEN)
    elif reps % 2 == 0 and reps < 8:
        count_down(SHORT_BREAK_MIN*60)
        timer_label.config(text="Break", fg=PINK)
    elif reps == 8:
        count_down(LONG_BREAK_MIN*60)
        timer_label.config(text="Break", fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    minute = math.floor(count/60)
    sec = math.floor(count % 60)
    if sec < 10:
        sec = f"0{sec}"
    if minute == 0:
        minute = "00"
    canvas.itemconfig(timer_text, text=f"{minute}:{sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            mark += "✔"
            check_label.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = tkinter.Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"), highlightthickness=0)
timer_label.grid(column=1, row=0)
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 132, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)
start_button = tkinter.Button(text="Start", width=8, highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)
reset_button = tkinter.Button(text="Reset", width=8, highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)
check_label = tkinter.Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"), highlightthickness=0)
check_label.grid(column=1, row=3)

window.mainloop()
