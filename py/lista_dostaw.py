#!/usr/bin/env python

from lxml import etree
import cgi
import cgitb

import codecs
import psycopg2
from config import config
cgitb.enable()
form = cgi.FieldStorage()
designated_dostawca =form.getvalue("designated_dostawca", "")

def lista_dostaw():
    """ Pobiera liste dostaw przebazujac ja w tabela html """
    conn = None
    try:
        # laczy z baza danych
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        polecenie = "set search_path to try1;"
        cur.execute(polecenie)
        polecenie = "SELECT * FROM try1.pobierz_liste_dostaw('%s') ORDER BY 2 DESC;" % (designated_dostawca)
        cur.execute(polecenie)
 
        # display the PostgreSQL database server version
        db_version = cur.fetchall()
        print"<table><tr><th>Numer dostawy</th><th>Data dostawy</th><th>Adres hurtownii</th><th>Adres sklepu</th></tr>"
        for nr,date,a1,a2 in db_version:
            print"""<tr>
            <td>%s</td>
            <td> %s</td>
            <td>  %s</td>
            <td>|  %s  </td>
        </tr>
        """ % (nr,date,a1[6:-1],a2[6:-1])
        print"</table>"
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
 
 
if __name__ == '__main__':
    print "Content-type: text/html\n"
    lista_dostaw()