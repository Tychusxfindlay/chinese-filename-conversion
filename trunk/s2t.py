#!/usr/bin/env python

from langconv import *
import os,sys,glob

def convertion(input):
  c = Converter('zh-hant')
  return c.convert(input.decode('utf8')).encode('utf8')

if (len(sys.argv)==1):
  dir = './*'
else:
  dir = sys.argv[1]

filenames = glob.glob(dir)
for filename in filenames:
  print filename.ljust(50),  convertion(filename)

input = raw_input("Confirm changes? y/n [y]:")
if (input==''):
  input = 'y'
if (input=='y'):
  for filename in filenames:
    os.rename(filename, convertion(filename))
