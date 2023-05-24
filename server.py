import json
from datetime import datetime
from flask import Flask, render_template, request, redirect, flash, url_for


def loadClubs():
    with open('clubs.json') as c:
        listOfClubs = json.load(c)['clubs']
        return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
        listOfCompetitions = json.load(comps)['competitions']
        return listOfCompetitions


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/showSummary', methods=['POST'])
def showSummary():
    if request.form['email'] == '':
        flash("email must not be empty")
        return render_template('index.html')

    club = None
    for c in clubs:
        if c['email'] == request.form['email']:
            club = c
            break

    if club:
        return render_template('welcome.html', club=club, competitions=competitions)
    else:
        flash("email not found")
        return render_template('index.html')


@app.route('/book/<competition>/<club>')
def book(competition, club):

    # found_club = [c for c in clubs if c['name'] == club][0]
    found_club = None
    for c in clubs:
        if c['name'] == club:
            found_club = c
            break

    # found_competition = [c for c in competitions if c['name'] == competition][0]
    found_competition = None
    for c in competitions:
        if c['name'] == competition:
            datetime_str = c['date']
            datetime_object = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
            if datetime_object < datetime.now():
                flash("This competition is done.")
                return render_template('welcome.html', club=found_club, competitions=competitions)
            found_competition = c
            break

    if found_club and found_competition:
        return render_template('booking.html', club=found_club, competition=found_competition)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=found_club, competitions=competitions)


@app.route('/purchasePlaces', methods=['POST'])
def purchasePlaces():
    # club = [c for c in clubs if c['name'] == request.form['club']][0]
    club = None
    for c in clubs:
        if c['name'] == request.form['club']:
            club = c
            break

    # competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    competition = None
    for c in competitions:
        if c['name'] == request.form['competition']:
            competition = c
            break

    if not club or not competition:
        flash("Something went wrong-please try again.")
        return render_template('welcome.html', club=club, competitions=competitions)

    places_required = int(request.form['places'])
    club_points = int(club['points'])

    # We do not reserve more than we have points
    if places_required > club_points:
        flash('Not enough points available.')
        return render_template('booking.html', club=club, competition=competition)

    competition['numberOfPlaces'] = int(competition['numberOfPlaces']) - places_required

    flash('Great-booking complete!')
    return render_template('welcome.html', club=club, competitions=competitions)


# TODO: Add route for points display
@app.route('/viewsPoints')
def view_points():
    return render_template('points.html', clubs=clubs)

@app.route('/logout')
def logout():
    return redirect(url_for('index'))
