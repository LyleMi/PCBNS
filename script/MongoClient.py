from pymongo import MongoClient
from time import clock
from random import randint
import json
import fileinput

def insert(fjson, col):
	x = []
	for line in fileinput.input(fjson):
	  x.append(json.JSONDecoder().decode(line))

	start = clock()
	for i in x:
	  col.insert(i)

	end = clock()
	print (end-start)
	f.close()

def find(url, col, times, ran):
	x = []
	f = open(url)
	for i in f:
		x.append({"url":domain})
	start = clock()
	
	for i in range(times):
		col.find(x[randint(0,ran)])
	
	end = clock()
	print (end-start)
	f.close()

if __name__ == '__main__':
	conn = MongoClient('localhost')
	db = conn.html
	col = db.table
	insert('data.json', col)
	find('url', col, 20, 200)

