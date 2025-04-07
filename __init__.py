from flask import Flask

app = Flask(__name__)

@app.route('/somme/<path:valeurs>')
def somme(valeurs):
    liste_nombres = valeurs.split('/')
    liste_nombres = [int(n) for n in liste_nombres]
    res = sum(liste_nombres)
    return str(res)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
