#!/usr/bin/env python

# Author: Hezekiah Watson
# Last Edit: February 28, 2025

# Chapter 1 of the game

import play_rps

def chapter_1(character):
    """Chapter 1"""
    print("\nChapter 1: The Test Begins")
    print(f"{character.get_nickname()}, a brilliant programmer at a global technology company, volunteers for an experimental project that interfaces the human brain directly with a virtual network.")
    print(f"{character.get_nickname()} enters the interface and sees floating data. The AI agent, Smith, tells {character.get_nickname()} that they are trapped and must play Rock, Paper, Scissors against the system to get out.")
    return play_rps.play_rps(character)
