import pygame
pygame.mixer.init()
pygame.mixer.music.load("440Hz_44100Hz_16bit_05sec.wav")
pygame.mixer.music.play()
# while pygame.mixer.music.get_busy() == True:
#     continue