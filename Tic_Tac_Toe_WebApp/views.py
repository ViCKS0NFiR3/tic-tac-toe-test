"""
Routes and views for the flask application.
"""

from datetime import datetime
from Tic_Tac_Toe_WebApp import app
from flask import Flask, redirect, url_for, request,render_template
from Tic_Tac_Toe_WebApp.ticTac import TicTac

global current_player
global X_points
global O_points
global message
current_player = "X"
message = ""
X_points = 0
O_points = 0
X_tokens = list()
O_tokens = list()

#                1stH          2ndH          3rdH          1stV          2ndV          3rdV          LDia          RDia
patterns = [['1','2','3'],['4','5','6'],['7','8','9'],['1','4','7'],['2','5','8'],['3','6','9'],['1','5','9'],['7','5','3']]

def add_token(token,player):
	global current_player
	if player == "X":
		current_player = "O"
		X_tokens.append(token)
	elif player == "O":
		current_player = "X"
		O_tokens.append(token)
	check_win()


def check_win():
	global message
	for i in patterns:
		print(X_tokens)
		print(O_tokens)
		check_X = set(X_tokens) & set(i)
		check_O = set(O_tokens) & set(i)
		#check_X = X_tokens.intersection(i)
		#check_O = O_tokens.intersection(i)
		#print(check_X)
		if len(check_O) == 3:
			print("O Wins!")
			global O_points
			O_points = O_points + 1
			X_tokens.clear()
			O_tokens.clear()
			message = "Player O Wins!"
		elif len(check_X) == 3:
			print("X Wins!")
			global X_points
			X_points = X_points + 1
			X_tokens.clear()
			O_tokens.clear()
			message = "Player X Wins!"
		

@app.route('/')
def index():
	global current_player
	return render_template('index.html', title="Tic Tac Toe", year="2019", Xscore=X_points, Oscore=O_points, player=current_player, message=message)

@app.route('/pass',methods = ['POST','GET'])
def _pass():
	global current_player
	if request.method == 'POST':
		token = request.form['token']
		player = add_token(token,current_player)
		if token == 'Reset':
			current_player = "X"
			X_tokens.clear()
			O_tokens.clear()

	return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)