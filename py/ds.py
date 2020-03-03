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
pesel =form.getvalue("pole3", 0)


def insert_dostawca():
    """ dodanie wiersza do tablicy dastawcow """
    sql1 = "SELECT pesel FROM try1.dostawca;"
    sql = """INSERT INTO try1.dostawca
             VALUES(%s,%s,%s);"""
    conn = None
    try:
        #laczenie z baza danych
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql1)
        tu = cur.fetchall()
        spr = (pesel,)
        if spr in tu:
            print "Pesel %s already exists in the database" % (pesel)
        else:
            cur.execute(sql,(pesel,imie,nazwisko))
            conn.commit()
        
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
    insert_dostawca()
    #strona do wyswietlenia