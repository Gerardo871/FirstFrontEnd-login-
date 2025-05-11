from flask import Flask, render_template,request, redirect
#import requests
app = Flask(__name__)
#gunicorn -w 4 -b 0.0.0.0:8080 app:app     -->levantar proyecto
# Ruta para la página principal
@app.route('/')
def home():
    return render_template('index.html')

# Ruta para otra página (opcional)
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/redirect')
def redirect_to_target():
    target = request.args.get('target')
    if target == "123":
        return render_template("forgot_pass.html")
    else:
        return "Destino no válido", 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
