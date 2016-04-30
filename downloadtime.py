#!/usr/bin/env python

def calc(unit):
	if unit == 'm':
		kb = size*1024.0
	elif unit == 'g':
		kb = size*1024.0*1024.0
	elif unit == 'k':
		kb = size

	timesec = kb/speed
	timemin = timesec/60
	timehour = timemin/60

	print "{} hours | {} mins | {} seconds to download ".format(timehour, timemin, timesec)

speed = int(raw_input('Enter download speed in KB/s: '))
filesize = raw_input('Enter total download size (M|m / G|g / K|k) bytes: ')
size = int(filesize[:len(filesize)-1])

if (filesize.endswith('M') or filesize.endswith('m')):
	calc('m')

elif (filesize.endswith('G') or filesize.endswith('g')):
	calc('g')

elif (filesize.endswith('K') or filesize.endswith('k')):
	calc('k')


