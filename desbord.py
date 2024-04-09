from tkinter import*
from tkinter import ttk,messagebox
import sqlite3



class ims:
    def __init__(self,root):
        self.root=root
        self.root.state('zoomed')
        self.root.title("Inventory Management System")
        title=Label(self.root,text="Inventory Management System",font=("times new roman",20,"bold"),bd=10,fg="black",bg="navajowhite1").pack(fill=X)
        par_frame=Frame(root,bd=20)
        Label(par_frame,text="Purchase Entry",bd=10,bg="burlywood2",font=("times new roman",15,"bold")).pack(fill=X)
        parchase_frame=Frame(par_frame)
        parchase_table=ttk.Treeview(parchase_frame,columns=("purchaseid","productname","vendorname","vendormobile","purchasequantity","purchaseprice","date"))
        style = ttk.Style()

        



# _________________________________________________________________________________________________________________________________________________________________________________________________________________________________
# Main Display
        menu=Frame(self.root,bg="burlywood1",bd=20)
        menu.pack(side=LEFT,fill=Y)

        main_2=Frame(root,bd=10)
        Label(main_2,text="Purchase Entry \n [0]",bd=50,font=("times new roman",13,"bold"),bg="burlywood2").place(x=50,y=50,height=100,width=200)
        Label(main_2,text="Sales Entry \n [0]",bd=50,font=("times new roman",13,"bold"),bg="burlywood2").place(x=280,y=50,height=100,width=200)
        Label(main_2,text="Product List \n [0]",bd=50,font=("times new roman",13,"bold"),bg="burlywood2").place(x=510,y=50,height=100,width=200)
        Label(main_2,text="Stock \n [0]",bd=50,font=("times new roman",13,"bold"),bg="burlywood2").place(x=740,y=50,height=100,width=200)
        Label(main_2,text="Purchase Orders \n [0]",bd=50,font=("times new roman",13,"bold"),bg="burlywood2").place(x=50,y=180,height=100,width=200)
        Label(main_2,text="Sales Orders \n [0]",bd=50,font=("times new roman",13,"bold"),bg="burlywood2").place(x=280,y=180,height=100,width=200)
        Label(main_2,text="Profit Loss \n [0]",bd=50,font=("times new roman",13,"bold"),bg="burlywood2").place(x=510,y=180,height=100,width=200)
        main_2.pack(expand=1,fill=BOTH)
# _________________________________________________________________________________________________________________________________________________________________________________________________________________________________

        par_frame=Frame(root,bd=20)
        Label(par_frame,text="Purchase Entry",bd=10,bg="burlywood2",font=("times new roman",15,"bold")).pack(fill=X)
     

        Label(par_frame,text="Purchase ID:",font=("times new roman",14,"bold")).place(x=50,y=70)
        id_value=IntVar()
        id_name = Entry(par_frame,font=("times new roman",14), textvariable= id_value).place(x=170,y=70,width=70,height=30)
        Label(par_frame,text="Product Name:",font=("times new roman",14,"bold")).place(x=290,y=70)
        product_value=StringVar()
        product_name = Entry(par_frame,font=("times new roman",14), textvariable= product_value).place(x=430,y=70,width=300,height=30)
        Label(par_frame,text="Date(dd-mm-yyyy):",font=("times new roman",14,"bold")).place(x=780,y=70)
        date_value=StringVar()
        Date = Entry(par_frame,font=("times new roman",14), textvariable= date_value).place(x=950,y=70,width=140,height=30)


        Label(par_frame,text="Vendor Name:",font=("times new roman",14,"bold")).place(x=50,y=130)
        Vendor_value=StringVar()
        Vendor_name = Entry(par_frame,font=("times new roman",14), textvariable= Vendor_value).place(x=180,y=130,width=300,height=30)
        Label(par_frame,text="Vendor Mobile:",font=("times new roman",14,"bold")).place(x=530,y=130)
        mobile_value=IntVar()
        Vendor_mobile = Entry(par_frame,font=("times new roman",14), textvariable= mobile_value).place(x=670,y=130,width=200,height=30)


        Label(par_frame,text="Purchase Quantity:",font=("times new roman",14,"bold")).place(x=50,y=190)
        Purchase_Quantity_value=StringVar()
        Purchase_Quantity = Entry(par_frame,font=("times new roman",14), textvariable= Purchase_Quantity_value).place(x=220,y=190,width=150,height=30)
        Label(par_frame,text="Purchase Price:",font=("times new roman",14,"bold")).place(x=400,y=190)
        price_value=IntVar()
        price = Entry(par_frame,font=("times new roman",14), textvariable= price_value).place(x=550,y=190,width=150,height=30)


        parchase_frame=Frame(par_frame)
        scrolly=Scrollbar(parchase_frame,orient=VERTICAL)
        scrollx=Scrollbar(parchase_frame,orient=HORIZONTAL)

        parchase_table=ttk.Treeview(parchase_frame,columns=("purchaseid","productname","vendorname","vendormobile","purchasequantity","purchaseprice","date"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("times new roman", 13,"bold"))
        style.configure("Treeview.Column", font=("times new roman", 12))

        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.pack(side=BOTTOM,fill=X)

        parchase_table.heading("purchaseid",text="ID",anchor=W)
        parchase_table.heading("productname",text="Purchase Name",anchor=W)
        parchase_table.heading("vendorname",text="Vendor Name",anchor=W)
        parchase_table.heading("vendormobile",text="Vendor Mobile",anchor=W)
        parchase_table.heading("purchasequantity",text="Quantity",anchor=W)
        parchase_table.heading("purchaseprice",text="Purchase Price",anchor=W)
        parchase_table.heading("date",text="Date",anchor=W)

        parchase_table["show"]="headings"
        
        parchase_table.column("purchaseid",width=50)
        parchase_table.column("productname",width=250)
        parchase_table.column("vendorname",width=250)
        parchase_table.column("vendormobile",width=150)
        parchase_table.column("purchasequantity",width=100)
        parchase_table.column("purchaseprice",width=200)
        parchase_table.column("date",width=100)

        parchase_table.pack(fill=BOTH,side=BOTTOM)
        
        def show():
            f=parchase_table.focus()
            content=(parchase_table.item(f))
            row=content['values']
            print(row)
        
        
        
        
        parchase_table.bind("<ButtonRelease-1>")
        show()
        
    
# _________________________________________________________________________________________________________________________________________________________________________________________________________________________________
# functions
        
        def add_data():
            con=sqlite3.connect(database='ims.db')
            cur=con.cursor()
            try:
                if  id_value.get()=="":
                    messagebox.showerror("Error","ID must be required")
                else:
                    cur.execute("Select * from parchase_table where purchaseid=?",(id_value.get(),))
                    row=cur.fetchone()
                    if row !=None:
                        messagebox.showerror("Error","Id already assigned")
                    else:
                        cur.execute("Insert into parchase_table (purchaseid,productname,vendorname,vendormobile,purchasequantity,purchaseprice,date) values(?,?,?,?,?,?,?)",(
                            id_value.get(),
                            product_value.get(),
                            Vendor_value.get(),
                            mobile_value.get(),
                            Purchase_Quantity_value.get(),
                            price_value.get(),
                            date_value.get()
                        ))
                        con.commit()
                        messagebox.showinfo("Success","Purchase entry added")
                        add()
                        show()
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to :{str(ex)}")


        def add():
            con=sqlite3.connect(database='ims.db')
            cur=con.cursor()
            try:
                cur.execute("select * from parchase_table")
                rows=cur.fetchall()
                parchase_table.delete(*parchase_table.get_children())
                for row in rows:
                    parchase_table.insert('',END,values=row)

            except Exception as ex:
                messagebox.showerror("Error",f"Error due to :{str(ex)}")



        def purchase():
            hide(main_2)
            par_frame.pack(expand=1,fill=BOTH)
            parchase_frame.place(x=10,y=350,width=1300)
            add()


        Button(par_frame,text="Save",command=add_data,fg="white",bg="green",font=("times new roman",14,"bold")).place(x=50,y=250,width=100)
        Button(par_frame,text="Update",fg="white",bg="blue",font=("times new roman",14,"bold")).place(x=170,y=250,width=100)
        Button(par_frame,text="Delete",fg="white",bg="red",font=("times new roman",14,"bold")).place(x=290,y=250,width=100)

        def hide(widget): 
            widget.pack_forget() 

        def mainmenu():
            hide(par_frame)
            hide(parchase_frame)
            main_2.pack(expand=1,fill=BOTH)

        def hide(widget): 
            widget.pack_forget() 
            


        l1=Button(menu,text="Menubar",command=mainmenu,font=("times new roman",18,"bold"),bg="burlywood1").pack(pady=10)
        Button(menu,text="Purchase Entry",command=purchase,font=("times new roman",13,"bold")).pack(pady=5,fill=X)
        Button(menu,text="Sales Entry",font=("times new roman",13,"bold")).pack(pady=5,fill=X)
        Button(menu,text="Product List",font=("times new roman",13,"bold")).pack(pady=5,fill=X)
        Button(menu,text="Stock",font=("times new roman",13,"bold")).pack(pady=5,fill=X)
        Button(menu,text="Purchase Orders",font=("times new roman",13,"bold")).pack(pady=5,fill=X)
        Button(menu,text="Sales Orders",font=("times new roman",13,"bold")).pack(pady=5,fill=X)
        Button(menu,text="Profit Loss",font=("times new roman",13,"bold")).pack(pady=5,fill=X)

        # footer=Label(root,text="copyright IMS | All rights reserved!",font=("times new roman",12),bg="navajowhite").pack(fill=X,side=BOTTOM)
root=Tk()
obj=ims(root)
root.mainloop()