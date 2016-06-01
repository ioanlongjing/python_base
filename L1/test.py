#!/usr/bin/env python2.7
# -*- coding: UTF-8 -*-
import sys

def switch_status(score):
	if 90 < score < 100:
		print "Good"
	elif score > 80:
		print "Not Bad"
	elif score > 70:
		print "Normal"
	else :
		print "ga n ba tsu te"

def check_range(score):
	if ( score > 100 ) or ( score < 0 ) :
		print "Are you kidding me?"
		sys.exit(0)

if __name__ == '__main__':
	score = input("Please Input your score:")
	check_range(score)
	print score
	switch_status(score)
