#!/usr/bin/env python

from lxml import etree
import cgi
import cgitb

import codecs
import psycopg2
from config import config
cgitb.enable()
form = cgi.FieldStorage()
designated_dostawca =form.getvalue("designated_dostawca", "")

def lista_nr_dostaw():
    """ Pobranie listy nr_dostawa z opcja select html """
    conn = None
    try:
        # laczenie z baza danych
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

	polecenie = """SELECT nr_dostawy FROM try1.dostawa;"""
        cur.execute(polecenie)
 
        db_version = cur.fetchall()
	print"<select name=\"nr_dostawy\">"
        for nr in db_version:
		print"<option value=\"%s\">%s</option>" % (nr[0],nr[0])
	print"</select>"

       
       # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
 
 
if __name__ == '__main__':
    print "Content-type: text/html\n"
    lista_nr_dostaw()