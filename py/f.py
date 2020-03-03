#!/usr/bin/env python

 
import cgi
import cgitb
import codecs
import psycopg2
from config import config
cgitb.enable()
form = cgi.FieldStorage()

nr_dostawy = form.getvalue("nr_dostawy", 0)
kwota = form.getvalue("kwota", 0)
rodzaj_zaplaty =form.getvalue("rodzaj_zaplaty", 0)
data_wystawienia =form.getvalue("data_wystawienia", 0)

def insert_faktura():
    """ dodanie wiersza do tablicy faktura """
 
    sql = """INSERT INTO try1.faktura
             VALUES(%s,%s,%s,%s);"""
    conn = None
    try:
        #laczenie z baza danych
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql,(nr_dostawy,kwota,rodzaj_zaplaty,data_wystawienia))
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
    insert_faktura()
