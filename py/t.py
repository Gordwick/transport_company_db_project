#!/usr/bin/env python

 
import cgi
import cgitb
import codecs
import psycopg2
from config import config
cgitb.enable()
form = cgi.FieldStorage()

nr_dostawy = form.getvalue("nr_dostawy", 0)
nazwa = form.getvalue("nazwa", 0)
data_waznosci =form.getvalue("data_waznosci", 0)
nr_serii =form.getvalue("nr_serii", 0)

def insert_towar():
    """ dodanie jednego wiersza do tabeli towar"""
 
    sql = """INSERT INTO try1.towar
             VALUES(%s,%s,%s,%s);"""
    conn = None
    try:
         #tworzenie lacza z baza danych
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql,(nr_serii,nazwa,data_waznosci,nr_dostawy))
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Numer serii musi byc niepowtarzalny.")
        file = codecs.open("../../p/dodawanie/error_page.html", 'r')
        print file.read()
    else:
        file = codecs.open("../../p/dodawanie/final_page.html", 'r')
        print file.read()
    finally:
        if conn is not None:
            conn.close()

if __name__ =='__main__':
    print "Content-type: text/html\n"
    insert_towar()
