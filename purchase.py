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



# =======================================================================================================================================================================================================
        
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


# =============================================================================================================================================================================================================
# purchase entry 


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
        
        
        # Functions


        def show():
            f = parchase_table.focus()
            content = parchase_table.item(f)
            row = content.get('values')  
            if row:  
                id_value.set(row[0]),
                product_value.set(row[1]),
                Vendor_value.set(row[2]),
                mobile_value.set(row[3]),
                Purchase_Quantity_value.set(row[4]),
                price_value.set(row[5]),
                date_value.set(row[6])


        parchase_table.bind("<ButtonRelease-1>", lambda event: show())
    
        
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


        def update_data():
            con=sqlite3.connect(database='ims.db')
            cur=con.cursor()
            try:
                if  id_value.get()=="":
                    messagebox.showerror("Error","ID must be required")
                else:
                    cur.execute("Select * from parchase_table where purchaseid=?",(id_value.get(),))
                    row=cur.fetchone()
                    if row ==None:
                        messagebox.showerror("Error","Invalid employee ID")
                    else:
                        cur.execute("Update parchase_table set productname=?,vendorname=?,vendormobile=?,purchasequantity=?,purchaseprice=?,date=? where purchaseid=?",(
                            
                            product_value.get(),
                            Vendor_value.get(),
                            mobile_value.get(),
                            Purchase_Quantity_value.get(),
                            price_value.get(),
                            date_value.get(),
                            id_value.get()
                        ))
                        con.commit()
                        messagebox.showinfo("Success","Purchase entry Update")
                        add()
                        show()
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to :{str(ex)}")


        def delete_data():
            con=sqlite3.connect(database='ims.db')
            cur=con.cursor()
            try:
                if  id_value.get()=="":
                    messagebox.showerror("Error","ID must be required")
                else:
                    cur.execute("Select * from parchase_table where purchaseid=?",(id_value.get(),))
                    row=cur.fetchone()
                    if row ==None:
                        messagebox.showerror("Error","Invalid employee ID")
                    else:
                        op=messagebox.askyesno("Confirm","Do you want to delete")
                        if op==True:
                            cur.execute("delete from parchase_table where purchaseid=?",(id_value.get(),))
                            con.commit()
                            messagebox.showerror("Delete","Iteam Deleted")
                            add()
                            show()
                            clear()
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to :{str(ex)}")


        def clear():
            id_value.set("")  
            product_value.set("")  
            Vendor_value.set("")  
            mobile_value.set("")  
            Purchase_Quantity_value.set("")  
            price_value.set("")  
            date_value.set("")  




        

        Button(par_frame,text="Save",command=add_data,fg="white",bg="green",font=("times new roman",14,"bold")).place(x=50,y=250,width=100)
        Button(par_frame,text="Update",command=update_data,fg="white",bg="blue",font=("times new roman",14,"bold")).place(x=170,y=250,width=100)
        Button(par_frame,text="Delete",command=delete_data,fg="white",bg="red",font=("times new roman",14,"bold")).place(x=290,y=250,width=100)
        Button(par_frame,text="Clear",command=clear,fg="white",bg="red",font=("times new roman",14,"bold")).place(x=410,y=250,width=100)






# ========================================================================================================================================================================================================================
# Sales Entry

        sales_frame=Frame(root,bd=20)
        Label(sales_frame,text="Sales Entry",bd=10,bg="burlywood2",font=("times new roman",15,"bold")).pack(fill=X)
     

        
        Label(sales_frame,text="Sales ID:",font=("times new roman",14,"bold")).place(x=50,y=70)
        salesid_value=IntVar()
        salesid_name = Entry(sales_frame,font=("times new roman",14), textvariable= salesid_value).place(x=170,y=70,width=70,height=30)
        Label(sales_frame,text="Product Name:",font=("times new roman",14,"bold")).place(x=290,y=70)
        salesproduct_value=StringVar()
        salesproduct_name = Entry(sales_frame,font=("times new roman",14), textvariable= salesproduct_value).place(x=430,y=70,width=300,height=30)
        Label(sales_frame,text="Date(dd-mm-yyyy):",font=("times new roman",14,"bold")).place(x=780,y=70)
        salesdate_value=StringVar()
        salesDate = Entry(sales_frame,font=("times new roman",14), textvariable= salesdate_value).place(x=950,y=70,width=140,height=30)

        Label(sales_frame,text="Vendor Name:",font=("times new roman",14,"bold")).place(x=50,y=130)
        salesVendor_value=StringVar()
        salesVendor_name = Entry(sales_frame,font=("times new roman",14), textvariable= salesVendor_value).place(x=180,y=130,width=300,height=30)
        Label(sales_frame,text="Vendor Mobile:",font=("times new roman",14,"bold")).place(x=530,y=130)
        salesmobile_value=IntVar()
        salesVendor_mobile = Entry(sales_frame,font=("times new roman",14), textvariable= salesmobile_value).place(x=670,y=130,width=200,height=30)

        Label(sales_frame,text="Sales Quantity:",font=("times new roman",14,"bold")).place(x=50,y=190)
        sales_Quantity_value=StringVar()
        sales_Quantity = Entry(sales_frame,font=("times new roman",14), textvariable= sales_Quantity_value).place(x=220,y=190,width=150,height=30)
        Label(sales_frame,text="Sales Price:",font=("times new roman",14,"bold")).place(x=400,y=190)
        salesprice_value=IntVar()
        salesprice = Entry(sales_frame,font=("times new roman",14), textvariable= salesprice_value).place(x=550,y=190,width=150,height=30)



        sales2_frame=Frame(sales_frame)
        scrolly=Scrollbar(sales2_frame,orient=VERTICAL)
        scrollx=Scrollbar(sales2_frame,orient=HORIZONTAL)

        sales_table=ttk.Treeview(sales2_frame,columns=("salesid","productname","vendorname","vendormobile","salesquantity","salesprice","date"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("times new roman", 13,"bold"))
        style.configure("Treeview.Column", font=("times new roman", 12))

        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.pack(side=BOTTOM,fill=X)

        sales_table.heading("salesid",text="ID",anchor=W)
        sales_table.heading("productname",text="sales Name",anchor=W)
        sales_table.heading("vendorname",text="Vendor Name",anchor=W)
        sales_table.heading("vendormobile",text="Vendor Mobile",anchor=W)
        sales_table.heading("salesquantity",text="Quantity",anchor=W)
        sales_table.heading("salesprice",text="sales Price",anchor=W)
        sales_table.heading("date",text="Date",anchor=W)

        sales_table["show"]="headings"
        
        sales_table.column("salesid",width=50)
        sales_table.column("productname",width=250)
        sales_table.column("vendorname",width=250)
        sales_table.column("vendormobile",width=150)
        sales_table.column("salesquantity",width=100)
        sales_table.column("salesprice",width=200)
        sales_table.column("date",width=100)

        sales_table.pack(fill=BOTH,side=BOTTOM)


        sales_table.bind("<ButtonRelease-1>", lambda event: salesshow())



        def salesshow():
                f2 = sales_table.focus()
                content2 = sales_table.item(f2)
                row = content2.get('values')  
                if row:  
                    salesid_value.set(row[0]),
                    salesproduct_value.set(row[1]),
                    salesVendor_value.set(row[2]),
                    salesmobile_value.set(row[3]),
                    sales_Quantity_value.set(row[4]),
                    salesprice_value.set(row[5]),
                    salesdate_value.set(row[6])


        




        def salesadd_data():
            con=sqlite3.connect(database='ims.db')
            cur=con.cursor()
            try:
                if  salesid_value.get()=="":
                    messagebox.showerror("Error","ID must be required")
                else:
                    cur.execute("Select * from sales_table where salesid=?",(salesid_value.get(),))
                    row=cur.fetchone()
                    if row !=None:
                        messagebox.showerror("Error","Id already assigned")
                    else:
                        cur.execute("Insert into sales_table (salesid,productname,vendorname,vendormobile,salesquantity,salesprice,date) values(?,?,?,?,?,?,?)",(
                            salesid_value.get(),
                            salesproduct_value.get(),
                            salesVendor_value.get(),
                            salesmobile_value.get(),
                            sales_Quantity_value.get(),
                            salesprice_value.get(),
                            salesdate_value.get()
                        ))
                        con.commit()
                        messagebox.showinfo("Success","Purchase entry added")
                        
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to :{str(ex)}")





        def salesadd():
            con2=sqlite3.connect(database='ims.db')
            cur2=con2.cursor()
            try:
                cur2.execute("select * from sales_table")
                rows2=cur2.fetchall()
                sales_table.delete(*sales_table.get_children())
                for row in rows2:
                    sales_table.insert('',END,values=row)

            except Exception as ex:
                messagebox.showerror("Error",f"Error due to :{str(ex)}")


        def salesupdate_data():
            con=sqlite3.connect(database='ims.db')
            cur=con.cursor()
            try:
                if  id_value.get()=="":
                    messagebox.showerror("Error","ID must be required")
                else:
                    cur.execute("Select * from sales_table where salesid=?",(salesid_value.get(),))
                    row=cur.fetchone()
                    if row ==None:
                        messagebox.showerror("Error","Invalid employee ID")
                    else:
                        cur.execute("Update sales_table set productname=?,vendorname=?,vendormobile=?,salesquantity=?,salesprice=?,date=? where salesid=?",(
                            
                            salesproduct_value.get(),
                            salesVendor_value.get(),
                            salesmobile_value.get(),
                            sales_Quantity_value.get(),
                            salesprice_value.get(),
                            salesdate_value.get(),
                            salesid_value.get()
                        ))
                        con.commit()
                        messagebox.showinfo("Success","Sales entry Update")
                        salesadd()
                        salesshow()
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to :{str(ex)}")


        def salesdelete_data():
            con=sqlite3.connect(database='ims.db')
            cur=con.cursor()
            try:
                if  id_value.get()=="":
                    messagebox.showerror("Error","ID must be required")
                else:
                    cur.execute("Select * from sales_table where salesid=?",(salesid_value.get(),))
                    row=cur.fetchone()
                    if row ==None:
                        messagebox.showerror("Error","Invalid employee ID")
                    else:
                        op=messagebox.askyesno("Confirm","Do you want to delete")
                        if op==True:
                            cur.execute("delete from sales_table where salesid=?",(salesid_value.get(),))
                            con.commit()
                            messagebox.showerror("Delete","Iteam Deleted")
                            salesadd()
                            salesshow()
                            salesclear()
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to :{str(ex)}")


        def salesclear():
            salesid_value.set("")  
            salesproduct_value.set("")  
            salesVendor_value.set("")  
            salesmobile_value.set("")  
            sales_Quantity_value.set("")  
            salesprice_value.set("")  
            salesdate_value.set("")  











        Button(sales_frame,text="Save",command=salesadd_data,fg="white",bg="green",font=("times new roman",14,"bold")).place(x=50,y=250,width=100)
        Button(sales_frame,text="Update",command=salesupdate_data,fg="white",bg="blue",font=("times new roman",14,"bold")).place(x=170,y=250,width=100)
        Button(sales_frame,text="Delete",command=salesdelete_data,fg="white",bg="red",font=("times new roman",14,"bold")).place(x=290,y=250,width=100)
        Button(sales_frame,text="Clear",command=salesclear,fg="white",bg="red",font=("times new roman",14,"bold")).place(x=410,y=250,width=100)







# ===================================================================================================================================================================================================================================
         
        def purchase():
            hide(main_2)
            hide(sales_frame)
            par_frame.pack(expand=1,fill=BOTH)
            parchase_frame.place(x=10,y=350,width=1300)
            add()


        def sales():
                hide(main_2)
                hide(par_frame)
                hide(parchase_frame)
                sales_frame.pack(expand=1,fill=BOTH)
                sales2_frame.place(x=10,y=350,width=1300)
                salesadd()

        
        def mainmenu():
            hide(sales_frame)
            hide(par_frame)
            hide(parchase_frame)
            main_2.pack(expand=1,fill=BOTH)

        def hide(widget): 
            widget.pack_forget() 

        l1=Button(menu,text="Menubar",command=mainmenu,font=("times new roman",18,"bold"),bg="burlywood1").pack(pady=10)
        Button(menu,text="Purchase Entry",command=purchase,font=("times new roman",13,"bold")).pack(pady=5,fill=X)
        Button(menu,text="Sales Entry",command=sales,font=("times new roman",13,"bold")).pack(pady=5,fill=X)
        Button(menu,text="Product List",font=("times new roman",13,"bold")).pack(pady=5,fill=X)
        Button(menu,text="Stock",font=("times new roman",13,"bold")).pack(pady=5,fill=X)
        Button(menu,text="Purchase Orders",font=("times new roman",13,"bold")).pack(pady=5,fill=X)
        Button(menu,text="Sales Orders",font=("times new roman",13,"bold")).pack(pady=5,fill=X)
        Button(menu,text="Profit Loss",font=("times new roman",13,"bold")).pack(pady=5,fill=X)



root=Tk() 
obj=ims(root)
root.mainloop()
