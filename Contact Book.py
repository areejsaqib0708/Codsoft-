import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
# **********************MAIN WINDOW**********************
contacts = [
        {"name": "Ali Saqib", "phone": "0336-1426343", "email": "alisaqib@gmail.com", "address": "123 Main St"},
        {"name": "Ayesha", "phone": "0351-4280787", "email": "ayesha@gmail.com", "address": "739 Pine Road"}]

def Main_Window():
    root = Tk()
    root.title("")
    root.geometry("440x390+100+200")

    title_lbl = Label(root, text="CONTACT BOOK", font=("Bradley Hand ITC", 25, "bold"), bg="gray", fg="Black")
    title_lbl.place(x=0, y=0, width=440, height=45)

    add_Button=Button(root,command=ADD ,text="Add Contact", font=("times new roman", 22), bg="Black", fg="white")
    add_Button.place(x=110,y=55,width=200,height=50)

    View_Button = Button(root,command=VIEW_CONTACTS, text="View Contacts", font=("times new roman", 22), bg="Black", fg="white")
    View_Button.place(x=110, y=115, width=200, height=50)

    delete_Button = Button(root,command=DELETE_CONTACT,text="Delete Contact", font=("times new roman", 22), bg="Black",fg="white")
    delete_Button.place(x=110, y=175, width=200, height=50)

    update_Button = Button(root,command=UPDATE_CONTACT, text="Update Contact", font=("times new roman", 22), bg="Black", fg="white")
    update_Button.place(x=110, y=235, width=200, height=50)

    Search_Button = Button(root, command=SEARCH_CONTACT, text="Search Contact ", font=("times new roman", 22), bg="Black", fg="white")
    Search_Button.place(x=110, y=295, width=200, height=50)
    root.mainloop()

def ADD():
    root = Tk()
    root.title("")
    root.geometry("440x300+100+200")
    title_lbl = Label(root, text="ADD CONTACT", font=("Bradley Hand ITC", 25, "bold"), bg="gray", fg="Black")
    title_lbl.place(x=0, y=0, width=440, height=45)

    name_lbl = Label(root, relief="ridge", borderwidth=2, text="Name", font=("Bradley Hand ITC", 25, "bold"), bg="white", fg="Black")
    name_lbl.place(x=10, y=50, width=160, height=35)
    name_entry = Entry(root, relief="ridge", borderwidth=2)
    name_entry.place(x=200, y=50, width=190, height=35)

    Phone_lbl = Label(root, relief="ridge", borderwidth=2, text=" Number", font=("Bradley Hand ITC", 25, "bold"), bg="white", fg="Black")
    Phone_lbl.place(x=10, y=90, width=160, height=35)
    Phone_entry = Entry(root, relief="ridge", borderwidth=2)
    Phone_entry.place(x=200, y=90, width=190, height=35)

    Email_lbl = Label(root, relief="ridge", borderwidth=2, text=" Email", font=("Bradley Hand ITC", 25, "bold"), bg="white", fg="Black")
    Email_lbl.place(x=10, y=130, width=160, height=35)
    Email_entry = Entry(root, relief="ridge", borderwidth=2)
    Email_entry.place(x=200, y=130, width=190, height=35)

    Address_lbl = Label(root, relief="ridge", borderwidth=2, text=" Address", font=("Bradley Hand ITC", 25, "bold"), bg="white", fg="Black")
    Address_lbl.place(x=10, y=170, width=160, height=35)
    Address_entry = Entry(root, relief="ridge", borderwidth=2)
    Address_entry.place(x=200, y=170, width=190, height=35)

    def add_to_contacts():
        new_contact = {
            "name": name_entry.get(),
            "phone": Phone_entry.get(),
            "email": Email_entry.get(),
            "address": Address_entry.get()}
        contacts.append(new_contact)
        messagebox.showinfo("Contact Added", "Contact has been successfully added!")
    add_Button = Button(root,command=add_to_contacts, text="Add to Contacts", font=("times new roman", 23), bg="Black", fg="white")
    add_Button.place(x=100, y=220, width=240, height=50)
    root.mainloop()

def VIEW_CONTACTS():
    root = Tk()
    root.title("")
    root.geometry("550x300+100+200")

    title_lbl = Label(root, text="CONTACTS LISTS", font=("Bradley Hand ITC", 25, "bold"), bg="Gray", fg="white")
    title_lbl.place(x=0, y=0, width=550, height=45)

    List = ttk.Treeview(root, columns=("Name", "Phone Number", "Email", "Address"), show="headings")
    List.place(x=10, y=50, width=530, height=240)

    List.heading("Name", text="Name")
    List.heading("Phone Number", text="Phone Number")
    List.heading("Email", text="Email")
    List.heading("Address", text="Address")

    List.column("Name", width=100)
    List.column("Phone Number", width=120)
    List.column("Email", width=150)
    List.column("Address", width=160)
    for contact in contacts:
        List.insert("", "end", values=(contact["name"], contact["phone"], contact["email"], contact["address"]))
    root.mainloop()

def DELETE_CONTACT():
    def delete_selected():
        selected_item = List.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select a contact to delete.")
            return
        for item in selected_item:
            contact_index = List.index(item)
            del contacts[contact_index]
            List.delete(item)
        messagebox.showinfo("Contact Deleted", "Contact(s) have been successfully deleted!")
        root.destroy()

    root = Tk()
    root.title("")
    root.geometry("500x300+100+200")
    title_lbl = Label(root, text="DELETE CONTACT", font=("Bradley Hand ITC", 25, "bold"), bg="gray", fg="Black")
    title_lbl.place(x=0, y=0, width=500, height=45)
    List = ttk.Treeview(root, columns=("Name", "Phone Number", "Email", "Address"), show="headings")
    List.place(x=10, y=50, width=480, height=240)

    List.heading("Name", text="Name")
    List.heading("Phone Number", text="Phone Number")
    List.heading("Email", text="Email")
    List.heading("Address", text="Address")

    List.column("Name", width=100)
    List.column("Phone Number", width=120)
    List.column("Email", width=150)
    List.column("Address", width=100)

    for contact in contacts:
        List.insert("", "end", values=(contact["name"], contact["phone"], contact["email"], contact["address"]))
    delete_button = Button(root, command=delete_selected, text="Delete Selected Contact", font=("times new roman", 19),bg="red", fg="white")
    delete_button.place(x=120, y=230, width=280, height=38)

    root.mainloop()

def UPDATE_CONTACT():
    def update_selected():
        selected_item = List.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select a contact to update.")
            return

        for item in selected_item:
            contact_index = List.index(item)
            updated_contact = {
                "name": name_entry.get(),
                "phone": Phone_entry.get(),
                "email": Email_entry.get(),
                "address": Address_entry.get()
            }
            contacts[contact_index] = updated_contact
            List.item(item, values=(updated_contact["name"], updated_contact["phone"], updated_contact["email"], updated_contact["address"]))
        messagebox.showinfo("Contact Updated", "Contact(s) have been successfully updated!")
        root.destroy()

    root = Tk()
    root.title("")
    root.geometry("600x400+100+200")
    title_lbl = Label(root, text="UPDATE CONTACT", font=("Bradley Hand ITC", 25, "bold"), bg="Gray", fg="white")
    title_lbl.place(x=0, y=0, width=600, height=45)

    List = ttk.Treeview(root, columns=("Name", "Phone Number", "Email", "Address"), show="headings")
    List.place(x=10, y=50, width=580, height=160)

    List.heading("Name", text="Name")
    List.heading("Phone Number", text="Phone Number")
    List.heading("Email", text="Email")
    List.heading("Address", text="Address")

    List.column("Name", width=150)
    List.column("Phone Number", width=120)
    List.column("Email", width=150)
    List.column("Address", width=160)

    for contact in contacts:
        List.insert("", "end", values=(contact["name"], contact["phone"], contact["email"], contact["address"]))
    name_lbl = Label(root, text="Name", font=("Bradley Hand ITC", 15, "bold"), bg="rosybrown", fg="white")
    name_lbl.place(x=10, y=220, width=100, height=25)
    name_entry = Entry(root)
    name_entry.place(x=120, y=220, width=200, height=25)

    Phone_lbl = Label(root, text="Number", font=("Bradley Hand ITC", 15, "bold"), bg="rosybrown", fg="white")
    Phone_lbl.place(x=10, y=250, width=100, height=25)
    Phone_entry = Entry(root)
    Phone_entry.place(x=120, y=250, width=200, height=25)

    Email_lbl = Label(root, text="Email", font=("Bradley Hand ITC", 15, "bold"), bg="rosybrown", fg="white")
    Email_lbl.place(x=10, y=280, width=100, height=25)
    Email_entry = Entry(root)
    Email_entry.place(x=120, y=280, width=200, height=25)

    Address_lbl = Label(root, text="Address", font=("Bradley Hand ITC", 15, "bold"), bg="rosybrown", fg="white")
    Address_lbl.place(x=10, y=310, width=100, height=25)
    Address_entry = Entry(root)
    Address_entry.place(x=120, y=310, width=200, height=25)

    update_button = Button(root, command=update_selected, text="Update Selected Contact", font=("times new roman", 14), bg="dodgerblue", fg="white")
    update_button.place(x=350, y=260, width=200, height=40)

    root.mainloop()

def SEARCH_CONTACT():
    def search():
        query = search_entry.get().lower()
        matching_contacts = []
        for contact in contacts:
            if (query in contact["name"].lower()
                or query in contact["phone"]
                or query in contact["email"].lower()
                or query in contact["address"].lower() ):
                matching_contacts.append(contact)

        result_list.delete(0, "end")
        if not matching_contacts:
            error_label.config(text="No matching contacts found.")
        else:
            error_label.config(text="")
            for contact in matching_contacts:
                result_list.insert("end", f"{contact['name']} - {contact['phone']}- {contact['email']}- {contact['address']}")

    root = Tk()
    root.title("")
    root.geometry("500x250+100+200")
    title_lbl = Label(root, text="SEARCH CONTACT", font=("Bradley Hand ITC", 25, "bold"), bg="Gray", fg="white")
    title_lbl.place(x=0, y=0, width=450, height=45)

    search_lbl = Label(root, text="Search:", font=("Bradley Hand ITC", 15, "bold"), bg="rosybrown", fg="white")
    search_lbl.place(x=10, y=60, width=80, height=25)
    search_entry = Entry(root)
    search_entry.place(x=100, y=60, width=200, height=25)
    search_button = Button(root, command=search, text="Search", font=("times new roman", 14), bg="dodgerblue", fg="white")
    search_button.place(x=310, y=60, width=80, height=25)

    error_label = Label(root, text="", font=("times new roman", 14), fg="red")
    error_label.place(x=10, y=90, width=380, height=25)

    result_list = Listbox(root, font=("times new roman", 14), bg="white", fg="black")
    result_list.place(x=10, y=120, width=480, height=100)

    root.mainloop()

Main_Window()


