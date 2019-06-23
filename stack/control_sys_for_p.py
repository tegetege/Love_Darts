#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request

#外部ファイルインポート
import game_sys

class MyException_bad_score(Exception):
	pass

app = Flask(__name__)

@app.route('/', methods=['GET'])
def game_top():
	count_01_cul.delete_log() #delete log data
	return render_template('game_top.html',title='game_top')


@app.route('/zero_one_game', methods = ['POST', 'GET'])
def zero_one_game():

	if request.method == 'POST':
		#compile POST date for using 
		result = request.form
		result = dict(result)
		app.logger.debug(result)


		try: 
			game_data = {}
			game_data['game_log'] =[]

			if 'round_score' in result :
				if int(result['round_score'][0]) >= 0 and int(result['round_score'][0]) <= 180:
					game_data['score_board'] = count_01_cul.score_board_cal(result['score_board'][0],result['round_score'][0])
					game_data['round_count'] = count_01_cul.get_round_count()
					game_data['game_log'] = count_01_cul.get_game_log()

					#Result
					if int(game_data['score_board']) == 0 or len(game_data['game_log']) >= 15:
						result_data = {}
						result_data['game_log'] = count_01_cul.get_game_log()
						result_data['stats'] = count_01_cul.get_stats()		
						return render_template('zero_one_result.html',title='zero_one_game',game_data = result_data)

				else:
					raise MyException_bad_score()
			else:
				#When 'Game Start'. Set 80% stats line

				game_data['score_board'] = int(result['game_kind'][0])
				count_01_cul.set_80line(result['game_kind'][0])


		#文字列が入力された場合のエラー処理
		#Error handling when input str()
		except ValueError:
			game_data['error'] = '不正な値が入力されました'
			game_data['score_board'] = result['score_board'][0]
			game_data['game_log'] = count_01_cul.get_game_log()
			game_data['round_count'] = len(game_data['game_log'])

		#負の値,181以上のスコアが入力された場合のエラー処理
		#Error handling when input negative num
		except MyException_bad_score:
			game_data['error'] = '不正な値が入力されました'
			game_data['score_board'] = result['score_board'][0]
			game_data['game_log'] = count_01_cul.get_game_log()
			game_data['round_count'] = len(game_data['game_log'])

	return render_template('zero_one_game.html',title='zero_one_game',game_data = game_data)		

	if request.method == 'GET':
		return render_template('zero_one_game.html',title='zero_one_game')

count_01_cul = game_sys.Count_01()

if __name__ == "__main__":
	app.run(host='0.0.0.0',debug = True,port=80)