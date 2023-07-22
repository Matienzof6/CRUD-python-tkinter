from tkinter import *
import sqlite3
from tkinter import messagebox



root=Tk()


frm=Frame(root, width=600, height=600, relief=RAISED, border=5)
frm.pack()




idStrVar=StringVar()
nameStrVar=StringVar()
passStrVar=StringVar()
lastNameStrVar=StringVar()
addressStrVar=StringVar()

# --------FUNCIONES TK--------

def askExit():
    value=messagebox.askokcancel("Salir","¿Seguro que desea salir de la aplicacion?")
    if value:
        root.destroy()

def deleteFields():
    idStrVar.set("")
    nameStrVar.set("")
    passStrVar.set("")
    lastNameStrVar.set("")
    addressStrVar.set("")
    commentText.delete(0.0, END)



# ----CONECTAR-----

def connectDataBase():
    try:
        global myConnection
        myConnection=sqlite3.connect("Usuarios")
        global myCursor
        myCursor=myConnection.cursor()

        myCursor.execute('''CREATE TABLE DATOSUSUARIOS(
            ID INTEGER PRIMARY KEY AUTOINCREMENT, 
            NOMBRE_USUARIO VARCHAR(50), 
            PASSWORD VARCHAR(50), 
            APELLIDO VARCHAR(50), 
            DIRECCION VARCHAR(50), 
            COMENTARIOS TEXT )''')
        myConnection.close()
        messagebox.showinfo("BBDD","La base de datos ha sido creada con Exito")
    except sqlite3.OperationalError:
        messagebox.showerror("BBDD", "La base de datos ya ha sido creada")
        








# -------CUADROS DE TEXTOS------



entryId=Entry(frm,textvariable=idStrVar)
entryId.grid(row=0, column=1, padx=20, pady=10)
lblId=Label(frm, text="id :").grid(row=0,column=0)



entryName=Entry(frm, textvariable=nameStrVar)
entryName.grid(row=1, column=1, padx=20, pady=10)
lblName=Label(frm, text="Nombre :").grid(row=1,column=0)




entryPass=Entry(frm, textvariable=passStrVar)
entryPass.grid(row=2, column=1, padx=20, pady=10)
entryPass.config(show="•")
lblPass=Label(frm, text="Contraseña :").grid(row=2,column=0)




entryLastName=Entry(frm,textvariable=lastNameStrVar)
entryLastName.grid(row=3, column=1, padx=20, pady=10)
lblName=Label(frm, text="Apellido :").grid(row=3,column=0)





entryAdress=Entry(frm,textvariable=addressStrVar)
entryAdress.grid(row=4, column=1, padx=20, pady=10)
lblAdress=Label(frm, text="Dirección :").grid(row=4,column=0)





commentText=Text(frm, width=20, height=5)
commentText.grid(row=5, column=1, padx=20, pady=10, columnspan=3)
lblComment=Label(frm, text="Comentarios :").grid(row=5,column=0)
scrollCommentText=Scrollbar(frm, command=commentText.yview)
scrollCommentText.grid(row=5,column=2, sticky="nsew")
commentText.config(yscrollcommand=scrollCommentText.set)




# ------FUNCIONES SQL--------

# CREATE


def createBBDD():
    valuesFields=[
    (entryName.get()),
    (entryPass.get()),
    (entryLastName.get()),
    (entryAdress.get()),
    (commentText.get("0.0",'end-1c'))
    ]   
    if idStrVar.get()=="":
        myConnection=sqlite3.connect("Usuarios")
        myCursor=myConnection.cursor()
        myCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,?,?,?,?,?)", valuesFields)
        myCursor.execute("SELECT MAX(ID) FROM DATOSUSUARIOS")
        lastID=myCursor.fetchall()
        myConnection.commit()
        messagebox.showinfo("BBDD","Registro creado con éxito en el ID: " + str(lastID[0][0]))
        deleteFields()
    else:
        messagebox.showerror("BBDD","Para crear un nuevo registro, el campo id debe estar vacío")


# READ

def readBBDD():
    
    myConnection=sqlite3.connect("Usuarios")
    myCursor=myConnection.cursor()
    idNumber=entryId.get()
    myCursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID=?", (idNumber,))
    valuesFields=myCursor.fetchall()
    commentText.delete(0.0, END)
    for valueField in valuesFields:
        nameStrVar.set(valueField[1])
        passStrVar.set(valueField[2])
        lastNameStrVar.set(valueField[3])
        addressStrVar.set(valueField[4])
        commentText.insert(0.0,valueField[5])
    myConnection.commit()



# UPDATE


def updateBBDD():
    valuesFields=[
    (entryName.get()),
    (entryPass.get()),
    (entryLastName.get()),
    (entryAdress.get()),
    (commentText.get("0.0",'end-1c')),
    (entryId.get())
    ]

    myConnection=sqlite3.connect("Usuarios")
    myCursor=myConnection.cursor()
    myCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO=?,PASSWORD=?,APELLIDO=?,DIRECCION=?,COMENTARIOS=? WHERE ID=?", valuesFields)
    myConnection.commit()
    messagebox.showinfo("BBDD","El registro se ha actualizado con éxito")

# DELETE

def deleteBBDD():
    
    dltValuesFields=entryId.get()

    myConnection=sqlite3.connect("Usuarios")
    myCursor=myConnection.cursor()
    myCursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID=?", (dltValuesFields,))
    myConnection.commit()

    deleteFields()
    messagebox.showinfo("BBDD","Registro eliminado con éxito.")



# --------Buttons----------

frm2=Frame(frm)
frm2.grid(row=6, column=1)



btnCreate=Button(frm2, text="Create", command=createBBDD)
btnCreate.grid(row=0, column=0, padx=5, pady=10)


btnRead=Button(frm2, text="Read", command=readBBDD)
btnRead.grid(row=0, column=1, padx=5, pady=10)

btnUpdate=Button(frm2, text="Update", command=updateBBDD)
btnUpdate.grid(row=0, column=2, padx=5, pady=10)

btnDelete=Button(frm2, text="Delete", command=deleteBBDD)
btnDelete.grid(row=0,column=3, padx=5, pady=10)


# ----------Menu-----------

menuBar=Menu(root)
root.config(menu=menuBar, width=300, height=300)

bbddMenu=Menu(menuBar, tearoff=0)
bbddMenu.add_command(label="Conectar", command=connectDataBase)
bbddMenu.add_command(label="Salir", command=askExit)

deleteFieldsMenu=Menu(menuBar, tearoff=0)
deleteFieldsMenu.add_command(label="Borrar campos", command=deleteFields)


crudMenu=Menu(menuBar, tearoff=0)
crudMenu.add_command(label="Crear", command=createBBDD)
crudMenu.add_command(label="Leer", command=readBBDD)
crudMenu.add_command(label="Actualizar",command=updateBBDD)
crudMenu.add_command(label="Eliminar",command=deleteBBDD)

helpMenu=Menu(menuBar, tearoff=0)





menuBar.add_cascade(label="BBDD", menu=bbddMenu)
menuBar.add_cascade(label="Borrar", menu=deleteFieldsMenu)
menuBar.add_cascade(label="CRUD", menu=crudMenu)
menuBar.add_cascade(label="Ayuda", menu=helpMenu)





root.mainloop()


