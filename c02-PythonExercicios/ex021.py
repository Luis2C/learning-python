# Desafio 021 (Aula 08)
#
# Faça um programa em Python que abre e reproduza o áudio de um arquivo MP3.
#

import pygame

pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('ex021a.mp3')
#pygame.mixer.music.load('ex021b.mp3')
pygame.mixer.music.play()
pygame.event.wait()
