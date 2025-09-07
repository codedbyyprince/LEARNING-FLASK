from flask import Flask, render_template, request
#importing modules

app = Flask (__name__) #initializing flask app


SPORTS = [              # sports list
    "Basketball",
    "Soccer",
    "Cricket"
]

REGISTRAINTS = {}


@app.route('/')          #route for homepage
def index():
    return render_template('index.html', sports = SPORTS)

@app.route('/register', methods=['POST'])   #route for registration form 
def register():
    name = request.form.get("name")
    if not name:
        return render_template('error.html', message="Name missing.") #error handling for name
    
    sport = request.form.get("sport")
    if not sport:
        return render_template('error.html', message="Sport missing") #error handling for sport
    if sport not in SPORTS:
        return render_template('error.html', message="Invalid sport selected.") #error handling for invalid sport
    
    REGISTRAINTS[name] = sport
    return render_template('success.html', name=name, sport=sport) #success page

@app.route('/registrants')
def registrants():
    return render_template('registrants.html', registrants=REGISTRAINTS) #route to display all registrants

if __name__ == '__main__': #running the app
    app.run(debug=True)