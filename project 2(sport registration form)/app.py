from flask import Flask, render_template, request

app = Flask (__name__)


SPORTS = [
    "Basketball",
    "Soccer",
    "Cricket"
]

REGISTRAINTS = {}


@app.route('/')
def index():
    return render_template('index.html', sports = SPORTS)

@app.route('/register', methods=['POST'])
def register():
    name = request.form.get("name")
    if not name:
        return render_template('error.html', message="Name missing.")
    
    sport = request.form.get("sport")
    if not sport:
        return render_template('error.html', message="Sport missing")
    if sport not in SPORTS:
        return render_template('error.html', message="Invalid sport selected.")
    
    REGISTRAINTS[name] = sport
    return render_template('success.html', name=name, sport=sport)

@app.route('/registrants')
def registrants():
    return render_template('registrants.html', registrants=REGISTRAINTS)

if __name__ == '__main__':
    app.run(debug=True)