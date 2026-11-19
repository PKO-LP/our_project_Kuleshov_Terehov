import tkinter as tk
from tkinter import messagebox

purchases = []
next_id = 1

def add():
    global next_id
    title = e_title.get().strip()
    price = e_price.get().strip()
    date = e_date.get().strip()

    if not title or not date or not price.isdigit():
        messagebox.showwarning("Ошибка", "Заполните все поля (цена — целое число)!")
        return

    purchases.append({
        "id": next_id,
        "title": title,
        "price": int(price),
        "date": date,
        "status": "Запланировано"
    })
    next_id += 1
    e_title.delete(0, tk.END)
    e_price.delete(0, tk.END)
    show()

def show():
    listbox.delete(0, tk.END)
    q = e_search.get().strip().lower()
    st = status_var.get()

    for p in purchases:
        if (q in p["title"].lower() or q == str(p["id"])) and (st == "Все" or p["status"] == st):
            listbox.insert(tk.END, f"#{p['id']} | {p['date']} | {p['title']} - {p['price']} руб. [{p['status']}]")

def next_status():
    sel = listbox.curselection()
    if not sel:
        messagebox.showwarning("Ошибка", "Выберите покупку в списке!")
        return

    # Находим покупку по номеру #id из выбранной строки списка
    item_id = int(listbox.get(sel[0]).split("|")[0].replace("#", "").strip())
    for p in purchases:
        if p["id"] == item_id:
            if p["status"] == "Запланировано":
                p["status"] = "Оплачено"
            elif p["status"] == "Оплачено":
                p["status"] = "Проверено"
            else:
                messagebox.showinfo("Инфо", "Уже финальный статус «Проверено»")
            break
    show()

root = tk.Tk()
root.title("Трекер расходов (Спринт 2)")
root.geometry("560x1080")

try:
    img = tk.PhotoImage(file="images.png")
    tk.Label(root, image=img).pack(pady=5)
except Exception:
    pass

tk.Label(root, text="Название покупки:").pack()
e_title = tk.Entry(root)
e_title.pack()

tk.Label(root, text="Стоимость (руб.):").pack()
e_price = tk.Entry(root)
e_price.pack()

tk.Label(root, text="Дата:").pack()
e_date = tk.Entry(root)
e_date.insert(0, "19.11.2026")
e_date.pack()

tk.Button(root, text="Добавить покупку", command=add).pack(pady=5)

tk.Label(root, text="Поиск по названию или номеру:").pack()
e_search = tk.Entry(root)
e_search.pack()

status_var = tk.StringVar(value="Все")
tk.OptionMenu(root, status_var, "Все", "Запланировано", "Оплачено", "Проверено").pack(pady=2)
tk.Button(root, text="Найти / Фильтровать", command=show).pack(pady=5)

listbox = tk.Listbox(root, width=65, height=12)
listbox.pack(pady=5)

tk.Button(root, text="Следующий статус", command=next_status).pack(pady=5)

root.mainloop()
