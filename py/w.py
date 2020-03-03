#!/usr/bin/env python

 
import cgi
import cgitb
from itertools import islice
import codecs
import psycopg2
from config import config
cgitb.enable()
form = cgi.FieldStorage()

imie =form.getvalue("pole1", 0)
nazwisko =form.getvalue("pole2", 0)
NIP =form.getvalue("pole3", 0)


def insert_wlasciciel():
    """ dodanie jednego wiersza do tabeli wlasciciel"""

    sql1 = "SELECT NIP FROM try1.wlasciciel;"

    sql2 = """INSERT INTO try1.wlasciciel
             VALUES(%s,%s,%s) RETURNING NIP;"""
    conn = None
    try:
        #tworzenie lacza z baza danych
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql1)
        tu = cur.fetchall()
        spr = (NIP,)
        #sprawdzenie poprawnosci klucza glownego
        if spr in tu:
            raise Exception("NIP %s already exists in the database" % (NIP))
        else:
            cur.execute(sql2,(NIP,imie,nazwisko))
            conn.commit()
       	# close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
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
    insert_wlasciciel()