import re
from flask import Flask, render_template, request, redirect, url_for
from clases import Libro, Conexion
from mysql.connector import Error

lista_libros = []

app = Flask(__name__, template_folder="templates")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/enviar_libro", methods=["POST"])
def enviar_libro():
    #limpiamos la lista
    lista_libros.clear()
    #creamos las conexiones para la base de datos
    configuraciones = Conexion("127.0.0.1","obed","1234","lab_10")
    
    # captura de datos del formulario
    titulo = request.form["Titulo"]
    autor = request.form["Autor"]
    editorial = request.form["Editorial"]
    paginas = request.form["Paginas"]
    anio = request.form["Anio"]
    isbn = request.form["ISBN"]

    #Validamos los campos, creamos el objeto y lo agregamos a la lista y redireccionamos a la pagina de ver libros
    if titulo and autor and editorial and validar_numero_de_paginas(paginas) and validar_anio(anio) and isbn:
        
        #cramos la conexion a la base de datos
        connect = configuraciones.conexion()
        cursor = connect.cursor()
        #creamos la consulta
        query = "insert into `lab_10`.`Libro` (Titulo, Autor, Editorial, Paginas, Anio, ISBN) values (%s,%s,%s,%s,%s,%s);"
        #creamos la tupla de argumentos
        argumentos = (titulo, autor, editorial, paginas, anio, isbn)
        
        try:
            cursor.execute(query, argumentos)
            connect.commit()
            cursor.close()
            connect.close()
        except Error as error:
            print({"mensaje": f"Error al insertar: {error}"})
        
        busqueda = configuraciones.conexion()
        cursor2 = busqueda.cursor()
        query2 = "select * from `lab_10`.`Libro`"
        
        cursor2.execute(query2)
        Lista_base = cursor2.fetchall()
        
        for i in Lista_base:
            lista_libros.append(Libro(i[1], i[2], i[3], i[4], i[5], i[6]))
        
        cursor2.close()
        busqueda.close()
        return redirect(url_for("ver_libros"))
    #Si los campos estan vacios, se muestra un mensaje de error al fial de la pagina
    else:
        return render_template("index.html", mensaje="Rellene los campos con datos válidos")

@app.route("/ver_libros")
def ver_libros():
    # pasa la lista de libros a la plantilla
    return render_template("ver_libros.html", lista=lista_libros)

#validaciones de campos y sus formas
#valida el año en formato de 4 digitos
def validar_anio(anio):
    # Expresión regular que coincide con cualquier número de cuatro dígitos
    patron = re.compile(r'^[0-9]{4}$')

    # Intenta encontrar una coincidencia con el patrón; si no se encuentra, devuelve False
    if patron.match(anio):
        return True
    else:
        return False

#valida el formato numero del numero de paginas
def validar_numero_de_paginas(num):
    # Expresión regular que coincide con cualquier número entero positivo
    patron = re.compile(r'^[1-9]\d*$')

    # Intenta encontrar una coincidencia con el patrón; si no se encuentra, devuelve False
    if patron.match(num):
        return True
    else:
        return False

if __name__ == "__main__":
    app.debug = True
    app.run()
