import pygame
import math
from random import *


class Bar():
    def __init__(self, name, x=30, margin=30, height=15, alpha=75):
        self.name = name
        self.rank = None
        self.value = 0
        self.width = 0
        self.height = height
        self.margin = self.height + margin
        self.color = (randint(100, 200), randint(100, 200), randint(100, 200))
        self.alpha = alpha
        self.y = 0
        self.x = x
        self.data_bar = None
        self.show = {
            'y': 0,
            'width': 0,
            'value': 0
        }
        self.speed = {
            'y': 0,
            'width': 0,
            'value': 0
        }

    def sudden(self, rank, value, max_value):
        self.rank = rank
        self.value = value
        self.width = (value / max_value) * 500
        self.y = rank * self.margin
        self.show = {
            'y': self.y,
            'width': self.width,
            'value': self.value
        }

    def draw(self):
        self.jojo()
        self.data_bar = pygame.Surface((self.show['width'], self.height))
        self.data_bar.fill(self.color)
        self.data_bar.set_alpha(self.alpha)

    def update(self, rank, value, max_value):
        self.speed['value'] = (value - self.value) / 50
        self.speed['y'] = (rank * self.margin - self.y) / 50
        self.speed['width'] = ((value / max_value) * 500 - self.width) / 50
        self.rank = rank
        self.y = rank * self.margin
        self.width = (value / max_value) * 500
        self.value = value

    def jojo(self):
        self.show['value'] += self.speed['value']
        self.show['y'] += self.speed['y']
        self.show['width'] += self.speed['width']