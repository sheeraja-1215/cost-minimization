from flask import Flask, request, render_template
from backend import minCashFlow

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('num_persons.html')

@app.route('/matrix', methods=['POST'])
def matrix():
    numPersons = int(request.form['numPersons'])
    return render_template('matrix.html', numPersons=numPersons)

@app.route('/calculate', methods=['POST'])
def calculate():
    numPersons = int(request.form['numPersons'])
    graph = [[0 for _ in range(numPersons)] for _ in range(numPersons)]
    for key, value in request.form.items():
        if key.startswith('graph'):
            indices = key[6:-1].split('][')
            i, j = int(indices[0]), int(indices[1])
            graph[i][j] = int(value)
    result = minCashFlow(graph, numPersons)
    result_str = '<br>'.join(result)
    return render_template('result.html', result=result_str)

if __name__ == '__main__':
    app.run(debug=True)
