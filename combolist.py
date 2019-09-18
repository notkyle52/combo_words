#!/usr/bin/env python

import re

wheel_file = open("wheels.txt", "r")
word_file = open("words.txt", "r")

wheels = []
words = []

split_whitespace = re.compile('\s')

for wheel_line in wheel_file:
	wheel = []
	for letter in wheel_line:
		if letter != '\n':
			wheel.append(letter)	
	wheels.append(wheel)

for word_line in word_file:
	words.extend(split_whitespace.split(word_line))


combos = []
def add_combo(combo):
	copy = []
	for w in combo:
		copy.append(w)
	combos.append(copy)

def push_letter(combo, wheel, letter):
	combo[wheel] = letter

	if wheel+1 == len(wheels):
		add_combo(combo)
		return

	for next_wheel_position in wheels[wheel+1]:
		push_letter(combo, wheel+1, next_wheel_position)

combo = []
for wheel in wheels:
	combo.append('*')

for letter in wheels[0]:
	push_letter(combo, 0, letter)


combo_words = []
for combo in combos:
	combo_words.append(''.join(combo))

#for word in words:
#	print(word)

for combo_word in combo_words:
	for dict_word in words:
		if dict_word == combo_word:
			print(dict_word)
