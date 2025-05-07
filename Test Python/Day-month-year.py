import tkinter as tk
from tkcalendar import Calendar
from datetime import datetime
from threading import Thread
import time

# === สร้างหน้าต่าง ===
window = tk.Tk()
window.geometry("500x500")
window.title("To-Do List + Thai Date + Clock")

try:
    icon = tk.PhotoImage(file="../Logo.png")
    window.iconphoto(False, icon)
except:
    pass

# === ปฏิทิน ===
today = datetime.today()
cal = Calendar(window, selectmode="day", day=today.day, month=today.month, year=today.year, locale="th")
cal.pack(pady=10)

# === แสดงวันที่ภาษาไทย ===
def format_thai_date(dt):
    thai_months = [
        "", "มกราคม", "กุมภาพันธ์", "มีนาคม", "เมษายน", "พฤษภาคม", "มิถุนายน",
        "กรกฎาคม", "สิงหาคม", "กันยายน", "ตุลาคม", "พฤศจิกายน", "ธันวาคม"
    ]
    thai_days = ["วันจันทร์", "วันอังคาร", "วันพุธ", "วันพฤหัสบดี", "วันศุกร์", "วันเสาร์", "วันอาทิตย์"]
    weekday = dt.weekday()
    return f"{thai_days[weekday]} ที่ {dt.day} {thai_months[dt.month]} {dt.year + 543}"

def on_date_select(event):
    date = cal.get_date()
    dt = datetime.strptime(date, "%d/%m/%Y")
    label_thai.config(text=f"คุณเลือก: {format_thai_date(dt)}")

label_thai = tk.Label(window, text=f"วันนี้คือ: {format_thai_date(today)}", font=("Tahoma", 14))
label_thai.pack()
cal.bind("<<CalendarSelected>>", on_date_select)

# === เวลาแบบอัปเดต ===
label_date = tk.Label(window, font=("Arial", 16))
label_date.pack()
label_time = tk.Label(window, font=("Arial", 24))
label_time.pack()

def get_datetime():
    now = datetime.now()
    return now.strftime("%d/%m/%Y"), now.strftime("%H:%M:%S")

class UpdateTime(Thread):
    def run(self):
        while True:
            date, t = get_datetime()
            window.after(0, lambda: label_date.config(text=f"วันที่: {date}"))
            window.after(0, lambda: label_time.config(text=f"เวลา: {t}"))
            time.sleep(1)
# ไอคอน (ถ้ามีไฟล์ Logo.png)

def on_date_select(event):
    date = cal.get_date()  # ได้วันที่ในรูปแบบ dd/mm/yyyy
    dt = datetime.strptime(date, "%d/%m/%Y")
    thai_date = format_thai_date(dt)


    # แสดงใน Text Widget ด้วย
    T.insert(tk.END, f"\n[{thai_date}] เขียนโน้ตของคุณที่นี่...\n")


# === Label: Fact of the Day ===
label_fact = tk.Label(window, text="Event To-Do List Day", font=("Courier", 14))
label_fact.pack()

# === Text widget ===
T = tk.Text(window, height=4, width=45)
T.insert(tk.END, "")
T.pack()

# === ปุ่ม ===
b1 = tk.Button(window, text="Next")
b1.pack()
b2 = tk.Button(window, text="Exit", command=window.destroy)
b2.pack()

UpdateTime().start()
window.mainloop()
