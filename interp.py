#!/usr/bin/env python3
from cacho import *

a = Player('Ilan')
b = SafeNaivePlayerAI('Anton')

g = Game([a,b])

r = Round([a,b])