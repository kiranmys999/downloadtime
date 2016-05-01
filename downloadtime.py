#!/usr/bin/env python
import argparse

def showtime(unit, size, speed):
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

def showspeed(unit, size, sec):
	if unit == 'm':
		kb = size*1024.0
	elif unit == 'g':
		kb = size*1024.0*1024.0
	elif unit == 'k':
		kb = size

	dlspeed = kb/sec

	print "required download speed is {} KB/s".format(dlspeed)


def calctime():
	speed = int(raw_input('Enter download speed in KB/s: '))
	filesize = raw_input('Enter total download size (M|m / G|g / K|k) bytes: ')
	size = int(filesize[:len(filesize)-1])

	if (filesize.endswith('M') or filesize.endswith('m')):
		showtime('m', size, speed)

	elif (filesize.endswith('G') or filesize.endswith('g')):
		showtime('g', size, speed)

	elif (filesize.endswith('K') or filesize.endswith('k')):
		showtime('k', size, speed)


def calcspeed():
	downloadtime = raw_input('Enter download time in hours(h)/minutes(m): ')
	filesize = raw_input('Enter total download size (M|m / G|g / K|k) bytes: ')
	size = int(filesize[:len(filesize)-1])
	dtime = float(downloadtime[:len(downloadtime)-1])

	if downloadtime.endswith('h'):
		sec = dtime*60*60
	elif downloadtime.endswith('m'):
		sec = dtime*60

	if (filesize.endswith('M') or filesize.endswith('m')):
		showspeed('m', size, sec)

	elif (filesize.endswith('G') or filesize.endswith('g')):
		showspeed('g', size, sec)

	elif (filesize.endswith('K') or filesize.endswith('k')):
		showspeed('k', size, sec)

if __name__=="__main__":
	#calctime()
	#calcspeed()

	parser = argparse.ArgumentParser()
	subparser = parser.add_subparsers(dest="test")
	parser_t = subparser.add_parser('t', help="calculate time needed to download a file at given speed")
	parser_s = subparser.add_parser('s', help="calculate speed needed to download a file in given time")
	args = parser.parse_args()
	
	if args.test == 't':
		calctime()

	elif args.test == 's':
		calcspeed()

