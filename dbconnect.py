#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3

conn = sqlite3.connect('connect.db')
print "Opened database successfully";

c = conn.cursor()

def insert_rec ():
    try:	
        c.execute("INSERT into PYTHON_TABLE values ('557','DORA') ")
	conn.commit()
	tmp=c.execute("SELECT id, name from PYTHON_TABLE")
	for row in tmp:
   	    print "ID = ", row[0]
   	    print "NAME = ", row[1],"\n"
        print "Records created successfully";
    except Exception as e:
        print(e)

def update_rec():
    try:    
        c.execute("UPDATE PYTHON_TABLE set NAME = 'jade' WHERE ID = 111")
	print("Record is getting updated.......")
	tmp=c.execute("SELECT id, name from PYTHON_TABLE")
	for row in tmp:
             print "ID = ", row[0]
   	     print "NAME = ", row[1], "\n"

	print "Records Updated successfully"
    except Exception as e:
        print(e)


print "####.....DATABASE CONNECTION.....####"
print "1. Insert"
print "2. Update"
choice=input("Enter your Choice")
if choice == 1:
    insert_rec()
else:
    update_rec()
conn.close()
