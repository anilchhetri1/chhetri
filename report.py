import mysql.connector
import haha
from tkinter import*
from tkinter import ttk
from tkinter import messagebox


class Project():
    def __init__(self,interface):
        try:
            self.con = mysql.connector.connect(
                host="localhost",
                password="7410",
                user="root",
                database="homework",
            )
            self.cur = self.con.cursor()

        except mysql.connector.Error as e:
            print(e)

        self.interface = interface
        self.interface.geometry("600x300")
        self.interface.resizable(False,False)

        self.search_entry = Entry(self.interface, width=10)

        self.combo_sort = ttk.Combobox(self.interface, width=15, state=READABLE)
        self.combo_sort['values'] = ('student_id', 'fname', 'lname', 'degree', 'address', 'num')

        self.combo = ttk.Combobox(self.interface, width=15, state=READABLE)
        self.combo['values'] = ('student_id', 'fname', 'lname', 'degree', 'address', 'num')

        self.interface.title("display form")
        self.main_lbl1 = Label(self.interface, text="Softwarica College Portal", bd=20,
                               font="cambria 18 bold", bg="gray")
        self.main_lbl1.grid(row=1, column=3)

        self.student = ttk.Button(self.interface,text = "Register Here ",command=self.add_student, width=30)
        self.student.grid(row=3,column=3)

        self.exit1 =ttk.Button(self.interface, text="Exit",width=20,command=self.interface.quit)
        self.exit1.grid(row=3,column=4,padx=10)

    def add_student(self):
        self.interface.destroy()
        interface1 = Tk()
        self.interface1 = interface1
        self.interface1.geometry("1100x450")
        self.interface1.title("Student Registration form")
        self.main_lbl1 = Label(self.interface1, text="Softwarica college portal", font="cambria 18 bold")
        self.main_lbl1.pack(side = TOP,fill=X)
        ####Reuirement#############333
        self.square_frame = Frame(self.interface1, bd=10, bg="gray", relief="ridge")
        self.square_frame.place(x=10, y=70, width=500, height=350)
        #####################lable########################
        self.student_id = Label(self.square_frame, text="Student_id", bg="gray", font=" Arial 14 bold")
        self.student_id.grid(row=2, column=1)
        self.first_name = Label(self.square_frame, text="First Name", bg="gray", font=" Arial 14 bold")
        self.first_name.grid(row=3, column=1)
        self.last_name = Label(self.square_frame, text="Last Name", bg="gray", font=" Arial 14 bold")
        self.last_name.grid(row=4, column=1)

        self.std_degree = Label(self.square_frame, text="Degree", bg="gray", font=" Arial 14 bold")
        self.std_degree.grid(row=5, column=1)
        self.contact_num = Label(self.square_frame, text="Contact Number", bg="gray", font=" Arial 14 bold")
        self.contact_num.grid(row=7, column=1)

        #####Entry##################################333
        self.e_id = Entry(self.square_frame, width=40)
        self.e_id.grid(row=2, column=2)

        self.e_fname = Entry(self.square_frame, width=40)
        self.e_fname.grid(row=3, column=2)

        self.e_lname = Entry(self.square_frame, width=40)
        self.e_lname.grid(row=4, column=2)

        self.e_degree = Entry(self.square_frame, width=40)
        self.e_degree.grid(row=5, column=2)

        self.e_address = Entry(self.square_frame, width=40)
        self.e_address.grid(row=6, column=2)

        self.e_num = Entry(self.square_frame, width=40)
        self.e_num.grid(row=7, column=2)

        self.std_address = Label(self.square_frame, text="Address", bg="gray", font=" Arial 14 bold")
        self.std_address.grid(row=6, column=1)

        self.contact_num = Label(self.square_frame, text="Contact Number", bg="gray", font=" Arial 14 bold")
        self.contact_num.grid(row=7, column=1)

        ###############Frame33333333333333333333333
        self.btn_frame = Frame(self.square_frame, bd=4, bg="gray", relief="solid")
        self.btn_frame.place(x=10, y=200, width=460)

        self.search_frame = Frame(self.interface1, relief=RIDGE, bg="gray")
        self.search_frame.place(x=530, y=50, width=560, height=370)

        self.help_frame = Frame(self.search_frame,bd=4,relief=RIDGE,bg='gray')
        self.help_frame.place(x=10,y=8,width=550,height=100)

        self.table_frame = Frame(self.search_frame, bd=4, relief="solid")
        self.table_frame.place(x=20, y=110, width=500, height=250)

        ##############################
        self.search_label = Label(self.help_frame, text="Search By", bg="gray", fg="white", font="Arial 12 bold")
        self.search_label.grid(row=0, column=0, pady=10, padx=20)
        self.sort_label = Label(self.help_frame,text='Sort By',bg='gray',fg='white',font='Arial 12 bold')
        self.sort_label.grid(row=1,column=0,pady=10,padx=20)

        self.combo = ttk.Combobox(self.help_frame, width=15, state=READABLE)
        self.combo['values'] = ('student_id', 'fname', 'lname', 'degree', 'address', 'num')
        self.combo.grid(row=0, column=1, pady=10, padx=20)

        self.search_btnn = ttk.Button(self.help_frame, text="Search", command=self.search)
        self.search_btnn.grid(row=0, column=4)
        self.search_entry = Entry(self.help_frame, width=10)
        self.search_entry.grid(row=0, column=3, pady=10, padx=20)

        self.combo_sort=ttk.Combobox(self.help_frame,width=15,state=READABLE)
        self.combo_sort['values']=('student_id', 'fname', 'lname', 'degree', 'address', 'num')
        self.combo_sort.grid(row=1,column=1,pady=10,padx=20)

        self.sort_btnn = ttk.Button(self.help_frame, text="Sort", command=self.sort)
        self.sort_btnn.grid(row=1, column=3)


        # -------scrollbar--------
        self.scroll_x = Scrollbar(self.table_frame, orient=HORIZONTAL)
        self.scroll_x.pack(side=BOTTOM, fill=X)
        self.scroll_y = Scrollbar(self.table_frame, orient=VERTICAL)
        self.scroll_y.pack(side=RIGHT, fill=Y)

        #####################table#######################
        self.student_table = ttk.Treeview(self.table_frame,
                                          columns=("std_id", "fname", "lname", "degree", "address", "num"),
                                          xscrollcommand=self.scroll_x.set, yscrollcommand=self.scroll_y.set)

        self.student_table.heading("std_id", text="Std_id")
        self.student_table.heading("fname", text="Fname")
        self.student_table.heading("lname", text="Lname")
        self.student_table.heading("degree", text="Degree")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("num", text="Num")
        self.student_table.pack(fill=BOTH, expand=True)
        self.student_table["show"] = "headings"

        self.student_table.column("std_id", width=10)
        self.student_table.column("fname", width=10)
        self.student_table.column("lname", width=10)
        self.student_table.column("degree", width=10)
        self.student_table.column("address", width=10)
        self.student_table.column("num", width=10)
        self.show()

        self.student_table.bind('<ButtonRelease-1>', self.pointer)

        self.scroll_x.config(command=self.student_table.xview)
        self.scroll_y.config(command=self.student_table.yview)

        #####################Button##########################
        self.addButton = Button(self.btn_frame, text="Add",command=self.add_info, width=10, height=2)
        self.addButton.grid(row=10, column=0, padx=10, pady=10)

        self.updateButton = Button(self.btn_frame, text="Update", width=10,command=self.update, height=2)
        self.updateButton.grid(row=10, column=1, padx=8, pady=8)

        self.deleteButton = Button(self.btn_frame, text="Delete",command=self.delete, width=10, height=2)
        self.deleteButton.grid(row=10, column=2, padx=8, pady=8)

        self.clearButton = Button(self.btn_frame, text="Clear", width=10,command=self.clear, height=2)
        self.clearButton.grid(row=10, column=3, padx=8, pady=8)

        self.showall_btn = Button(self.btn_frame,width=6,height=2, text="Showall", command=self.show)
        self.showall_btn.grid(row=10, column=4,padx=8,pady=8)

    def add_info(self):
        self.std_id = self.e_id.get()
        self.fname = self.e_fname.get()
        self.lname = self.e_lname.get()
        self.degree = self.e_degree.get()
        self.address = self.e_address.get()
        self.num = self.e_num.get()
        if self.std_id == '' or self.fname == '' or self.lname == '' or self.degree == '' or self.address == '' or self.num == '':
            messagebox.showerror("Error", 'Input missing')
        else:
            self.query = "insert into student_infos values(%s,%s,%s,%s,%s,%s)"
            self.values = (self.std_id, self.fname, self.lname, self.degree, self.address, self.num)
            self.cur.execute(self.query, self.values)
            messagebox.showinfo("added", "one row added sucessfully")
            self.con.commit()
            self.show()
            self.clear()





    def show(self):
        self.query = 'select * from student_infos '
        self.cur.execute(self.query)
        self.rows = self.cur.fetchall()

        if len(self.rows) != 0:
            self.student_table.delete(*self.student_table.get_children())

        for row in self.rows:
            self.student_table.insert('', END, values=row)

    def clear(self):
        self.e_id.delete(0, END)
        self.e_fname.delete(0, END)
        self.e_lname.delete(0, END)
        self.e_degree.delete(0, END)
        self.e_address.delete(0, END)
        self.e_num.delete(0, END)


    def pointer(self, event):
        self.point = self.student_table.focus()
        self.content = self.student_table.item(self.point)
        self.row = self.content["values"]
        self.clear()
        self.e_id.insert(0, self.row[0])
        self.e_fname.insert(0, self.row[1])
        self.e_lname.insert(0, self.row[2])
        self.e_degree.insert(0, self.row[3])
        self.e_address.insert(0, self.row[4])
        self.e_num.insert(0, self.row[5])


    def update(self):
        self.point=self.student_table.focus()
        self.content =self.student_table.item(self.point)
        self.focused_id= self.content["values"][0]
        self.student_id = int(self.e_id.get())
        self.fname = self.e_fname.get()
        self.lname = self.e_lname.get()
        self.degree = self.e_degree.get()
        self.address = self.e_address.get()
        self.num = int(self.e_num.get())

        self.query = 'update student_infos  set student_id=%s, fname=%s,lname=%s,degree=%s,address=%s,num=%s where student_id=%s'
        self.values=(self.student_id,self.fname,self.lname,self.degree,self.address,self.num,self.focused_id)
        self.cur.execute(self.query,self.values)
        self.con.commit()
        self.clear()
        self.show()


    def delete(self):

        self.id=self.e_id.get()

        print(self.id)
        self.query = f'delete from student_infos where student_id={self.id}'
        self.cur.execute(self.query)
        self.con.commit()
        messagebox.showinfo("deleted", "one row deleted sucessfully")
        self.clear()
        self.show()

    def search(self):
        self.key = self.search_entry.get()
        self.index = self.combo.get()
        self.query = 'select * from student_infos'
        self.cur.execute(self.query)
        self.data = self.cur.fetchall()
        self.search = haha.LinearSearch(self.data, self.key, self.index)

        if len(self.search.output) != 0:
            self.student_table.delete(*self.student_table.get_children())

        for row in self.search.output:
            self.student_table.insert('', END, values=row)

    def bubble_sort(self, array):
        x = len(array)

        b1 = self.combo_sort.get()
        if b1 == 'student_id':
            area = 0
        elif b1 == 'fname':
            area = 1
        elif b1 == 'lname':
            area = 2
        elif b1 == 'address':
            area = 4
        elif b1 == 'degree':
            area = 3
        elif b1 == 'num':
            area = 5
        else:
            area = 6

        # Transversing through all array elements
        for i in range(x):

            # Last i elements are already in place
            for j in range(0, x - i - 1):

                # traverse the array from 0 to n-i-1
                # Swap if the element found is greater
                # than the next element
                if array[j][area] > array[j + 1][area]:
                    array[j], array[j + 1] = array[j + 1], array[j]
        return array



    def sort(self):
        self.querys = 'select *from student_infos'
        self.cur.execute(self.querys)
        self.table1 = self.cur.fetchall()
        self.con.commit()
        # print(new_table)
        self.rows1 = self.bubble_sort(self.table1)

        if len(self.rows1) != 0:
            self.student_table.delete(*self.student_table.get_children())

        for row in self.rows1:
            self.student_table.insert('', END, values=row)


if __name__ == '__main__':
    interface2 = Tk()
    gui = Project(interface2)
    interface2.mainloop()
