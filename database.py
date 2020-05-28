from tkinter import *
import psycopg2
import parser
import tkinter.messagebox

conn=psycopg2.connect(

    database='studentdb',
    user='postgres',
    password='Roydud',
    host='localhost',
    port='5433'

)


def insert():

    try:

        name = namee.get()
        rollno = rolle.get()
        email = str(emaile.get()).lower()
        gender = var.get()
        dob = dobe.get()
        cur = conn.cursor()

        cur.execute(
            'create table  if not exists student(rollno varchar(10) primary key,name varchar(50) not null,email varchar(50) unique,'
            'gender varchar(10),dob date not null)')
        cur.execute('insert into student(rollno,name,email,gender,dob) values(%s,%s,%s,%s,%s)',
                    (rollno, name, email, gender, dob))
        cur.close()
        conn.commit()
        tkinter.messagebox.showinfo('ADD STUDENT','Student is added')
        na.set('')
        ro.set('')
        em.set('')
        do.set('')


    except Exception:
        cur = conn.cursor()
        tkinter.messagebox.showinfo('ERROR', 'Error while adding data')
        cur.close()
        conn.commit()


def update():
    try:
        name = namee.get()
        rollno = rolle.get()
        email = emaile.get()
        gender = var.get()
        dob = dobe.get()

        cur = conn.cursor()
        if name != '':
            cur.execute('update student set name=%s where rollno=%s', (name, rollno,))
        if email != '':
            cur.execute('update student set email=%s where rollno=%s', (email, rollno,))
        if gender != '':
            cur.execute('update student set gender=%s where rollno=%s', (gender, rollno,))
        if dob != '':
            cur.execute('update student set dob=%s where rollno=%s', (dob, rollno,))
        cur.close()
        conn.commit()
        tkinter.messagebox.showinfo('UPDATE', 'Info is updated')
        na.set('')
        ro.set('')
        em.set('')
        do.set('')

    except Exception:
        cur = conn.cursor()
        tkinter.messagebox.showerror('ERROR', 'Error while updating data')
        cur.close()
        conn.commit()


def delete():
    try:
        rollno = rolle.get()
        cur = conn.cursor()
        cur.execute('delete from student where rollno=%s', (rollno,))
        cur.close()
        conn.commit()
        tkinter.messagebox.showinfo('DELETE', 'Student is deleted')
        ro.set('')
    except Exception:
        cur = conn.cursor()
        tkinter.messagebox.showerror('ERROR', 'something is wrong')
        cur.close()
        conn.commit()



def show():
    try:
        showbox.delete(0, END)
        cur = conn.cursor()
        cur.execute('select * from student')
        rows = cur.fetchall()
        i = 0
        for r in rows:
            showbox.insert(i, r)
            i += 1
        cur.close()
        conn.commit()
    except Exception:
        cur = conn.cursor()
        tkinter.messagebox.showerror('ERROR', 'error in fetching data')
        cur.close()
        conn.commit()

def find():
    global screen

    def search():
        global lst
        try:
            searchbox.delete(0, END)
            namef = namefe.get()
            rollf = rollfe.get()
            cur = conn.cursor()
            if rollf !='':
                cur.execute('select * from student where rollno=%s', (rollf,))
                rows = cur.fetchall()
                i = 0
                for r in rows:
                    searchbox.insert(i, r)
                cur.close()
                conn.commit()
            elif namef !='':
                searchbox.delete(0, END)
                namef = namefe.get()
                rollf = rollfe.get()
                cur = conn.cursor()
                cur.execute('select * from student where name=%s', (namef,))
                rows = cur.fetchall()
                i = 0
                for r in rows:
                    searchbox.insert(i, r)
                    i += 1
                cur.close()
                conn.commit()
            if len(rows)==0:
                searchbox.insert(0,'Data is not found')
        except Exception:
            cur = conn.cursor()
            tkinter.messagebox.showerror('ERROR', 'Something went wrong')
            cur.close()
            conn.commit()
        fro.set('')
        fna.set('')


    screen=Toplevel(root)
    screen.geometry('500x580+200+20')
    screen.configure(bg='grey')
    screen.resizable(width=False, height=False)
    namefl=Label(screen,text='NAME',font=('bold',15,), bg='grey',fg='black').place(x=40,y=40)
    fna=StringVar()
    fna.set('')
    namefe = Entry(screen, font=('bold', 15,), bg='dark grey', textvar=fna, fg='black', width=25, bd=4)
    namefe.place(x=160,y=40)

    orl=Label(screen,text='OR',font=('bold',15,), bg='grey',fg='black').place(x=280,y=90)

    rollfl = Label(screen, text='ROLL NO.',font=('bold', 15,), bg='grey', fg='black').place(x=40, y=140)
    fro = StringVar()
    fro.set('')
    rollfe = Entry(screen, font=('bold', 15,), bg='dark grey', textvar=fro, fg='black', width=25, bd=4)
    rollfe.place(x=160,
                                                                                                              y=140)
    Button(screen, text='SEARCH', width=27, height=1, font=('arial', 13, 'bold'), bd=4,command=lambda : search(), bg='grey',fg='black').place(x=150,y=220)
    searchbox = Listbox(screen, width=39, height=8, font=('bold', 15), bg='dark grey', fg='black', bd=2)
    searchbox.place(x=40, y=300)

    screen.mainloop()


root = Tk()
root.title("STUDENT DATABASE")
root.config(background='grey')
root.resizable(width=False, height=False)
root.geometry('500x650+0+0')
display=Frame(root)

title=Label(root,text='STUDENT DETAIL',font=('arial',20,'bold'),fg='black',bg='grey')
title.place(x=180,y=10)
namel=Label(root,text='FULL NAME',font=('bold',15),fg='black',bg='grey')
namel.place(x=50,y=60)
na=StringVar()
na.set('')

namee=Entry(root,font=('bold',15,), bg='dark grey',textvar=na,fg='black',width=25,bd=4)
namee.grid()
namee.place(x=180,y=60)

roll1=Label(root,text='Roll no.',font=('bold',15),fg='black',bg='grey')
roll1.place(x=50,y=110)
ro=StringVar()
ro.set('')
rolle=Entry(root,font=('bold',15,), bg='dark grey',textvar=ro,fg='black',width=25,bd=4)
rolle.grid()
rolle.place(x=180,y=110)


email1=Label(root,text='Email Id',font=('bold',15),fg='black',bg='grey')
email1.place(x=50,y=160)
em=StringVar()
em.set('')
emaile=Entry(root,font=('bold',15), bg='dark grey',textvar=em,fg='black',width=25,bd=4)
emaile.grid()
emaile.place(x=180,y=160)

gen=Label(root,text='Gender',font=('bold',15),fg='black',bg='grey')
gen.place(x=50,y=210)

var=StringVar()
radm=Radiobutton(text='Male',padx=5,variable=var,font=('bold',15),fg='white',value='Male',bg='grey')
radm.place(x=170,y=210)

radf=Radiobutton(text='Female',padx=5,variable=var,font=('bold',15),fg='white',value='Female',bg='grey')
radf.place(x=260,y=210)

rado=Radiobutton(text='Others',padx=5,variable=var,font=('bold',15),fg='white',value='Others',bg='grey')
rado.place(x=380,y=210)

dob=Label(root,text='DOB',font=('bold',15),fg='black',bg='grey')
dob.place(x=50,y=260)
dfor=Label(root,text='mm/dd/yyyy',font=('bold',10),fg='black',bg='grey')
dfor.place(x=180,y=290)

do=StringVar()
do.set('')
dobe=Entry(root,font=('bold',15,),textvar=do, bg='dark grey',fg='black',width=25,bd=4)
dobe.place(x=180,y=260)
# dobe.insert(0,'mm/dd/yyyy')

addbtn=Button(root, text='ADD', width=7, height=1, font=('arial', 15, 'bold'), bd=4,command=lambda : insert(),bg='grey',fg='black').place(x=20,y=330)
upbtn=Button(root, text='UPDATE', width=7, height=1, font=('arial', 15, 'bold'), bd=4,command=lambda : update(), bg='grey',fg='black').place(x=140,y=330)
delbtn=Button(root, text='DELETE', width=7, height=1, font=('arial', 15, 'bold'), bd=4,command=lambda : delete(), bg='grey',fg='black').place(x=260,y=330)
showbtn=Button(root, text='SHOW', width=7, height=1, font=('arial', 15, 'bold'), bd=4,command=lambda : show(), bg='grey',fg='black').place(x=390,y=330)

showbox=Listbox(root,width=42,height=8,font=('bold',15),bg='dark grey',fg='black',bd=2)
showbox.place(x=20,y=390)

findbtn=Button(root, text='FIND STUDENTS', width=20, height=1, font=('arial', 13, 'bold'), bd=4,command=lambda : find(), bg='grey',fg='black').place(x=140,y=600)

root.config()
root.mainloop()
conn.commit()
conn.close()