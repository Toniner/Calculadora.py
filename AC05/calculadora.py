import os
from flask import Flask, abort, render_template, request
import math

app = Flask(__name__)


@app.route("/")
def main():
    return render_template('calculadora.html')


@app.route('/calculadora', methods=['POST', 'GET'])
def calculadora():
    number = request.form['d1']
    result = request.form['result']

    number = int(number)

    if(result == 'raiz'):
        operation = math.sqrt(number)
    elif(result == 'exponenciacao'):
        operation = math.exp(number)
    elif(result == 'logaritmo'):
        operation = math.log(number)
    else:
        abort(404)

    return str(operation)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5005))
    app.run(host='127.0.0.1', port=port)
