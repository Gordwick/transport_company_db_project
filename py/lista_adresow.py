#!/usr/bin/env python

from lxml import etree
import cgi
import cgitb

import codecs
import psycopg2
from config import config
cgitb.enable()
form = cgi.FieldStorage()

def lista_adresow():
    """ zwraca lista adresow z opcja select html"""
    conn = None
    try:
        # laczy z baza danych
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute('SELECT w.nr_id,w.miejscowosc,w.ulica,w.nr_budynku from try1.adres w;')
        adres = cur.fetchall()
        print"<select id=\"nip_select\" class=\"select_bar\" name=\"pole3\">"
        for nr_id,miejscowosc,ulica,nr_budynku in adres:
            print "<option value=\"%s\">%s, %s %s</option>" % (nr_id,miejscowosc,ulica,nr_budynku)
        print"</select>"

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
 
 
if __name__ == '__main__':
    print "Content-type: text/html\n"
    lista_adresow()