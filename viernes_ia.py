import threading
from viernes_listen import listen
from viernes_say import say
from web_automation import *
from audiospectrum import *

'''
Comandos
Reproduce [algo]
Busca en Wikipedia [algo]
Buscar imagen [algo]
Que hora es
Que fecha es
traduce [algo]
'''

audiospectrum = threading.Thread(name='spectrum', target=graphAudio, daemon=True)

if __name__ == '__main__':    
    audiospectrum.start()
    say('Hola, ¿Cómo estás?. Un gusto poder ayudarte.')
    while True:
        print('Disponible... esperando `okay viernes` o `salir`')
        words = listen().lower()
        if "okay viernes" in words:
            say('¿En que puedo ayudarte?')
            repeat = False
            while not repeat:
                print('Escuchando...')
                instruction = listen().lower()
                print(instruction)
                
                if 'hora' in instruction:
                    whatTimeIsIt()
                    repeat = True
                elif 'fecha' in instruction:
                    whatDateIsIt()
                    repeat = True
                elif 'wikipedia' in instruction:
                    index = instruction.find('wikipedia')
                    index += len('wikipedia')
                    searchText = instruction[index:len(instruction)]
                    obtainWikipediaInfo(searchText)
                    repeat = True
                elif 'reproduce' in instruction:
                    index = instruction.find('reproduce')
                    index += len('reproduce')
                    searchText = instruction[index:len(instruction)]
                    playMusicVideo(searchText)
                    repeat = True
                elif 'imagen' in instruction:
                    index = instruction.find('imagen')
                    index += len('imagen')+3
                    searchText = instruction[index:len(instruction)]
                    searchImages(searchText)
                    repeat = True
                elif 'traduce' in instruction:
                    index = instruction.find('traduce')
                    index += len('traduce')
                    searchText = instruction[index:len(instruction)]
                    translatePhraseBing(searchText)
                    repeat = True
                elif '¿' in instruction:
                    say(instruction)
                    repeat = False
        elif "salir" in words:
            print('Estoy para servirte, nos vemos.')
            say('Estoy para servirte, nos vemos.')
            break
            