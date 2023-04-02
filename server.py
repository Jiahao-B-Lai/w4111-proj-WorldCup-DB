
"""
Columbia's COMS W4111.001 Introduction to Databases
Example Webserver
To run locally:
    python server.py
Go to http://localhost:8111 in your browser.
A debugger such as "pdb" may be helpful for debugging.
Read about it online.
"""
import os
  # accessible as a variable in index.html:
from sqlalchemy import *
from sqlalchemy.pool import NullPool
from flask import Flask, request, render_template, g, redirect, Response, session

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=tmpl_dir)
app.secret_key = os.urandom(24)

#
# The following is a dummy URI that does not connect to a valid database. You will need to modify it to connect to your Part 2 database in order to use the data.
#
# XXX: The URI should be in the format of:
#
#     postgresql://USER:PASSWORD@34.73.36.248/project1
#
# For example, if you had username zy2431 and password 123123, then the following line would be:
#
#     DATABASEURI = "postgresql://zy2431:123123@34.73.36.248/project1"
#
# Modify these with your own credentials you received from TA!
DATABASE_USERNAME = "jl6274"
DATABASE_PASSWRD = "6439"
DATABASE_HOST = "34.148.107.47" # change to 34.28.53.86 if you used database 2 for part 2
DATABASEURI = f"postgresql://{DATABASE_USERNAME}:{DATABASE_PASSWRD}@{DATABASE_HOST}/project1"


#
# This line creates a database engine that knows how to connect to the URI above.
#
engine = create_engine(DATABASEURI)

#
# Example of running queries in your database
# Note that this will probably not work if you already have a table named 'test' in your database, containing meaningful data. This is only an example showing you how to run queries in your database using SQLAlchemy.
#
# with engine.connect() as conn:
#         create_table_command = """
#         CREATE TABLE IF NOT EXISTS test (
#                 id serial,
#                 name text
#         )
#         """
#         res = conn.execute(text(create_table_command))
#         insert_table_command = """INSERT INTO test(name) VALUES ('grace hopper'), ('alan turing'), ('ada lovelace')"""
#         res = conn.execute(text(insert_table_command))
#         # you need to commit for create, insert, update queries to reflect
#         conn.commit()


@app.before_request
def before_request():
        """
        This function is run at the beginning of every web request
        (every time you enter an address in the web browser).
        We use it to setup a database connection that can be used throughout the request.

        The variable g is globally accessible.
        """
        try:
                g.conn = engine.connect()
        except:
                print("uh oh, problem connecting to database")
                import traceback; traceback.print_exc()
                g.conn = None

@app.teardown_request
def teardown_request(exception):
        """
        At the end of the web request, this makes sure to close the database connection.
        If you don't, the database could run out of memory!
        """
        try:
                g.conn.close()
        except Exception as e:
                pass


#
# @app.route is a decorator around index() that means:
#   run index() whenever the user tries to access the "/" path using a GET request
#
# If you wanted the user to go to, for example, localhost:8111/foobar/ with POST or GET then you could use:
#
#       @app.route("/foobar/", methods=["POST", "GET"])
#
# PROTIP: (the trailing / in the path is important)
#
# see for routing: https://flask.palletsprojects.com/en/1.1.x/quickstart/#routing
# see for decorators: http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/
#
@app.route('/')
def index():
        """
        request is a special object that Flask provides to access web request information:

        request.method:   "GET" or "POST"
        request.form:     if the browser submitted a form, this contains the data in the form
        request.args:     dictionary of URL arguments, e.g., {a:1, b:2} for http://localhost?a=1&b=2

        See its API: https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data
        """

        # DEBUG: this is debugging code to see what request looks like
        print(request.args)


        #
        # example of a database query
        #
        select_query = "SELECT g.group_id, t.team_name, g.points, g.ranking from groups as g join teams as t on g.team_id = t.team_id order by g.group_id asc"
        cursor = g.conn.execute(text(select_query))
        all_groups = []
        groupA = []
        groupB = []
        groupC = []
        groupD = []
        groupE = []
        groupF = []
        groupG = []
        groupH = []
        for result in cursor:
            if result[0] == 'A':
                groupA.append((result[0],result[1],result[2],result[3]))
            elif result[0] == 'B':
                groupB.append((result[0],result[1],result[2],result[3]))
            elif result[0] == 'C':
                groupC.append((result[0],result[1],result[2],result[3]))
            elif result[0] == 'D':
                groupD.append((result[0],result[1],result[2],result[3]))
            elif result[0] == 'E':
                groupE.append((result[0],result[1],result[2],result[3]))
            elif result[0] == 'F':
                groupF.append((result[0],result[1],result[2],result[3]))
            elif result[0] == 'G':
                groupG.append((result[0],result[1],result[2],result[3]))
            else:
                groupH.append((result[0],result[1],result[2],result[3]))
        all_groups.append(groupA)
        all_groups.append(groupB)
        all_groups.append(groupC)
        all_groups.append(groupD)
        all_groups.append(groupE)
        all_groups.append(groupF)
        all_groups.append(groupG)
        all_groups.append(groupH)
        
        cursor.close()

        #
        # Flask uses Jinja templates, which is an extension to HTML where you can
        # pass data to a template and dynamically generate HTML based on the data
        # (you can think of it as simple PHP)
        # documentation: https://realpython.com/primer-on-jinja-templating/
        #
        # You can see an example template in templates/index.html
        #
        # context are the variables that are passed to the template.
        # for example, "data" key in the context variable defined below will be
        # accessible as a variable in index.html:
        #
        #     # will print: [u'grace hopper', u'alan turing', u'ada lovelace']
        #     <div>{{data}}</div>
        #
        #     # creates a <div> tag for each element in data
        #     # will print:
        #     #
        #     #   <div>grace hopper</div>
        #     #   <div>alan turing</div>
        #     #   <div>ada lovelace</div>
        #     #
        #     {% for n in data %}
        #     <div>{{n}}</div>
        #     {% endfor %}
        #
        context = dict(data = all_groups)


        #
        # render_template looks in the templates/ folder for files.
        # for example, the below file reads template/index.html
        #
        return render_template("index.html", **context)

#
# This is for teams data
#
@app.route('/teams')
def teams():
        return render_template("teams.html")

#
# This is for players data
#
@app.route('/players')
def players():
        select_query = "select * from players"
        cursor = g.conn.execute(text(select_query))
        all_players = cursor.fetchall()
        cursor.close()
        context = dict(all_players_data = all_players)
        return render_template("players.html",**context)

# Adding new player to the database (players table)
@app.route('/add', methods=['POST'])
def add():
        # accessing form inputs from user
        player_name = request.form['player_name']
        position = request.form['position']
        club = request.form['club']

        # passing params in for each variable into query
        params = {}
        # Only pass 3 attributes to have a try:
        params["new_name"] = player_name
        params["new_position"] = position
        params["new_club"] = club
        g.conn.execute(text('INSERT INTO players(full_name,position,club) VALUES ((:new_name),(:new_position),(:new_club))'), params)
        g.conn.commit()
        # ---------------------------------
        # Trying to show the new added data:
        cursor = g.conn.execute(text('SELECT full_name, position, club FROM players WHERE lower(full_name) LIKE lower((:new_name))'), params)
        new_player_data = []
        for new in cursor:
            new_player_data.append(new)
        cursor.close
        context_new = dict(new_player = new_player_data)
        return render_template('/players.html',**context_new)

#-------------------------------------------------------------------------------
# Searching team's match record data for the team user input
@app.route('/searchmatches', methods=['POST'])
def searchmatches():
        # accessing form inputs from user
        name = request.form['name']

        # passing params in for each variable into query
        params = {"search_team_name": f"%{name}%"}
        # params["search_team_name"] = name
        select_query = "SELECT m.match_date, m.match_time, s.stadium_name, t1.team_name AS home_team, m.score, t2.team_name AS away_team, r.full_name as referee_name FROM matches AS m JOIN teams AS t1 ON m.home_team_id = t1.team_id JOIN teams AS t2 ON m.away_team_id = t2.team_id JOIN stadiums AS s on s.stadium_id = m.stadium_id JOIN referees AS r on r.referee_id = m.referee_id WHERE (lower(t1.team_name) LIKE lower((:search_team_name)) OR lower(t2.team_name) LIKE lower((:search_team_name)))"

        cursor = g.conn.execute(text(select_query),params)
        match_records = []
        for record in cursor:
            match_records.append(record)
        cursor.close()
        context1 = dict(data1 = match_records)

        # Searching teams squad:
        select_query2 = "SELECT p.full_name AS player_name, p.position, p.club, p.jersey_number FROM teams AS t JOIN players AS p ON p.team_id = t.team_id WHERE lower(t.team_name) LIKE lower((:search_team_name))"
        cursor = g.conn.execute(text(select_query2),params)
        team_makeup = []
        for player in cursor:
            team_makeup.append(player)
        cursor.close()
        context2 = dict(data2 = team_makeup)
        return render_template("teams.html",**context1, **context2)
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# searching data for the player user input
@app.route('/searchP', methods=['POST'])
def searchP():
        # accessing form inputs from user
        name = request.form['name']
        # passing params in for each variable into query
        params = {"search_player_name": f"%{name}%"}
        # Query the basic information of the player the user searching for
        select_query1 = "SELECT p.full_name as Name, p.position, p.date_of_birth, p.club AS Club_team, t.team_name AS National_team, p.jersey_number AS National_jersey_number, p.height, p.weight FROM players as p left join teams as t on p.team_id = t.team_id WHERE lower(p.full_name) LIKE lower((:search_player_name))"
        cursor = g.conn.execute(text(select_query1),params)
        player_data = []
        for pdata in cursor:
            player_data.append(pdata)
        cursor.close()
        context1 = dict(data1 = player_data)

        # Query all match records and events of that player:
        select_query2 = "SELECT p.full_name AS Name, m.match_date,m.match_time, t1.team_name AS home_team, m.score, t2.team_name AS away_team, e.event_type, e.time_in_match AS event_time FROM events AS e JOIN matches AS m ON e.match_id = m.match_id JOIN players AS p ON e.action_player_1 = p.player_id JOIN teams AS t1 ON m.home_team_id = t1.team_id JOIN teams AS t2 ON m.away_team_id = t2.team_id WHERE (e.event_type NOT IN ('Substitution') AND lower(p.full_name) LIKE lower((:search_player_name))) ORDER BY match_date DESC"
        cursor = g.conn.execute(text(select_query2),params)
        match_records = []
        for record in cursor:
            match_records.append(record)
        cursor.close()
        # context = dict(data = match_records)
        context2 = dict(data2 = match_records)
        # g.conn.commit()
        return render_template("players.html",**context1,**context2)
#------------------------------------------------------------------------------

@app.route('/login')
def login():
        abort(401)
        this_is_never_executed()


if __name__ == "__main__":
        import click

        @click.command()
        @click.option('--debug', is_flag=True)
        @click.option('--threaded', is_flag=True)
        @click.argument('HOST', default='0.0.0.0')
        @click.argument('PORT', default=8111, type=int)
        def run(debug, threaded, host, port):
                """
                This function handles command line parameters.
                Run the server using:

                        python server.py

                Show the help text using:

                        python server.py --help

                """

                HOST, PORT = host, port
                print("running on %s:%d" % (HOST, PORT))
                app.run(host=HOST, port=PORT, debug=debug, threaded=threaded)

run()
