from tkinter import *
from datetime import datetime
from threading import Thread
import time

# สร้างหน้าต่างหลัก
root = Tk()
root.title("Real-time Clock")
root.geometry("300x150")

# === Label แสดงวันที่และเวลา ===
date_label = Label(root, text="Date", font=("Arial", 20))
date_label.grid(row=0, column=0, pady=10)

time_label = Label(root, text="Time", font=("Arial", 40))
time_label.grid(row=1, column=0, pady=10)

# === ฟังก์ชันดึงวัน-เวลา ===
def get_datetime():
    now = datetime.now()
    date = now.strftime("%d/%m/%Y")
    current_time = now.strftime("%H:%M:%S")
    return date, current_time

# === Thread สำหรับอัปเดตเวลาทุกวินาที ===
class UpdateTime(Thread):
    def __init__(self):
        super().__init__()
        self.daemon = True  # ปิด thread เมื่อปิดหน้าต่าง

    def run(self):
        while True:
            date, current_time = get_datetime()
            # ใช้ .after เพื่อแก้ปัญหา Tkinter + Thread
            root.after(0, lambda: date_label.config(text=f"{date}"))
            root.after(0, lambda: time_label.config(text=f"{current_time}"))
            time.sleep(1)

# เริ่ม thread
update_thread = UpdateTime()
update_thread.start()

# เริ่มแสดงผล GUI
root.mainloop()
