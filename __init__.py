from flask import Flask
from flask import render_template
from flask import json                                                                                                                                     
app = Flask(__name__)                                                                                                                  


@app.route('/<int:valeur>')
def exercice(valeur):
    val = [0, 1]
    result = []
    result.append(val[0])
    result.append(val[1])
    
    for _ in range(2, valeur):
        result.append(val[0] + val[1])
        val[1] += val[0]
        val[0] = val[1] - val[0]
    return jsonify(result)

if __name__ == "__main__":
  app.run(debug=True) 
