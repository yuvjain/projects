
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import mysql.connector


class Plant:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1530x790+0+0')
        self.root.title('SEED MANAGEMENT SYSTEM')
        
        #criminal variables start
        self.var_com_customersearch = StringVar()
        self.var_customersearch = StringVar()

        self.var_customerId=IntVar()
        self.var_customerName=StringVar()
        self.var_DateOfBirth=StringVar()
        self.var_Email=StringVar()
        self.var_ContactNumber=IntVar() 
        self.var_country=StringVar()
        self.var_PaymentMethod=StringVar()

        #crime variables start
        self.var_com_seedsearch = StringVar()
        self.var_seedsearch = StringVar()

        self.var_CategoryId=IntVar()
        self.var_CategoryName=StringVar()
        self.var_Description=StringVar()

        #case variables start
        self.var_com_sales_search = StringVar()
        self.var_sales_search = StringVar()

        self.var_TransactionId=StringVar()
        self.var_TransactionDate=StringVar()
        self.var_PaymentStatus=StringVar()
        self.var_TotalAmount=StringVar()
        self.var_QuantitySold=StringVar()
        self.var_customerId=StringVar()
        self.var_ProductId=StringVar()
        #case variables end

        #prison variables start
        self.var_com_SeedProduct_search = StringVar()
        self.var_SeedProduct_search = StringVar()
        #prison variables end

        #officer variables start
        self.var_com_supplier_search = StringVar()
        self.var_supplier_search = StringVar()
        
        #officer variables end  
        lbl_title=Label(self.root,text='SEED SOFTWARE',font=('times new roman',35,'bold'),bg='black',fg='gold')
        lbl_title.place(x=0,y=0,width=1530,height=70)

        # style = ttk.Style()
        # style.configure('TNotebook', background='lightblue')
        # style.configure('TNotebook.Tab', background='lightblue')
        

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(pady=100)
        self.notebook.pack(fill=BOTH, expand=YES)

        self.create_customer_tab()
        self.create_transaction_tab()
        self.create_category_tab()
        self.create_seedprod_tab()
        self.create_supplier_tab()

    def create_customer_tab(self):
        style = ttk.Style()

        # Configure the style for the notebook frame
        style.configure('Custom.TFrame', background='lightblue')
        customer_tab = ttk.Frame(self.notebook, style='Custom.TFrame')
        self.notebook.add(customer_tab, text="Customer")

        ttk.Label(customer_tab, text="").pack()

        # Upper_frame 
        upper_frame = LabelFrame(customer_tab, bd=2, relief=RIDGE, text='Customer Information', font=('times new roman', 11, 'bold'), fg='red', bg='white')
        upper_frame.place(x=10, y=10, width=1500, height=560)

        firstname=Label(upper_frame,text='CustomerName:',font=('arial',11,'bold'),bg='white')
        firstname.grid(row=0,column=0,padx=2,sticky=W)

        caseentry=ttk.Entry(upper_frame, textvariable=self.var_customerName, width=22,font=('arial',11,'bold'))
        caseentry.grid(row=0,column=1,padx=2,sticky=W)

        #DOB
        lbl_dob=Label(upper_frame,font=('arial',12,'bold'),text="DOB:",bg='white')
        lbl_dob.grid(row=0,column=4,sticky=W,padx=2,pady=7)

        txt_dob=ttk.Entry(upper_frame,textvariable=self.var_DateOfBirth,width=22,font=('arial',11,'bold'))
        txt_dob.grid(row=0,column=5,sticky=W,padx=2,pady=7)

        #Email
        lbl_Email=Label(upper_frame,font=('arial',12,'bold'),text="Email:",bg='white')
        lbl_Email.grid(row=1,column=4,sticky=W,padx=2,pady=7)

        txt_Email=ttk.Entry(upper_frame,textvariable=self.var_Email,width=22,font=('arial',11,'bold'))
        txt_Email.grid(row=1,column=5,sticky=W,padx=2,pady=7)

        # ContactNumber
        ContactNumber=Label(upper_frame,font=('arial',12,'bold'),text="ContactNumber:",bg='white')
        ContactNumber.grid(row=1,column=0,sticky=W,padx=2,pady=7)

        txt_ContactNumber=ttk.Entry(upper_frame,textvariable=self.var_ContactNumber,width=22,font=('arial',11,'bold'))
        txt_ContactNumber.grid(row=1,column=1,sticky=W,padx=2,pady=7)

        #country
        lbl_country=Label(upper_frame,font=('arial',12,'bold'),text="country:",bg='white')
        lbl_country.grid(row=1,column=2,sticky=W,padx=2,pady=7)

        txt_country=ttk.Entry(upper_frame,textvariable=self.var_country,width=22,font=('arial',11,'bold'))
        txt_country.grid(row=1,column=3,sticky=W,padx=2,pady=7)

        lbl_coustomer_id=Label(upper_frame,font=('arial',12,'bold'),text="customerId:",bg='white')
        lbl_coustomer_id.grid(row=2,column=0,sticky=W,padx=2,pady=7)

        txt_coustomer_id=ttk.Entry(upper_frame,textvariable=self.var_customerId,width=22,font=('arial',11,'bold'))
        txt_coustomer_id.grid(row=2,column=1,sticky=W,padx=2,pady=7)

        #Status
        lbl_status=Label(upper_frame,font=('arial',12,'bold'),text="payment Status:",bg='white')
        lbl_status.grid(row=3,column=0,sticky=W,padx=2,pady=7)

        txt_status=ttk.Entry(upper_frame,textvariable=self.var_PaymentMethod,width=22,font=('arial',11,'bold'))
        txt_status.grid(row=3,column=1,sticky=W,padx=2,pady=7)


        # Buttons for Criminal Information
        button_frame = Frame(upper_frame, bd=2, relief=RIDGE, bg='white')
        button_frame.place(x=5, y=200, width=620, height=45)
        btn_add = Button(button_frame,command=self.add_customer_data, text='Save', font=('arial', 13, 'bold'), width=14, bg='blue', fg='white')
        btn_add.grid(row=0, column=0, padx=3, pady=5)
        
        btn_update=Button(button_frame,command=self.update_customer_data,text='Update',font=('arial',13,'bold'),width=14,bg='blue',fg='white')
        btn_update.grid(row=0,column=1,padx=3,pady=5)

        #Delete Button
        btn_delete = Button(button_frame, text='Delete', font=('arial', 13, 'bold'), width=14, bg='blue', fg='white', command=self.delete_customer_button_clicked)
        btn_delete.grid(row=0, column=2, padx=3, pady=5)

        #Clear Button
        btn_clear=Button(button_frame,command=self.clear_customer_data,text='Clear',font=('arial',13,'bold'),width=14,bg='blue',fg='white')
        btn_clear.grid(row=0,column=3,padx=3,pady=5)

        #Main_frame
        Main_frame = Frame(customer_tab, bd=2, relief=RIDGE, bg='white')
        Main_frame.place(x=10, y=280, width=1500, height=560)
        
        down_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text='Customer Information Table',font=('times new roman',11,'bold'),fg='red',bg='white')
        down_frame.place(x=10,y=10,width=1480,height=270)

        search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,text='Search Customer Record',font=('times new roman',11,'bold'),fg='red',bg='white')
        search_frame.place(x=0,y=0,width=1470,height=60)

        search_by=Label(search_frame,font=("arial",11,"bold"),text="Search By:",bg="red",fg="white")
        search_by.grid(row=0,column=0,sticky=W,padx=5)

        # self.var_com_search=StringVar()
        combo_search_box=ttk.Combobox(search_frame,textvariable=self.var_com_customersearch,font=("arial",11,"bold"),width=18,state='readonly')
        combo_search_box['value']=('Select Option','ProductId','customerId')
        combo_search_box.current(0)
        combo_search_box.grid(row=0,column=1,sticky=W,padx=5)

        # self.var_search=StringVar()
        search_txt=ttk.Entry(search_frame,textvariable=self.var_customersearch,width=18,font=("arial",11,"bold"))
        search_txt.grid(row=0,column=2,sticky=W,padx=5)

        #search button
        btn_search=Button(search_frame,command=self.search_customer_data,text='Search',font=("arial",13,"bold"),width=14,bg='blue')
        btn_search.grid(row=0,column=3,padx=3,pady=5)

        #all button
        btn_all=Button(search_frame,command = self.fetch_customer_data,text='Show All',font=("arial",13,"bold"),width=14,bg='blue')
        btn_all.grid(row=0,column=4,padx=3,pady=5)

        crimeagency=Label(search_frame,font=("arial",30,"bold"),text="SEED PRODUCTION",bg='white',fg='crimson')
        crimeagency.grid(row=0,column=5,sticky=W,padx=50,pady=0)

        # Table Frame
        table_frame=Frame(down_frame,bd=2,relief=RIDGE)
        table_frame.place(x=0,y=60,width=1470,height=170)

        # Scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.customer_table=ttk.Treeview(table_frame,column=("1","2","3","4","5","6","7"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.customer_table.xview)
        scroll_y.config(command=self.customer_table.yview)

        self.customer_table.heading("1",text="customerId")
        self.customer_table.heading("2",text="customerName")
        self.customer_table.heading("3",text="ContactNumber")
        self.customer_table.heading("4",text="country")
        self.customer_table.heading("5",text="Email")
        self.customer_table.heading("6",text="DateOfBirth")
        self.customer_table.heading("7",text="PaymentMethod")

        self.customer_table['show']='headings'

        self.customer_table.column("1",width=100)
        self.customer_table.column("2",width=100)
        self.customer_table.column("3",width=100)
        self.customer_table.column("4",width=100)
        self.customer_table.column("5",width=100)
        self.customer_table.column("6",width=100)
        self.customer_table.column("7",width=100)

        self.customer_table.pack(fill=BOTH,expand=1)
        self.customer_table.bind("<ButtonRelease>", self.get_customer_cursor)
        self.fetch_customer_data()

    def fetch_customer_data(self):
        # Clear the current data in the Treeview
        for item in self.customer_table.get_children():
            self.customer_table.delete(item)
        
        # Fetch the updated list of customers from the database
        conn = mysql.connector.connect(host='localhost', username='root', password='password', database='seeds')
        my_cursor = conn.cursor()
        my_cursor.execute('SELECT * FROM customer')
        rows = my_cursor.fetchall()
        conn.close()
        
        # Repopulate the Treeview with the updated data
        for row in rows:
            self.customer_table.insert('', 'end', values=row)

    def add_customer_data(self):
        if self.var_customerId.get()=="":
            messagebox.showerror('Error','All fields are required')
        else:
            try:
                conn=mysql.connector.connect(host='localhost', username='root',password='password', database='seeds')
                my_cursor=conn.cursor()
                my_cursor.execute('insert into customer values(%s,%s,%s,%s,%s,%s,%s)',(
                    self.var_customerId.get(),
                    self.var_customerName.get(),
                    self.var_ContactNumber.get(),
                    self.var_country.get(),
                    self.var_Email.get(),
                    self.var_DateOfBirth.get(),
                    self.var_PaymentMethod.get()))
                conn.commit()
                self.fetch_customer_data()
                self.clear_customer_data()
                conn.close()
                messagebox.showinfo('successful', 'Customer record has been added')
            except Exception as es:
                messagebox.showerror('error',f'Due to{str(es)}')

    def clear_customer_data(self):
        self.var_customerId.set("")
        self.var_customerName.set("")
        self.var_DateOfBirth.set("")
        self.var_Email.set("")
        self.var_ContactNumber.set("")
        self.var_country.set("")
        self.var_PaymentMethod.set("")

    def get_customer_cursor(self, event=""):
        cursor_row = self.customer_table.focus()
        content = self.customer_table.item(cursor_row)
        data = content['values']

        self.var_customerId.set(data[0])
        self.var_customerName.set(data[1])
        self.var_ContactNumber.set(data[2])
        self.var_country.set(data[3])
        self.var_Email.set(data[4])
        self.var_DateOfBirth.set(data[5])
        self.var_PaymentMethod.set(data[6])
    
    def delete_customer_button_clicked(self):
        # Get the selected customer ID from the Treeview
        selected_item = self.customer_table.focus()
        if selected_item:
            customer_id = self.customer_table.item(selected_item)['values'][0]  # Assuming customer ID is in the first column

            # Call the function to delete the customer data
            self.delete_customer_data(customer_id)

    def delete_customer_data(self, customer_id):
        selected_item = self.customer_table.focus()  # Get the selected item in the Treeview
        if selected_item:  # Check if an item is selected
            # Get the data associated with the selected item
            selected_data = self.customer_table.item(selected_item)['values']
            customer_id = selected_data[0]  # Assuming customer ID is in the first column
            try:
                conn = mysql.connector.connect(host='localhost', username='root', password='password', database='seeds')
                my_cursor = conn.cursor()
                # Execute SQL query to delete the customer data
                my_cursor.execute('DELETE FROM customer WHERE CustomerID = %s', (customer_id,))
                conn.commit()
                conn.close()
                # Refresh the customer data in the Treeview after deletion
                self.fetch_customer_data()
                # Clear the input fields after deletion
                self.clear_customer_data()
                messagebox.showinfo('Successful', 'Customer record has been deleted')
            except Exception as e:
                messagebox.showerror('Error', f'Failed to delete customer record: {str(e)}')
        else:
            messagebox.showerror('Error', 'Please select a customer record to delete')


    def update_customer_data(self):
        if self.var_customerId.get()=="":
            messagebox.showerror('Error','All fields are required')
        else:
            try:
                conn=mysql.connector.connect(host='localhost', username='root',password='password', database='seeds')
                my_cursor=conn.cursor()
                my_cursor.execute('update customer set customerName=%s, ContactNumber=%s, country=%s, Email=%s, DateOfBirth=%s, PaymentMethod=%s where customerId=%s',(
                    self.var_customerName.get(),
                    self.var_ContactNumber.get(),
                    self.var_country.get(),
                    self.var_Email.get(),
                    self.var_DateOfBirth.get(),
                    self.var_PaymentMethod.get(),
                    self.var_customerId.get()))
                conn.commit()
                self.fetch_customer_data()
                self.clear_customer_data()
                conn.close()
                messagebox.showinfo('successful', 'customer record has been added')
            except Exception as es:
                messagebox.showerror('error',f'Due to{str(es)}')

    def search_customer_data(self): 
        if self.var_com_customersearch.get()=="":
            messagebox.showerror('Error','All fields are required') 
        else:
            try:
                conn=mysql.connector.connect(host='localhost', username='root',password='password', database='seeds')
                my_cursor=conn.cursor()
                my_cursor.execute('select * from customer where '+str(self.var_com_customersearch.get())+" LIKE'%"+str(self.var_customersearch.get()+"%'"))
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.customer_table.delete(*self.customer_table.get_children())
                    for i in rows:
                        self.customer_table.insert('',END,values=i)
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror('error',f'Due to{str(es)}')


    def create_transaction_tab(self):
        transaction_tab = ttk.Frame(self.notebook)
        self.notebook.add(transaction_tab, text="transactions")

        ttk.Label(transaction_tab, text="").pack()

        # Upper_frame (Criminal Information)
        upper_frame = LabelFrame(transaction_tab, bd=2, relief=RIDGE, text='seed Related Information', font=('times new roman', 11, 'bold'), fg='red', bg='white')
        upper_frame.place(x=10, y=10, width=1500, height=560)

        caseid=Label(upper_frame,text='TransactionId:',font=('arial',11,'bold'),bg='white')
        caseid.grid(row=0,column=0,padx=2,sticky=W)

        caseentry=ttk.Entry(upper_frame,textvariable=self.var_TransactionId,width=22,font=('arial',11,'bold'))
        caseentry.grid(row=0,column=1,padx=2,sticky=W)

        startDate=Label(upper_frame,font=('arial',12,'bold'),text="TransactionDate:",bg='white')
        startDate.grid(row=0,column=2,sticky=W,padx=2,pady=7)

        txt_sDate=ttk.Entry(upper_frame,textvariable = self.var_TransactionDate,width=22,font=('arial',11,'bold'))
        txt_sDate.grid(row=0,column=3,sticky=W,padx=2,pady=7)

        #End date
        endDate=Label(upper_frame,font=('arial',12,'bold'),text="PaymentStatus:",bg='white')
        endDate.grid(row=0,column=4,sticky=W,padx=2,pady=7)

        txt_eDate=ttk.Entry(upper_frame,textvariable=self.var_PaymentStatus,width=22,font=('arial',11,'bold'))
        txt_eDate.grid(row=0,column=5,sticky=W,padx=2,pady=7)

        #TotalAmount
        TotalAmount=Label(upper_frame,font=('arial',12,'bold'),text="TotalAmount:",bg='white')
        TotalAmount.grid(row=1,column=0,sticky=W,padx=2,pady=7)

        txt_TotalAmount=ttk.Entry(upper_frame,textvariable=self.var_TotalAmount,width=22,font=('arial',11,'bold'))
        txt_TotalAmount.grid(row=1,column=1,sticky=W,padx=2,pady=7)

        # QuantitySold
        QuantitySold=Label(upper_frame,font=('arial',12,'bold'),text="QuantitySold:",bg='white')
        QuantitySold.grid(row=1,column=2,sticky=W,padx=2,pady=7)

        txt_QuantitySold=ttk.Entry(upper_frame,textvariable=self.var_QuantitySold,width=22,font=('arial',11,'bold'))
        txt_QuantitySold.grid(row=1,column=3,sticky=W,padx=2,pady=7)

        #criminal id
        lbl_coustomer_id=Label(upper_frame,font=('arial',12,'bold'),text="customerId:",bg='white')
        lbl_coustomer_id.grid(row=1,column=4,sticky=W,padx=2,pady=7)

        txt_coustomer_id=ttk.Entry(upper_frame,textvariable=self.var_customerId,width=22,font=('arial',11,'bold'))
        txt_coustomer_id.grid(row=1,column=5,sticky=W,padx=2,pady=7)

        #crime-id
        crimeid=Label(upper_frame,font=('arial',12,'bold'),text="CategoryId:",bg='white')
        crimeid.grid(row=2,column=0,sticky=W,padx=2,pady=7)

        txt_crimeid=ttk.Entry(upper_frame,textvariable=self.var_CategoryId, width=22,font=('arial',11,'bold'))
        txt_crimeid.grid(row=2,column=1,sticky=W,padx=2,pady=7)

        # Buttons for Information
        button_frame = Frame(upper_frame, bd=2, relief=RIDGE, bg='white')
        button_frame.place(x=5, y=200, width=620, height=45)
        btn_add = Button(button_frame,command=self.add_case_data, text='Save', font=('arial', 13, 'bold'), width=14, bg='blue', fg='white')
        btn_add.grid(row=0, column=0, padx=3, pady=5)
        
        btn_update=Button(button_frame,command=self.update_case_data,text='Update',font=('arial',13,'bold'),width=14,bg='blue',fg='white')
        btn_update.grid(row=0,column=1,padx=3,pady=5)

        #Delete Button
        btn_delete=Button(button_frame,text='Delete',font=('arial',13,'bold'),width=14,bg='blue',fg='white')
        btn_delete.grid(row=0,column=2,padx=3,pady=5)

        #Clear Button
        btn_clear=Button(button_frame,command=self.clear_case_data,text='Clear',font=('arial',13,'bold'),width=14,bg='blue',fg='white')
        btn_clear.grid(row=0,column=3,padx=3,pady=5)

         #Main_frame
        Main_frame = Frame(transaction_tab, bd=2, relief=RIDGE, bg='white')
        Main_frame.place(x=10, y=280, width=1500, height=560)
        
        down_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text='sales information Table',font=('times new roman',11,'bold'),fg='red',bg='white')
        down_frame.place(x=10,y=10,width=1480,height=270)

        search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,text='Search Customer Record',font=('times new roman',11,'bold'),fg='red',bg='white')
        search_frame.place(x=0,y=0,width=1470,height=60)

        search_by=Label(search_frame,font=("arial",11,"bold"),text="Search By:",bg="red",fg="white")
        search_by.grid(row=0,column=0,sticky=W,padx=5)

        # self.var_com_search=StringVar()
        combo_search_box=ttk.Combobox(search_frame,textvariable=self.var_com_sales_search,font=("arial",11,"bold"),width=18,state='readonly')
        combo_search_box['value']=('Select Option','TransactionId','customerId','CategoryId','TotalAmount')
        combo_search_box.current(0)
        combo_search_box.grid(row=0,column=1,sticky=W,padx=5)

        # self.var_search=StringVar()
        search_txt=ttk.Entry(search_frame,textvariable=self.var_sales_search,width=18,font=("arial",11,"bold"))
        search_txt.grid(row=0,column=2,sticky=W,padx=5)

        #search button
        btn_search=Button(search_frame,command=self.search_case_data,text='Search',font=("arial",13,"bold"),width=14,bg='blue')
        btn_search.grid(row=0,column=3,padx=3,pady=5)

        #all button
        btn_all=Button(search_frame,command=self.fetch_case_data,text='Show All',font=("arial",13,"bold"),width=14,bg='blue')
        btn_all.grid(row=0,column=4,padx=3,pady=5)

        crimeagency=Label(search_frame,font=("arial",30,"bold"),text="FARMING",bg='white',fg='crimson')
        crimeagency.grid(row=0,column=5,sticky=W,padx=50,pady=0)

        # Table Frame
        table_frame=Frame(down_frame,bd=2,relief=RIDGE)
        table_frame.place(x=0,y=60,width=1470,height=170)

        # Scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.transaction_table=ttk.Treeview(table_frame,column=("1","2","3","4","5","6","7"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.transaction_table.xview)
        scroll_y.config(command=self.transaction_table.yview)

        self.transaction_table.heading("1",text="TransactionId")
        self.transaction_table.heading("2",text="TransactionDate")
        self.transaction_table.heading("3",text="PaymentStatus")
        self.transaction_table.heading("4",text="TotalAmount")
        self.transaction_table.heading("5",text="QuantitySold")
        self.transaction_table.heading("6",text="customerId")
        self.transaction_table.heading("7",text="CategoryId")

        self.transaction_table['show']='headings'

        self.transaction_table.column("1",width=100)
        self.transaction_table.column("2",width=100)
        self.transaction_table.column("3",width=100)
        self.transaction_table.column("4",width=100)
        self.transaction_table.column("5",width=100)
        self.transaction_table.column("6",width=100)
        self.transaction_table.column("7",width=100)

        self.transaction_table.pack(fill=BOTH,expand=1)
        self.transaction_table.bind("<ButtonRelease>", self.get_case_cursor)
        self.fetch_case_data()

    def fetch_case_data(self):
        conn=mysql.connector.connect(host='localhost', username='root',password='password', database='seeds')
        my_cursor=conn.cursor()
        my_cursor.execute('select * from salestransaction')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.transaction_table.delete(*self.transaction_table.get_children())
            for i in data:
                self.transaction_table.insert('',END,values=i)
            conn.commit()
        conn.close()

    def add_case_data(self):
        if self.var_TransactionId.get()=="":
            messagebox.showerror('Error','All fields are required')
        else:
            try:
                conn=mysql.connector.connect(host='localhost', username='root',password='password', database='seeds')
                my_cursor=conn.cursor()
                my_cursor.execute('insert into salestransaction values(%s,%s,%s,%s,%s,%s,%s)',(
                    self.var_TransactionId.get(),
                    self.var_customerId.get(),
                    self.var_CategoryId.get(),
                    self.var_QuantitySold.get(),
                    self.var_TotalAmount.get(),
                    self.var_TransactionDate.get(),
                    self.var_PaymentStatus.get()))
                conn.commit()
                self.fetch_case_data()
                self.clear_case_data()
                conn.close()
                messagebox.showinfo('successful', 'Transaction record has been added')
            except Exception as es:
                messagebox.showerror('error',f'Due to{str(es)}')

    def clear_case_data(self):
        self.var_TransactionId.set("")
        self.var_TransactionDate.set("")
        self.var_PaymentStatus.set("")
        self.var_TotalAmount.set("")
        self.var_QuantitySold.set("")
        self.var_customerId.set("")
        self.var_CategoryId.set("")

    def get_case_cursor(self,event=""):
        cursor_row=self.transaction_table.focus()
        content=self.transaction_table.item(cursor_row)
        data=content['values']

        self.var_TransactionId.set(data[0])
        self.var_TransactionDate.set(data[1])
        self.var_PaymentStatus.set(data[2])
        self.var_TotalAmount.set(data[3])
        self.var_QuantitySold.set(data[4])
        self.var_customerId.set(data[5])
        self.var_CategoryId.set(data[6])

    def update_case_data(self):
        if not all([self.var_TransactionId.get(), self.var_customerId.get(), self.var_CategoryId.get(), self.var_QuantitySold.get(), self.var_TotalAmount.get(), self.var_TransactionDate.get(), self.var_PaymentStatus.get()]):
            messagebox.showerror('Error', 'All fields are required')
            return

        try:
            conn = mysql.connector.connect(host='localhost', username='root', password='password', database='seeds')
            my_cursor = conn.cursor()
            my_cursor.execute('UPDATE salestransaction SET customerId=%s, CategoryId=%s, QuantitySold=%s, TotalAmount=%s, TransactionDate=%s, PaymentStatus=%s WHERE TransactionId=%s', (
                self.var_customerId.get(),
                self.var_CategoryId.get(),
                self.var_QuantitySold.get(),
                self.var_TotalAmount.get(),
                self.var_TransactionDate.get(),
                self.var_PaymentStatus.get(),
                self.var_TransactionId.get()
            ))
            conn.commit()
            self.fetch_case_data()
            self.clear_case_data()
            conn.close()
            messagebox.showinfo('Successful', 'Transaction record has been updated')
        except mysql.connector.Error as err:
            messagebox.showerror('Error', f'Due to {err}')

    def search_case_data(self): 
        if self.var_com_sales_search.get()=="":
            messagebox.showerror('Error','All fields are required') 
        else:
            try:
                conn=mysql.connector.connect(host='localhost', username='root',password='password', database='seeds')
                my_cursor=conn.cursor()
                my_cursor.execute('select * from salestransaction where '+str(self.var_com_sales_search.get())+" LIKE'%"+str(self.var_sales_search.get()+"%'"))
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.transaction_table.delete(*self.transaction_table.get_children())
                    for i in rows:
                        self.transaction_table.insert('',END,values=i)
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror('error',f'Due to{str(es)}')


    
    def create_category_tab(self):
        category_tab = ttk.Frame(self.notebook)
        self.notebook.add(category_tab, text="Categories")

        ttk.Label(category_tab, text="").pack()

        # Upper_frame (Criminal Information)
        upper_frame = LabelFrame(category_tab, bd=2, relief=RIDGE, text='Seed Category Details', font=('times new roman', 11, 'bold'), fg='red', bg='white')
        upper_frame.place(x=10, y=10, width=1500, height=560)

        crimeid=Label(upper_frame,text='CategoryId:',font=('arial',11,'bold'),bg='white')
        crimeid.grid(row=0,column=0,padx=2,sticky=W)

        caseentry=ttk.Entry(upper_frame,textvariable=self.var_CategoryId,width=22,font=('arial',11,'bold'))
        caseentry.grid(row=0,column=1,padx=2,sticky=W)

        crimeName=Label(upper_frame,font=('arial',12,'bold'),text="CategoryName:",bg='white')
        crimeName.grid(row=0,column=2,sticky=W,padx=2,pady=7)

        txt_cname=ttk.Entry(upper_frame,textvariable=self.var_CategoryName,width=22,font=('arial',11,'bold'))
        txt_cname.grid(row=0,column=3,sticky=W,padx=2,pady=7)

        #Crime Desc
        seedDesc=Label(upper_frame,font=('arial',12,'bold'),text="Seed description:",bg='white')
        seedDesc.grid(row=0,column=4,sticky=W,padx=2,pady=7)

        txt_sdesc=ttk.Entry(upper_frame,textvariable=self.var_Description,width=22,font=('arial',11,'bold'))
        txt_sdesc.grid(row=0,column=5,sticky=W,padx=2,pady=7)

        # Buttons for Information
        button_frame = Frame(upper_frame, bd=2, relief=RIDGE, bg='white')
        button_frame.place(x=5, y=200, width=620, height=45)
        btn_add = Button(button_frame,command=self.add_seed_data, text='Save', font=('arial', 13, 'bold'), width=14, bg='blue', fg='white')
        btn_add.grid(row=0, column=0, padx=3, pady=5)
        
        btn_update=Button(button_frame,command=self.update_seed_data,text='Update',font=('arial',13,'bold'),width=14,bg='blue',fg='white')
        btn_update.grid(row=0,column=1,padx=3,pady=5)

        #Delete Button
        btn_delete = Button(button_frame, text='Delete', font=('arial', 13, 'bold'), width=14, bg='blue', fg='white', command=self.delete_category_button_clicked)
        btn_delete.grid(row=0, column=2, padx=3, pady=5)

        #Clear Button
        btn_clear=Button(button_frame,command=self.clear_seed_data,text='Clear',font=('arial',13,'bold'),width=14,bg='blue',fg='white')
        btn_clear.grid(row=0,column=3,padx=3,pady=5)

        #Main_frame
        Main_frame = Frame(category_tab, bd=2, relief=RIDGE, bg='white')
        Main_frame.place(x=10, y=280, width=1500, height=560)
        
        down_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text='Category Information Table',font=('times new roman',11,'bold'),fg='red',bg='white')
        down_frame.place(x=10,y=10,width=1480,height=270)

        search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,text='Search Category Record',font=('times new roman',11,'bold'),fg='red',bg='white')
        search_frame.place(x=0,y=0,width=1470,height=60)

        search_by=Label(search_frame,font=("arial",11,"bold"),text="Search By:",bg="red",fg="white")
        search_by.grid(row=0,column=0,sticky=W,padx=5)

        # self.var_com_search=StringVar()
        combo_search_box=ttk.Combobox(search_frame,textvariable=self.var_com_seedsearch,font=("arial",11,"bold"),width=18,state='readonly')
        combo_search_box['value']=('Select Option','CategoryID','CategoryName')
        combo_search_box.current(0)
        combo_search_box.grid(row=0,column=1,sticky=W,padx=5)

        # self.var_search=StringVar()
        search_txt=ttk.Entry(search_frame,textvariable=self.var_seedsearch,width=18,font=("arial",11,"bold"))
        search_txt.grid(row=0,column=2,sticky=W,padx=5)

        #search button
        btn_search=Button(search_frame,command=self.search_seed_data,text='Search',font=("arial",13,"bold"),width=14,bg='blue')
        btn_search.grid(row=0,column=3,padx=3,pady=5)

        #all button
        btn_all=Button(search_frame,command=self.fetch_seed_data,text='Show All',font=("arial",13,"bold"),width=14,bg='blue')
        btn_all.grid(row=0,column=4,padx=3,pady=5)

        crimeagency=Label(search_frame,font=("arial",30,"bold"),text="FARMING",bg='white',fg='crimson')
        crimeagency.grid(row=0,column=5,sticky=W,padx=50,pady=0)

        # Table Frame
        table_frame=Frame(down_frame,bd=2,relief=RIDGE)
        table_frame.place(x=0,y=60,width=1470,height=170)

        # Scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.seedcategory_table=ttk.Treeview(table_frame,column=("1","2","3","4","5","6","7","8"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.seedcategory_table.xview)
        scroll_y.config(command=self.seedcategory_table.yview)

        self.seedcategory_table.heading("1",text="Category Id")
        self.seedcategory_table.heading("2",text="Category Name")
        self.seedcategory_table.heading("3",text="Seed description")

        self.seedcategory_table['show']='headings'

        self.seedcategory_table.column("1",width=100)
        self.seedcategory_table.column("2",width=100)
        self.seedcategory_table.column("3",width=120)
        self.seedcategory_table.column("4",width=100)
        self.seedcategory_table.column("5",width=100)
        self.seedcategory_table.column("6",width=100)
        self.seedcategory_table.column("7",width=100)
        self.seedcategory_table.column("8",width=100)

        self.seedcategory_table.pack(fill=BOTH,expand=1)
        self.seedcategory_table.bind("<ButtonRelease>", self.get_crime_cursor)
        self.fetch_seed_data()

    def add_seed_data(self):
        if self.var_CategoryId.get()=="":
            messagebox.showerror('Error','All fields are required')
        else:
            try:
                conn=mysql.connector.connect(host='localhost', username='root',password='password', database='seeds')
                my_cursor=conn.cursor()
                my_cursor.execute('insert into seedcategory values(%s,%s,%s)',(
                    self.var_CategoryId.get(),
                    self.var_CategoryName.get(),
                    self.var_Description.get()))
                conn.commit()
                self.fetch_seed_data()
                self.clear_seed_data()
                conn.close()
                messagebox.showinfo('successful', 'seed data has been added')
            except Exception as es:
                messagebox.showerror('error',f'Due to{str(es)}')

    def fetch_seed_data(self):
        try:
            conn = mysql.connector.connect(host='localhost', username='root', password='password', database='seeds')
            my_cursor = conn.cursor()
            my_cursor.execute('SELECT * FROM seedcategory')
            data = my_cursor.fetchall()
            if data:
                # Clear the existing Treeview entries
                self.seedcategory_table.delete(*self.seedcategory_table.get_children())
                # Re-insert the updated data
                for row in data:
                    self.seedcategory_table.insert('', 'end', values=row)  # Insert entire row directly
        except mysql.connector.Error as err:
            print("Error:", err)
            # Optionally, show an error message in the GUI
            messagebox.showerror('Error', f'Failed to fetch seed data: {err}')
        finally:
            conn.close()


    def search_seed_data(self): 
        if self.var_com_seedsearch.get()=="":
            messagebox.showerror('Error','All fields are required') 
        else:
            try:
                conn=mysql.connector.connect(host='localhost', username='root',password='password', database='seeds')
                my_cursor=conn.cursor()
                my_cursor.execute('select * from seedcategory where '+str(self.var_com_seedsearch.get())+" LIKE'%"+str(self.var_seedsearch.get()+"%'"))
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.seedcategory_table.delete(*self.seedcategory_table.get_children())
                    for i in rows:
                        self.seedcategory_table.insert('',END,values=i)
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror('error',f'Due to{str(es)}')

    def clear_seed_data(self):
        self.var_CategoryId.set(""),
        self.var_CategoryName.set(""),
        self.var_Description.set("")

    def get_crime_cursor(self, event=""):
        cursor_row = self.seedcategory_table.focus()
        if cursor_row:
            content = self.seedcategory_table.item(cursor_row)
            data = content['values']
            if data:
                self.var_CategoryId.set(data[0])
                self.var_CategoryName.set(data[1])
                self.var_Description.set(data[2])


    def delete_category_button_clicked(self):
        # Get the selected category ID from the Treeview
        selected_item = self.seedcategory_table.focus()
        if selected_item:
            category_id = self.seedcategory_table.item(selected_item)['values'][0] # Assuming category ID is in the first column
            # Call the function to delete the category data
            self.delete_category_data(category_id)

    def delete_category_data(self, category_id):
        try:
            conn = mysql.connector.connect(host='localhost', username='root', password='password', database='seeds')
            my_cursor = conn.cursor()
            # Execute SQL query to delete the category data
            my_cursor.execute('DELETE FROM seedcategory WHERE CategoryId = %s', (category_id,))
            conn.commit()
            conn.close()
            # Refresh the category data in the Treeview after deletion
            self.fetch_seed_data()
            # Optionally, clear the input fields after deletion
            self.clear_seed_data()
            messagebox.showinfo('Successful', 'Category record has been deleted')
        except Exception as e:
            messagebox.showerror('Error', f'Failed to delete category record: {str(e)}')


    def update_seed_data(self):
        if self.var_CategoryId.get()=="":
            messagebox.showerror('Error','All fields are required')
        else:
            try:
                conn=mysql.connector.connect(host='localhost', username='root',password='password', database='seeds')
                my_cursor=conn.cursor()
                my_cursor.execute('update seedcategory set CategoryName=%s, Description=%s where CategoryId=%s',(
                    self.var_CategoryName.get(),
                    self.var_Description.get(),
                    self.var_CategoryId.get()))
                conn.commit()
                self.fetch_seed_data()
                self.clear_seed_data()
                conn.close()
                messagebox.showinfo('successful', 'seed record has been added')
            except Exception as es:
                messagebox.showerror('error',f'Due to{str(es)}')
 
    def create_seedprod_tab(self):
        seedprod_tab = ttk.Frame(self.notebook)
        self.notebook.add(seedprod_tab, text="Seeds")

        ttk.Label(seedprod_tab, text="").pack()
        #Main_frame
        Main_frame = Frame(seedprod_tab, bd=2, relief=RIDGE, bg='white')
        Main_frame.place(x=10, y=20, width=1500, height=560)
        
        down_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text='Seed Information Table',font=('times new roman',11,'bold'),fg='red',bg='white')
        down_frame.place(x=10,y=10,width=1480,height=270)

        search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,text='Search Seed',font=('times new roman',11,'bold'),fg='red',bg='white')
        search_frame.place(x=0,y=0,width=1470,height=60)

        search_by=Label(search_frame,font=("arial",11,"bold"),text="Search By:",bg="red",fg="white")
        search_by.grid(row=0,column=0,sticky=W,padx=5)

        # self.var_com_search=StringVar()
        combo_search_box=ttk.Combobox(search_frame,textvariable=self.var_com_SeedProduct_search,font=("arial",11,"bold"),width=18,state='readonly')
        combo_search_box['value']=('Select Option','ProductId')
        combo_search_box.current(0)
        combo_search_box.grid(row=0,column=1,sticky=W,padx=5)

        # self.var_search=StringVar()
        search_txt=ttk.Entry(search_frame,textvariable=self.var_SeedProduct_search,width=18,font=("arial",11,"bold"))
        search_txt.grid(row=0,column=2,sticky=W,padx=5)

        #search button
        btn_search=Button(search_frame,command=self.search_seeds_data,text='Search',font=("arial",13,"bold"),width=14,bg='blue')
        btn_search.grid(row=0,column=3,padx=3,pady=5)

        #all button
        btn_all=Button(search_frame,command=self.fetch_seeds_data,text='Show All',font=("arial",13,"bold"),width=14,bg='blue')
        btn_all.grid(row=0,column=4,padx=3,pady=5)

        crimeagency=Label(search_frame,font=("arial",30,"bold"),text="FARMING",bg='white',fg='crimson')
        crimeagency.grid(row=0,column=5,sticky=W,padx=50,pady=0)

        # Table Frame
        table_frame=Frame(down_frame,bd=2,relief=RIDGE)
        table_frame.place(x=0,y=60,width=1470,height=170)

        # Scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.seed_table=ttk.Treeview(table_frame,column=("1","2","3","4","5","6"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.seed_table.xview)
        scroll_y.config(command=self.seed_table.yview)

        self.seed_table.heading("1",text="ProductId")
        self.seed_table.heading("2",text="productName")
        self.seed_table.heading("3",text="category Id")
        self.seed_table.heading("4",text="supplier Id")
        self.seed_table.heading("5",text="pricePerUnit")
        self.seed_table.heading("6",text="Expiry Date")

        self.seed_table['show']='headings'

        self.seed_table.column("1",width=100)
        self.seed_table.column("2",width=100)
        self.seed_table.column("3",width=100)
        self.seed_table.column("4",width=100)
        self.seed_table.column("5",width=100)
        self.seed_table.column("6",width=150)

        self.seed_table.pack(fill=BOTH,expand=1)
        self.fetch_seeds_data()

    def search_seeds_data(self): 
        if self.var_com_SeedProduct_search.get()=="":
            messagebox.showerror('Error','All fields are required') 
        else:
            try:
                conn=mysql.connector.connect(host='localhost', username='root',password='password', database='seeds')
                my_cursor=conn.cursor()
                my_cursor.execute('select * from ProductId where '+str(self.var_com_SeedProduct_search.get())+" LIKE'%"+str(self.var_SeedProduct_search.get()+"%'"))
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.seed_table.delete(*self.seed_table.get_children())
                    for i in rows:
                        self.seed_table.insert('',END,values=i)
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror('error',f'Due to{str(es)}') 

    def fetch_seeds_data(self):
        conn=mysql.connector.connect(host='localhost', username='root',password='password', database='seeds')
        my_cursor=conn.cursor()
        my_cursor.execute('select * from seedproduct')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.seed_table.delete(*self.seed_table.get_children())
            for i in data:
                self.seed_table.insert('',END,values=i)
            conn.commit()
        conn.close()


    def create_supplier_tab(self):
        supplier_tab = ttk.Frame(self.notebook)
        self.notebook.add(supplier_tab, text="Supplier")

        ttk.Label(supplier_tab, text="").pack()
        #Main_frame
        Main_frame = Frame(supplier_tab, bd=2, relief=RIDGE, bg='white')
        Main_frame.place(x=10, y=20, width=1500, height=560)
        
        down_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text='supplier Information Table',font=('times new roman',11,'bold'),fg='red',bg='white')
        down_frame.place(x=10,y=10,width=1480,height=270)

        search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,text='Search supplier',font=('times new roman',11,'bold'),fg='red',bg='white')
        search_frame.place(x=0,y=0,width=1470,height=60)

        search_by=Label(search_frame,font=("arial",11,"bold"),text="Search By:",bg="red",fg="white")
        search_by.grid(row=0,column=0,sticky=W,padx=5)

        # self.var_com_search=StringVar()
        combo_search_box=ttk.Combobox(search_frame,textvariable=self.var_com_supplier_search,font=("arial",11,"bold"),width=18,state='readonly')
        combo_search_box['value']=('Select Option','supplierId')
        combo_search_box.current(0)
        combo_search_box.grid(row=0,column=1,sticky=W,padx=5)

        # self.var_search=StringVar()
        search_txt=ttk.Entry(search_frame,textvariable=self.var_supplier_search,width=18,font=("arial",11,"bold"))
        search_txt.grid(row=0,column=2,sticky=W,padx=5)

        #search button
        btn_search=Button(search_frame,command=self.search_supplier_data,text='Search',font=("arial",13,"bold"),width=14,bg='blue')
        btn_search.grid(row=0,column=3,padx=3,pady=5)

        #all button
        btn_all=Button(search_frame,command=self.fetch_supplier_data,text='Show All',font=("arial",13,"bold"),width=14,bg='blue')
        btn_all.grid(row=0,column=4,padx=3,pady=5)

        crimeagency=Label(search_frame,font=("arial",30,"bold"),text="FARMING",bg='white',fg='crimson')
        crimeagency.grid(row=0,column=5,sticky=W,padx=50,pady=0)

        # Table Frame
        table_frame=Frame(down_frame,bd=2,relief=RIDGE)
        table_frame.place(x=0,y=60,width=1470,height=170)

        # Scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.supplier_table=ttk.Treeview(table_frame,column=("1","2","3","4","5","6","7"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.supplier_table.xview)
        scroll_y.config(command=self.supplier_table.yview)

        self.supplier_table.heading("1",text="supplierId")
        self.supplier_table.heading("2",text="supplierName")
        self.supplier_table.heading("3",text="Email")
        self.supplier_table.heading("4",text="contactNumber")
        self.supplier_table.heading("5",text="Country")
        self.supplier_table.heading("7",text="contactNumber")

        self.supplier_table['show']='headings'

        self.supplier_table.column("1",width=100)
        self.supplier_table.column("2",width=100)
        self.supplier_table.column("3",width=100)
        self.supplier_table.column("4",width=100)
        self.supplier_table.column("5",width=100)
        self.supplier_table.column("7",width=100)

        self.supplier_table.pack(fill=BOTH,expand=1)
        self.fetch_supplier_data()

    def fetch_supplier_data(self):
        conn=mysql.connector.connect(host='localhost', username='root',password='password', database='seeds')
        my_cursor=conn.cursor()
        my_cursor.execute('select * from seedsupplier')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.supplier_table.delete(*self.supplier_table.get_children())
            for i in data:
                self.supplier_table.insert('',END,values=i)
            conn.commit()
        conn.close()

    def search_supplier_data(self): 
        if self.var_com_supplier_search.get()=="":
            messagebox.showerror('Error','All fields are required') 
        else:
            try:
                conn=mysql.connector.connect(host='localhost', username='root',password='password', database='seeds')
                my_cursor=conn.cursor()
                my_cursor.execute('select * from seedsupplier where '+str(self.var_com_supplier_search.get())+" LIKE'%"+str(self.var_supplier_search.get()+"%'"))
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.supplier_table.delete(*self.supplier_table.get_children())
                    for i in rows:
                        self.supplier_table.insert('',END,values=i)
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror('error',f'Due to{str(es)}')


if __name__=="__main__":
    root=Tk()
    obj=Plant(root)
    root.mainloop()


