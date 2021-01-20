#!/usr/bin/env python3
import sys
import random

consonants = list("bcdfghjklmnpqrstvwxyz") + ["ch", "sh", "th"]
vowels = "aeiouy"
symbols = {
    "C": consonants,
    "V": vowels
}
max_syllable = "CVVC"
min_syllable = "CV"

def string_difference(s1, s2):
    idx = s1.find(s2)
    if idx == -1:
        print("Error: max syllable must include the min syllable!")
        sys.exit(1)
    end = idx + len(s2)
    return s1[:idx], s1[end:]

extras_before, extras_after = string_difference(max_syllable, min_syllable)    
syllable_length = random.randint(*map(int, sys.argv[1:3]))
word = ""

def generate_from_tmplt(template):
    return "".join(random.choice(symbols[s]) if s in symbols else s for s in template)

def pick_random_phonemes(phonemes):
    if not len(phonemes): return []
    return random.sample(phonemes, k=random.randint(0, len(phonemes)-1))

gen_random_sounds = lambda sounds: generate_from_tmplt(pick_random_phonemes(sounds))

for _ in range(syllable_length):
    minimal = generate_from_tmplt(min_syllable)
    eb = gen_random_sounds(extras_before)
    ea = gen_random_sounds(extras_after)
    word += eb + minimal + ea

# on a second thought, all caps names suck, removing
wordt = list(word)
wordt[0] = wordt[0].upper()
final= "".join(wordt)
print(final)
