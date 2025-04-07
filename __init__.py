from flask import Flask

app = Flask(__name__)

@app.route('/<int:n>')
def fibo(n):
    a, b = 0, 1
    res = str(a)  # Initialisation avec le premier terme
    
    for _ in range(1, min(n, 50)):  # Limité à 50 termes pour la sécurité
        res += f", {b}"
        a, b = b, a + b
    
    return res

if __name__ == '__main__':
    app.run(host='0.0.0.0')
