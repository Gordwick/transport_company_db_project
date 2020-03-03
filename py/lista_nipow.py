#!/usr/bin/env python

from lxml import etree
import cgi
import cgitb

import codecs
import psycopg2
from config import config
cgitb.enable()
form = cgi.FieldStorage()

def lista_nipow():
    """Pobiera liste NIP-ow z opcja select html """
    conn = None
    try:
        #laczenie z baza danych
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute('SELECT NIP,imie,nazwisko from try1.wlasciciel')
        osoby = cur.fetchall()
        print"<select id=\"nip_select\" class=\"select_bar\" name=\"pole2\">"
        for nip,imie,nazwisko in osoby:
            print "<option value=\"%s\">%s - %s %s</option>" % (nip,nip,imie,nazwisko)
        print"</select>"
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
 
 
if __name__ == '__main__':
    print "Content-type: text/html\n"
    lista_nipow()