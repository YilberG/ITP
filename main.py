from flask import Flask, render_template, request, redirect, url_for, flash, session #pip install Flask
from flask_mysqldb import MySQL # pip install Flask-MySQLdb
from os import path
#from notifypy import Notify
import mysql.connector,string

app = Flask(__name__)
# Conexion De Base De Datos
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "itp"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"
mysql = MySQL(app)


#configuracion de session
app.secret_key = "XDXD"

@app.route("/")
def Index():
    
    return render_template("/index.html")

#Logeo del usuario
@app.route("/login.html", methods=["GET", "POST"])
def Login():
    if request.method == 'POST':
        cur = mysql.connection.cursor()
        correo = request.form['email']
        try:
            password = request.form['Contraseña']
        except:
            password = ""

        if correo == "":
            flash("Ingrese un Email")
        else:
            cur.execute("SELECT * FROM usuarios WHERE email=%s", (correo,))
            user = cur.fetchone()
            if not user:
                flash("El email no se encuentra registrado")
            else:
                if password == "":
                    flash("Ingrese la contraseña")
                else:
                    #print(user)
                    if password != user["contraseña"]:
                        flash("Contraseña incorrecta")
                    else:
                        cur.close()
                        session['nombres'] = user['nombres']
                        #session['Contraseña'] = user['contraseña']
                        session['email'] = user['email']
                        session['roles'] = user['id_rol']
                        if session['roles'] ==1:
                            return redirect(url_for("alumnos"))
                        if session['roles'] ==2:
                            return redirect(url_for("profesor"))
                        elif session['roles']==3:
                            return redirect(url_for("admin"))
        return render_template("/login.html", correo = correo)
    else:
        return render_template("/login.html")

#Registros De Usuarios-------------------------------------
@app.get("/registro.html")
def registro():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM rol")
    roles = cur.fetchall()

    cur.close()
    return render_template("/registro.html", roles = roles)

@app.route("/registro.html", methods=["POST"])
def registroPost():


    if request.method =="POST":
        nombre = request.form["Nombre"]
        correo = request.form["email"]
        contraseña = request.form["Contraseña"]
        rol = request.form["roles"]

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO usuarios(nombres, email, contraseña, id_rol) VALUES(%s,%s,%s,%s)",(
            nombre,
            correo,
            contraseña,
            rol,
        ))
        mysql.connection.commit()

        return redirect(url_for("Index"))


#Paginas de los roles----------------------------------------
#Pagina De Estudiantes---------------------------------
@app.route("/estudiante.html")
def alumnos():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM materias")
    materias = cur.fetchall()

    cur.close()
    return render_template("/estudiante.html", materias = materias)

@app.post("/registroMaterias")
def registroMateriasPost():
    return redirect(url_for("alumnos"))
#Pagina Profesor-------------------------------------------
@app.route("/profesor.html", methods=["GET"])
def profesor():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM usuarios WHERE id_rol = 1")
    data = cur.fetchall()

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM usuarios")
    data2 = cur.fetchone()
    return render_template("/profesor.html", datos=data, datos2=data2)

@app.post('/registroProfesor')
def registroProfesorPost():
    if request.method == "POST":
        nombre = request.form["nombre"]
        correo = request.form["email"]
        contraseña = request.form["contraseña"]
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO usuarios(nombres, email, contraseña, id_rol) VALUES(%s,%s,%s,1)",(
            nombre,
            correo,
            contraseña,
        ))
        mysql.connection.commit()
        flash('CONTACTO AGREGADO SATISFACTORIAMENTE')

    return redirect(url_for("profesor"))

@app.route("/delete/<string:id>")
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM usuarios WHERE id = {0}".format(id))
    mysql.connection.commit()
    flash("CONTACTO REMOVIDO SATISFACTORIAMENTE")
    return redirect(url_for("profesor"))

@app.route("/edit/<id>")
def editProfesor(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM usuarios WHERE id = {0}".format(id))
    data = cur.fetchone()
    return render_template("editProf.html", datos = data)

#Actualizar Contacto
@app.route("/update/<id>", methods=["POST"])
def update_contactos(id):
    if request.method == "POST":
        nombre = request.form["nombre"]
        email = request.form["email"]
    cur = mysql.connection.cursor()
    cur.execute("UPDATE usuarios SET nombres = %s, email = %s WHERE id = %s ",(nombre, email, id))
    mysql.connection.commit()
    flash("ESTUDIANTE ACTUALIZADO SATISFACTORIAMENTE")
    return redirect(url_for("profesor"))

#Pagina Administrador--------------------------------------

@app.route("/admin.html", methods=["GET"])
def admin():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM usuarios WHERE id_rol<=2")
    data = cur.fetchall()

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM rol")
    roles = cur.fetchall()

    cur.close()
    return render_template("/admin.html", datos2=data, roles2 = roles)

@app.post('/registroAdmin')
def registroAdminPost():
    if request.method == "POST":
        nombre = request.form["nombre"]
        correo = request.form["email"]
        contraseña = request.form["contraseña"]
        rol = request.form["roles"]
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO usuarios(nombres, email, contraseña, id_rol) VALUES(%s,%s,%s,%s)",(
            nombre,
            correo,
            contraseña,
            rol
        ))
        mysql.connection.commit()
        flash('CONTACTO AGREGADO SATISFACTORIAMENTE')
    return redirect(url_for("admin"))

@app.route("/deleteAdmin/<string:id>")
def delete_contact_admin(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM usuarios WHERE id = {0}".format(id))
    mysql.connection.commit()
    flash("CONTACTO REMOVIDO SATISFACTORIAMENTE")
    return redirect(url_for("admin"))

@app.route("/editAdmin/<id>")
def editAdmin(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM usuarios WHERE id = {0}".format(id))
    data = cur.fetchone()

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM rol")
    roles = cur.fetchall()

    cur.close()
    return render_template("adminEdit.html", datos2 = data, roles2 = roles)

#Actualizar Contacto
@app.route("/updateAdmin/<id>", methods=["POST"])
def update_contactos_admin(id):
    if request.method == "POST":
        nombre = request.form["nombre"]
        email = request.form["email"]
        contraseña = request.form["contraseña"]
        rol = request.form["roles"]
    cur = mysql.connection.cursor()
    cur.execute("UPDATE usuarios SET nombres = %s, email = %s, contraseña = %s, id_rol = %s WHERE id = %s ",(
        nombre,
        email,
        contraseña,
        rol,
        id))
    mysql.connection.commit()
    flash("CONTACTO ACTUALIZADO SATISFACTORIAMENTE")
    return redirect(url_for("admin"))

#Cerrar Session
@app.get("/cerrarsession")
def cerrarSession():
    session.clear()

    return redirect(url_for('Login'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)