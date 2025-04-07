from flask import Flask
from flask import render_template
from flask import json                                                                                                                                     
app = Flask(__name__)                                                                                                                  


@app.route('/<int:valeur>')
def exercice(n):
    count = ['0', '1'] if n > 1 else ['0']

    for _ in range(2, n):
        count.append(str(int(count[-1]) + int(count[-2])))

    return ', '.join(count[:n])

if __name__ == "__main__":
  app.run(debug=True) 
