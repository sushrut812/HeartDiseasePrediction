from tkinter import *
from PIL import Image,ImageTk
import csv
import random
import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
        
def regpat(frame,h,w,root,inc):
    
    frame.pack_forget()
    frame = Frame(root,width=w,height=h)
    frame.pack()
    
    load=Image.open("2.png")
    render=ImageTk.PhotoImage(load)
    img=Label(frame,image=render)
    img.image=render
    img.place(x=0,y=0)

    wel=Label(frame,text="Enter The Details of Patient",font=("Calibri",20))
    wel.pack()
    wel.place(x=350,y=165)

    usr=Label(frame,text="Name",font=("Calibri",15))
    usr.pack()
    usr.place(x=375,y=230)

    usr=Label(frame,text="Surname",font=("Calibri",15))
    usr.pack()
    usr.place(x=350,y=280)

    pas=Label(frame,text="Age",font=("Calibri",15))
    pas.pack()
    pas.place(x=390,y=330)

    pas=Label(frame,text="Gender",font=("Calibri",15))
    pas.pack()
    pas.place(x=360,y=380)
    
    entry1=Entry(frame,font=("Calibri",15))
    entry1.pack()
    entry1.place(x=450,y=230)

    entry2=Entry(frame,font=("Calibri",15))
    entry2.pack()
    entry2.place(x=450,y=280)

    entry3=IntVar()
    entry3=Entry(frame,font=("Calibri",15))
    entry3.pack()
    entry3.place(x=450,y=330)
 
    v = IntVar()
    
    male=Radiobutton(frame,text="Male",value=1,variable=v,font=("Calibri",12))
    male.pack()
    male.place(x=450,y=380)

    female=Radiobutton(frame,text="Female",value=2,variable=v,font=("Calibri",12))
    female.pack()
    female.place(x=535,y=380)
    
    submit=Button(frame, text = 'Submit',font=("Calibri",15),command=lambda:regpat1(frame,h,w,root,entry1.get(),entry2.get(),entry3.get(),v))
    submit.pack()
    submit.place(x=600,y=530)
    
    home=Button(frame, text = 'Back to Home Page',font=("Calibri",15),command=lambda:main(frame,h,w,root))
    home.pack()
    home.place(x=280,y=530)

    if(inc==1):
        inc=Label(frame,text="Please feed the information properly",font=("Calibri",12))
        inc.pack()
        inc.place(x=375,y=452)

def regpat1(frame,h,w,root,first,last,age,gender):

    if(first=="" or last=="" or age=="" or gender.get()==0):
        num=1
        regpat(frame,h,w,root,num)
    else:
        regpat2(frame,h,w,root,first,last,age,gender)

def regpat2(frame,h,w,root,first,last,age,gender):
    
    f = open('patient.csv', 'r')
    r = csv.reader(f)

    next(r)
    i=0

    for row in r:
        i=i+1

    f.close()
    username=first+str(i+1)

    if(gender.get()==1):
        gen="Male"
    else:
        gen="Female"
        
    frame.pack_forget()
    frame = Frame(root,width=w,height=h)
    frame.pack()
    
    load=Image.open("2.png")
    render=ImageTk.PhotoImage(load)
    img=Label(frame,image=render)
    img.image=render
    img.place(x=0,y=0)

    usr=Label(frame,text="Your username is "+username,font=("Calibri",15))
    usr.pack()
    usr.place(x=400,y=200)

    usr=Label(frame,text="Please enter a password",font=("Calibri",15))
    usr.pack()
    usr.place(x=400,y=250)

    entry=Entry(frame,font=("Calibri",15))
    entry.pack()
    entry.place(x=400,y=300)

    submit=Button(frame, text = 'Submit',font=("Calibri",15),command=lambda:regpat3(frame,h,w,root,first,last,age,gen,username,entry.get()))
    submit.pack()
    submit.place(x=580,y=350)
    
    home=Button(root, text = 'Back to Home Page',font=("Calibri",15),command=lambda:main(frame,h,w,root))
    home.pack()
    home.place(x=300,y=350)

def regpat3(frame,h,w,root,first,last,age,gender,username,password):

    num=0
    data=[first,last,age,username,password,gender,num]
    f = open('patient.csv', 'a',newline='')
    writer = csv.writer(f)
    writer.writerow(data)
    f.close()

    frame.pack_forget()
    frame = Frame(root,width=w,height=h)
    frame.pack()

    load=Image.open("2.png")
    render=ImageTk.PhotoImage(load)
    img=Label(frame,image=render)
    img.image=render
    img.place(x=0,y=0)
    
    info=Label(frame,text="Use the following information to Login",font=("Calibri",15))
    info.pack()
    info.place(x=350,y=200)    

    usr=Label(frame,text="Username:- "+username,font=("Calibri",15))
    usr.pack()
    usr.place(x=440,y=250)

    pas=Label(frame,text="Password:- "+password,font=("Calibri",15))
    pas.pack()
    pas.place(x=440,y=300)    
    
    home=Button(root, text = 'Back to Home Page',font=("Calibri",15),command=lambda:main(frame,h,w,root))
    home.pack()
    home.place(x=430,y=350)
    
def logpatho(frame,h,w,root,inc):

    frame.pack_forget()
    frame = Frame(root,width=w,height=h)
    frame.pack()
    
    load=Image.open("2.png")
    render=ImageTk.PhotoImage(load)
    img=Label(frame,image=render)
    img.image=render
    img.place(x=0,y=0)

    wel=Label(frame,text="Enter Your Login Details",font=("Calibri",25))
    wel.pack()
    wel.place(x=350,y=195)

    usr=Label(frame,text="Username",font=("Calibri",15))
    usr.pack()
    usr.place(x=360,y=260)

    pas=Label(frame,text="Password",font=("Calibri",15))
    pas.pack()
    pas.place(x=365,y=310)

    entry1=Entry(frame,font=("Calibri",15))
    entry1.pack()
    entry1.place(x=460,y=260)

    entry2=Entry(frame,show='*',font=("Calibri",15))
    entry2.pack()
    entry2.place(x=460,y=310)
    
    submit=Button(frame, text = 'Submit',font=("Calibri",15),command=lambda:logpatho1(frame,h,w,root,entry1.get(),entry2.get()))
    submit.pack()
    submit.place(x=590,y=360)

    num=0
    
    home=Button(frame, text = 'Back to Home Page',font=("Calibri",15),command=lambda:main(frame,h,w,root))
    home.pack()
    home.place(x=350,y=360)
    
    if(inc==1):
        inc=Label(frame,text="Incorrect Username and Password...Please Try Again",font=("Calibri",12))
        inc.pack()
        inc.place(x=335,y=452)

def logpatho1(frame,h,w,root,username,password):

    if(username=='admin' and password=='admin'):
        inc=0
        logpatho2(frame,h,w,root,inc)
    else:
        num=1
        logpatho(frame,h,w,root,num)
        
def logpatho2(frame,h,w,root,inc):

    frame.pack_forget()
    frame = Frame(root,width=w,height=h)
    frame.pack()
    
    load=Image.open("2.png")
    render=ImageTk.PhotoImage(load)
    img=Label(frame,image=render)
    img.image=render
    img.place(x=0,y=0)

    patid=Label(frame,text="Enter The Patient id",font=("Calibri",25))
    patid.pack()
    patid.place(x=370,y=270)

    entry=Entry(frame,font=("Calibri",15))
    entry.pack()
    entry.place(x=400,y=330)

    num=0
    
    home=Button(frame, text = 'Back to Home Page',font=("Calibri",15),command=lambda:main(frame,h,w,root))
    home.pack()
    home.place(x=330,y=370)
    
    submit=Button(frame, text = 'Submit',font=("Calibri",15),command=lambda:logpatho3(frame,h,w,root,entry.get()))
    submit.pack()
    submit.place(x=580,y=370)

    if(inc==1):
        incl=Label(frame,text="Incorrect Patinet Id...Please Try Again",font=("Calibri",12))
        incl.pack()
        incl.place(x=375,y=452)

    if(inc==2):
        iaf=Label(frame,text="Information of the given patient id is already filled",font=("Calibri",12))
        iaf.pack()
        iaf.place(x=350,y=452)
        
def logpatho3(frame,h,w,root,patid):

    f = open('patient.csv', 'r')
    r = csv.reader(f)

    next(r)
    
    for row in r:
        if(row[3]==patid and row[6]=='0'):
            fail=0
            break
        elif(row[3]==patid and row[6]=='1'):
            fail=1
            break
        else:
            fail=2

    f.close()
    
    if(fail==0):
        inc=0
        logpatho4(frame,h,w,root,inc,patid)
    elif(fail==1):
        num=2
        logpatho2(frame,h,w,root,num)
    else:
        num=1
        logpatho2(frame,h,w,root,num)
        
def logpatho4(frame,h,w,root,inc,patid):

    frame.pack_forget()
    frame = Frame(root,width=w,height=h)
    frame.pack()
    
    load=Image.open("2.png")
    render=ImageTk.PhotoImage(load)
    img=Label(frame,image=render)
    img.image=render
    img.place(x=0,y=0) 

    info=Label(frame,text="Enter The Info of Patient Id: "+patid,font=("Calibri",20))
    info.pack()
    info.place(x=335,y=120)

    hemo=Label(frame,text="Hemoglobin",font=("Calibri",12))
    hemo.pack()
    hemo.place(x=250,y=170)

    entry1=Entry(frame,font=("Calibri",12))
    entry1.pack()
    entry1.place(x=340,y=170)

    rbc=Label(frame,text="RBC",font=("Calibri",12))
    rbc.pack()
    rbc.place(x=570,y=170)

    entry2=Entry(frame,font=("Calibri",12))
    entry2.pack()
    entry2.place(x=610,y=170)

    pcv=Label(frame,text="PCV",font=("Calibri",12))
    pcv.pack()
    pcv.place(x=300,y=210)

    entry3=Entry(frame,font=("Calibri",12))
    entry3.pack()
    entry3.place(x=340,y=210)

    mcv=Label(frame,text="MCV",font=("Calibri",12))
    mcv.pack()
    mcv.place(x=565,y=210)

    entry4=Entry(frame,font=("Calibri",12))
    entry4.pack()
    entry4.place(x=610,y=210)

    mch=Label(frame,text="MCH",font=("Calibri",12))
    mch.pack()
    mch.place(x=295,y=250)

    entry5=Entry(frame,font=("Calibri",12))
    entry5.pack()
    entry5.place(x=340,y=250)

    mchc=Label(frame,text="MCHC",font=("Calibri",12))
    mchc.pack()
    mchc.place(x=555,y=250)

    entry6=Entry(frame,font=("Calibri",12))
    entry6.pack()
    entry6.place(x=610,y=250)

    rdw=Label(frame,text="RDW",font=("Calibri",12))
    rdw.pack()
    rdw.place(x=295,y=290)

    entry7=Entry(frame,font=("Calibri",12))
    entry7.pack()
    entry7.place(x=340,y=290)

    wbc=Label(frame,text="WBC",font=("Calibri",12))
    wbc.pack()
    wbc.place(x=565,y=290)

    entry8=Entry(frame,font=("Calibri",12))
    entry8.pack()
    entry8.place(x=610,y=290)
    
    pla=Label(frame,text="Platelet",font=("Calibri",12))
    pla.pack()
    pla.place(x=277,y=330)

    entry9=Entry(frame,font=("Calibri",12))
    entry9.pack()
    entry9.place(x=340,y=330)

    neu=Label(frame,text="Neutrophils",font=("Calibri",12))
    neu.pack()
    neu.place(x=520,y=330)

    entry10=Entry(frame,font=("Calibri",12))
    entry10.pack()
    entry10.place(x=610,y=330)

    lym=Label(frame,text="Lymphocytes",font=("Calibri",12))
    lym.pack()
    lym.place(x=242,y=370)

    entry11=Entry(frame,font=("Calibri",12))
    entry11.pack()
    entry11.place(x=340,y=370)

    eos=Label(frame,text="Eosinophils",font=("Calibri",12))
    eos.pack()
    eos.place(x=520,y=370)

    entry12=Entry(frame,font=("Calibri",12))
    entry12.pack()
    entry12.place(x=610,y=370)

    mon=Label(frame,text="Monocytes",font=("Calibri",12))
    mon.pack()
    mon.place(x=253,y=410)

    entry13=Entry(frame,font=("Calibri",12))
    entry13.pack()
    entry13.place(x=340,y=410)

    bas=Label(frame,text="Basophils",font=("Calibri",12))
    bas.pack()
    bas.place(x=530,y=410)

    entry14=Entry(frame,font=("Calibri",12))
    entry14.pack()
    entry14.place(x=610,y=410)

    home=Button(frame, text = 'Back to Home Page',font=("Calibri",15),command=lambda:main(frame,h,w,root))
    home.pack()
    home.place(x=250,y=470)
    
    submit=Button(frame, text = 'Submit',font=("Calibri",15),command=lambda:logpatho5(frame,h,w,root,patid,entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry6.get(),entry7.get(),entry8.get(),entry9.get(),entry10.get(),entry11.get(),entry12.get(),entry13.get(),entry14.get()))
    submit.pack()
    submit.place(x=700,y=470)   

    if(inc==1):
        inc=Label(frame,text="Please Feed Information Correctly...",font=("Calibri",12))
        inc.pack()
        inc.place(x=355,y=600)
        
def logpatho5(frame,h,w,root,patid,e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14):

    if(e1=='' or e2=='' or e3=='' or e4=='' or e5=='' or e6=='' or e7=='' or e8=='' or e9=='' or e10=='' or e11=='' or e12=='' or e13=='' or e14==''):
        inc=1;
        logpatho4(frame,h,w,root,inc,patid)
    else:
        logpatho6(frame,h,w,root,patid,e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14)
        
def logpatho6(frame,h,w,root,patid,e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14):

    f = open('patient.csv', 'r')
    r = csv.reader(f)

    next(r)
    
    for row in r:
        if(row[3]==patid):
            p1=row[0]
            p2=row[1]
            p3=row[2]
            p4=row[3]
            p5=row[4]
            p6=row[5]
            
    f.close()

    num=0
    data=[p1,p2,p3,p4,p5,p6,e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,num]

    f = open('patient1.csv','a',newline='')
    writer = csv.writer(f)
    writer.writerow(data)
    f.close()

    input = open('patient.csv', 'r')
    output = open('patientc.csv', 'w',newline='')

    writer = csv.writer(output)
    for row in csv.reader(input):
        if row[3]!=patid:
            writer.writerow(row)
        else:
            row[6]=1
            writer.writerow(row)
    input.close()
    output.close()

    os.remove("patient.csv")
    os.rename('patientc.csv', 'patient.csv')
    
    frame.pack_forget()
    frame = Frame(root,width=w,height=h)
    frame.pack()
    
    load=Image.open("2.png")
    render=ImageTk.PhotoImage(load)
    img=Label(frame,image=render)
    img.image=render
    img.place(x=0,y=0) 

    info=Label(frame,text="Information Successfully Filled",font=("Calibri",25))
    info.pack()
    info.place(x=300,y=300)

    home=Button(frame, text = 'Back to Home Page',font=("Calibri",15),command=lambda:main(frame,h,w,root))
    home.pack()
    home.place(x=420,y=360)

def logdoc(frame,h,w,root,inc):

    frame.pack_forget()
    frame = Frame(root,width=w,height=h)
    frame.pack()
    
    load=Image.open("2.png")
    render=ImageTk.PhotoImage(load)
    img=Label(frame,image=render)
    img.image=render
    img.place(x=0,y=0)

    wel=Label(frame,text="Enter Your Login Details",font=("Calibri",25))
    wel.pack()
    wel.place(x=350,y=195)

    usr=Label(frame,text="Username",font=("Calibri",15))
    usr.pack()
    usr.place(x=360,y=260)

    pas=Label(frame,text="Password",font=("Calibri",15))
    pas.pack()
    pas.place(x=365,y=310)

    entry1=Entry(frame,font=("Calibri",15))
    entry1.pack()
    entry1.place(x=460,y=260)

    entry2=Entry(frame,show='*',font=("Calibri",15))
    entry2.pack()
    entry2.place(x=460,y=310)
    
    submit=Button(frame, text = 'Submit',font=("Calibri",15),command=lambda:logdoc1(frame,h,w,root,entry1.get(),entry2.get()))
    submit.pack()
    submit.place(x=590,y=360)

    num=0
    
    home=Button(frame, text = 'Back to Home Page',font=("Calibri",15),command=lambda:main(frame,h,w,root))
    home.pack()
    home.place(x=350,y=360)
    
    if(inc==1):
        inc=Label(frame,text="Incorrect Username and Password...Please Try Again",font=("Calibri",12))
        inc.pack()
        inc.place(x=335,y=452)

def logdoc1(frame,h,w,root,username,password):

    flag=1
    f = open('doctor.csv', 'r')
    r = csv.reader(f)

    next(r)
    
    for row in r:
        if(row[1]==username and row[2]==password):
            flag=0
            name=row[0]
            break

    f.close()
    
    if(flag==0):
        logdoc2(frame,h,w,root,flag,name)
    else:
        logdoc(frame,h,w,root,flag)

def logdoc2(frame,h,w,root,inc,name):

    print(name)
    
    frame.pack_forget()
    frame = Frame(root,width=w,height=h)
    frame.pack()
    
    load=Image.open("2.png")
    render=ImageTk.PhotoImage(load)
    img=Label(frame,image=render)
    img.image=render
    img.place(x=0,y=0)

    welcome=Label(frame,text="Welcome... Dr. "+name,font=("Calibri",25))
    welcome.pack()
    welcome.place(x=350,y=200)
    
    patid=Label(frame,text="Enter The Patinet id",font=("Calibri",25))
    patid.pack()
    patid.place(x=370,y=270)

    entry=Entry(frame,font=("Calibri",15))
    entry.pack()
    entry.place(x=400,y=330)

    num=0
    
    home=Button(frame, text = 'Back to Home Page',font=("Calibri",15),command=lambda:main(frame,h,w,root))
    home.pack()
    home.place(x=310,y=370)
    
    submit=Button(frame, text = 'Submit',font=("Calibri",15),command=lambda:logdoc3(frame,h,w,root,entry.get(),name))
    submit.pack()
    submit.place(x=560,y=370)

    if(inc==1):
        incl=Label(frame,text="Incorrect Patinet Id...Please Try Again",font=("Calibri",12))
        incl.pack()
        incl.place(x=375,y=452)

    if(inc==2):
        iaf=Label(frame,text="Information of the given patient id is already filled",font=("Calibri",12))
        iaf.pack()
        iaf.place(x=350,y=452)
        
def logdoc3(frame,h,w,root,patid,name):

    f = open('patient1.csv', 'r')
    r = csv.reader(f)

    next(r)
    
    for row in r:
        if(row[3]==patid and row[20]=='0'):
            fail=0
            break
        elif(row[3]==patid and row[20]=='1'):
            fail=1
            break
        else:
            fail=2

    f.close()
    
    if(fail==0):
        inc=0
        logdoc4(frame,h,w,root,inc,patid,name)
    elif(fail==1):
        num=2
        logdoc2(frame,h,w,root,num,name)
    else:
        num=1
        logdoc2(frame,h,w,root,num,name)

def logdoc4(frame,h,w,root,inc,patid,name):

    frame.pack_forget()
    frame = Frame(root,width=w,height=h)
    frame.pack()
    
    load=Image.open("2.png")
    render=ImageTk.PhotoImage(load)
    img=Label(frame,image=render)
    img.image=render
    img.place(x=0,y=0)

    f = open('patient1.csv', 'r')
    r = csv.reader(f)

    next(r)

    data=[]
    for row in r:
        if(row[3]==patid):
            data=row

    namel=Label(frame,text="Name: "+data[0]+" "+data[1],font=("Calibri",15))
    namel.pack()
    namel.place(x=200,y=20)

    patids=Label(frame,text="Patient Id: "+data[3],font=("Calibri",15))
    patids.pack()
    patids.place(x=600,y=20)

    age=Label(frame,text="Age: "+data[2],font=("Calibri",15))
    age.pack()
    age.place(x=200,y=60)

    gen=Label(frame,text="Gender: "+data[5],font=("Calibri",15))
    gen.pack()
    gen.place(x=600,y=60)
    
    cbc=Label(frame,text="Complete Blood Count",font=("Calibri",20))
    cbc.pack()
    cbc.place(x=335,y=100)

    para=Label(frame,text="Parameters",font=("Calibri",12))
    para.pack()
    para.place(x=50,y=150)

    hemo=Label(frame,text="Hemoglobin",font=("Calibri",12))
    hemo.pack()
    hemo.place(x=50,y=180)

    rbc=Label(frame,text="RBC",font=("Calibri",12))
    rbc.pack()
    rbc.place(x=50,y=210)

    pcv=Label(frame,text="(Hematocrit)PCV",font=("Calibri",12))
    pcv.pack()
    pcv.place(x=50,y=240)

    mcv=Label(frame,text="MCV",font=("Calibri",12))
    mcv.pack()
    mcv.place(x=50,y=270)

    mch=Label(frame,text="MCH",font=("Calibri",12))
    mch.pack()
    mch.place(x=50,y=300)

    mchc=Label(frame,text="MCHC",font=("Calibri",12))
    mchc.pack()
    mchc.place(x=50,y=330)

    rdw=Label(frame,text="RDW",font=("Calibri",12))
    rdw.pack()
    rdw.place(x=50,y=360)

    wbc=Label(frame,text="WBC",font=("Calibri",12))
    wbc.pack()
    wbc.place(x=50,y=390)
    
    pla=Label(frame,text="Platelet Count",font=("Calibri",12))
    pla.pack()
    pla.place(x=50,y=420)

    dwc=Label(frame,text="DIFF WBC Count",font=("Calibri",12))
    dwc.pack()
    dwc.place(x=50,y=450)
    
    neu=Label(frame,text="Neutrophils",font=("Calibri",12))
    neu.pack()
    neu.place(x=70,y=480)

    lym=Label(frame,text="Lymphocytes",font=("Calibri",12))
    lym.pack()
    lym.place(x=70,y=510)

    eos=Label(frame,text="Eosinophils",font=("Calibri",12))
    eos.pack()
    eos.place(x=70,y=540)

    mon=Label(frame,text="Monocytes",font=("Calibri",12))
    mon.pack()
    mon.place(x=70,y=570)

    bas=Label(frame,text="Basophils",font=("Calibri",12))
    bas.pack()
    bas.place(x=70,y=600)
    
    res=Label(frame,text="Result",font=("Calibri",12))
    res.pack()
    res.place(x=375,y=150)
    
    d1=float(data[6])    
    if(d1>=12 and d1<=18):
        hemo1=Label(frame,text=data[6],font=("Calibri",12))
    else:
        hemo1=Label(frame,text=data[6],font=("Calibri",12,"bold"))    
    hemo1.pack()
    hemo1.place(x=375,y=180)

    d1=float(data[7])    
    if(d1>=4 and d1<=6):
        rbc1=Label(frame,text=data[7],font=("Calibri",12))
    else:
        rbc1=Label(frame,text=data[7],font=("Calibri",12,"bold"))  
    rbc1.pack()
    rbc1.place(x=375,y=210)

    d1=float(data[8])
    if(d1>=35 and d1<=47):
        pcv1=Label(frame,text=data[8],font=("Calibri",12))
    else:
        pcv1=Label(frame,text=data[8],font=("Calibri",12,"bold"))  
    pcv1.pack()
    pcv1.place(x=375,y=240)

    d1=float(data[9])
    if(d1>=78 and d1<=100):
        mcv1=Label(frame,text=data[9],font=("Calibri",12))
    else:
        mcv1=Label(frame,text=data[9],font=("Calibri",12,"bold"))    
    mcv1.pack()
    mcv1.place(x=375,y=270)

    d1=float(data[10])
    if(d1>=27 and d1<=32):
        mch1=Label(frame,text=data[10],font=("Calibri",12))
    else:
        mch1=Label(frame,text=data[10],font=("Calibri",12,"bold"))    
    mch1.pack()
    mch1.place(x=375,y=300)

    d1=float(data[11])
    if(d1>=30 and d1<=36):
        mchc1=Label(frame,text=data[11],font=("Calibri",12))
    else:
        mchc1=Label(frame,text=data[11],font=("Calibri",12,"bold"))    
    mchc1.pack()
    mchc1.place(x=375,y=330)

    d1=float(data[12])
    if(d1>=11 and d1<=14):
        rdw1=Label(frame,text=data[12],font=("Calibri",12))
    else:
        rdw1=Label(frame,text=data[12],font=("Calibri",12,"bold"))
    rdw1.pack()
    rdw1.place(x=375,y=360)

    d1=float(data[13])
    if(d1>=4000 and d1<=10000):
        wbc1=Label(frame,text=data[13],font=("Calibri",12))
    else:
        wbc1=Label(frame,text=data[13],font=("Calibri",12,"bold"))
    wbc1.pack()
    wbc1.place(x=375,y=390)

    d1=float(data[14])
    if(d1>=150000 and d1<=450000):
        pla1=Label(frame,text=data[14],font=("Calibri",12))
    else:
        pla1=Label(frame,text=data[14],font=("Calibri",12,"bold"))    
    pla1.pack()
    pla1.place(x=375,y=420)

    d1=float(data[15])
    if(d1>=45 and d1<=75):
        neu1=Label(frame,text=data[15],font=("Calibri",12))
    else:
       neu1=Label(frame,text=data[15],font=("Calibri",12,"bold"))    
    neu1.pack()
    neu1.place(x=375,y=480)

    d1=float(data[16])
    if(d1>=20 and d1<=40):
        lym1=Label(frame,text=data[16],font=("Calibri",12))
    else:
       lym1=Label(frame,text=data[16],font=("Calibri",12,"bold"))
    lym1.pack()
    lym1.place(x=375,y=510)

    d1=float(data[17])
    if(d1>=0 and d1<=4):
        eos1=Label(frame,text=data[17],font=("Calibri",12))
    else:
        eos1=Label(frame,text=data[17],font=("Calibri",12,"bold"))
    eos1.pack()
    eos1.place(x=375,y=540)

    d1=float(data[18])
    if(d1>=2 and d1<=8):
        mon1=Label(frame,text=data[18],font=("Calibri",12))
    else:
        mon1=Label(frame,text=data[18],font=("Calibri",12,"bold"))
    mon1.pack()
    mon1.place(x=375,y=570)

    d1=float(data[19])
    if(d1>=0 and d1<=1):
        bas1=Label(frame,text=data[19],font=("Calibri",12))
    else:
        bas1=Label(frame,text=data[19],font=("Calibri",12,"bold"))
    bas1.pack()
    bas1.place(x=375,y=600)
    
    nor=Label(frame,text="Normal Range",font=("Calibri",12))
    nor.pack()
    nor.place(x=615,y=150)

    hemo2=Label(frame,text="(12.0-18.0 gm/dl)",font=("Calibri",12))
    hemo2.pack()
    hemo2.place(x=615,y=180)

    rbc2=Label(frame,text="(4.0-6.0 mil/cu.mm)",font=("Calibri",12))
    rbc2.pack()
    rbc2.place(x=615,y=210)

    pcv2=Label(frame,text="(35-47%)",font=("Calibri",12))
    pcv2.pack()
    pcv2.place(x=615,y=240)

    mcv2=Label(frame,text="(78-100 fl)",font=("Calibri",12))
    mcv2.pack()
    mcv2.place(x=615,y=270)

    mch2=Label(frame,text="(27-32 pg)",font=("Calibri",12))
    mch2.pack()
    mch2.place(x=615,y=300)

    mchc2=Label(frame,text="(30-36 g/dl)",font=("Calibri",12))
    mchc2.pack()
    mchc2.place(x=615,y=330)

    rdw2=Label(frame,text="(11-14%)",font=("Calibri",12))
    rdw2.pack()
    rdw2.place(x=615,y=360)

    wbc2=Label(frame,text="(4000-10000/c.mm in adults)",font=("Calibri",12))
    wbc2.pack()
    wbc2.place(x=615,y=390)
    
    pla2=Label(frame,text="(150000-450000 /c. mm.)",font=("Calibri",12))
    pla2.pack()
    pla2.place(x=615,y=420)
    
    neu2=Label(frame,text="% (45-75%)",font=("Calibri",12))
    neu2.pack()
    neu2.place(x=615,y=480)

    lym2=Label(frame,text="% (20-40%)",font=("Calibri",12))
    lym2.pack()
    lym2.place(x=615,y=510)

    eos2=Label(frame,text="% (00-04%)",font=("Calibri",12))
    eos2.pack()
    eos2.place(x=615,y=540)

    mon2=Label(frame,text="% (02-08%)",font=("Calibri",12))
    mon2.pack()
    mon2.place(x=615,y=570)

    bas2=Label(frame,text="% (0-1%)",font=("Calibri",12))
    bas2.pack()
    bas2.place(x=615,y=600)

    dis=Label(frame,text="Disease",font=("Calibri",15))
    dis.pack()
    dis.place(x=1010,y=100)

    ol=["Fever","Cold","Cold&Cough","Diarrhea","Hemorrhage","Leukemia","Anemia","Neutropenia","Lupus","Celiac"]
    var=StringVar()
    var.set("Fever")
    entry=OptionMenu(root,var,*ol,command=func)
    entry.pack()
    entry.place(x=1100,y=100)

    m1=Label(frame,text="Medicine",font=("Calibri",15))
    m1.pack()
    m1.place(x=1000,y=150)

    entry1=Entry(frame,font=("Calibri",15))
    entry1.pack()
    entry1.place(x=1100,y=150)

    entry2=Entry(frame,font=("Calibri",15))
    entry2.pack()
    entry2.place(x=1100,y=200)

    entry3=Entry(frame,font=("Calibri",15))
    entry3.pack()
    entry3.place(x=1100,y=250)

    home=Button(frame, text = 'Back to Home Page',font=("Calibri",15),command=lambda:main(frame,h,w,root))
    home.pack()
    home.place(x=950,y=300)
    
    submit=Button(frame, text = 'Submit',font=("Calibri",15),command=lambda:logdoc5(frame,h,w,root,var.get(),entry1.get(),entry2.get(),entry3.get(),data,name))
    submit.pack()
    submit.place(x=1230,y=300)

    if(inc==1):
        inc=Label(frame,text="Please enter some disease...Please Try Again",font=("Calibri",12))
        inc.pack()
        inc.place(x=1000,y=350)

    if(inc==2):
        inc=Label(frame,text="Please enter some medicine...Please Try Again",font=("Calibri",12))
        inc.pack()
        inc.place(x=1000,y=350)

def func(value):
    a=value
        
def logdoc5(frame,h,w,root,dis,m1,m2,m3,data,name):

    if(m1=='' and m2=='' and m3==''):
        num=2
        logdoc4(frame,h,w,root,num,data[3],name)
    else:
        num=1
        logdoc6(frame,h,w,root,num,data[3],dis,m1,m2,m3,data,name)

def logdoc6(frame,h,w,root,num,patid,dis,m1,m2,m3,data,name):

    print(name)
    print(type(name))
    row=[data[0],data[1],data[2],data[3],data[4],data[5],dis,m1,m2,m3,name]
    f = open('patient2.csv','a',newline='')
    writer = csv.writer(f)
    writer.writerow(row)
    f.close()

    input = open('patient1.csv', 'r')
    output = open('patientc.csv', 'w',newline='')

    writer = csv.writer(output)
    for d in csv.reader(input):
        if d[3]!=patid:
            writer.writerow(d)
        else:
            d[20]=1
            writer.writerow(d)
    input.close()
    output.close()
    
    os.remove("patient1.csv")
    os.rename('patientc.csv', 'patient1.csv')

    frame.pack_forget()
    frame = Frame(root,width=w,height=h)
    frame.pack()
    
    load=Image.open("2.png")
    render=ImageTk.PhotoImage(load)
    img=Label(frame,image=render)
    img.image=render
    img.place(x=0,y=0) 

    info=Label(frame,text="Information Successfully Filled",font=("Calibri",25))
    info.pack()
    info.place(x=300,y=300)

    home=Button(frame, text = 'Back to Home Page',font=("Calibri",15),command=lambda:main(frame,h,w,root))
    home.pack()
    home.place(x=420,y=360)        
    
def logpat(frame,h,w,root,inc):

    frame.pack_forget()
    frame = Frame(root,width=w,height=h)
    frame.pack()
    
    load=Image.open("2.png")
    render=ImageTk.PhotoImage(load)
    img=Label(frame,image=render)
    img.image=render
    img.place(x=0,y=0)

    wel=Label(frame,text="Enter Your Login Details",font=("Calibri",25))
    wel.pack()
    wel.place(x=350,y=195)

    usr=Label(frame,text="Patient Id",font=("Calibri",15))
    usr.pack()
    usr.place(x=360,y=260)

    pas=Label(frame,text="Password",font=("Calibri",15))
    pas.pack()
    pas.place(x=365,y=310)

    entry1=Entry(frame,font=("Calibri",15))
    entry1.pack()
    entry1.place(x=460,y=260)

    entry2=Entry(frame,show='*',font=("Calibri",15))
    entry2.pack()
    entry2.place(x=460,y=310)
    
    submit=Button(frame, text = 'Submit',font=("Calibri",15),command=lambda:logpat1(frame,h,w,root,entry1.get(),entry2.get()))
    submit.pack()
    submit.place(x=590,y=360)

    num=0
    
    home=Button(frame, text = 'Back to Home Page',font=("Calibri",15),command=lambda:main(frame,h,w,root))
    home.pack()
    home.place(x=350,y=360)
    
    if(inc==1):
        inc=Label(frame,text="Incorrect Patient Id and Password...Please Try Again",font=("Calibri",12))
        inc.pack()
        inc.place(x=335,y=452)

def logpat1(frame,h,w,root,patid,password):

    f = open('patient.csv', 'r')
    r = csv.reader(f)
    
    next(r)
    inc=1
    
    for row in r:    
        if(row[3]==patid and row[4]==password):
            inc=0
             
    if(inc==0):
        num=1                
    elif(inc==1):
        num=0

    f.close()

    if(num==1):
        logpat2(frame,h,w,root,patid,password)
    elif(num==0):
        logpat(frame,h,w,root,inc)
        
def logpat2(frame,h,w,root,patid,password):

    frame.pack_forget()
    frame = Frame(root,width=w,height=h)
    frame.pack()

    load=Image.open("2.png")
    render=ImageTk.PhotoImage(load)
    img=Label(frame,image=render)
    img.image=render
    img.place(x=0,y=0)

    f = open('patient.csv', 'r')
    r = csv.reader(f)

    next(r)
    
    for row in r:    
        if(row[3]==patid and row[4]==password):
            data=row
            break

    name=data[0]+" "+data[1]

    info=Label(frame,text="Welcome..."+name,font=("Calibri",25))
    info.pack()
    info.place(x=350,y=50)
    
    submit=Button(frame, text = 'Check Your Report',font=("Calibri",15),command=lambda:logpat3(frame,h,w,root,patid,password))
    submit.pack()
    submit.place(x=430,y=250)
    
    submit=Button(frame, text = 'Check Your Prescription',font=("Calibri",15),command=lambda:logpat4(frame,h,w,root,patid,password))
    submit.pack()
    submit.place(x=410,y=310)
    
    home=Button(frame, text = 'Back to Home Page',font=("Calibri",15),command=lambda:main(frame,h,w,root))
    home.pack()
    home.place(x=430,y=370)

def logpat3(frame,h,w,root,patid,password):

    f = open('patient.csv', 'r')
    r = csv.reader(f)

    next(r)
    
    for row in r:    
        if(row[3]==patid and row[4]==password and row[6]=='0'):
            num=5
        elif(row[3]==patid and row[4]==password and row[6]=='1'):
            num=6
    
    if(num==5):
        logpat5(frame,h,w,root,patid,password)
    elif(num==6):
        logpat6(frame,h,w,root,patid,password)

def logpat4(frame,h,w,root,patid,password):

    f = open('patient.csv', 'r')
    r = csv.reader(f)

    next(r)
    
    for row in r:    
        if(row[3]==patid and row[4]==password and row[6]=='0'):
            num=5
        elif(row[3]==patid and row[4]==password and row[6]=='1'):
            num=7

    if(num==5):
        logpat5(frame,h,w,root,patid,password)
    elif(num==7):
        logpat7(frame,h,w,root,patid,password)
                
def logpat5(frame,h,w,root,patid,password):

    frame.pack_forget()
    frame = Frame(root,width=w,height=h)
    frame.pack()
    
    load=Image.open("2.png")
    render=ImageTk.PhotoImage(load)
    img=Label(frame,image=render)
    img.image=render
    img.place(x=0,y=0)

    info=Label(frame,text="Please visit Pathologist and do the blood checkup",font=("Calibri",15))
    info.pack()
    info.place(x=300,y=300)

    home=Button(frame, text = 'Go to Back Page',font=("Calibri",15),command=lambda:logpat2(frame,h,w,root,patid,password))
    home.pack()
    home.place(x=420,y=360)

def logpat6(frame,h,w,root,patid,password):

    frame.pack_forget()
    frame = Frame(root,width=w,height=h)
    frame.pack()

    load=Image.open("2.png")
    render=ImageTk.PhotoImage(load)    
    img=Label(frame,image=render)
    img.image=render
    img.place(x=0,y=0)
    
    f = open('patient1.csv', 'r')
    r = csv.reader(f)

    next(r)

    data=[]
    for row in r:
        if(row[3]==patid):
            data=row

    name=Label(frame,text="Name: "+data[0]+" "+data[1],font=("Calibri",15))
    name.pack()
    name.place(x=200,y=20)

    patids=Label(frame,text="Patient Id: "+data[3],font=("Calibri",15))
    patids.pack()
    patids.place(x=600,y=20)

    age=Label(frame,text="Age: "+data[2],font=("Calibri",15))
    age.pack()
    age.place(x=200,y=60)

    gen=Label(frame,text="Gender: "+data[5],font=("Calibri",15))
    gen.pack()
    gen.place(x=600,y=60)
    
    cbc=Label(frame,text="Complete Blood Count",font=("Calibri",20))
    cbc.pack()
    cbc.place(x=335,y=100)

    para=Label(frame,text="Parameters",font=("Calibri",12))
    para.pack()
    para.place(x=50,y=150)

    hemo=Label(frame,text="Hemoglobin",font=("Calibri",12))
    hemo.pack()
    hemo.place(x=50,y=180)

    rbc=Label(frame,text="RBC",font=("Calibri",12))
    rbc.pack()
    rbc.place(x=50,y=210)

    pcv=Label(frame,text="(Hematocrit)PCV",font=("Calibri",12))
    pcv.pack()
    pcv.place(x=50,y=240)

    mcv=Label(frame,text="MCV",font=("Calibri",12))
    mcv.pack()
    mcv.place(x=50,y=270)

    mch=Label(frame,text="MCH",font=("Calibri",12))
    mch.pack()
    mch.place(x=50,y=300)

    mchc=Label(frame,text="MCHC",font=("Calibri",12))
    mchc.pack()
    mchc.place(x=50,y=330)

    rdw=Label(frame,text="RDW",font=("Calibri",12))
    rdw.pack()
    rdw.place(x=50,y=360)

    wbc=Label(frame,text="WBC",font=("Calibri",12))
    wbc.pack()
    wbc.place(x=50,y=390)
    
    pla=Label(frame,text="Platelet Count",font=("Calibri",12))
    pla.pack()
    pla.place(x=50,y=420)

    dwc=Label(frame,text="DIFF WBC Count",font=("Calibri",12))
    dwc.pack()
    dwc.place(x=50,y=450)
    
    neu=Label(frame,text="Neutrophils",font=("Calibri",12))
    neu.pack()
    neu.place(x=70,y=480)

    lym=Label(frame,text="Lymphocytes",font=("Calibri",12))
    lym.pack()
    lym.place(x=70,y=510)

    eos=Label(frame,text="Eosinophils",font=("Calibri",12))
    eos.pack()
    eos.place(x=70,y=540)

    mon=Label(frame,text="Monocytes",font=("Calibri",12))
    mon.pack()
    mon.place(x=70,y=570)

    bas=Label(frame,text="Basophils",font=("Calibri",12))
    bas.pack()
    bas.place(x=70,y=600)
    
    res=Label(frame,text="Result",font=("Calibri",12))
    res.pack()
    res.place(x=375,y=150)

    hemo1=Label(frame,text=data[6],font=("Calibri",12))
    hemo1.pack()
    hemo1.place(x=375,y=180)

    rbc1=Label(frame,text=data[7],font=("Calibri",12))
    rbc1.pack()
    rbc1.place(x=375,y=210)

    pcv1=Label(frame,text=data[8],font=("Calibri",12))
    pcv1.pack()
    pcv1.place(x=375,y=240)

    mcv1=Label(frame,text=data[9],font=("Calibri",12))
    mcv1.pack()
    mcv1.place(x=375,y=270)

    mch1=Label(frame,text=data[10],font=("Calibri",12))
    mch1.pack()
    mch1.place(x=375,y=300)

    mchc1=Label(frame,text=data[11],font=("Calibri",12))
    mchc1.pack()
    mchc1.place(x=375,y=330)

    rdw1=Label(frame,text=data[12],font=("Calibri",12))
    rdw1.pack()
    rdw1.place(x=375,y=360)

    wbc1=Label(frame,text=data[13],font=("Calibri",12))
    wbc1.pack()
    wbc1.place(x=375,y=390)
    
    pla1=Label(frame,text=data[14],font=("Calibri",12))
    pla1.pack()
    pla1.place(x=375,y=420)
    
    neu1=Label(frame,text=data[15],font=("Calibri",12))
    neu1.pack()
    neu1.place(x=375,y=480)

    lym1=Label(frame,text=data[16],font=("Calibri",12))
    lym1.pack()
    lym1.place(x=375,y=510)

    eos1=Label(frame,text=data[17],font=("Calibri",12))
    eos1.pack()
    eos1.place(x=375,y=540)

    mon1=Label(frame,text=data[18],font=("Calibri",12))
    mon1.pack()
    mon1.place(x=375,y=570)

    bas1=Label(frame,text=data[19],font=("Calibri",12))
    bas1.pack()
    bas1.place(x=375,y=600)
    
    nor=Label(frame,text="Normal Range",font=("Calibri",12))
    nor.pack()
    nor.place(x=615,y=150)

    hemo2=Label(frame,text="(12.0-18.0 gm/dl)",font=("Calibri",12))
    hemo2.pack()
    hemo2.place(x=615,y=180)

    rbc2=Label(frame,text="(4.0-6.0 mil/cu.mm)",font=("Calibri",12))
    rbc2.pack()
    rbc2.place(x=615,y=210)

    pcv2=Label(frame,text="(35-47%)",font=("Calibri",12))
    pcv2.pack()
    pcv2.place(x=615,y=240)

    mcv2=Label(frame,text="(78-100 fl)",font=("Calibri",12))
    mcv2.pack()
    mcv2.place(x=615,y=270)

    mch2=Label(frame,text="(27-32 pg)",font=("Calibri",12))
    mch2.pack()
    mch2.place(x=615,y=300)

    mchc2=Label(frame,text="(30-36 g/dl)",font=("Calibri",12))
    mchc2.pack()
    mchc2.place(x=615,y=330)

    rdw2=Label(frame,text="(11-14%)",font=("Calibri",12))
    rdw2.pack()
    rdw2.place(x=615,y=360)

    wbc2=Label(frame,text="(4000-10000/c.mm in adults)",font=("Calibri",12))
    wbc2.pack()
    wbc2.place(x=615,y=390)
    
    pla2=Label(frame,text="(150000-450000 /c. mm.)",font=("Calibri",12))
    pla2.pack()
    pla2.place(x=615,y=420)
    
    neu2=Label(frame,text="% (45-75%)",font=("Calibri",12))
    neu2.pack()
    neu2.place(x=615,y=480)

    lym2=Label(frame,text="% (20-40%)",font=("Calibri",12))
    lym2.pack()
    lym2.place(x=615,y=510)

    eos2=Label(frame,text="% (00-04%)",font=("Calibri",12))
    eos2.pack()
    eos2.place(x=615,y=540)

    mon2=Label(frame,text="% (02-08%)",font=("Calibri",12))
    mon2.pack()
    mon2.place(x=615,y=570)

    bas2=Label(frame,text="% (0-1%)",font=("Calibri",12))
    bas2.pack()
    bas2.place(x=615,y=600)

    home=Button(frame, text = 'Go to back Page',font=("Calibri",15),command=lambda:logpat2(frame,h,w,root,patid,password))
    home.pack()
    home.place(x=350,y=650)

def logpat7(frame,h,w,root,patid,password):

    f = open('patient1.csv', 'r')
    r = csv.reader(f)

    next(r)
    
    for row in r:    
        if(row[3]==patid and row[4]==password and row[20]=='0'):
            num=8
        elif(row[3]==patid and row[4]==password and row[20]=='1'):
            num=9

    if(num==8):
        logpat8(frame,h,w,root,patid,password)
    elif(num==9):
         logpat9(frame,h,w,root,patid,password)   
            
def logpat8(frame,h,w,root,patid,password):

    frame.pack_forget()
    frame = Frame(root,width=w,height=h)
    frame.pack()
    
    load=Image.open("2.png")
    render=ImageTk.PhotoImage(load)
    img=Label(frame,image=render)
    img.image=render
    img.place(x=0,y=0)

    info=Label(frame,text="Please visit the Doctor and get the prescription",font=("Calibri",15))
    info.pack()
    info.place(x=300,y=300)

    home=Button(frame, text = 'Go to back Page',font=("Calibri",15),command=lambda:logpat2(frame,h,w,root,patid,password))
    home.pack()
    home.place(x=420,y=360)

def logpat9(frame,h,w,root,patid,password):

    frame.pack_forget()
    frame = Frame(root,width=w,height=h)
    frame.pack()
    
    load=Image.open("2.png")
    render=ImageTk.PhotoImage(load)
    img=Label(frame,image=render)
    img.image=render
    img.place(x=0,y=0)
    
    f = open('patient2.csv', 'r')
    r = csv.reader(f)

    next(r)

    data=[]
    for row in r:
        if(row[3]==patid):
            data=row

    name=Label(frame,text="Name: "+data[0]+" "+data[1],font=("Calibri",15))
    name.pack()
    name.place(x=200,y=20)

    patids=Label(frame,text="Patient Id: "+data[3],font=("Calibri",15))
    patids.pack()
    patids.place(x=600,y=20)

    age=Label(frame,text="Age: "+data[2],font=("Calibri",15))
    age.pack()
    age.place(x=200,y=60)

    gen=Label(frame,text="Gender: "+data[5],font=("Calibri",15))
    gen.pack()
    gen.place(x=600,y=60)

    name=Label(frame,text="Prescribed By Dr. "+data[10],font=("Calibri",15))
    name.pack()
    name.place(x=250,y=250)
    
    if(row[8]=='' and row[9]==''):
        bas2=Label(frame,text="The Disease you have is "+row[6]+" and you should take "+row[7]+" medicine",font=("Calibri",15))
        bas2.pack()
        bas2.place(x=200,y=300)
    elif(row[9]==''):
        bas2=Label(frame,text="The Disease you have is "+row[6]+" and you should take "+row[7]+" and "+row[8]+" medicine",font=("Calibri",15))
        bas2.pack()
        bas2.place(x=200,y=300)
    else:
        bas2=Label(frame,text="The Disease you have is "+row[6]+" and you should take "+row[7]+", "+row[8]+" and "+row[9]+" medicine",font=("Calibri",15))
        bas2.pack()
        bas2.place(x=200,y=300)
        
    home=Button(frame, text = 'Go to back Page',font=("Calibri",15),command=lambda:logpat2(frame,h,w,root,patid,password))
    home.pack()
    home.place(x=430,y=350)
        
def analysis(frame,h,w,root,inc):

    frame.pack_forget()
    frame = Frame(root,width=w,height=h)
    frame.pack()
    
    load=Image.open("2.png")
    render=ImageTk.PhotoImage(load)
    img=Label(frame,image=render)
    img.image=render
    img.place(x=0,y=0)

    wel=Label(frame,text="Enter The Admistrative Details",font=("Calibri",25))
    wel.pack()
    wel.place(x=300,y=195)

    usr=Label(frame,text="Username",font=("Calibri",15))
    usr.pack()
    usr.place(x=350,y=260)

    pas=Label(frame,text="Password",font=("Calibri",15))
    pas.pack()
    pas.place(x=355,y=310)

    entry1=Entry(frame,font=("Calibri",15))
    entry1.pack()
    entry1.place(x=450,y=260)

    entry2=Entry(frame,show='*',font=("Calibri",15))
    entry2.pack()
    entry2.place(x=450,y=310)
    
    submit=Button(frame, text = 'Submit',font=("Calibri",15),command=lambda:analysis1(frame,h,w,root,entry1.get(),entry2.get()))
    submit.pack()
    submit.place(x=580,y=360)

    num=0
    
    home=Button(frame, text = 'Back to Home Page',font=("Calibri",15),command=lambda:main(frame,h,w,root))
    home.pack()
    home.place(x=350,y=360)
    
    if(inc==1):
        inc=Label(frame,text="Incorrect Username and Password...Please Try Again",font=("Calibri",12))
        inc.pack()
        inc.place(x=335,y=452)

def analysis1(frame,h,w,root,username,password):

    if(username=='admin' and password=='admin'):
        inc=0
        analysis2(frame,h,w,root,inc)
    else:
        num=1
        analysis(frame,h,w,root,num)
        
def analysis2(frame,h,w,root,inc):
    
    frame.pack_forget()
    frame = Frame(root,width=w,height=h)
    frame.pack()
    
    load=Image.open("2.png")
    render=ImageTk.PhotoImage(load)
    img=Label(frame,image=render)
    img.image=render
    img.place(x=0,y=0)
    
    ana=Label(frame,text="Analysis of The Patients",font=("Calibri",25))
    ana.pack()
    ana.place(x=350,y=30)

    df=pd.read_csv("patient1.csv")
    df1=pd.read_csv("patient2.csv")
    
    a=0
    b=0
    c=0
    
    ages=Button(frame, text = 'Age',font=("Calibri",15),command=lambda:age(df,a,b,c))
    ages.pack()
    ages.place(x=350,y=100)

    genders=Button(frame, text = 'Gender',font=("Calibri",15),command=lambda:gender(df,a,b))
    genders.pack()
    genders.place(x=590,y=100)

    hemos=Button(frame, text = 'Hemoglobin',font=("Calibri",15),command=lambda:hemo(df,a,b,c))
    hemos.pack()
    hemos.place(x=350,y=150)

    rbcs=Button(frame, text = 'RBC',font=("Calibri",15),command=lambda:rbc(df,a,b,c))
    rbcs.pack()
    rbcs.place(x=590,y=150)

    pcvs=Button(frame, text = 'PCV',font=("Calibri",15),command=lambda:pcv(df,a,b,c))
    pcvs.pack()
    pcvs.place(x=350,y=200)

    pcvs=Button(frame, text = 'MCV',font=("Calibri",15),command=lambda:mcv(df,a,b,c))
    pcvs.pack()
    pcvs.place(x=590,y=200)
    
    mchs=Button(frame, text = 'MCH',font=("Calibri",15),command=lambda:mch(df,a,b,c))
    mchs.pack()
    mchs.place(x=350,y=250)

    mchcs=Button(frame, text = 'MCHC',font=("Calibri",15),command=lambda:mchc(df,a,b,c))
    mchcs.pack()
    mchcs.place(x=590,y=250)

    rdws=Button(frame, text = 'RDW',font=("Calibri",15),command=lambda:rdw(df,a,b,c))
    rdws.pack()
    rdws.place(x=350,y=300)

    wbcs=Button(frame, text = 'WBC',font=("Calibri",15),command=lambda:wbc(df,a,b,c))
    wbcs.pack()
    wbcs.place(x=590,y=300)

    plas=Button(frame, text = 'Platelet',font=("Calibri",15),command=lambda:pla(df,a,b,c))
    plas.pack()
    plas.place(x=350,y=350)

    neus=Button(frame, text = 'Neutrophils',font=("Calibri",15),command=lambda:neu(df,a,b,c))
    neus.pack()
    neus.place(x=590,y=350)

    lyms=Button(frame, text = 'Lymphocytes',font=("Calibri",15),command=lambda:lym(df,a,b,c))
    lyms.pack()
    lyms.place(x=350,y=400)

    eoss=Button(frame, text = 'Eosinophils',font=("Calibri",15),command=lambda:eos(df,a,b,c))
    eoss.pack()
    eoss.place(x=590,y=400)    

    mons=Button(frame, text = 'Monocytes',font=("Calibri",15),command=lambda:mon(df,a,b,c))
    mons.pack()
    mons.place(x=350,y=450)

    bass=Button(frame, text = 'Basophils',font=("Calibri",15),command=lambda:bas(df,a,b,c))
    bass.pack()
    bass.place(x=590,y=450)

    diss=Button(frame, text = 'Diseases',font=("Calibri",15),command=lambda:dis(df1))
    diss.pack()
    diss.place(x=480,y=500)
    
    home=Button(frame, text = 'Back to Home Page',font=("Calibri",15),command=lambda:main(frame,h,w,root))
    home.pack()
    home.place(x=435,y=550)

def dis(df):

    a=b=c=d=e=f=g=h=i=j=0
    
    dfList = df['Disease'].tolist()
    
    for x in range(len(dfList)):
        if(dfList[x]=="Fever"):
            a=a+1
        elif(dfList[x]=="Cold"):
            b=b+1
        elif(dfList[x]=="Cold&Cough"):
            c=c+1
        elif(dfList[x]=="Diarrhea"):
            d=d+1
        elif(dfList[x]=="Hemorrhage"):
            e=e+1
        elif(dfList[x]=="Leukemia"):
            f=f+1
        elif(dfList[x]=="Anemia"):
            g=g+1
        elif(dfList[x]=="Neutropenia"):
            h=h+1
        elif(dfList[x]=="Lupus"):
            i=i+1
        else:
            j=j+1
           
    labels = "Fever","Cold","Cold&Cough","Diarrhea","Hemorrhage","Leukemia","Anemia","Neutropenia","Lupus","Celiac"
    sizes=[a,b,c,d,e,f,g,h,i,j]
    plot1(labels,sizes)
    
def age(df,a,b,c):
    
    dfList = df['Age'].tolist()
    
    for x in range(len(dfList)):
        if(dfList[x]<18):
            a=a+1
        elif((dfList[x]>=18) & (dfList[x]<59)):
            b=b+1
        else:
            c=c+1

    labels = '0-17', '18-59', '60+'
    sizes=[a,b,c]
    plot1(labels,sizes)
    
def gender(df,a,b):
    
    dfList = df['Gender'].tolist()

    for x in range(len(dfList)):
        if(dfList[x]=='Male'):
            a=a+1
        else:
            b=b+1


    labels = 'Male', 'Female'
    sizes=[a,b]
    plot1(labels,sizes)

def plot1(labels,sizes):
    plt.pie(sizes,labels=labels,autopct='%1.1f%%',)
    plt.axis('equal')
    plt.show()
    
def hemo(df,a,b,c):

    dfList = df['Hemoglobin'].tolist()
    
    for x in range(len(dfList)):
        if(dfList[x]<12):
            a=a+1
        elif((dfList[x]>=12) & (dfList[x]<=18)):
            b=b+1
        else:
            c=c+1

    plot2(a,b,c)

def rbc(df,a,b,c):

    dfList = df['RBC'].tolist()
    
    for x in range(len(dfList)):
        if(dfList[x]<4):
            a=a+1
        elif((dfList[x]>=4) & (dfList[x]<=6)):
            b=b+1
        else:
            c=c+1

    plot2(a,b,c)

def pcv(df,a,b,c):
    
    dfList = df['PCV'].tolist()
    
    for x in range(len(dfList)):
        if(dfList[x]<35):
            a=a+1
        elif((dfList[x]>=35) & (dfList[x]<=47)):
            b=b+1
        else:
            c=c+1

    plot2(a,b,c)

def mcv(df,a,b,c):
    
    dfList = df['MCV'].tolist()
    
    for x in range(len(dfList)):
        if(dfList[x]<78):
            a=a+1
        elif((dfList[x]>=78) & (dfList[x]<=100)):
            b=b+1
        else:
            c=c+1

    plot2(a,b,c)

def mch(df,a,b,c):

    dfList = df['MCH'].tolist()
    
    for x in range(len(dfList)):
        if(dfList[x]<27):
            a=a+1
        elif((dfList[x]>=27) & (dfList[x]<=32)):
            b=b+1
        else:
            c=c+1

    plot2(a,b,c)

def mchc(df,a,b,c):

    dfList = df['MCHC'].tolist()
    
    for x in range(len(dfList)):
        if(dfList[x]<30):
            a=a+1
        elif((dfList[x]>=30) & (dfList[x]<=36)):
            b=b+1
        else:
            c=c+1

    plot2(a,b,c)

def rdw(df,a,b,c):

    dfList = df['RDW'].tolist()
    
    for x in range(len(dfList)):
        if(dfList[x]<11):
            a=a+1
        elif((dfList[x]>=11) & (dfList[x]<=14)):
            b=b+1
        else:
            c=c+1

    plot2(a,b,c)

def wbc(df,a,b,c):

    dfList = df['WBC'].tolist()
    
    for x in range(len(dfList)):
        if(dfList[x]<4000):
            a=a+1
        elif((dfList[x]>=4000) & (dfList[x]<=10000)):
            b=b+1
        else:
            c=c+1

    plot2(a,b,c)

def pla(df,a,b,c):

    dfList = df['Platelet'].tolist()
    
    for x in range(len(dfList)):
        if(dfList[x]<150000):
            a=a+1
        elif((dfList[x]>=150000) & (dfList[x]<=450000)):
            b=b+1
        else:
            c=c+1

    plot2(a,b,c)

def neu(df,a,b,c):

    dfList = df['Neutrophils'].tolist()
    
    for x in range(len(dfList)):
        if(dfList[x]<45):
            a=a+1
        elif((dfList[x]>=45) & (dfList[x]<=75)):
            b=b+1
        else:
            c=c+1

    plot2(a,b,c)

def lym(df,a,b,c):

    dfList = df['Lymphocytes'].tolist()
    
    for x in range(len(dfList)):
        if(dfList[x]<20):
            a=a+1
        elif((dfList[x]>=20) & (dfList[x]<=40)):
            b=b+1
        else:
            c=c+1

    plot2(a,b,c)

def eos(df,a,b,c):

    dfList = df['Eosinophils'].tolist()
    
    for x in range(len(dfList)):
        if(dfList[x]<0):
            a=a+1
        elif((dfList[x]>=0) & (dfList[x]<=4)):
            b=b+1
        else:
            c=c+1

    plot2(a,b,c)

def mon(df,a,b,c):

    dfList = df['Monocytes'].tolist()
    
    for x in range(len(dfList)):
        if(dfList[x]<2):
            a=a+1
        elif((dfList[x]>=2) & (dfList[x]<=8)):
            b=b+1
        else:
            c=c+1

    plot2(a,b,c)

def bas(df,a,b,c):

    dfList = df['Basophils'].tolist()
    
    for x in range(len(dfList)):
        if(dfList[x]<0):
            a=a+1
        elif((dfList[x]>=0) & (dfList[x]<=1)):
            b=b+1
        else:
            c=c+1

    plot2(a,b,c)

def plot2(a,b,c):

    labels = 'Low', 'Normal', 'High'
    sizes=[a,b,c]
    plt.pie(sizes,labels=labels,autopct='%1.1f%%',)
    plt.axis('equal')
    plt.show()
    
root = Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))

frame = Frame(root,width=w,height=h)
frame.pack()

def main(frame,h,w,root):
    
    frame.pack_forget()
    frame = Frame(root,width=w,height=h)
    frame.pack()
    
    load=Image.open("1.png")
    render=ImageTk.PhotoImage(load)
    img=Label(frame,image=render)
    img.image=render
    img.place(x=0,y=0)

    num=0
    
    doctor=Button(frame, text = 'Login As Doctor',font=("Calibri",15),command=lambda:logdoc(frame,h,w,root,num))
    doctor.pack()
    doctor.place(x=330,y=240)
    
    pathologist=Button(frame, text = 'Login As Pathologist',font=("Calibri",15),command=lambda:logpatho(frame,h,w,root,num))
    pathologist.pack()
    pathologist.place(x=500,y=240)

    lpatient=Button(frame, text = 'Login As Patient',font=("Calibri",15),command=lambda:logpat(frame,h,w,root,num))
    lpatient.pack()
    lpatient.place(x=330,y=300)
    
    cpatient=Button(frame, text = 'Create a Patient Account',font=("Calibri",15),command=lambda:regpat(frame,h,w,root,num))
    cpatient.pack()
    cpatient.place(x=500,y=300)

    cpatient=Button(frame, text = 'Analysis',font=("Calibri",15),command=lambda:analysis(frame,h,w,root,num))
    cpatient.pack()
    cpatient.place(x=450,y=360)
    
    root.mainloop()

if __name__=="__main__":
    main(frame,h,w,root)
