import customtkinter as ctk

window = ctk.CTk()
window.geometry("300x500")
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
window.title("Login Page")

# frame
login_frame = ctk.CTkFrame(width=250, height=360, border_width=3, corner_radius=20, master=window)
login_frame.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

# label
login_label = ctk.CTkLabel(master=login_frame, text="Login", font=("decorative", 40), bg_color='transparent')
login_label.place(relx=0.5, rely=0.2, anchor=ctk.CENTER)
# Email/Username Entry
user_entry = ctk.CTkEntry(master=login_frame, width=200, placeholder_text="Username")
user_entry.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
# Password Entry
password_entry = ctk.CTkEntry(master=login_frame, width=200, placeholder_text="Password")
password_entry.place(relx=0.5, rely=0.6, anchor=ctk.CENTER)

# login button
login_button = ctk.CTkButton(width=100,text="Log in", master=login_frame, hover_color="Black")
login_button.place(relx=0.5, rely=0.8, anchor=ctk.CENTER)

signup_label = ctk.CTkLabel(master=login_frame, text="Don't have an account:", font=("Arial", 10),
                            bg_color='transparent')
signup_label.place(relx=0.5, rely=0.9, anchor=ctk.CENTER)

window.mainloop()
