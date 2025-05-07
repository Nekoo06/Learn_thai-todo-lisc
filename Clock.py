import tkinter as tk

# สร้างหน้าต่างหลัก
window = tk.Tk()

# กำหนดขนาดหน้าต่าง
window.geometry("250x170")

# สร้าง Text widget สำหรับแสดงข้อความ
T = tk.Text(window, height=5, width=30)

# สร้าง Label
l = tk.Label(window, text="Fact of the Day")
l.config(font=("Courier", 14))

# ข้อความ Fact
Fact = """A man can be arrested in
Italy for wearing a skirt in public."""

# สร้างปุ่ม Next (ยังไม่มีฟังก์ชัน)
b1 = tk.Button(window, text="Next")

# สร้างปุ่ม Exit และเชื่อมกับ window.destroy เพื่อปิดโปรแกรม
b2 = tk.Button(window, text="Exit", command=window.destroy)

# จัดวาง widget ด้วย pack
l.pack()
T.pack()
b1.pack()
b2.pack()

# ใส่ข้อความเข้าไปใน Text
T.insert(tk.END, Fact)

# เริ่ม loop GUI
window.mainloop()
