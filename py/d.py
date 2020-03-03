#!/usr/bin/env python

import cgi
import cgitb
from itertools import islice
import codecs
import psycopg2
from config import config
cgitb.enable()
form = cgi.FieldStorage()

nr_dostawy =form.getvalue("wybrany_numer_dostawy", 0)
data_dostawy =form.getvalue("wybrana_data_dostawy", 0)
hurtownia =form.getvalue("wybrana_hurtownia", 0)
sklep =form.getvalue("wybrany_sklep", 0)
dostawca =form.getvalue("wybrany_dostawca", 0)

def insert_dostawa():
    """ dodanie wiersza do tablicy dostaw """
    sql1 ="SELECT nr_dostawy FROM try1.dostawa;"
    sql2 = """INSERT INTO try1.dostawa
             VALUES(%s,%s,%s,%s,%s);"""
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql1)
        els = cur.fetchall()
        nr_d = "('" + nr_dostawy + "',)"
        for el in els:
            if nr_d == str(el):
                raise Exception("<p>Dostawa juz istnieje w bazie</p>")
        cur.execute(sql2,(nr_dostawy,data_dostawy,sklep,hurtownia,dostawca))
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
    insert_dostawa()
    #strona do wyswietlenia