#/usr/env python
# ProjectG - Pomodoro Timer
# Interface : terminal
# author: gomes

from time import time, sleep
from datetime import datetime, timedelta
import os

# Intervalos de tempos
# variaáveis para possível customização
pomodoro_time = 25
long_break = 30
short_break = 5

class timer():
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end
        self.restante = end.now() - begin.now()
        self.dif = datetime.now()
        if(os.uname()[0] == 'Linux'):
            self.cmd = 'clear'
        else:
            self.cmd = 'cls'
        pass

    def start_pomodoro(self):
        global pomodoro_time
        self.dif = datetime.now()
        self.end = self.end.now() + timedelta(minutes=+pomodoro_time)
        self.restante = self.begin
        while  self.end > self.dif:
            os.system(self.cmd)
            print("Tempo inicial: " + str(self.begin.time()))
            print("Tempo corrente: " + ":".join(str(i) for i in [self.dif.hour,self.dif.minute,self.dif.second]))
            print("Tempo final: " + str(self.end.time()))
            self.restante = self.end.now() - self.dif.now()
            print("Tempo restante: " + str())
            sleep(0.5)
            self.dif = datetime.now()
        os.system(self.cmd)
        pass

    def start_short_break(self):
        global short_break
        self.dif = datetime.now()
        self.end = self.end.now() + timedelta(minutes=+short_break)
        self.restante = self.begin
        while  self.end > self.dif:
            os.system(self.cmd)
            print("Tempo inicial: " + str(self.begin.time()))
            print("Tempo corrente: " + ":".join(str(i) for i in [self.dif.hour,self.dif.minute,self.dif.second]))
            print("Tempo final: " + str(self.end.time()))
            self.restante = self.end.now() - self.dif.now()
            print("Tempo restante: " + str())
            sleep(0.5)
            self.dif = datetime.now()
        os.system(self.cmd)
        pass

    def start_long_break(self):
        global long_break
        self.dif = datetime.now()
        self.end = self.end.now() + timedelta(minutes=+long_break)
        self.restante = self.begin
        while  self.end > self.dif:
            os.system(self.cmd)
            print("Tempo inicial: " + str(self.begin.time()))
            print("Tempo corrente: " + ":".join(str(i) for i in [self.dif.hour,self.dif.minute,self.dif.second]))
            print("Tempo final: " + str(self.end.time()))
            self.restante = self.end.now() - self.dif.now()
            print("Tempo restante: " + str())
            sleep(0.5)
            self.dif = datetime.now()
        os.system(self.cmd)
        pass

    def configure(self):
        global pomodoro_time, short_break, long_break
        os.system(self.cmd)
        #print("TODO : Configurações")
        pomodoro_time = int(input("Entre com o tempo do Pomodoro: "))
        short_break = int(input("Entre com o tempo do Short Break: "))
        long_break = int(input("Entre com o tempo do Long Break: "))
        os.system(self.cmd)
        pass

    def instrucoes(self):
        os.system(self.cmd)
        print("TODO : Instruções")
        pass

t = timer(datetime.now(), (datetime.now() + timedelta(minutes=+0)) )
ops = {
        '1' :   t.start_pomodoro,
        '2' :   t.start_short_break,
        '3' :   t.start_long_break,
        '4' :   t.configure,
        '5' :   t.instrucoes
    }

# String de todas as opções do programa
str_ops = '''
Escolha uma opção:
    1 :: Pomodoro
    2 :: Short Break
    3 :: Long Break
    4 :: Configurar
    5 :: Instruções
    0 :: Sair
'''

try:
    escolha = ''
    while escolha!='0':
        escolha = str(input(str_ops))
        if escolha in ops : ops[escolha]()

except Exception as e:
    print(str(e))