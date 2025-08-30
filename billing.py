from tkinter import*
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk,messagebox
class BillClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Stock Management System | Developed By Komal Thitame")
        self.root.config(bg="WHITE")

#title
        self.icon_title=PhotoImage(file="images/logo1.png")        
        title=Label(self.root,text="Stock Management System",font=("time new roman",40,"bold"),bg="orange",fg="white",anchor="w",padx=20,image=self.icon_title,compound=LEFT).place(x=0,y=0,relwidth=1,height=70)
#btn_logout        
        btn_logout=Button(self.root,text="Logout",font=("time new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1100,y=10,height=50,width=150)
  #clock      
        self.lbl_clock=Label(self.root,text="Welcome to Stock Management System\t\t Date:DD-MM-YYYY\t\t Time:HH:MM:SS",font=("time new roman",15,),bg="#00A6A6",fg="black")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)
 #======product_frame====
        self.var_search=StringVar()
        ProductFrame1=Frame(self.root, bd=4, relief=RIDGE,bg="white")
        ProductFrame1.place(x=6,y=110,width=410, height=550)
        
        pTitle=Label(ProductFrame1, text="All Products", font=("goudy old style",20,"bold"), bg="#262626",fg="white").pack(side=TOP,fill=X)

        ProductFrame2=Frame(ProductFrame1, bd=2, relief=RIDGE,bg="white")
        ProductFrame2.place(x=2,y=42,width=398, height=90)
        
        lbl_search=Label( ProductFrame2,text="Search Product | By Name ",font=("times new roman", 15, "bold"), bg="white",fg="green").place(x=2,y=5)
        
        lbl_search=Label( ProductFrame2,text="Product Name",font=("times new roman", 15, "bold"), bg="white").place(x=5,y=45)
        txt_search=Label( ProductFrame2,textvariable=self.var_search,font=("times new roman", 15, ), bg="lightyellow").place(x=128,y=47,width=150,height=22)
        btn_search=Button (ProductFrame2, text="Search", font=("goudy old style", 15), bg="#2196f3",fg="white",cursor="hand2").place(x=285,y=45,width=100,height=25)
        btn_show_all=Button (ProductFrame2, text="Show All", font=("goudy old style", 15), bg="#083531",fg="white",cursor="hand2").place(x=285,y=10,width=100,height=25)
        
        
        ProductFrame3=Frame(ProductFrame1,bd=3,relief=RIDGE)
        ProductFrame3.place(x=2,y=140,width=398,height=375)

        scrollx=Scrollbar(ProductFrame3,orient=HORIZONTAL)#--------------------------------------------------
        scrolly=Scrollbar(ProductFrame3,orient=VERTICAL)

        self.product_Table=ttk.Treeview(ProductFrame3,columns=("pid","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        scrollx.config(command=self.product_Table.xview)
        scrolly.config(command=self.product_Table.yview)

        self.product_Table.heading("pid",text="pid ")
        self.product_Table.heading("name",text="Name") 
        self.product_Table.heading("price",text="Price")
        self.product_Table.heading("qty",text="QTY")
        self.product_Table.heading("status",text="Status")

        self.product_Table["show"]="headings"

        self.product_Table.column("pid",width=100)
        self.product_Table.column("name",width=100) 
        self.product_Table.column("price",width=100)
        self.product_Table.column("qty",width=100)
        self.product_Table.column("status",width=100)

        self.product_Table.pack(fill=BOTH,expand=1)
       # self.product_Table.bind("<ButtonRelease-1>",self.get_data)
        lbl_note=Label(ProductFrame1,text="Note:'Enter 0 quantity to remove product from the cart",font=("goudy old style",12),anchor='w',bg="white",fg="red").pack(side=BOTTOM,fill=X)

if __name__=="__main__":       
    root=Tk()
    obj=BillClass(root)
    root.mainloop()