#!/usr/bin/env python

 
import cgi
import cgitb
from itertools import islice
import codecs
import psycopg2
from config import config
cgitb.enable()
form = cgi.FieldStorage()

nazwa =form.getvalue("pole1", 0)
nip =form.getvalue("pole2", 0)
adres =form.getvalue("pole3", 0)

def insert_hurtownia():
    """ dodanie wiersza do tablicy hurtownia """
    sql1 = "SELECT count(*) FROM try1.hurtownia;"

    sql2 = """INSERT INTO try1.hurtownia
             VALUES(%s,%s,%s,%s);"""
    conn = None
    try:
        # laczenie z baza danych
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql1)
        row_counter = cur.fetchone()
        
        row_count = 'H'
        for _ in range( len(str(row_counter[0]+1)),3):
            row_count+='0'
        row_count += str(row_counter[0]+1)

        wynik = cur.execute(sql2,(row_count,nazwa,nip,adres))
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
    insert_hurtownia()
    #strona do wyswietlenia