from tkinter import*
from PIL import Image,ImageTk #pip install pillow
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product import productClass
from sales import salesClass
class IMS:
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
 #leftmenu
        self.MenuLogo=Image.open("images/logo11.png")
        self.MenuLogo=self.MenuLogo.resize((100,100),Image.LANCZOS) 
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)

        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        LeftMenu.place(x=0,y=102,width=200,height=556)  

        lbl_menuLogo=Label(LeftMenu,image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP,fill=X) 

        self.icon_side16=PhotoImage(file="images/side16.png") 
        

        lbl_MENU=Label(LeftMenu,text="MENU",font=("time new roman",15),bg="#16A085").pack(side=TOP,fill=X)

        btn_Employee=Button(LeftMenu,text="Employee",command=self.employee,image=self.icon_side16,compound=LEFT,padx=5,anchor="w",font=("time new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_Supplier=Button(LeftMenu,text="Supplier",command=self.supplier,image=self.icon_side16,compound=LEFT,padx=5,anchor="w",font=("time new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_Category=Button(LeftMenu,text="Category",command=self.category,image=self.icon_side16,compound=LEFT,padx=5,anchor="w",font=("time new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_Product=Button(LeftMenu,text="Product",command=self.product,image=self.icon_side16,compound=LEFT,padx=5,anchor="w",font=("time new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_Sales=Button(LeftMenu,text="Sales",command=self.sales,image=self.icon_side16,compound=LEFT,padx=5,anchor="w",font=("time new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_Exit=Button(LeftMenu,text="Exit",image=self.icon_side16,compound=LEFT,padx=5,anchor="w",font=("time new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)

        #content
        self.lbl_employee=Label(self.root,text="Total Employee\n[ 0 ]",bd=5,relief=RIDGE ,bg="#FF4B4B",fg="white",font=("goudt old style",20,"bold"))
        self.lbl_employee.place(x=300,y=120,height=150,width=300)

        self.lbl_Supplier=Label(self.root,text="Total Supplier\n[ 0 ]",bd=5,relief=RIDGE ,bg="#66CC33",fg="white",font=("goudt old style",20,"bold"))
        self.lbl_Supplier.place(x=650,y=120,height=150,width=300)

        self.lbl_Category=Label(self.root,text="Total Category\n[ 0 ]",bd=5,relief=RIDGE ,bg="#66CCCC",fg="white",font=("goudt old style",20,"bold"))
        self.lbl_Category.place(x=1000,y=120,height=150,width=300)

        self.lbl_Product=Label(self.root,text="Total Product\n[ 0 ]",bd=5,relief=RIDGE ,bg="#9900CC",fg="white",font=("goudt old style",20,"bold"))
        self.lbl_Product.place(x=300,y=300,height=150,width=300)

        self.lbl_Sales=Label(self.root,text="Total Sales\n[ 0 ]",bd=5,relief=RIDGE ,bg="#2F4F4F",fg="white",font=("goudt old style",20,"bold"))
        self.lbl_Sales.place(x=650,y=300,height=150,width=300)

        #footer      
        lbl_footer=Label(self.root,text="SMS=Stock Management System | Developed By Komal Thitame\nfor any Technical Issue Contact:1234***04",font=("time new roman",12,),bg="#00A6A6",fg="black").pack(side=BOTTOM,fill=X)
 #==================================================
    
    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)

    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierClass(self.new_win)

    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=categoryClass(self.new_win)
    
    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=productClass(self.new_win)

    def sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=salesClass(self.new_win)



if __name__=="__main__":       
    root=Tk()
    obj=IMS(root)
    root.mainloop()


