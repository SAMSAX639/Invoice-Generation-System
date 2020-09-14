from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import os,datetime,smtplib

class Login_System:
	def __init__(self,root):
		self.root = root
		self.root.title("Login Window")
		self.root.geometry("1000x600+500+200")
		self.uname = StringVar()
		self.pwd  = StringVar()

		self.bg_icon = ImageTk.PhotoImage(file="pictures/back.jpg")
		self.user_icon = PhotoImage(file="pictures/user.png")
		self.pass_icon = PhotoImage(file="pictures/pwd.png")
		self.logo_icon = PhotoImage(file="pictures/comm.png")
		bg_lbl = Label(self.root,image=self.bg_icon).pack()
		title = Label(self.root,text="Invoice Generation System",font=("times new roman",40,"bold"),bg="#2c3e50",fg="#dcdde1",bd=2,relief=GROOVE)
		title.place(x=0,y=0,relwidth=1)

		login_frame = Frame(self.root,background="white",width=350,height=300)
		login_frame.place(x=230,y=150)
		logolbl = Label(login_frame,image=self.logo_icon,width=100,height=100).grid(row=0,column=0,padx=20,pady=20)
		userlbl = Label(login_frame,text="Hotel ITC Rama\nInternational",font=("times new roman",22,"bold"),bg="white",fg="black").grid(row=0,column=1)
		lbluser = Label(login_frame,text="Username",image=self.user_icon,compound=LEFT,font=("times new roman",15,"bold"),bg="white",fg="black").grid(row=1,column=0,padx=20,pady=10)
		txtuser = Entry(login_frame,bd=2,textvariable=self.uname,relief=SUNKEN,font=("times new roman",15)).grid(row=1,column=1,padx=20)
		lblpass = Label(login_frame,text="Password",image=self.pass_icon,compound=LEFT,font=("times new roman",15,"bold"),bg="white",fg="black").grid(row=2,column=0,padx=20,pady=10)
		txtpass = Entry(login_frame,show="*",bd=2,textvariable=self.pwd,relief=SUNKEN,font=("times new roman",15)).grid(row=2,column=1,padx=20)
		btn_log = Button(login_frame,text="SUBMIT",width=15,command=self.login,font=("times new roman",14,"bold"),bg="#2c3e50",fg="#dcdde1").grid(row=3,column=1,padx=20,pady=10)
		btn_log = Button(login_frame,text="EXIT",width=15,command=self.exitlogin,font=("times new roman",14,"bold"),bg="#2c3e50",fg="#dcdde1").grid(row=3,column=0,padx=20,pady=10)

	def login(self):
		if self.uname.get()=="" or self.pwd.get()=="":
			messagebox.showerror("Error","All Fields are required!!")
		elif self.uname.get()=="gcoej" and self.pwd.get()=="gcoej":
			messagebox.showinfo("Welcome","Successfully Logged In")
			generation()
		else:
			messagebox.showerror("Error","Invalid Username or Password")

	def exitlogin(self):
		self.root.destroy()

class generation:
	def __init__(self):
		self.root = Toplevel()
		self.root.title("Generation Window")
		self.root.geometry("1920x950+0+0")
		bgcolor = "#2c3e50"
		fgcolor = "#dcdde1"
		title = Label(self.root,text="Hotel ITC  Rama International",font=("times new roman",40,"bold"),bg=bgcolor,fg=fgcolor,bd=2,relief=GROOVE)
		title.place(x=0,y=0,relwidth=1)

		(self.name,self.phone,self.email) = (StringVar(),StringVar(),StringVar())
		cframe = LabelFrame(self.root,text="Customer Details",font=("times new roman",15,"bold"),bg=bgcolor,fg="gold",bd=5,relief=GROOVE)
		cframe.place(x=0,y=82,relwidth=1)
		cnamelbl = Label(cframe,text="Customer Name",font=("times new roman",20,"bold"),bg=bgcolor,fg=fgcolor).grid(row=0,column=0,padx=20,pady=5)
		cnametxt = Entry(cframe,width=20,textvariable=self.name,font="ariel 15",bd=2,relief=SUNKEN).grid(row=0,column=1,pady=5)
		cphonelbl = Label(cframe,text="Phone Number",font=("times new roman",20,"bold"),bg=bgcolor,fg=fgcolor).grid(row=0,column=3,padx=20,pady=5)
		cphonetxt = Entry(cframe,width=10,textvariable=self.phone,font="ariel 15",bd=2,relief=SUNKEN).grid(row=0,column=4,pady=5)
		cemaillbl = Label(cframe,text="Email Address",font=("times new roman",20,"bold"),bg=bgcolor,fg=fgcolor).grid(row=0,column=5,padx=20,pady=5)
		cemailtxt = Entry(cframe,width=30,textvariable=self.email,font="ariel 15",bd=2,relief=SUNKEN).grid(row=0,column=6,pady=5)

		(self.v1,self.v2,self.v3,self.v4,self.v5,self.v6,self.v7,self.v8) = (StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar())
		(self.v1.set("0"),self.v2.set("0"),self.v3.set("0"),self.v4.set("0"),self.v5.set("0"),self.v6.set("0"),self.v7.set("0"),self.v8.set("0"))
		vegframe = LabelFrame(self.root,text="Vegetarian",font=("times new roman",15,"bold"),bg=bgcolor,fg="gold",bd=5,relief=GROOVE)
		vegframe.place(x=0,y=172,width=410,height=500)
		vrlbl = Label(vegframe,text="Rate",font=("times new roman",15,"bold"),bg=bgcolor,fg="silver").grid(row=0,column=1,padx=10,pady=5)
		vqlbl = Label(vegframe,text="Quantity",font=("times new roman",15,"bold"),bg=bgcolor,fg="silver").grid(row=0,column=2,padx=10,pady=5)
		v1lbl = Label(vegframe,text="Paneer 65",font=("times new roman",15,"bold"),bg=bgcolor,fg=fgcolor).grid(row=1,column=0,padx=10,pady=5)
		vr1lbl = Label(vegframe,text="140/-",font=("times new roman",15,"bold"),bg=bgcolor,fg=fgcolor).grid(row=1,column=1,padx=10,pady=5)
		v1txt = Entry(vegframe,width=5,textvariable=self.v1,font="ariel 15",bd=2,relief=SUNKEN).grid(row=1,column=2,padx=10,pady=5)
		v2lbl = Label(vegframe,text="Paneer Chilli",font=("times new roman",15,"bold"),bg=bgcolor,fg=fgcolor).grid(row=2,column=0,padx=10,pady=5)
		vr2lbl = Label(vegframe,text="120/-",font=("times new roman",15,"bold"),bg=bgcolor,fg=fgcolor).grid(row=2,column=1,padx=10,pady=5)
		v2txt = Entry(vegframe,width=5,textvariable=self.v2,font="ariel 15",bd=2,relief=SUNKEN).grid(row=2,column=2,padx=10,pady=5)
		v3lbl = Label(vegframe,text="Mushroom Chilli",font=("times new roman",15,"bold"),bg=bgcolor,fg=fgcolor).grid(row=3,column=0,padx=10,pady=5)
		vr3lbl = Label(vegframe,text="100/-",font=("times new roman",15,"bold"),bg=bgcolor,fg=fgcolor).grid(row=3,column=1,padx=10,pady=5)
		v3txt = Entry(vegframe,width=5,textvariable=self.v3,font="ariel 15",bd=2,relief=SUNKEN).grid(row=3,column=2,padx=10,pady=5)
		v4lbl = Label(vegframe,text="Paneer Masala",font=("times new roman",15,"bold"),bg=bgcolor,fg=fgcolor).grid(row=4,column=0,padx=10,pady=5)
		vr4lbl = Label(vegframe,text="130/-",font=("times new roman",15,"bold"),bg=bgcolor,fg=fgcolor).grid(row=4,column=1,padx=10,pady=5)
		v4txt = Entry(vegframe,width=5,textvariable=self.v4,font="ariel 15",bd=2,relief=SUNKEN).grid(row=4,column=2,padx=10,pady=5)
		v5lbl = Label(vegframe,text="Butter Paneer",font=("times new roman",15,"bold"),bg=bgcolor,fg=fgcolor).grid(row=5,column=0,padx=10,pady=5)
		vr5lbl = Label(vegframe,text="140/-",font=("times new roman",15,"bold"),bg=bgcolor,fg=fgcolor).grid(row=5,column=1,padx=10,pady=5)
		v5txt = Entry(vegframe,width=5,textvariable=self.v5,font="ariel 15",bd=2,relief=SUNKEN).grid(row=5,column=2,padx=10,pady=5)
		v6lbl = Label(vegframe,text="Paneer Tikka",font=("times new roman",15,"bold"),bg=bgcolor,fg=fgcolor).grid(row=6,column=0,padx=10,pady=5)
		vr6lbl = Label(vegframe,text="140/-",font=("times new roman",15,"bold"),bg=bgcolor,fg=fgcolor).grid(row=6,column=1,padx=10,pady=5)
		v6txt = Entry(vegframe,width=5,textvariable=self.v6,font="ariel 15",bd=2,relief=SUNKEN).grid(row=6,column=2,padx=10,pady=5)
		v7lbl = Label(vegframe,text="Kaju Masala",font=("times new roman",15,"bold"),bg=bgcolor,fg=fgcolor).grid(row=7,column=0,padx=10,pady=5)
		vr7lbl = Label(vegframe,text="150/-",font=("times new roman",15,"bold"),bg=bgcolor,fg=fgcolor).grid(row=7,column=1,padx=10,pady=5)
		v7txt = Entry(vegframe,width=5,textvariable=self.v7,font="ariel 15",bd=2,relief=SUNKEN).grid(row=7,column=2,padx=10,pady=5)
		v8lbl = Label(vegframe,text="Kaju Curry",font=("times new roman",15,"bold"),bg=bgcolor,fg=fgcolor).grid(row=8,column=0,padx=10,pady=5)
		vr8lbl = Label(vegframe,text="140/-",font=("times new roman",15,"bold"),bg=bgcolor,fg=fgcolor).grid(row=8,column=1,padx=10,pady=5)
		v8txt = Entry(vegframe,width=5,textvariable=self.v8,font="ariel 15",bd=2,relief=SUNKEN).grid(row=8,column=2,padx=10,pady=5)

		(self.nv1,self.nv2,self.nv3,self.nv4,self.nv5,self.nv6,self.nv7,self.nv8) = (StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar())
		(self.nv1.set("0"),self.nv2.set("0"),self.nv3.set("0"),self.nv4.set("0"),self.nv5.set("0"),self.nv6.set("0"),self.nv7.set("0"),self.nv8.set("0"))
		nonvegframe = LabelFrame(self.root,text="Non-Vegetarian",font=("times new roman",15,"bold"),bg=bgcolor,fg="gold",bd=5,relief=GROOVE)
		nonvegframe.place(x=411,y=172,width=410,height=500)
		nvrlbl = Label(nonvegframe,text="Rate",font=("times new roman",15,"bold"),bg=bgcolor,fg="silver").grid(row=0,column=1,padx=10,pady=5)
		nvqlbl = Label(nonvegframe,text="Quantity",font=("times new roman",15,"bold"),bg=bgcolor,fg="silver").grid(row=0,column=2,padx=10,pady=5)
		nv1lbl = Label(nonvegframe,text="Chicken 65",font=("times new roman",15,"bold"),bg=bgcolor,fg=fgcolor).grid(row=1,column=0,padx=10,pady=5)
		nvr1lbl = Label(nonvegframe,text="160/-",font=("times new roman",15,"bold"),bg=bgcolor,fg=fgcolor).grid(row=1,column=1,padx=10,pady=5)
		nv1txt = Entry(nonvegframe,width=5,textvariable=self.nv1,font="ariel 15",bd=2,relief=SUNKEN).grid(row=1,column=2,padx=10,pady=5)
		nv2lbl = Label(nonvegframe,text="Crispy Chicken",font=("times new roman",15,"bold"),bg=bgcolor,fg=fgcolor).grid(row=2,column=0,padx=10,pady=5)
		nvr2lbl = Label(nonvegframe,text="160/-",font=("times new roman",15,"bold"),bg=bgcolor,fg=fgcolor).grid(row=2,column=1,padx=10,pady=5)
		nv2txt = Entry(nonvegframe,width=5,textvariable=self.nv2,font="ariel 15",bd=2,relief=SUNKEN).grid(row=2,column=2,padx=10,pady=5)
		nv3lbl = Label(nonvegframe,text="Chilli Chicken",font=("times new roman",15,"bold"),bg=bgcolor,fg=fgcolor).grid(row=3,column=0,padx=10,pady=5)
		nvr3lbl = Label(nonvegframe,text="150/-",font=("times new roman",15,"bold"),bg=bgcolor,fg=fgcolor).grid(row=3,column=1,padx=10,pady=5)
		nv3txt = Entry(nonvegframe,width=5,textvariable=self.nv3,font="ariel 15",bd=2,relief=SUNKEN).grid(row=3,column=2,padx=10,pady=5)
		nv4lbl = Label(nonvegframe,text="Chicken Lollipop",font=("times new roman",15,"bold"),bg=bgcolor,fg=fgcolor).grid(row=4,column=0,padx=10,pady=5)
		nvr4lbl = Label(nonvegframe,text="170/-",font=("times new roman",15,"bold"),bg=bgcolor,fg=fgcolor).grid(row=4,column=1,padx=10,pady=5)
		nv4txt = Entry(nonvegframe,width=5,textvariable=self.nv4,font="ariel 15",bd=2,relief=SUNKEN).grid(row=4,column=2,padx=10,pady=5)
		nv5lbl = Label(nonvegframe,text="Roasted Chicken",font=("times new roman",15,"bold"),bg=bgcolor,fg=fgcolor).grid(row=5,column=0,padx=10,pady=5)
		nvr5lbl = Label(nonvegframe,text="170/-",font=("times new roman",15,"bold"),bg=bgcolor,fg=fgcolor).grid(row=5,column=1,padx=10,pady=5)
		nv5txt = Entry(nonvegframe,width=5,textvariable=self.nv5,font="ariel 15",bd=2,relief=SUNKEN).grid(row=5,column=2,padx=10,pady=5)
		nv6lbl = Label(nonvegframe,text="Murgh Bhuna",font=("times new roman",15,"bold"),bg=bgcolor,fg=fgcolor).grid(row=6,column=0,padx=10,pady=5)
		nvr6lbl = Label(nonvegframe,text="190/-",font=("times new roman",15,"bold"),bg=bgcolor,fg=fgcolor).grid(row=6,column=1,padx=10,pady=5)
		nv6txt = Entry(nonvegframe,width=5,textvariable=self.nv6,font="ariel 15",bd=2,relief=SUNKEN).grid(row=6,column=2,padx=10,pady=5)
		nv7lbl = Label(nonvegframe,text="Chicken Handi",font=("times new roman",15,"bold"),bg=bgcolor,fg=fgcolor).grid(row=7,column=0,padx=10,pady=5)
		nvr7lbl = Label(nonvegframe,text="310/-",font=("times new roman",15,"bold"),bg=bgcolor,fg=fgcolor).grid(row=7,column=1,padx=10,pady=5)
		nv7txt = Entry(nonvegframe,width=5,textvariable=self.nv7,font="ariel 15",bd=2,relief=SUNKEN).grid(row=7,column=2,padx=10,pady=5)
		nv8lbl = Label(nonvegframe,text="Mutton Handi",font=("times new roman",15,"bold"),bg=bgcolor,fg=fgcolor).grid(row=8,column=0,padx=10,pady=5)
		nvr8lbl = Label(nonvegframe,text="390/-",font=("times new roman",15,"bold"),bg=bgcolor,fg=fgcolor).grid(row=8,column=1,padx=10,pady=5)
		nv8txt = Entry(nonvegframe,width=5,textvariable=self.nv8,font="ariel 15",bd=2,relief=SUNKEN).grid(row=8,column=2,padx=10,pady=5)

		(self.r1,self.r2,self.r3,self.r4) = (StringVar(),StringVar(),StringVar(),StringVar())
		(self.r1.set("0"),self.r2.set("0"),self.r3.set("0"),self.r4.set("0"))
		ricesframe = LabelFrame(self.root,text="Rices",font=("times new roman",15,"bold"),bg=bgcolor,fg="gold",bd=5,relief=GROOVE)
		ricesframe.place(x=822,y=172,width=410,height=270)
		rrlbl = Label(ricesframe,text="Rate",font=("times new roman",15,"bold"),bg=bgcolor,fg="silver").grid(row=0,column=1,padx=10,pady=5)
		rqlbl = Label(ricesframe,text="Quantity",font=("times new roman",15,"bold"),bg=bgcolor,fg="silver").grid(row=0,column=2,padx=10,pady=5)
		r1lbl = Label(ricesframe,text="Jeera Rice",font=("times new roman",15,"bold"),bg=bgcolor,fg=fgcolor).grid(row=1,column=0,padx=10,pady=5)
		rr1lbl = Label(ricesframe,text="60/-",font=("times new roman",15,"bold"),bg=bgcolor,fg=fgcolor).grid(row=1,column=1,padx=10,pady=5)
		r1txt = Entry(ricesframe,width=5,textvariable=self.r1,font="ariel 15",bd=2,relief=SUNKEN).grid(row=1,column=2,padx=10,pady=5)
		r2lbl = Label(ricesframe,text="Veg Biryani",font=("times new roman",15,"bold"),bg=bgcolor,fg=fgcolor).grid(row=2,column=0,padx=10,pady=5)
		rr2lbl = Label(ricesframe,text="130/-",font=("times new roman",15,"bold"),bg=bgcolor,fg=fgcolor).grid(row=2,column=1,padx=10,pady=5)
		r2txt = Entry(ricesframe,width=5,textvariable=self.r2,font="ariel 15",bd=2,relief=SUNKEN).grid(row=2,column=2,padx=10,pady=5)
		r3lbl = Label(ricesframe,text="Chicken Biryani",font=("times new roman",15,"bold"),bg=bgcolor,fg=fgcolor).grid(row=3,column=0,padx=10,pady=5)
		rr3lbl = Label(ricesframe,text="170/-",font=("times new roman",15,"bold"),bg=bgcolor,fg=fgcolor).grid(row=3,column=1,padx=10,pady=5)
		r3txt = Entry(ricesframe,width=5,textvariable=self.r3,font="ariel 15",bd=2,relief=SUNKEN).grid(row=3,column=2,padx=10,pady=5)
		r4lbl = Label(ricesframe,text="Mutton Biryani",font=("times new roman",15,"bold"),bg=bgcolor,fg=fgcolor).grid(row=4,column=0,padx=10,pady=5)
		rr4lbl = Label(ricesframe,text="210/-",font=("times new roman",15,"bold"),bg=bgcolor,fg=fgcolor).grid(row=4,column=1,padx=10,pady=5)
		r4txt = Entry(ricesframe,width=5,textvariable=self.r4,font="ariel 15",bd=2,relief=SUNKEN).grid(row=4,column=2,padx=10,pady=5)

		(self.b1,self.b2,self.b3) = (StringVar(),StringVar(),StringVar())
		(self.b1.set("0"),self.b2.set("0"),self.b3.set("0"))
		breadsframe = LabelFrame(self.root,text="Breads",font=("times new roman",15,"bold"),bg=bgcolor,fg="gold",bd=5,relief=GROOVE)
		breadsframe.place(x=822,y=443,width=410,height=230)
		brlbl = Label(breadsframe,text="Rate",font=("times new roman",15,"bold"),bg=bgcolor,fg="silver").grid(row=0,column=1,padx=20,pady=5)
		bqlbl = Label(breadsframe,text="Quantity",font=("times new roman",15,"bold"),bg=bgcolor,fg="silver").grid(row=0,column=2,padx=20,pady=5)
		b1lbl = Label(breadsframe,text="Tawa Roti",font=("times new roman",15,"bold"),bg=bgcolor,fg=fgcolor).grid(row=1,column=0,padx=10,pady=5)
		br1lbl = Label(breadsframe,text="12/-",font=("times new roman",15,"bold"),bg=bgcolor,fg=fgcolor).grid(row=1,column=1,padx=10,pady=5)
		b1txt = Entry(breadsframe,width=5,textvariable=self.b1,font="ariel 15",bd=2,relief=SUNKEN).grid(row=1,column=2,padx=10,pady=5)
		b2lbl = Label(breadsframe,text="Tandoori Roti",font=("times new roman",15,"bold"),bg=bgcolor,fg=fgcolor).grid(row=2,column=0,padx=10,pady=5)
		br2lbl = Label(breadsframe,text="15/-",font=("times new roman",15,"bold"),bg=bgcolor,fg=fgcolor).grid(row=2,column=1,padx=10,pady=5)
		b2txt = Entry(breadsframe,width=5,textvariable=self.b2,font="ariel 15",bd=2,relief=SUNKEN).grid(row=2,column=2,padx=10,pady=5)
		b3lbl = Label(breadsframe,text="Butter Naan",font=("times new roman",15,"bold"),bg=bgcolor,fg=fgcolor).grid(row=3,column=0,padx=10,pady=5)
		br3lbl = Label(breadsframe,text="20/-",font=("times new roman",15,"bold"),bg=bgcolor,fg=fgcolor).grid(row=3,column=1,padx=10,pady=5)
		b3txt = Entry(breadsframe,width=5,textvariable=self.b3,font="ariel 15",bd=2,relief=SUNKEN).grid(row=3,column=2,padx=10,pady=5)

		dtframe = Frame(self.root,bd=5,relief=GROOVE,background=bgcolor)
		dtframe.place(x=1233,y=172,width=610,height=59)
		dt = str(datetime.datetime.now()).split()
		date = dt[0].split("-")
		time = dt[1].split(":")
		time[2] = time[2][0:2]
		datelbl = Label(dtframe,text="Date    :",font=("times new roman",20,"bold"),bg=bgcolor,fg=fgcolor).grid(row=0,column=0,padx=10,pady=5)
		datetxt = Label(dtframe,text="{0}/{1}/{2}".format(date[2],date[1],date[0]),font=("times new roman",20,"bold"),bg=bgcolor,fg=fgcolor).grid(row=0,column=1,padx=10,pady=5)
		timelbl = Label(dtframe,text="Time    :",font=("times new roman",20,"bold"),bg=bgcolor,fg=fgcolor).grid(row=0,column=2,padx=10,pady=5)
		timetxt = Label(dtframe,text="{0}:{1}:{2}".format(time[0],time[1],time[2]),font=("times new roman",20,"bold"),bg=bgcolor,fg=fgcolor).grid(row=0,column=3,padx=10,pady=5)

		self.inv = StringVar()
		searchframe = Frame(self.root,bd=5,relief=GROOVE,background=bgcolor)
		searchframe.place(x=1233,y=231,width=610,height=59)
		invlbl = Label(searchframe,text="Invoice No.",font=("times new roman",20,"bold"),bg=bgcolor,fg=fgcolor).grid(row=0,column=0,padx=10,pady=5)
		invtxt = Entry(searchframe,width=10,textvariable=self.inv,font="ariel 15 bold",bd=2,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=5)
		searchbtn = Button(searchframe,text="Search",command=self.searchbill,width=10,font=("times new roman",15,"bold"),fg=bgcolor,bg=fgcolor).grid(row=0,column=2,padx=10,pady=5)

		billframe = Frame(self.root,bd=5,relief=GROOVE)
		billframe.place(x=1233,y=290,width=610,height=600)
		billtitle = Label(billframe,text="Billing Area",font=("times new roman",15,"bold"),bd=2,relief=GROOVE,bg=bgcolor,fg="gold").pack(fill=X)
		scrol_y = Scrollbar(billframe,orient=VERTICAL)
		self.txtarea = Text(billframe,yscrollcommand=scrol_y.set,font=("courier",12,"bold"),fg=bgcolor,state="normal")
		scrol_y.pack(side=RIGHT,fill=Y)
		scrol_y.config(command=self.txtarea.yview)
		self.txtarea.pack(fill=BOTH,expand=1)

		(self.ga,self.ta,self.dis,self.total) = (StringVar(),StringVar(),StringVar(),StringVar())
		self.dis.set("0")
		amountframe = LabelFrame(self.root,text="Billing Menu",font=("times new roman",15,"bold"),bg=bgcolor,fg="gold",bd=5,relief=GROOVE)
		amountframe.place(x=0,y=674,width=820,height=215)
		galbl = Label(amountframe,text="Groce Amount",font=("times new roman",15,"bold"),bg=bgcolor,fg=fgcolor).grid(row=0,column=0,padx=10,pady=20)
		gatxt = Entry(amountframe,width=10,state="readonly",textvariable=self.ga,font="ariel 15",bd=2,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=20)
		talbl = Label(amountframe,text="Taxable Amount",font=("times new roman",15,"bold"),bg=bgcolor,fg=fgcolor).grid(row=1,column=0,padx=10,pady=20)
		tatxt = Entry(amountframe,width=10,state="readonly",textvariable=self.ta,font="ariel 15",bd=2,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=20)
		dislbl = Label(amountframe,text="Discount",font=("times new roman",15,"bold"),bg=bgcolor,fg=fgcolor).grid(row=0,column=2,padx=10,pady=20)
		distxt = Entry(amountframe,width=10,textvariable=self.dis,font="ariel 15",bd=2,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=20)
		totallbl = Label(amountframe,text="Total Amount",font=("times new roman",15,"bold"),bg=bgcolor,fg=fgcolor).grid(row=1,column=2,padx=10,pady=20)
		totaltxt = Entry(amountframe,width=10,state="readonly",textvariable=self.total,font="ariel 15",bd=2,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=20)

		btnframe = Frame(self.root,bd=5,relief=GROOVE,background=bgcolor)
		btnframe.place(x=822,y=674,width=410,height=215)
		totalbtn = Button(btnframe,text="Total",command=self.totalbill,width=10,height=2,font=("times new roman",19,"bold"),fg=bgcolor,bg=fgcolor).grid(row=0,column=0,padx=5,pady=5)
		generatebtn = Button(btnframe,text="Generate\nInvoice",command=self.generatebill,width=10,height=2,font=("times new roman",19,"bold"),fg=bgcolor,bg=fgcolor).grid(row=0,column=1,padx=5,pady=5)
		clearbtn = Button(btnframe,text="Clear",command=self.cleardata,width=10,height=2,font=("times new roman",19,"bold"),fg=bgcolor,bg=fgcolor).grid(row=1,column=0,padx=5,pady=5)
		exitbtn = Button(btnframe,text="Exit",command=self.exitwindow,width=10,height=2,font=("times new roman",19,"bold"),fg=bgcolor,bg=fgcolor).grid(row=1,column=1,padx=5,pady=5)

		self.welcomebill()

	def totalbill(self):
		(v1,v2,v3,v4,v5,v6,v7,v8) = (self.v1.get(),self.v2.get(),self.v3.get(),self.v4.get(),self.v5.get(),self.v6.get(),self.v7.get(),self.v8.get())
		(nv1,nv2,nv3,nv4,nv5,nv6,nv7,nv8) = (self.nv1.get(),self.nv2.get(),self.nv3.get(),self.nv4.get(),self.nv5.get(),self.nv6.get(),self.nv7.get(),self.nv8.get())
		(r1,r2,r3,r4) = (self.r1.get(),self.r2.get(),self.r3.get(),self.r4.get())
		(b1,b2,b3) = (self.b1.get(),self.b2.get(),self.b3.get())
		discount = self.dis.get()

		if v1.isdigit() and v2.isdigit() and v3.isdigit() and v4.isdigit() and v5.isdigit() and v6.isdigit() and v7.isdigit() and v8.isdigit() and nv1.isdigit() and nv2.isdigit() and nv3.isdigit() and nv4.isdigit() and nv5.isdigit() and nv6.isdigit() and nv7.isdigit() and nv8.isdigit() and r1.isdigit() and r2.isdigit() and r3.isdigit() and r4.isdigit() and b1.isdigit() and b2.isdigit() and b3.isdigit() and discount.isdigit():
			(v1,v2,v3,v4,v5,v6,v7,v8) = (int(v1),int(v2),int(v3),int(v4),int(v5),int(v6),int(v7),int(v8))
			(nv1,nv2,nv3,nv4,nv5,nv6,nv7,nv8) = (int(nv1),int(nv2),int(nv3),int(nv4),int(nv5),int(nv6),int(nv7),int(nv8))
			(r1,r2,r3,r4) = (int(r1),int(r2),int(r3),int(r4))
			(b1,b2,b3) = (int(b1),int(b2),int(b3))
			discount = int(discount)

			if v1 >= 0 and v2 >= 0 and v3 >= 0 and v4 >= 0 and v5 >= 0 and v6 >= 0 and v7 >= 0 and v8 >= 0 and nv1 >= 0 and nv2 >= 0 and nv3 >= 0 and nv4 >= 0 and nv5 >= 0 and nv6 >= 0 and nv7 >= 0 and nv8 >= 0 and r1 >= 0 and r2 >= 0 and r3 >= 0 and r4 >= 0 and b1 >= 0 and b2 >= 0 and b3 >= 0 and discount >= 0:
				(v1,v2,v3,v4,v5,v6,v7,v8) = (v1*140,v2*120,v3*100,v4*130,v5*140,v6*140,v7*150,v8*140)
				(nv1,nv2,nv3,nv4,nv5,nv6,nv7,nv8) = (nv1*160,nv2*160,nv3*150,nv4*170,nv5*170,nv6*190,nv7*310,nv8*390)
				(r1,r2,r3,r4) = (r1*60,r2*130,r3*170,r4*210)
				(b1,b2,b3) = (b1*12,b2*15,b3*20)
				groceamount = float(v1 + v2 + v3 + v4 + v5 + v6 + v7 + v8 + nv1 + nv2 + nv3 + nv4 + nv5 + nv6 + nv7 + nv8 + r1 + r2 + r3 + r4 + b1 + b2 + b3)
				taxableamount = float(groceamount*0.05)
				total = groceamount + taxableamount - discount
				self.ga.set("Rs. "+str(round(groceamount,2)))
				self.ta.set("Rs. "+str(round(taxableamount,2)))
				self.total.set("Rs. "+str(round(total,2)))
			else:
 				messagebox.showerror("Error","Quantity & Discount Should be Positive Number")
		else:
			messagebox.showerror("Error","Quantity & Discount Should be Numeric")

	def welcomebill(self):
		infile = open("InvNum.txt","r")
		invnum = infile.readline().rstrip()
		infile.close()
		dt = str(datetime.datetime.now()).split()
		self.txtarea.delete("1.0",END)
		self.txtarea.insert(END,"\n {0:^48s}\n".format("Hotel ITC Rama International"))
		self.txtarea.insert(END,"\n{0:<15s}{1:^5s}{2}".format(" Customer Name",":",self.name.get()))
		self.txtarea.insert(END,"\n{0:<15s}{1:^5s}{2}".format(" Phone Number",":",self.phone.get()))
		self.txtarea.insert(END,"\n{0:<15s}{1:^5s}{2}".format(" Email Address",":",self.email.get()))
		self.txtarea.insert(END,"\n{0:<15s}{1:^5s}{2}".format(" Invoice Number",":",invnum))
		self.txtarea.insert(END,"\n{0:<15s}{1:^5s}{2:<15s}{3}".format(" Date & Time",":",dt[0],dt[1][0:8]))
		self.txtarea.insert(END,"\n\n{:*<48s}".format(""))
		self.txtarea.insert(END,"\n{0:^20s}{1:^8s}{2:^8s}{3:^12s}".format(" Item","Rate","Qty","Price"))
		self.txtarea.insert(END,"\n{:*<48s}".format(""))

	def generatebill(self):
		name = self.name.get().strip()
		phone = self.phone.get().strip()
		email = self.email.get().strip()
		if name != "" and phone != "" and email != "":

			if phone.isdigit() and len(phone) == 10 and email.find("@") != -1 and email.find(".") != -1 and email.count("@")==1:
				(v1,v2,v3,v4,v5,v6,v7,v8) = (self.v1.get(),self.v2.get(),self.v3.get(),self.v4.get(),self.v5.get(),self.v6.get(),self.v7.get(),self.v8.get())
				(nv1,nv2,nv3,nv4,nv5,nv6,nv7,nv8) = (self.nv1.get(),self.nv2.get(),self.nv3.get(),self.nv4.get(),self.nv5.get(),self.nv6.get(),self.nv7.get(),self.nv8.get())
				(r1,r2,r3,r4) = (self.r1.get(),self.r2.get(),self.r3.get(),self.r4.get())
				(b1,b2,b3) = (self.b1.get(),self.b2.get(),self.b3.get())
				discount = self.dis.get()

				if v1.isdigit() and v2.isdigit() and v3.isdigit() and v4.isdigit() and v5.isdigit() and v6.isdigit() and v7.isdigit() and v8.isdigit() and nv1.isdigit() and nv2.isdigit() and nv3.isdigit() and nv4.isdigit() and nv5.isdigit() and nv6.isdigit() and nv7.isdigit() and nv8.isdigit() and r1.isdigit() and r2.isdigit() and r3.isdigit() and r4.isdigit() and b1.isdigit() and b2.isdigit() and b3.isdigit() and discount.isdigit():
					(v1,v2,v3,v4,v5,v6,v7,v8) = (int(v1),int(v2),int(v3),int(v4),int(v5),int(v6),int(v7),int(v8))
					(nv1,nv2,nv3,nv4,nv5,nv6,nv7,nv8) = (int(nv1),int(nv2),int(nv3),int(nv4),int(nv5),int(nv6),int(nv7),int(nv8))
					(r1,r2,r3,r4) = (int(r1),int(r2),int(r3),int(r4))
					(b1,b2,b3) = (int(b1),int(b2),int(b3))
					discount = int(discount)

					if v1 >= 0 and v2 >= 0 and v3 >= 0 and v4 >= 0 and v5 >= 0 and v6 >= 0 and v7 >= 0 and v8 >= 0 and nv1 >= 0 and nv2 >= 0 and nv3 >= 0 and nv4 >= 0 and nv5 >= 0 and nv6 >= 0 and nv7 >= 0 and nv8 >= 0 and r1 >= 0 and r2 >= 0 and r3 >= 0 and r4 >= 0 and b1 >= 0 and b2 >= 0 and b3 >= 0 and discount >= 0:
						(qv1,qv2,qv3,qv4,qv5,qv6,qv7,qv8) = (v1*140,v2*120,v3*100,v4*130,v5*140,v6*140,v7*150,v8*140)
						(qnv1,qnv2,qnv3,qnv4,qnv5,qnv6,qnv7,qnv8) = (nv1*160,nv2*160,nv3*150,nv4*170,nv5*170,nv6*190,nv7*310,nv8*390)
						(qr1,qr2,qr3,qr4) = (r1*60,r2*130,r3*170,r4*210)
						(qb1,qb2,qb3) = (b1*12,b2*15,b3*20)
						groceamount = float(qv1 + qv2 + qv3 + qv4 + qv5 + qv6 + qv7 + qv8 + qnv1 + qnv2 + qnv3 + qnv4 + qnv5 + qnv6 + qnv7 + qnv8 + qr1 + qr2 + qr3 + qr4 + qb1 + qb2 + qb3)
						taxableamount = float(groceamount*0.05)
						total = groceamount + taxableamount - discount
						self.ga.set("Rs. "+str(round(groceamount,2)))
						self.ta.set("Rs. "+str(round(taxableamount,2)))
						self.total.set("Rs. "+str(round(total,2)))

						if(self.total.get() != "Rs. 0.0"):
							self.welcomebill()
							if v1 != 0:
								self.txtarea.insert(END,"\n{0:<20s}{1:^8s}{2:^8d}{3:^12d}".format(" Paneer 65","140",v1,qv1))
							if v2 != 0:
								self.txtarea.insert(END,"\n{0:<20s}{1:^8s}{2:^8d}{3:^12d}".format(" Paneer Chilli","120",v2,qv2))
							if v3 != 0:
								self.txtarea.insert(END,"\n{0:<20s}{1:^8s}{2:^8d}{3:^12d}".format(" Mushroom Chilli","100",v3,qv3))
							if v4 != 0:
								self.txtarea.insert(END,"\n{0:<20s}{1:^8s}{2:^8d}{3:^12d}".format(" Paneer Masala","130",v4,qv4))
							if v5 != 0:
								self.txtarea.insert(END,"\n{0:<20s}{1:^8s}{2:^8d}{3:^12d}".format(" Butter Paneer","140",v5,qv5))
							if v6 != 0:
								self.txtarea.insert(END,"\n{0:<20s}{1:^8s}{2:^8d}{3:^12d}".format(" Paneer Tikka","140",v6,qv6))
							if v7 != 0:
								self.txtarea.insert(END,"\n{0:<20s}{1:^8s}{2:^8d}{3:^12d}".format(" Kaju Masala","150",v7,qv7))
							if v8 != 0:
								self.txtarea.insert(END,"\n{0:<20s}{1:^8s}{2:^8d}{3:^12d}".format(" Kaju Curry","140",v8,qv8))

							if nv1 != 0:
								self.txtarea.insert(END,"\n{0:<20s}{1:^8s}{2:^8d}{3:^12d}".format(" Chicken 65","160",nv1,qnv1))
							if nv2 != 0:
								self.txtarea.insert(END,"\n{0:<20s}{1:^8s}{2:^8d}{3:^12d}".format(" Crispy Chicken","160",nv2,qnv2))
							if nv3 != 0:
								self.txtarea.insert(END,"\n{0:<20s}{1:^8s}{2:^8d}{3:^12d}".format(" Chilli Chicken","150",nv3,qnv3))
							if nv4 != 0:
								self.txtarea.insert(END,"\n{0:<20s}{1:^8s}{2:^8d}{3:^12d}".format(" Chicken Lollipop","170",nv4,qnv4))
							if nv5 != 0:
								self.txtarea.insert(END,"\n{0:<20s}{1:^8s}{2:^8d}{3:^12d}".format(" Roasted Chicken","170",nv5,qnv5))
							if nv6 != 0:
								self.txtarea.insert(END,"\n{0:<20s}{1:^8s}{2:^8d}{3:^12d}".format(" Murgh Bhuna","190",nv6,qnv6))
							if nv7 != 0:
								self.txtarea.insert(END,"\n{0:<20s}{1:^8s}{2:^8d}{3:^12d}".format(" Chicken Handi","310",nv7,qnv7))
							if nv8 != 0:
								self.txtarea.insert(END,"\n{0:<20s}{1:^8s}{2:^8d}{3:^12d}".format(" Mutton Handi","390",nv8,qnv8))

							if r1 != 0:
								self.txtarea.insert(END,"\n{0:<20s}{1:^8s}{2:^8d}{3:^12d}".format(" Jeera Rice","60",r1,qr1))
							if r2 != 0:
								self.txtarea.insert(END,"\n{0:<20s}{1:^8s}{2:^8d}{3:^12d}".format(" Veg Biryani","130",r2,qr2))
							if r3 != 0:
								self.txtarea.insert(END,"\n{0:<20s}{1:^8s}{2:^8d}{3:^12d}".format(" Chicken Biryani","170",r3,qr3))
							if r4 != 0:
								self.txtarea.insert(END,"\n{0:<20s}{1:^8s}{2:^8d}{3:^12d}".format(" Mutton Biryani","210",r4,qr4))

							if b1 != 0:
								self.txtarea.insert(END,"\n{0:<20s}{1:^8s}{2:^8d}{3:^12d}".format(" Tawa Roti","12",b1,qb1))
							if b2 != 0:
								self.txtarea.insert(END,"\n{0:<20s}{1:^8s}{2:^8d}{3:^12d}".format(" Tandoori Roti","15",b2,qb2))
							if b3 != 0:
								self.txtarea.insert(END,"\n{0:<20s}{1:^8s}{2:^8d}{3:^12d}".format(" Butter Naan","20",b3,qb3))

							self.txtarea.insert(END,"\n{:*<48s}".format(""))
							self.txtarea.insert(END,"\n{0:>36s}{1:^12.2f}".format("Groce Amount",groceamount))
							self.txtarea.insert(END,"\n{0:>36s}{1:^12.2f}".format("GST 5%",taxableamount))
							self.txtarea.insert(END,"\n{0:>36s}{1:^12.2f}".format("Discount",0 - discount))
							self.txtarea.insert(END,"\n{:*<48s}".format(""))
							self.txtarea.insert(END,"\n{0:>36s}{1:^12.2f}".format("Total Amount",total))
							self.txtarea.insert(END,"\n{:*<48s}".format(""))

							self.savebill()
						else:
							messagebox.showerror("Error","You Have Not Buyed Any Think !!")
					else:
                                		messagebox.showerror("Error","Quantity & Discount Should be Positive Number !!")
				else:
					messagebox.showerror("Error","Quantity & Discount Should be Numeric !!")
			else:
				messagebox.showerror("Error","Provide Valid Customer Details !!")
		else:
			messagebox.showerror("Error","Customer Details Are Required !!")

	def savebill(self):
		op = messagebox.askyesno("Save Invoice","Do you Want To Save The Invoice !!")
		if op>0:
			billdata = self.txtarea.get("1.0",END)
			infile = open("InvNum.txt","r")
			invnum = infile.readline().rstrip()
			infile.close()
			outfile = open("Data/Inv"+invnum+".txt","w")
			outfile.write(billdata)
			outfile.close()
			outfile = open("InvNum.txt","w")
			outfile.write(str(int(invnum) + 1))
			outfile.close()
			messagebox.showinfo("Saved Invoice","Invoice No. {0} Saved Successfully !!".format(invnum))
			try:
				s = smtplib.SMTP('smtp.gmail.com',587)
				s.starttls()
				s.login("ramainternational639@gmail.com","Gcoej@123")
				s.sendmail("ramainternational639@gmail.com",self.email.get(),billdata)
				s.quit()
				messagebox.showinfo("Sent Invoice","Mail Sent Successfully !!")
			except:
				messagebox.showerror("Not Sent","Mail Can'nt Sent !!")
		else:
			return

	def searchbill(self):
		searchinv = self.inv.get()
		if (searchinv != ""):
			if (searchinv.isdigit()):
				flag = 1
				for i in os.listdir("Data/"):
					if i.split(".")[0][3:] == searchinv:
						infile = open("Data/Inv"+searchinv+".txt","r")
						self.txtarea.delete("1.0",END)
						for line in infile:
							self.txtarea.insert(END,line)
						infile.close()
						flag = 0
				if (flag):
					messagebox.showerror("Not Found","Invoice No. {0} Does Not Exist !!".format(searchinv))
			else:
				messagebox.showerror("Error","Invoice Number Should be Numeric !!")
		else:
			messagebox.showerror("Error","Provide Valid Invoice Number !!")

	def cleardata(self):
		op = messagebox.askyesno("Clear Data","Do you Really Want To Clear Data !!")
		if (op>0):
			(self.name.set(""),self.phone.set(""),self.email.set(""))
			(self.v1.set("0"),self.v2.set("0"),self.v3.set("0"),self.v4.set("0"),self.v5.set("0"),self.v6.set("0"),self.v7.set("0"),self.v8.set("0"))
			(self.nv1.set("0"),self.nv2.set("0"),self.nv3.set("0"),self.nv4.set("0"),self.nv5.set("0"),self.nv6.set("0"),self.nv7.set("0"),self.nv8.set("0"))
			(self.r1.set("0"),self.r2.set("0"),self.r3.set("0"),self.r4.set("0"))
			(self.b1.set("0"),self.b2.set("0"),self.b3.set("0"))
			(self.ga.set(""),self.ta.set(""),self.dis.set("0"),self.total.set(""))
			self.welcomebill()
		else:
			return

	def exitwindow(self):
		op = messagebox.askyesno("Exit Window","Do you Really Want To Exit !!")
		if (op>0):
			self.root.destroy()
		else:
			return

root = Tk()
Login_System(root)
root.mainloop()
