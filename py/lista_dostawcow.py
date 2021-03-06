#!/usr/bin/env python

from lxml import etree
import cgi
import cgitb

import codecs
import psycopg2
from config import config
cgitb.enable()
form = cgi.FieldStorage()

def lista_dostawcow():
    """ Connect to the PostgreSQL database server to retrive first names and last names of all 'dostawcow' """
    conn = None
    try:
        # laczenie z baza danych
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute('SELECT PESEL,imie,nazwisko from try1.dostawca;')
        db_version = cur.fetchall()
        print"<select id=\"dostawca_select\" class=\"select_bar\" name=\"wybrany_dostawca\">"
        for pesel,imie,nazwisko in db_version:
            print "<option value=\"%s\">%s %s</option>" % (pesel,imie,nazwisko)
        print"</select>"

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
 
 
if __name__ == '__main__':
    print "Content-type: text/html\n"
    lista_dostawcow()