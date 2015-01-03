#/usr/env python
# ProjectG - Pomodoro Timer
# Interface : terminal
# author: gomes

from time import time, sleep
from datetime import datetime, timedelta
import os

class timer():
	def __init__(self, begin, end):
		self.begin = begin
		self.end = end
		pass

	def start_pomodoro(self):
		print("Começou! Tempo inicial: " )
		tempo = datetime.now()
		while  self.end > tempo:
			os.system('clear')
			print("Tempo inicial: " + str(self.begin.time()))
			print("Tempo corrente: " + ":".join(str(i) for i in [tempo.hour,tempo.minute,tempo.second]))
			print("Tempo final: " + str(self.end.time()))
			sleep(0.5)
			tempo = datetime.now()
			pass

	def stop_pomodoro(self):
		# Stop timer
		pass
try:
	tempo = int(input("Entre com o tempo: "))
	t = timer(datetime.now(), (datetime.now() + timedelta(minutes=+tempo)) )
	t.start_pomodoro()
except Exception as e:
	print("Erro!")
