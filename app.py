from flask import Flask, render_template, request, flash
import re
import smtplib
app = Flask(__name__)

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        # obtengo valores de formulario
        username = request.form["Nombre"]
        contraseña = request.form["Pass"]
        if len(username) > 4 and len(contraseña)>7:
            return render_template('principalAdmin.html')
    return render_template('login.html')


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    return render_template('principalAdmin.html')


@app.route('/employee')
def employee():
    return render_template('principalEmpleado.html')


@app.route('/admin/product')
def product():
    return render_template('producto.html')


@app.route('/admin/add-employee', methods=['GET', 'POST'])
def add_employee():
     if request.method == "POST":
        #obtengo valores de formulario
        username = request.form["Nombre"]
        contraseña = request.form["Pass"]
        email = request.form["emails"]
        #Verificacion de datos
        if len(username) > 4 and len(contraseña)>7 and \
                re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',
                         email.lower()):
            from_addr = 'joiesss136@gmail.com'
            to = email.lower();
            message = 'Gracias por su registro, pueden ingresar a nuestra plataforma con las credenciales registradas'
            # Reemplaza estos valores con tus credenciales de Google Mail
            username = 'joiesss136@gmail.com'
            password = '1Giovanni23'
            server = smtplib.SMTP('smtp.gmail.com:587') #Creo un objeto smtp  especifico medio de envio y puerto
            server.starttls() #Inicio
            server.login(username, password) #Ingreso
            server.sendmail(from_addr, to, message) #Envio
            server.quit() #Cierro
            return render_template('agregarUsuario.html')
     return render_template('agregarUsuario.html')

@app.route('/admin/product/add')
def add_product():
    return render_template('agregarProducto.html')


@app.route('/admin/product/mod')
def mod_product():
    return render_template('modificarProducto.html')


@app.route('/employee/product-id')
def inventory():
    return render_template('editarCantidadProducto.html')


if __name__ == '__main__':
    app.run()
