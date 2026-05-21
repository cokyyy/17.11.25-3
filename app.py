from flask import Flask, render_template

app = Flask(__name__)

@app.route('/dla-ciebie')
def niespodzianka():
    return render_template('niespodzianka.html')

if __name__ == '__main__':
    app.run(debug=True)