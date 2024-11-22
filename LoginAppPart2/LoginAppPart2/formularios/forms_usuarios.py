import json
import tkinter as tk
from tkinter import ttk

class FormUsuarios(tk.Tk):
    def __init__(self, parent):
        self.tipo_action = "Guardar"
        self.tipo_user = ""
        self.frame = ttk.Frame(parent)
        self.frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        tk.Label(self.frame, text="Registro de usuarios", font=('Times', 16)).place(x=70, y=30)

        labelcedula = tk.Label(self.frame, text="Cedula", font=('Times', 14))
        labelcedula.place(x=70, y=100)
        self.ccedula = tk.Entry(self.frame, width=40)
        self.ccedula.place(x=220, y=100)

        labelnombre = tk.Label(self.frame, text="Nombre", font=('Times', 14))
        labelnombre.place(x=70, y=130)
        self.cnombre = tk.Entry(self.frame, width=40)
        self.cnombre.place(x=220, y=130)

        labelusuario = tk.Label(self.frame, text="Username", font=('Times', 14))
        labelusuario.place(x=70, y=160)
        self.cusuario = tk.Entry(self.frame, width=40)
        self.cusuario.place(x=220, y=160)

        labelcontrasena = tk.Label(self.frame, text="Contraseña", font=('Times', 14))
        labelcontrasena.place(x=500, y=100)
        self.ccontrasena = tk.Entry(self.frame, width=40, show="*")
        self.ccontrasena.place(x=600, y=100)

        labelcorreo = tk.Label(self.frame, text="Correo", font=('Times', 14))
        labelcorreo.place(x=500, y=130)
        self.ccorreo = tk.Entry(self.frame, width=40)
        self.ccorreo.place(x=600, y=130)

        labeltipo = tk.Label(self.frame, text="Rol", font=('Times', 14))
        labeltipo.place(x=500, y=160)
        self.ctipo = ttk.Combobox(self.frame, width=40)
        self.ctipo.place(x=600, y=160)
        self.ctipo["values"] = ("Administrador", "Vendedor")

        btn_guardar = tk.Button(self.frame, text="Guardar", font=('Times', 14), command=self.guardar_usuario)
        btn_guardar.place(x=70, y=190)

        self.listar_usuarios()

    def listar_usuarios(self):
        tk.Label(self.frame, text="LISTADO DE USUARIOS", font=('Times', 16)).place(x=70, y=230)
        # Implementación de la lista de usuarios
        self.tablausuarios = ttk.Treeview(self.frame, columns=("Nombre", "Username", "Email", "Rol"))
        self.tablausuarios.heading("#0", text="Cedula")
        self.tablausuarios.heading("Nombre", text="Nombre")
        self.tablausuarios.heading("Username", text="Username")
        self.tablausuarios.heading("Email", text="Email")
        self.tablausuarios.heading("Rol", text="Rol")

        with open(r"C:\Users\Biblioteca\Desktop\LoginAppPart2\LoginAppPart2\db_users.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            for usuarios in data["users"]:
                self.tablausuarios.insert("", "end", text=f'{usuarios["id"]}',values=(f'{usuarios["name"]}',f'{usuarios["username"]}',f'{usuarios["email"]}', f'{usuarios["role"]}'))

        self.tablausuarios.place(x=70, y=280)

        btnEliminar = tk.Button(self.frame, text="Eliminar", font=('Times', 14), command=self.eliminar_usuarios).place(x=70, y=580)
        btnActualizar = tk.Button(self.frame, text="Actualizar", font=('Times', 14), command=self.actualizar_usuarios).place(x=170, y=580)

    def guardar_usuario(self):
        nuevo_usuario = {
            "id": self.ccedula.get(),
            "name": self.cnombre.get(),
            "username": self.cusuario.get(),
            "password": self.ccontrasena.get(),
            "email": self.ccorreo.get(),
            "role": self.ctipo.get()
        }
        try:
            with open(r"C:\Users\Biblioteca\Desktop\LoginAppPart2\LoginAppPart2\db_users.json", "r+") as file:
                data = json.load(file)
                data["users"].append(nuevo_usuario)
                file.seek(0)
                json.dump(data, file, indent=4)
            print("Usuario guardado exitosamente.")
        except Exception as e:
            print(f"Error al guardar el usuario: {e}")

    def actualizar_usuarios(self):
        id_usuario = self.ccedula.get()
        datos_actualizados = {
            "name": self.cnombre.get(),
            "username": self.cusuario.get(),
            "password": self.ccontrasena.get(),
            "email": self.ccorreo.get(),
            "role": self.ctipo.get()
        }
        try:
            with open(r"C:\Users\Biblioteca\Desktop\LoginAppPart2\LoginAppPart2\db_users.json", "r+") as file:
                data = json.load(file)
                for user in data["users"]:
                    if user["id"] == id_usuario:
                        user.update(datos_actualizados)
                        break
                file.seek(0)
                json.dump(data, file, indent=4)
            print("Usuario actualizado exitosamente.")
        except Exception as e:
            print(f"Error al actualizar el usuario: {e}")

    def eliminar_usuarios(self):
        id_usuario = self.ccedula.get()
        try:
            with open(r"C:\Users\Biblioteca\Desktop\LoginAppPart2\LoginAppPart2\db_users.json", "r+") as file:
                data = json.load(file)
                data["users"] = [user for user in data["users"] if user["id"] != id_usuario]
                file.seek(0)
                json.dump(data, file, indent=4)
            print("Usuario eliminado exitosamente.")
        except Exception as e:
            print(f"Error al eliminar el usuario: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FormUsuarios(root)
    root.mainloop()


