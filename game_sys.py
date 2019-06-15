
class Count_01:
	"""docstring for Count_01"""
	def __init__(self):
		self.score_board = int()
		self.game_80_line = int()
		self.stats = float(0.0)
		print(self.stats)
		self.game_kind = int()
		self.game_log    = []

	#80%スタッツを確定する
	def set_80line(self,game_kind):
		self.game_kind = int(game_kind)
		self.game_80_line = self.game_kind*0.2
		print(self.game_80_line)

	def score_board_cal(self,score_board,round_score):

		self.set_game_log(int(round_score))

		if int(score_board) - int(round_score) >= 0:
			self.score_board = int(score_board) - int(round_score)

		#Bust
		else:
			self.score_board = int(score_board)
		
		self.cal_stats()

		return  str(self.score_board)

	def cal_stats(self):
		if self.score_board <= self.game_80_line and self.stats == 0.0:
			print("スタッツ計算")
			print(self.game_log)
			self.stats = (self.game_kind - self.score_board) / len(self.game_log)
			return 
		else:
			return 


	def delete_log(self):
		self.game_log.clear()
		self.stats = float(0.0)
		print(self.stats)

	def set_game_log(self,round_score):
		self.game_log.append(round_score)

	def get_game_log(self):
		return self.game_log

	def get_round_count(self):
		return len(self.game_log)

	def get_stats(self):
		return round(self.stats,2)