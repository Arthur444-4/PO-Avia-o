from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/estilos')
def pag1():
    return render_template('estilos.html')


if __name__ == '__main__':
    app.run(debug=True)
