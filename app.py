from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/carga')
def carga():
    return render_template('carga.html')

# @app.route('/mostrar_datos')
# def mostrar_datos():
#     # Simulando datos para mostrar
#     datos = [{"id": 1, "nombre": "Juan", "edad": 30},
#              {"id": 2, "nombre": "Maria", "edad": 25}]
#     return render_template('mostrar_datos.html', datos=datos)

if __name__ == '__main__':
    app.run(debug=True)