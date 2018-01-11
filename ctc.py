#!/usr/bin/env python3
from datetime import datetime as dt
import time
import argparse

class Convert:
	'Convert from Unix Epoch to a Human-readable format'

	def __init__(self,CLIctime,CLIformat):
		self.ctime = CLIctime
		self.localetime = None
		self.dateobj = None
		self.defaultFORMAT = '%m/%d/%Y %H:%M:%S'
		self.CLIformat = CLIformat
		self.ConvertTime()
		self.OutTime()

	def ConvertTime(self):
		if self.ctime == None:
			print('No ctime was provided to convert')
			quit()
		else:
			self.localetime = time.ctime(self.ctime)
			self.dateobj = dt.strptime(self.localetime, '%c')

	def OutTime(self):
		if self.CLIformat != None:
			print(dt.strftime(self.dateobj, self.CLIformat))
		else:
			print(dt.strftime(self.dateobj, self.defaultFORMAT))

class CommandLine:
	'Allow for command-line options to be passed'

	def __init__(self):
		self.inCTIME = None
		self.outFORMAT = None
		self.showFORMATTERS = False
		self.formatDICT = dict([('%a', 'Locale’s abbreviated weekday name'), ('%A', 'Locale’s full weekday name'), ('%b', 'Locale’s abbreviated month name'), ('%B', 'Locale’s full month name'), ('%c', 'Locale’s appropriate date and time representation'), ('%d', 'Day of the month as a decimal number [01,31]'), ('%H', 'Hour (24-hour clock) as a decimal number [00,23]'), ('%I', 'Hour (12-hour clock) as a decimal number [01,12]'), ('%j', 'Day of the year as a decimal number [001,366]'), ('%m', 'Month as a decimal number [01,12]'), ('%M', 'Minute as a decimal number [00,59]'), ('%p', 'Locale’s equivalent of either AM or PM (%p is only valid with %I)'), ('%S', 'Second as a decimal number [00,61]'), ('%w', 'Weekday as a decimal number [0(Sunday),6]'), ('%x', 'Locale’s appropriate date representation'), ('%X', 'Locale’s appropriate time representation'), ('%y', 'Year without century as a decimal number [00,99]'), ('%Y', 'Year with century as a decimal number'), ('%z', 'Time zone offset indicating a positive or negative time difference from UTC/GMT'), ('%Z', 'Time zone name (no characters if no time zone exists)'), ('%%', 'A literal "%" character')])
		self.switches()
		self.displayFormatters()

	def switches(self):
		parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
		#argparse.ArgumentParser()
		parser.add_argument('-c',metavar='ctime',type=int,help='10 digit ctime',action='store')
		parser.add_argument('-f',metavar='format',action='store',help='Set the output format')
		parser.add_argument('-fo',action='store_true',help='Display the formatting operators')
		args = parser.parse_args()
		self.inCTIME = args.c
		self.outFORMAT = args.f
		self.showFORMATTERS = args.fo

	def displayFormatters(self):
		if self.showFORMATTERS != False:
			for key in list(self.formatDICT.keys()):
				print(key + '\t' + self.formatDICT[key])
			quit()
			 
class UserInput:
	
	def __init__(self):
		self.timeINPUT = None
		self.formatINPUT = None
		self.InputCTIME()

	def InputCTIME(self):
		self.timeINPUT = input('What is the ctime to convert? >> ')
		if self.validateCTIME(self.timeINPUT) == 'ERROR':
			self.InputCTIME()
		formatINPUT = input('Enter the output format\n[default: MM/DD/YYYY HH:MM:SS] >> ') 
		self.validateFORMAT(formatINPUT)

	def validateCTIME(self,ctime):
		try:
			if ctime == None or ctime == '':
				self.timeINPUT = None
			else:
				self.timeINPUT = int(ctime)
		except ValueError:
			print('The ctime provided is not an integer, please try again')
			return('ERROR')
	
	def validateFORMAT(self,format):
		if format == '' or format == None:
			self.formatINPUT = None
		else:
			self.formatINPUT = format
		

cli = CommandLine()

if cli.inCTIME != None or cli.outFORMAT != None:
	cvt = Convert(cli.inCTIME,cli.outFORMAT)
else:
	ui = UserInput()
	cvt =  Convert(ui.timeINPUT,ui.formatINPUT)
