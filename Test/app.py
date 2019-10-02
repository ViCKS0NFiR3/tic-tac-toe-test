from flask import Flask, render_template
app = Flask(__name__, template_folder='templates')

player = "X"
switch_player = False

X_tokens = list()
O_tokens = list()
#             1stH    2ndH    3rdH    1stV    2ndV   3rdV     LDia    RDia
patterns = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(7,5,3)]

def add_token(token,player):
	switch_player = True
	if player == "X":
		player = "O"
		X_tokens.append(token)
	else:
		player = "X"
		O_tokens.append(token)

def check_win(player)
	

@app.route('/')
def index():
	return render_template('index.html', title="Tic Tac Toe", year="2019")

@app.route('/pass',methods = ['POST','GET'])
def _pass():
	if request.method == 'POST':
		token = request.form["token"]

		return "Hello World"

if __name__ == '__main__':
    app.run(debug=True)

