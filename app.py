import tkinter as tk

purchases = 0

def add():
    global purchases
    purchases += 1
    lbl["text"] = f"Покупок: {purchases}\nПоследняя: {e1.get()} - {e2.get()} руб."

root = tk.Tk()
root.title("Трекер расходов")
root.geometry("560x700")

img = tk.PhotoImage(file="images.png") 
tk.Label(root, image=img).pack(pady=10)

tk.Label(root, text="Название покупки:").pack()
e1 = tk.Entry(root)
e1.pack()

tk.Label(root, text="Стоимость (руб.):").pack()
e2 = tk.Entry(root)
e2.pack()

lbl = tk.Label(root, text="Покупок: 0")
lbl.pack(pady=10)

tk.Button(root, text="Добавить покупку", command=add).pack()

root.mainloop()
