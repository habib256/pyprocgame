import sys
import procgame
import pinproc
from threading import Thread
import random
import string
import time
import locale
import math
import copy
import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((300, 50))
pygame.display.set_caption('Press CTRL-C to exit')
circle = pygame.Surface([300, 50])
line = pygame.Surface([300,50])
color = pygame.Color(100,0,0,100)
pygame.draw.line(line, color, [0,25], [300,25], 2)
pygame.draw.circle(circle, color, [125,25], 20,8)
screen.blit(line, [0,0])
pygame.display.flip()
screen.blit(circle, [0,0])
pygame.display.flip()

class KeyboardHandler():
	"""docstring for KeyboardHandler"""
	def __init__(self):
		self.ctrl = 0

	def get_keyboard_events(self):
		key_events = []
		for event in pygame.event.get():
			key_event = {}
			if event.type == KEYDOWN:
				if event.key == K_RCTRL or event.key == K_LCTRL:
					self.ctrl = 1
				if event.key == K_c:
					if self.ctrl == 1:
						key_event['type'] = 99
						key_event['value'] = 'quit'
				elif (event.key == K_ESCAPE):
					key_event['type'] = 99
					key_event['value'] = 'quit'
				elif (event.key == K_RSHIFT):
					key_event['type'] = 1
					key_event['value'] = 1
				elif (event.key == K_LSHIFT):
					key_event['type'] = 1
					key_event['value'] = 3
			elif event.type == KEYUP:
				if event.key == K_RCTRL or event.key == K_LCTRL:
					self.ctrl = 0
				elif (event.key == K_RSHIFT):
					key_event['type'] = 2
					key_event['value'] = 1
				elif (event.key == K_LSHIFT):
					key_event['type'] = 2
					key_event['value'] = 3
			if len(key_event):
				key_events.append(key_event)
		return key_events

