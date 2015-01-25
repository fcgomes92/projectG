#/usr/env python
# ProjectG - Pomodoro Timer
# Interface : console
# author: gomes

from time import time, sleep
from datetime import datetime, timedelta
from os import system, uname
from pygame import init, mixer

# Inicia pygame service
init()

class timer():
    def __init__(self):
        self.begin = datetime.now()
        self.dif = datetime.now()
        self.end = datetime.now()
        self.play_music = True
        
        # Nome e caminho padrão do evento sonoro
        self.finish_sound = 'media/alarm.ogg'
        mixer.music.load(self.finish_sound)
        if self.play_music : mixer.music.play(1)
        
        # Intervalos de tempos
        # variaáveis para possível customização
        try:
            # Le os valores de inicialização
            # do arquivo de config : config.data
            config_file = open('config.data')
            self.pomodoro_time = int(config_file.readline())
            self.long_break = int(config_file.readline())
            self.short_break = int(config_file.readline())
            config_file.close()    
        except Exception as e:
            # Caso não consiga abrir o arquivo
            # Inicializa e mostra um erro.
            template = "An exception of type {0} occured. Arguments:\n{1!r}"
            message = template.format(type(e).__name__, ex.args)
            print (message)
            self.pomodoro_time = 25
            self.long_break = 30
            self.short_break = 5
        # Segundo modo de representação
        # das variáveis acima.
        '''
        self.config = {
            "pomodoro_time":25, 
            "long_break" = 30,
            "short_break" = 5
            }
        '''

        # Verificação do sistema Operacional
        # para setar o comando que limpa
        # a tela
        if(uname()[0] == 'Linux'):
            self.cmd = 'clear'
        else:
            self.cmd = 'cls'

        system(self.cmd)
        pass

    def _set_actual_time(self):
        self.begin = datetime.now()
        self.dif = datetime.now()
        #self.restante = self.begin
        pass

    def update_times(self):
        # Atualiza a quantidade de tempo restante
        self.restante = self.end.now() - self.dif.now()

        print("Tempo inicial:\t" + str(self.begin.time()))
        print("Tempo corrente:\t" + ":".join(str(i) for i in [self.dif.hour,self.dif.minute,self.dif.second]))
        print("Tempo final:\t" + str(self.end.time()))
        print("Tempo restante:\t" + str(self.restante))

        # Tempo entre atualizações
        sleep(0.5)

        # Tempo corrente
        self.dif = datetime.now()
        pass

    def start_pomodoro(self):
        # Pega o tempo atual
        self._set_actual_time()

        self.end = self.end.now() + timedelta(minutes=+self.pomodoro_time)

        while  self.end > self.dif:
            try:
                system(self.cmd)
                self.update_times()
            except KeyboardInterrupt:
                self.play_music=False
                print("Parando o processo!")
                break

        system(self.cmd)
        if self.play_music: mixer.music.play(3)
        self.play_music = True
        pass

    def start_short_break(self):
        # Pega o tempo atual
        self._set_actual_time()

        self.end = self.end.now() + timedelta(minutes=+self.short_break)

        while  self.end > self.dif:
            try:
                system(self.cmd)
                self.update_times()
            except KeyboardInterrupt:
                self.play_music = False
                print("Parando o processo!")
                break
           
        system(self.cmd)
        if self.play_music: mixer.music.play(3)
        self.play_music = True
        pass

    def start_long_break(self):
        # Pega o tempo atual
        self._set_actual_time()

        self.end = self.end.now() + timedelta(minutes=+self.long_break)

        while  self.end > self.dif:
            try:
                system(self.cmd)
                self.update_times()
            except KeyboardInterrupt:
                self.play_music = False
                print("Parando o processo!")
                break

        system(self.cmd)
        if self.play_music: mixer.music.play(3)
        self.play_music = True
        pass

    def status_var(self):
        system(self.cmd)
        str_status = ('Configurações dos tempos: \n' +
                        '{3}\t{0:>02d} min.\n' +
                        '{4}\t{1:>02d} min.\n' + 
                        '{5}\t{2:>02d} min.'
                    ).format(self.pomodoro_time
                        ,   self.short_break
                        ,   self.long_break
                        ,   'Tempo Pomodoro: '
                        ,   'Tempo Short Break: '
                        ,   'Tempo Long Break: '
                        )
        print(str_status)
        pass

    def configure(self):
        # Limpa a tela
        system(self.cmd)

        self.pomodoro_time = int(input("Entre com o tempo do Pomodoro: "))
        self.short_break = int(input("Entre com o tempo do Short Break: "))
        self.long_break = int(input("Entre com o tempo do Long Break: "))

        # Tentativa de persistir os dados
        # de configuração no arquivo: config.data
        try:
            config_file = open('config.data', 'w')
            config_file.write(str(self.pomodoro_time) + "\n")
            config_file.write(str(self.long_break) + "\n")
            config_file.write(str(self.short_break) + "\n")
            config_file.close()
        except Exception as e:
            template = "An exception of type {0} occured. Arguments:\n{1!r}"
            message = template.format(type(e).__name__, ex.args)
            print (message)
            print("As informações de configuração não foram persistidas.")

        system(self.cmd)
        pass

    def instrucoes(self):
        system(self.cmd)
        str_instrucoes = '''
The Pomodoro Technique is a time and focus management method which improves productivity and quality of work.
The name comes from a kitchen timer, which can be used to keep track of time. In short, you are supposed to 
focus on work for around 25 minutes and then have a well deserved break in which you should do nothing but 
relax. This cycle repeats once it reaches 4th break – then you should take a longer break (have a walk or 
something). It's that simple. It improves your focus, physical health and mental agility depending on how 
you spend your breaks and how strictly you follow the routine.
You can read more on pomodoro technique here: http://pomodorotechnique.com/
'''
        print(str_instrucoes)
        pass

t = timer()
ops = {
        '1' :   t.start_pomodoro
    ,   '2' :   t.start_short_break
    ,   '3' :   t.start_long_break
    ,   '4' :   t.configure
    ,   '5' :   t.status_var
    ,   '6' :   t.instrucoes
    }

# String de todas as opções do programa
str_ops = '''
Escolha uma opção:
    1 :: Pomodoro
    2 :: Short Break
    3 :: Long Break
    4 :: Configurar
    5 :: Status do Programa
    6 :: Instruções
    0 :: Sair
'''

try:
    escolha = ''
    while escolha!='0':
        try:
            escolha = str(input(str_ops))
            if escolha in ops : ops[escolha]()
        except KeyboardInterrupt:
            print("\nBye bye!\n")
            break
except Exception as e:
    print(str(e))