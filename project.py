from tkinter import *
import sqlite3
import webbrowser
from tkinter import ttk
connection=sqlite3.connect("project.db")
cursor=connection.cursor()

def third_page():
  perc= p.get()
  class Example(Frame):
      def __init__(self, parent):
          Frame.__init__(self, parent)
          text = Text(self, wrap="none")
          vsb = Scrollbar(orient="vertical", command=text.yview)
          text.configure(yscrollcommand=vsb.set)
          vsb.pack(side="right", fill="y")
          text.pack(fill="both", expand=True)
          def details(a):
            #print(a)
            webbrowser.open(a)
          cursor= connection.execute("SELECT * from UNI where cut_off <= %s order by cut_off desc" %(perc))
          global row
          count =0
          for row in cursor.fetchall():
            unib= Button(self,width=136,bg="white",fg="purple",font=("Calibri",13),text="%s\nFees:%s        Location:%s" %(row[0],row[1],row[3]) , command= lambda x=row[4]:details(x))
            text.window_create("end", window=unib)
            text.insert("end", "\n")
            count=count+1
          text.configure(state="disabled")
          Label(self,bg="black",fg="white",font=("Calibri",13),text="Congratulations you have got %s RESULTS !!!\n Click on the button to visit their website :)"%(count)).pack()

  if __name__ == "__main__":
      global t10
      t10 = Tk()
      t10.title("Your Universities")
      t10.geometry("1000x1000")
      Example(t10).pack(fill="both", expand=True)
      t10.mainloop()

def second_page():
  global t8
  t8=Toplevel(t2)
  t8.title("Percentage")
  t8.geometry("2000x1000")
  
  global p
  p= IntVar()
  global percent

  imgper= PhotoImage(file= "E:\PL\photos\\02.png")
  cr= Canvas(t8, width=600, height= 400)
  cr.pack(expand=YES, fill=BOTH)
  cr.create_image(600,400,image=imgper)
  
  Label(cr,text = "Mumbai Engineering University Counsellor\n LET'S GET STARTED!!", bg = "black",fg="white", width = "200", height = "2", font = ("Calibri", 20)).pack()
  Label(cr,text="Enter your percentage below:",bg="light blue",font = ("Calibri", 18)).pack(pady=30)
  
  percent=Entry(cr, textvariable = p)
  percent.pack()
  
  button=Button(cr, text="Submit",bg="black",fg="white",font = ("Calibri", 15), width = 15, height = 1, command=third_page)
  button.pack(pady=50)
  Label(cr,text="Once you have entered your percentages that you received for the 12th std, we will provide you with the best suited colleges for that\n particular percentage and also consider your prefered area if you have chosen any.  Once we suggest you the colleges your free to scroll through\nand explore their college websites and get a deeper insight into the details of the college and how the campus and their facilities are.\nWe will also give you our counsellor help, that will be available through e-mails and calls around the clock.",bg="light blue",font = ("Calibri", 13)).pack(pady=40)
  Label(cr,text="IT WAS A PLEASURE TO BE OF YOUR HELP.",bg="light blue",font = ("Calibri", 13)).pack(pady=20)
  Label(cr, text="Use the guidelines given below if your result in not given in percentage format:\nTo convert CGPA to Percentage, we need to multiply CGPA with 9.5 that will give us the percentage.\n A1-95%, A2-85.5%, B1-76%,B2-66.5%,C1-57%,C2-47.5%,D-38%", bg="yellow", fg="red",font = ("Calibri", 10)).pack(side=BOTTOM, fill=X)
  t8.mainloop()

def register_user(): 
  username_info = username.get()
  password_info = password.get()
  contact_info= contact.get()
  email_info= email.get()
 
  cursor.execute("INSERT INTO DATA VALUES (?,?,?,?)",(username.get(),password.get(),contact.get(),email.get()))
  connection.commit()
  
  #cursor.execute("Select * from DATA")
  #for row in cursor.fetchall():
  # print(row)
  #to check if the entries are going in the table

  Label(t1, text = "Registration Sucess!!", fg = "green" ,font = ("calibri", 11)).pack()


def login_verify():
  username1 = username_verify.get()
  password1 = password_verify.get()
  
  x=cursor.execute("Select username from DATA")
  for i in x:   
    if username1 in i:
      y=cursor.execute("Select password from DATA")
      for j in y:
        if password1 in j:
          second_page() 
  t2.mainloop()

def register():
  global t1
  t1=Toplevel(t)
  t1.title("Registration Form")
  t1.geometry("2000x1000")

  imgregis= PhotoImage(file= "E:\PL\photos\\reg.png")
  cr= Canvas(t1, width=650, height= 490) 
  cr.pack(expand=YES, fill=BOTH)
  cr.create_image(650,490,image=imgregis)

  Label(cr,text = "Mumbai Engineering University Counsellor\n REGISTRATION", bg = "black",fg="white", width = "200", height = "2", font = ("Calibri", 20)).pack()

  global username
  global password
  global contact
  global email
  
  username = StringVar()
  password = StringVar()
  contact = IntVar()
  email = StringVar()

  global username_entry
  global password_entry
  global contact_entry
  global email_entry
 
  Label(cr, text = "Please enter registration details below and get ready for a fun journey!",fg="white", bg="maroon",font = ("Calibri", 18)).pack(padx=20, pady=20)
  username_label= Label(cr, text = "Username",font = ("Calibri", 14)).pack()
  username_entry = Entry(cr, textvariable = username).pack()
  
  password_label= Label(cr, text = "Password",font = ("Calibri", 14)).pack()
  password_entry =  Entry(cr, textvariable = password).pack()
  
  contact_label= Label(cr, text = "Contact",font = ("Calibri", 14)).pack()
  contact_entry =  Entry(cr, textvariable = contact).pack()
  
  email_label= Label(cr, text = "Email ID",font = ("Calibri", 14)).pack()
  email_entry =  Entry(cr, textvariable = email).pack()
  Label(cr,text="Having trouble? Don't worry! Check out or FAQs by going to the help page present on the top left corner of the homepage or call our helpline anytime:) ", bg="black",fg="red",font = ("Calibri",8)).pack(side=BOTTOM, fill=X)
  
  Button(cr, text = "Register",bg="maroon",fg="white",font = ("Calibri", 14), width = 15, height = 1, command = register_user).pack(padx=20,pady=40)

  cr.mainloop()

  
def login():
  global t2
  t2 = Toplevel(t)
  t2.title("Login")
  t2.geometry("2000x1000")
  
  imglogin= PhotoImage(file= "E:\PL\photos\\log.png")
  cl= Canvas(t2, width=660, height= 360) 
  cl.pack(expand=YES, fill=BOTH)
  cl.create_image(660,360, image= imglogin)

  Label(cl,text = "Mumbai Engineering University Counsellor\n WELCOME BACKK", bg = "black",fg="white", width = "200", height = "2", font = ("Calibri", 20)).pack()
 
  global username_verify
  global password_verify
  
  username_verify = StringVar()
  password_verify = StringVar()
  
  global username_entry1
  global password_entry1

  Label(cl, text = "Please enter your login details below and let's get started!", fg="blue", bg="orange",font = ("Calibri", 20)).pack(padx=20, pady=20)
   
  username_label1= Label(cl, text = "Username ", bg="orange",fg="blue",font = ("Calibri", 15)).pack()
  username_entry1= Entry(cl, textvariable = username_verify)
  username_entry1.pack()
  
  password_label1= Label(cl, text = "Password ", bg="orange",fg="blue",font = ("Calibri", 15)).pack()
  password_entry1= Entry(cl, textvariable = password_verify)
  password_entry1.pack()

  Button(cl, text = "LOGIN",bg="blue",font = ("Calibri", 15), width = 10, height = 1, command = login_verify).pack( pady=108)

  Label(cl, text = "Check your Username and password carefully,\nIf you are unable to proceed after clicking Login", bg="orange",fg="blue",font = ("Calibri", 10)).pack()
  Label(cl,text="Forgot your password? You can send us your problem or check out or FAQs by going to the help page present on the top left corner of the homepage, and register again\nHope this helps else you can call or helpline anytime:) ",fg="red", bg="black",font = ("Calibri",10)).pack(side=BOTTOM, fill=X)
  
  t2.mainloop()
  
def main():
  global t
  t = Tk()
  t.geometry("2000x1000")
  t.title("Mumbai Engineering Universities")

  img = PhotoImage(file="E:\\PL\\uni1.png")
  c= Canvas(width=1000, height= 1000)
  c.pack(expand=YES, fill=BOTH)
  c.create_image(638,400,image=img)

  menu1= Menu(t)
  t.config(menu=menu1)
  menu1.add_cascade(label= "About",command=Abt)
  menu1.add_cascade(label= "Contact us",command=contact_us)
  menu1.add_cascade(label= "Help",command=help_us)
  
  l2=Label(c,text = "Mumbai Engineering University Counsellor", bg = "black",fg="white", width = "200", height = "2", font = ("Calibri", 20)).pack(anchor=CENTER)

  b1=Button(c,text = "Login",bg="black",fg="white", height = "1", width = "25", command = login, font = ("Calibri", 15))
  b1.pack(side=LEFT)
  b2=Button(c,text = "Register",bg="black",fg="white", height = "1", width = "25", command = register, font = ("Calibri", 15))
  b2.pack(side=RIGHT)

  t.mainloop()

def Abt():
  global t6
  t6 = Toplevel(t)
  t6.title("About Us")
  t6.geometry("2000x1000")

  frame=Frame(t6)
  frame.pack(expand=True, fill=BOTH)
  
  vbar=Scrollbar(frame, orient='vertical')
  vbar.pack(side=RIGHT,fill=Y)

  ca= Canvas(frame, width=300, height= 200,bg='light pink',scrollregion=(0,0,1400,1400),yscrollcommand=vbar.set)
  ca.config(width=300,height=200)
  ca.config(yscrollcommand=vbar.set)
  
  vbar.config(command=ca.yview)
 
  ca.pack(side=LEFT,expand=YES,fill=BOTH)
 
  l1=Label(ca,text = "\n\nMumbai Engineering University Counsellor\nABOUT US", bg = "black",fg="white", width = "200", height = "4", font = ("Calibri", 20))
  ca.create_window(620, 0, window=l1)
  l3=Label(ca,text="DREAM                                                  DISCOVER                                               DELIVER", fg="black",bg="light pink", font=("Comic sans",21))
  ca.create_window(50, 80, anchor='nw', window=l3)
  l4=Label(ca,text="OUR MISSION",fg="purple",bg="light pink",font=("Calibri",18))
  ca.create_window(560, 120, anchor='nw', window=l4)
  l5=Label(ca,text="Our mission is to add value for our students by helping them achieve the desired level of quality in their applications\nand thereby enable them to get into their dream university.\n We ensure our work has lasting benefits by developing a close bond with our students and being deeply committed to their success.", bg="light pink", fg="maroon",font=("calibri",13))
  ca.create_window(150, 150, anchor='nw', window=l5)
  l7=Label(ca,text="OUR VALUES",font=("calibri",18),fg="purple", bg="light pink")
  ca.create_window(560, 240, anchor='nw', window=l7)
  l8=Label(ca,text="Our commitment to support and add value for our students drives everything we do.\nWe strive to facilitate our students with the right path to achieve their career goals.\nWe offer comprehensive programmes and services which draw on our industry specific knowledge and technical expertise.", bg="light pink", fg="maroon",font=("calibri",13))
  ca.create_window(150, 270, anchor='nw', window=l8)
  l10=Label(ca,text="OUR STRATEGY",font=("calibri",18),fg="purple",bg="light pink")
  ca.create_window(560, 360, anchor='nw', window=l10)
  l11=Label(ca,text="Our deep industry knowledge coupled with our experience gathered over the years enables us to\nbring fresh perspectives and creative thinking while working on university applications.\nOur unfailing spirit drives us to continually discover better ways to address students’ needs and ultimately deliver superior services.", bg="light pink", fg="maroon",font=("calibri",13))
  ca.create_window(150, 390, anchor='nw', window=l11)
  l13=Label(ca,text="OUR RESULTS",font=("calibri",18),fg="purple",bg="light pink")
  ca.create_window(560, 480, anchor='nw', window=l13)
  l14=Label(ca,text="Our results speak volumes of our skills to get students placed in their desired university and course.\nThe counsellors are well-versed with the application processes and understand what the admission committee looks for in an applicant’s profile.", bg="light pink", fg="maroon",font=("calibri",13))
  ca.create_window(150, 510, anchor='nw', window=l14)
  l15=Label(ca,text="To get in touch with\nour counsellors call:\n9876578976/7898623456 ",font=("calibri",13),bg="purple", fg="white")
  ca.create_window(540, 590, anchor='nw', window=l15)
  l16=Label(ca,text="WHAT OUR STUDENTS SAY",font=("calibri",18),fg="purple",bg="light pink")
  ca.create_window(500, 680, anchor='nw', window=l16)
  l17=Label(ca,text="Anshul Mandhar",fg="blue",bg="light pink",font=("calibri",13))
  ca.create_window(580, 720, anchor='nw', window=l17)
  l18=Label(ca,text=" 'I thank university Counsellor for the crucial role they have played in helping\nme achieve my dreams. Their top notch counselling and stream-lines processes have been a constant assurance that I was in\nsafe hands. I am in the dream college as I wanted. I would like to suggest  University counsellor\n to all those wanting to study in Mumbai and are confused about how to go about. This is your destination! ' ",font=("calibri",13),fg="grey",bg="light pink")
  ca.create_window(170, 750, anchor='nw', window=l18)
  l19=Label(ca,text="Riya Joshi",fg="blue",bg="light pink",font=("calibri",13))
  ca.create_window(600, 850, anchor='nw', window=l19)
  l20=Label(ca,text=" 'It was an amazing experience with University counsellor. They played a very\nvital role in my college preferences as I was highly doubtful about them. They\nwere reachable through whenever I needed their guidance about the details\non the colleges and as I was new to Mumbai that was really helpful back then.' ",fg="grey",bg="light pink",font=("calibri",13))
  ca.create_window(350, 880,anchor='nw',window=l20)
  l6=Label(ca,text="10+ years of experience",bg="purple",font=("calibri",13), fg="white")
  ca.create_window(5, 980, anchor='nw', window=l6)
  l9=Label(ca,text="2000+ strong alumini network",bg="purple",font=("calibri",13), fg="white")
  ca.create_window(1040, 980, anchor='nw', window=l9)
  l12=Label(ca,text="80% students got their dream universities ",bg="purple",font=("calibri",13), fg="white")
  ca.create_window(470, 980, anchor='nw', window=l12)
  l21=Label(ca,text="MEET OUR TEAM",font=("calibri",18),fg="purple",bg="light pink")
  ca.create_window(540, 1020, anchor='nw', window=l21)
  l22=Label(ca,text="Rajshree Varma",fg="blue",bg="light pink",font=("calibri",13))
  ca.create_window(200, 1060, anchor='nw', window=l22)
  l23=Label(ca,text="Chief Operating Officer",fg="purple",bg="light pink",font=("calibri",12))
  ca.create_window(200, 1080, anchor='nw', window=l23)
  l24=Label(ca,text="After graduating from the Yale University got her master’s degree in\neducation from NMIMS and a certificate in college admissions counseling . She also\nworked as a counseling intern at NYU. At University Counsellor,\nRajshree oversees our essay team and is the General Manager.",fg="white",bg="light pink",font=("calibri",11)) 
  ca.create_window(5, 1110, anchor='nw', window=l24)
  l25=Label(ca,text="Yugandhara Verma",fg="blue",bg="light pink",font=("calibri",13))
  ca.create_window(910, 1060, anchor='nw', window=l25)
  l26=Label(ca,text="CEO & Managing Partner",fg="purple",bg="light pink",font=("calibri",12))
  ca.create_window(910, 1080, anchor='nw', window=l26)
  l39=Label(ca,text="Yugandhara studied finance and accounting at the University of Business,Delhi. She then\nenjoyed an almost decade-long career with global giant Credit Pune and quickly rose\nthrough the ranks to become a Vice President of Fixed Income on their trading floor.\nYugandhara spends her free time rooting for her beloved husband Udhan and children.",fg="white",bg="light pink",font=("calibri",11))
  ca.create_window(695, 1110, anchor='nw', window=l39)
  l27=Label(ca,text="Priya Vijayvargiya",fg="blue",bg="light pink",font=("calibri",13))
  ca.create_window(910, 1220, anchor='nw', window=l27)
  l28=Label(ca,text="Managing Patner",fg="purple",bg="light pink",font=("calibri",12))
  ca.create_window(910, 1240, anchor='nw', window=l28)
  l29=Label(ca,text="Given Priya's academic record in high school, her mother would be the first to tell you\nthat there wasn’t the remotest chance of her launching a career in education. Priya\nproved her wrong when she co-founded the Hyderabad branch",fg="white",bg="light pink",font=("calibri",11))
  ca.create_window(695, 1270, anchor='nw', window=l29)
  l30=Label(ca,text="Shashwat Verma",fg="blue",bg="light pink",font=("calibri",13))
  ca.create_window(200, 1220, anchor='nw', window=l30)
  l31=Label(ca,text="Student Mentor",fg="purple",bg="light pink",font=("calibri",12))
  ca.create_window(200, 1240, anchor='nw', window=l31)
  l32=Label(ca,text="Former Associate Director of Admissions and Liaison to Department of Athletics,\nSymbiosis University. He has evaluated over 17,000 college applications throughout his 15 years\nin college admissions. He's Ed.D in Higher Education Administration, Symbiosis University; B.A.",fg="white",bg="light pink",font=("calibri",11))
  ca.create_window(5, 1270, anchor='nw', window=l32)
  t6.mainloop()
 
def contact_us():
  global t7
  t7=Toplevel()
  t7.title("Contact us")
  t7.geometry("2000x1000")

  imgcon = PhotoImage(file="E:\PL\photos\\contact-banner.png")
  cu= Canvas(t7, width=660, height= 370)
  cu.pack(expand=YES, fill=BOTH)
  cu.create_image(660,370,image=imgcon)

  Label(cu,text = "Mumbai Engineering University Counsellor\n GET IN TOUCH AND CONNECT WITH US", bg = "black",fg="white", width = "200", height = "2", font = ("Calibri", 20)).pack(side=TOP)
  Label(cu,text="Email: universitycounsellor@gmail.com", fg='blue', bg='light blue',font=("calibri",15)).pack(pady=10)
  Label(cu,text="Contact No: +91-8889765436\nTelephone: 022-2435678", bg='black', fg='white',font=("calibri",15)).pack()
  Label(cu,text="Office of University counselor Admission:", fg='blue', bg="light blue",font=("calibri",15)).pack(pady=6)
  Label(cu,text="Plot no.6, BKC\nBandra, Mumbai\nPincode:482001 ", fg='black', bg="light blue",font=("calibri",12)).pack()
  Label(cu,text="The Office  is typically available by phone from Monday - Friday, 8:30 a.m. - 5:00 p.m. EST.\nBeginning January 4, we'll be available by phone for extended hours:\nMonday - Thursday, 8:30 a.m. - 7:00 p.m.\nFriday, 8:30 a.m. - 5:00 p.m.\nSaturday, 8:00 a.m. - 12:00 p.m", bg="light blue",font=("calibri",12)).pack(padx=20, pady=80)
  Label(cu,text="Instagram: Uni_Counsellor              Facebook:@Uni_Counsellor              Twitter:@Uni_Counsellor",bg="light blue",fg="blue",font=("calibri",12)).pack(pady=10)
  Button(cu,text="Subscribe",fg="purple",bg="white",font=("calibri",8), command=t7.destroy).pack(side=BOTTOM, fill=X)
  Label(cu,text="Register and Receive our newsletter, updates, deals, & more. We respect your privacy and won’t share your information.",fg="white",bg="blue",font=("calibri",8)).pack(side=BOTTOM,fill=X)
  t7.mainloop()

def help_us():
  global t9
  t9=Toplevel(t)
  t9.title("Help Page")
  t9.geometry("2000x1000")

  imghelp = PhotoImage(file="E:\PL\photos\\help.png")
  ch= Canvas(t9, width=650, height= 320)
  ch.pack(expand=YES, fill=BOTH)
  ch.create_image(650,320,image=imghelp)

  Label(ch,text = "Mumbai Engineering University Counsellor\n DON'T WORRY!", bg = "black",fg="white", width = "200", height = "2", font = ("Calibri", 20)).pack()
  Label(ch,text="We are here to help you :)",bg="black",fg="yellow",font=("calibri",20)).pack(pady=40)
 
  def open_faq(event):
    t11=Toplevel(t9)
    t11.geometry("1000x1000")
    t11.title("FAQ")
    
    imgfaq = PhotoImage(file="E:\PL\photos\\faq.png")
    cof= Canvas(t11, width=550, height= 470)
    cof.pack(expand=YES, fill=BOTH)
    cof.create_image(550,470,image=imgfaq)
    
    Label(cof,text = "Mumbai Engineering University Counsellor\n Frequently Asked Questions", bg = "black",fg="white", width = "200", height = "2", font = ("Calibri", 20)).pack()
    l11=Label(cof,text="1.How to convert my gpa into percentage?\nAns. Assuming 4.0 is the maximum GPA.\n( current GPA / 4.0 ) * 100 = % \n\n2.Is domicile a neccesity to apply in Mumbai University?\nAns. Yes\n\n3.What was the profile of student who got into IITB?\nAns. FIITJEE Delhi +2 course \n\n4.Does your agency also help us find house near colleges?\nAns. We can provide you regarding contacts.\n\n5.At what percentage shall I consider taking a drop?\nAns. Below 45%",fg="white",bg="dark blue",font=20)
    l11.pack(pady=40)
    t11.mainloop()

  def feedback(event):
    global feed
    global feedemail
    feed= StringVar()
    feedemail= StringVar()
    global feedback
    global feedbackemail
   
    def thankyou(event):
      fe=feed.get()
      fm= feedemail.get()
      cursor.execute("INSERT INTO FEEDBACK VALUES (?,?)",(fe,fm))
      connection.commit()
      Label(cfd,text="We Thank You for your valuable time.",bg="orange",font=8).pack(pady=10)
       
    t12=Toplevel(t9)
    t12.geometry("2000x1000")
    t12.title("Fill in a Feedback")

    imgfeed = PhotoImage(file="E:\PL\photos\\feedback.png")
    cfd= Canvas(t12, width=650, height= 450)
    cfd.pack(expand=YES, fill=BOTH)
    cfd.create_image(650,450,image=imgfeed)
    
    Label(cfd,text = "Mumbai Engineering University Counsellor\n Tell Us Your Experience", bg = "black",fg="white", width = "200", height = "2", font = ("Calibri", 20)).pack()
    Label(cfd,text="Kindly send us your feedback",bg="light green",font=10).pack(pady=50)
    feedback= Entry(cfd, textvariable=feed)
    feedback.pack(ipadx=30,ipady=30)
    #cursor.execute("alter table FEEDBACK ADD email TEXT;")
    Label(cfd,text="Please enter your email id",bg="pink",font=10).pack(pady=50)
    feedbackemail= Entry(cfd, textvariable=feedemail)
    feedbackemail.pack()
   
    bz=Button(cfd,text="Submit",bg="black",fg="white", width="10")
    bz.bind("<Button-1>",thankyou)
    bz.pack(pady=40)
    t12.mainloop()
   

  def problem(event):
    global prob
    prob=StringVar()
    global problem
    probmail= StringVar()
    global problememail
   
    def back(event):
      pr=prob.get()
      pm=probmail.get()
      cursor.execute("INSERT INTO PROBLEMS VALUES (?,?)",(pr,pm))
      connection.commit()
      Label(cpr,text="Our team will contact you shortly.\nThank You.",bg="white",font=8).pack()

       
    t13=Toplevel(t9)
    t13.geometry("2000x1000")
    t13.title("Report")

    imgprob = PhotoImage(file="E:\PL\photos\\problem.png")
    cpr= Canvas(t13, width=630, height= 410)
    cpr.pack(expand=YES, fill=BOTH)
    cpr.create_image(630,410,image=imgprob)
    
    Label(cpr,text = "Mumbai Engineering University Counsellor\n Faced Any Issues?", bg = "black",fg="white", width = "200", height = "2", font = ("Calibri", 20)).pack()
    Label(cpr,text="Report your problem here",bg="white",font=10).pack(pady=30)
    problem= Entry(cpr, textvariable=prob)
    problem.pack(ipadx=30,ipady=30,pady=20)
    #cursor.execute("alter table PROBLEMS ADD email TEXT;")
    Label(cpr,text="Please enter your email id",bg="white",font=10).pack(pady=30)
    problememail= Entry(cpr, textvariable=probmail)
    problememail.pack()
    bx=Button(cpr,text="Submit",bg="yellow",width="10")
    bx.bind("<Button-1>",back)
    bx.pack(pady=30)
    t13.mainloop()
   
   
  b=Button(ch,text="FAQ",fg="white",bg="black",width="20",font=("calibri",13))
  b.bind("<Button-1>",open_faq)
  b.pack(pady=10)

  b1=Button(ch,text="Give Feedback",fg="white",bg="black",width="20",font=("calibri",13))
  b1.bind("<Button-1>",feedback)
  b1.pack(pady=10)

  b2=Button(ch,text="Report A Problem",fg="white",bg="black",width="20",font=("calibri",13))
  b2.bind("<Button-1>",problem)
  b2.pack(pady=10)

  cgbackbut=Button(ch,text="Go back to Homepage", command=t9.destroy).pack(side=BOTTOM)
  t9.mainloop()


main()
connection.commit()
cursor.close()
connection.close()
