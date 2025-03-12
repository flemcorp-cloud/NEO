#!/usr/bin/env python

# Author: Hezekiah Watson
# Last Edit: February 28, 2025

# Chapter 4 of the game

import play_rps

def chapter_4(character):
    """Chapter 4"""
    print("\nChapter 4: Fracturing Mind")
    print(f"{character.get_nickname()}'s mind begins to fracture. Every choice feels like it might lead them down a dangerous path. The AI offers them a way out, but only if they can defeat it.")
    print(f"The interface glitches violently as if the system may crash, losing {character.get_nickname()} forever inside the construct.")
    return play_rps.play_rps(character)
