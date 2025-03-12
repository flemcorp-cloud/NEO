#!/usr/bin/env python

# Author: Hezekiah Watson
# Last Edit: February 28, 2025

# Defines the character for the game

class Character:
    def __init__(self, nickname, weapons, weaknesses):
        self.nickname = nickname
        self.weapons = weapons
        self.weaknesses = weaknesses

    def get_nickname(self):
        return self.nickname

