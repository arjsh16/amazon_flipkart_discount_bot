#importing the libraries
from  scraping import *
from send_mail import *
import time
import tkinter as tk
from tkinter import messagebox
#defining the fuc=nction that starts scraing when the button is clicked
def start_scraping():
    start_button.pack_forget()
    user_mail=mail_entry.get()
    book_link = link_entry.get()
    try:
        price_min = float(min_price_entry.get())
        price_max = 100
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for the minimum discount input.")
        return
    if price_min>=100:
        messagebox.showerror("Input Error", "Please enter valid numbers for the minimum discount input.")
        return
    if not mail_entry or not book_link:
        messagebox.showerror("Input Error", "Please fill in all the fields.")
        return

    if "amazon" in book_link:
        messagebox.showinfo("Success", f"Checking on Amazon for atleast {price_min}% discount")
        status_label.pack(pady=(10, 0))
        i=1
        while i<2:
            price=amazon_lookup(book_link)
            if price_min<=price:
                send_mail(user_mail,book_link,price)
                root.destroy()
                i+=5
                exit()
            time.sleep(300) 

    elif "flipkart" in book_link:
        messagebox.showinfo("Success", f"Checking on Flipkart for atleast {price_min}% discount")
        i=1
        while i<2:
            price=flipkart_lookup(book_link)
            price=float(price)
            if price_min<=price:
                send_mail(user_mail,book_link,price)
                root.destroy()
                i+=5
                exit()
            time.sleep(300) 
    else:
        messagebox.showerror("Input Error", "Please enter a valid Amazon or Flipkart link.")
        return
    
    status_label.config(text="Scraping started...")
#creating the gui
root = tk.Tk()
root.title("Item Discounts Checker")
root.geometry("400x350")
root.configure(bg='#001F3F')
#colour pallete for the gui
bg_color = '#001F3F'
input_bg_color = "#ECDFCC"
button_color = "#ECDFCC"
text_color = "#ECDFCC"

tk.Label(root, text="Mail ID:", bg=bg_color, fg=text_color,font=("Arial", 15)).pack(pady=(10, 0))
mail_entry = tk.Entry(root, width=40, bg=input_bg_color)
mail_entry.pack(pady=5)

tk.Label(root, text="Item Link:", bg=bg_color, fg=text_color,font=("Arial", 15)).pack(pady=(10, 0))
link_entry = tk.Entry(root, width=40, bg=input_bg_color)
link_entry.pack(pady=5)

tk.Label(root, text="Minimum Discount:", bg=bg_color, fg=text_color,font=("Arial", 15)).pack(pady=(10, 0))
min_price_entry = tk.Entry(root, width=40, bg=input_bg_color)
min_price_entry.pack(pady=5)

start_button = tk.Button(root, text="Start Scraping", bg=button_color, fg="#001F3F", command=start_scraping)
start_button.pack(pady=20)

status_label = tk.Label(root, text="", bg=bg_color, fg=text_color)
status_label.pack(pady=(10, 0))
#main loop
root.mainloop()
