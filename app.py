from flask import Flask, render_template, request

from mbta_helper import find_stop_near


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        try:
            place_name = request.form['name']
            city = request.form['city']
            state = "MA" #Since MBTA only operates in Greater Boston region

            place = place_name + ', ' + city + ', ' + state
            print(place_name)
            station_name, is_wheelchair_accessible = find_stop_near(place)
            print(station_name, is_wheelchair_accessible)
            if is_wheelchair_accessible:
                return render_template('result.html', place_name=place,
                                       station_name=station_name, is_wheelchair_accessible="")
            else:
                return render_template('result.html', place_name=place,
                                       station_name=station_name, is_wheelchair_accessible="NOT")
        except:
            return render_template('index.html', error=True)
    return render_template('index.html', error=None)

