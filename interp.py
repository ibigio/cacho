#!/usr/bin/env python3
from cacho import *

a = Player('Ilan')
b = SafeNaivePlayerAI('Anton')

g = Game([a,b])

r = Round([a,b])

def play():
	total = int(input('How many total dice: '))
	hand = [int(x) for x in input('What is your hand: ').strip()]
	while True:
		call_str = input('Previous call: ')
		if call_str.lower().strip() == 'start':
			b.step(hand, None, total)
		else:
			call_split = call_str.split(',')
			quantity = int(call_split[0])
			face = int(call_split[1])
			b.step(hand, Call(quantity, face), total)
		print()

play()