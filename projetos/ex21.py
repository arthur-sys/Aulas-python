from pygame import mixer
import pygame
from pygame import mixer
mixer.init()
mixer.music.load('ex112.mp3')
mixer.music.play()
x = input('Digite algo para parar...')

