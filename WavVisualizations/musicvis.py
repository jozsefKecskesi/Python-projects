# Simple bar music visualizations
import random
import sys, math, wave, numpy, pygame
from pygame.locals import *
from scipy.fftpack import dct

bars = 30 # No of bars
height = 600 # height of a bar
width = 40 # width of a bar
fps = 10 # frame per sec



file_name = sys.argv[0]
status = 'stopped'
fpsclock = pygame.time.Clock()

# screen init, music playback

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode([bars * width, 50 + height])
pygame.display.set_caption('Audio Visualizer')
my_font = pygame.font.SysFont('consolas', 16)
pygame.mixer.music.load("piano.wav")
pygame.mixer.music.play()
pygame.mixer.music.set_endevent()
pygame.mixer.music.set_volume(0.2)
status = "Playing"

#process wave data

f = wave.open("piano.wav", 'rb')
params = f.getparams()
nchannels, sampwidth, framerate, nframes = params[:4]
str_data = f.readframes(nframes)
f.close()
wave_data = numpy.fromstring(str_data, dtype = numpy.short)
wave_data.shape = -1, 2
wave_data = wave_data.T

num = nframes

def Visualizer(nums):
    num = int(nums)
    h = abs(dct(wave_data[0][nframes - num:nframes - num + bars]))
    h = [min(height, int(i**(1 / 2.5) * height / 100)) for i in h]
    draw_bars(h)

def vis(status):
    global num
    if status == "stopped":
        num = nframes
        return
    elif status == "paused":
        Visualizer(num)
    else:
        num -= framerate / fps
        if num > 0:
            Visualizer(num)

def get_time():
    seconds = max(0, pygame.mixer.music.get_pos() / 1000)
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    hms = ("%02d:%02d:%02d" % (h, m, s))
    return hms

def controller(key):
    global status
    if status == "stopped":
        if key == K_RETURN:
            pygame.mixer_music.play()
            status = "playing"
    elif status == "paused":
        if key == K_RETURN:
            pygame.mixer_music.stop()
            status = "stopped"
        elif key == K_SPACE:
            pygame.mixer.music.unpause()
            status = "playing"
    elif status == "playing":
        if key == K_RETURN:
            pygame.mixer.music.stop()
            status = "stopped"
        elif key == K_SPACE:
            pygame.mixer.music.pause()
            status = "paused"

def draw_bars(h):
    bars = []
    for i in h:
        bars.append([len(bars) * width , 50 + height - i, width - 1, i])
    for i in bars:
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        pygame.draw.rect(screen, [r,g,b], i, 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN:
            controller(event.key)

    if num <= 0:
        status = "stopped"

    name = my_font.render(file_name, True, (255,255,255))
    info = my_font.render(status.upper() + "" + get_time(), True, (255,255,255))
    screen.fill((0,0,0))
    screen.blit(name,(0,0))
    screen.blit(info,(0, 18))
    fpsclock.tick(fps)
    vis(status)
    pygame.display.update()