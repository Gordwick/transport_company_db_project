#!/usr/bin/env python

 
import cgi
import cgitb
from itertools import islice
import codecs
import psycopg2
from config import config
cgitb.enable()
form = cgi.FieldStorage()

def gets():
    """ insert a new vendor into the vendors table """
    sql1 = "SELECT nr_dostawy FROM try1.dostawa;"

    conn = None
    try:
        #laczenie z baza danych
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql1)
        # tworzenie sugerowanego numeru
        dostawa = cur.fetchall()
        dostawa =str(dostawa[-1][0])
        ex1,ex2 = dostawa.split("/")
        ex2 =  int(ex2) + 1
        ex2 = str(ex2)
        ex = str(ex1) + "/"
        for _ in range(len(ex2),5):
            ex+='0'
        ex+=ex2
        print '<p id="sugestia">Sugerowany numer '+ ex +'<p>'
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ =='__main__':
    print "Content-type: text/html\n"
    gets()