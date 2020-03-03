#!/usr/bin/env python
import cgi
import cgitb

import codecs
import psycopg2
from config import config
cgitb.enable()
form = cgi.FieldStorage()

def lista_hurtowni():
    """ Pobiera liste hurtowni z opcja select html"""
    conn = None
    try:
        # laczy z baza danych
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute('set search_path to try1;')
        cur.execute('SELECT s.nr_hurtownia,s.nazwa,pobierz_adres_hurtownia(s.nr_hurtownia) from try1.hurtownia s;')
        db_version = cur.fetchall()
        print"<select id=\"dostawca_select\" class=\"select_bar\" name=\"wybrana_hurtownia\">"
        for nr,nazwa,adres in db_version:
            print "<option value=\"%s\">%s : %s</option>" % (nr,nazwa,adres[6:-1])
        print"</select>"
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
 
 
if __name__ == '__main__':
    print "Content-type: text/html\n"
    lista_hurtowni()