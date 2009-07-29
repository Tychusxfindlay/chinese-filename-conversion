#!/usr/bin/env python

from langconv import *
import unicodedata
import os,sys,glob

def convertion(input):
  c = Converter('zh-hant')
  return c.convert(input.decode('utf8')).encode('utf8')

if (len(sys.argv)==1):
  dir = './*'
else:
  dir = sys.argv[1]

def chinesewidth(str):
  length = 0
  str = str.decode('utf8')
  for s in str:
    length += 1
    if unicodedata.east_asian_width(s) == 'W':
      length += 1
  return length

def whitespace(width):
  a=""
  for i in xrange(width):
    a=a+" "
  return a

def appendspace(str, width):
  initialwidth = chinesewidth(str)
  difference = width - initialwidth
  if (difference < 0):
    difference = 0
  return str + whitespace(difference)

filenames = glob.glob(dir)
for filename in filenames:
  filename = os.path.basename(filename)
  print appendspace(filename,40),  convertion(filename)

input = raw_input("Confirm changes? y/n [y]:")
if (input==''):
  input = 'y'
if (input=='y'):
  for filename in filenames:
    os.rename(filename, convertion(filename))
