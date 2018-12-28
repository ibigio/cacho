import random
import numpy as np
import re

class Game:
	
	def __init__(self, players):
		self.players = players
		self.rounds = []



class Round:
	
	def __init__(self, players, starting_player_indx=0):
		self.players = players
		self.calls = []
		self.cur_call = None
		self.starting_player_indx = starting_player_indx
		self.cur_player_indx = starting_player_indx
		# self.direction = None

	def print_round(self):
		print('Players:', [p.name for p in self.players])
		print('->' if self.direction is 1 else '<-')
		print('Calls:', self.calls)
		print('Starter:', self.starting_player)
		print('Current:', self.cur_player, 'calls', self.cur_call)

	def play_turn(self):
		call = None
		while 
		call = self.cur_player.make_call(self)
		# if len(self.calls) is 0:
		# 	self.direction = self.cur_player.choose_direction()
		self.calls.append(call)

	def validate_call(self, call):
		# this is a pull
		if call.q is 0 and call.v is 0:
			return True
		minq = self.cur_call.q
		minv = self.cur_call.
		if call.q < self.cur_call.q:
			return False
		if self.cur_call.v >= call.v:
				return False
		return True

	def next_player(self):
		self.cur_player = (self.cur_player + 1) % len(self.players)


class Call:

	def __init__(self, quantity, value):
		self.q = quantity
		self.v = value

	def __str__(self):
		return '(%s, %s)' % (self.q, self.v)


class Player:

	def __init__(self, name):
		self.name = name

	def __str__(self):
		return self.name

	def make_call(self, game_round):
		game_round.print_round()
		call_array = []
		while len(call_array) is not 2:	
			call_array = re.findall(r'\d+',input())
		return Call(call_array[0], call_array[1])

	# def choose_direction(self):
	# 	print('Choose direction (0 for Left, 1 for Right):')
	# 	direction_array = []
	# 	while len(call_array) is not 1:	
	# 		call_array = re.findall(r'\d',input())
	# 	return 1 if call_array[0] is 1 else -1


class PlayerAI:

	def __init__(self):
		self.game = None


class Cup:
	def __init__(self, num_dice=5):
		self.num_dice = num_dice
		self.dice = [self.roll_one() for i in range(self.num_dice)]
	def __str__(self):
		return str([die for die in self.dice])
	def roll_one(self):
		return random.randint(1, 6)
	def lose_one(self):
		self.num_dice -= 1
	def shake(self):
		self.dice = [self.roll_one() for i in range(self.num_dice)]
