import pyshine as ps

def graphAudio():
    audio, context = ps.audioCapture(mode='send')
    ps.showPlot(context, name='V    I   E   R   N   E   S')
    while True:
        frame = audio.get()
