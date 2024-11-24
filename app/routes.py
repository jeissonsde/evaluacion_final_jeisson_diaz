from app import app
from flask import render_template, request

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1')
def ejercicio1():
    return render_template('ejercicio1.html')

@app.route('/ejercicio2')
def ejercicio2():
    return render_template('ejercicio2.html')

@app.route('/resultado1', methods=['POST'])
def resultado1():
    nombre = request.form['nombre']
    edad = int(request.form['edad'])
    cantidad = int(request.form['cantidad'])

    precio_por_tarro = 9000
    total_sin_descuento = precio_por_tarro * cantidad

    # Calcular descuento según la edad
    if 18 <= edad <= 30:
        descuento = 0.15
    elif edad > 30:
        descuento = 0.25
    else:
        descuento = 0

    total_con_descuento = total_sin_descuento * (1 - descuento)

    return render_template('resultado1.html', nombre=nombre, total_sin_descuento=total_sin_descuento, total_con_descuento=total_con_descuento)

@app.route('/resultado2', methods=['POST'])
def resultado2():
    usuario = request.form['usuario']
    password = request.form['password']

    # Usuarios registrados
    usuarios = {
        "juan": "admin",
        "pepe": "user"
    }

    # Validar usuario y contraseña
    if usuario in usuarios and usuarios[usuario] == password:
        if usuario == "juan":
            mensaje = f"Bienvenido administrador {usuario}"
        else:
            mensaje = f"Bienvenido usuario {usuario}"
    else:
        mensaje = "Usuario o contraseña incorrectos"

    return render_template('resultado2.html', mensaje=mensaje)
