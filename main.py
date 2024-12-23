import sqlite3
import customtkinter
import tkinter

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('blue')

app = customtkinter.CTk()
app.title('Авторизация пользователя')
app.geometry('400x430')

def create_table():
    con = sqlite3.connect('users.db')
    cursor = con.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    con.commit()
    con.close()

create_table()

def save_new_user(username, password):
    con = sqlite3.connect('users.db')
    cursor = con.cursor()
    cursor.execute('''
        INSERT INTO users (username, password)
        VALUES (?, ?)
    ''', (username, password))
    con.commit()
    con.close()
    message_label.configure(text='Пользователь создан')

def login_user():
    username = login_entry.get("1.0", tkinter.END).strip()
    password = passwd_entry.get("1.0", tkinter.END).strip()
    con = sqlite3.connect('users.db')
    cursor = con.cursor()
    cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
    user = cursor.fetchone()
    con.close()

    if user:
        message_label1.configure(text=f'Добро пожаловать, {user[1]}!') 
        print(f'Добро пожаловать, {user[1]}!')
    else:
        message_label1.configure(text='Неправильный логин или пароль!')

label1 = customtkinter.CTkLabel(master=app, height=15, width=120, text="Введите логин").pack(pady=10)

login_entry = customtkinter.CTkTextbox(master=app, height=30, width=120)
login_entry.pack(pady=5)

label2 = customtkinter.CTkLabel(master=app, height=15, width=120, text="Введите пароль").pack(pady=5)

passwd_entry = customtkinter.CTkTextbox(master=app, height=30, width=120)
passwd_entry.pack(pady=5)

def register_user():
    username = new_login_entry.get("1.0", tkinter.END).strip()  
    password = new_password_entry.get("1.0", tkinter.END).strip() 
    if username and password:
        save_new_user(username, password)
        new_login_entry.delete("1.0", tkinter.END)  
        new_password_entry.delete("1.0", tkinter.END)  
    else:
        message_label.configure(text='Требуется заполнить все поля!')

signin_button = customtkinter.CTkButton(master=app, height=30, width=120, text='Войти', command=login_user).pack(pady=5)

def open_signup_window():
    app1 = customtkinter.CTk()
    app1.title('Регистрация нового пользователя')
    app1.geometry('400x430')
    
    global new_login_entry
    global new_password_entry
    global message_label

    label3 = customtkinter.CTkLabel(master=app1, height=15, width=120, text="Введите новый логин").pack(pady=5)
    new_login_entry = customtkinter.CTkTextbox(master=app1, height=30, width=120)
    new_login_entry.pack(pady=5)

    label4 = customtkinter.CTkLabel(master=app1, height=15, width=120, text="Введите новый пароль").pack(pady=5)
    new_password_entry = customtkinter.CTkTextbox(master=app1, height=30, width=120)
    new_password_entry.pack(pady=5)

    signup_button = customtkinter.CTkButton(master=app1, height=30, width=120, text='Сохранить пользователя', command=register_user)
    signup_button.pack(pady=5)

    message_label = customtkinter.CTkLabel(master=app1, text='')
    message_label.pack(pady=5)

    app1.mainloop()

signup_open_window = customtkinter.CTkButton(master=app, height=30, width=120, text='Зарегистрироваться', command=open_signup_window)
signup_open_window.pack(pady=5)

message_label1=customtkinter.CTkLabel(master=app, text='')
message_label1.pack(pady=5)

app.mainloop()