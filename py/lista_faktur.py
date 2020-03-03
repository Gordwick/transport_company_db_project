#!/usr/bin/env python

from lxml import etree
import cgi
import cgitb
from itertools import islice
import codecs
import psycopg2
from config import config
cgitb.enable()
form = cgi.FieldStorage()
place_holder =int(form.getvalue("designated_dostawca", 0))

def lista_faktur():
	""" Pobiera liste faktur wypisuje wraz z jQuery expanderem """
	conn = None
	try:
		params = config()

		conn = psycopg2.connect(**params)
		cur = conn.cursor()
        
		polecenie = "set search_path to try1;"
		cur.execute(polecenie)

		polecenie = """
SELECT f.nr_dostawy,f.kwota,d.data_dostawy,
	(SELECT nazwa from sklep s where s.nr_sklep=d.nr_sklep),
	pobierz_adres_sklep(d.nr_sklep),
	(SELECT imie from wlasciciel w where w.NIP=(SELECT nip_wlasciciel from sklep s where s.nr_sklep=d.nr_sklep)),
	(SELECT nazwisko from wlasciciel w where w.NIP=(SELECT nip_wlasciciel from sklep s where s.nr_sklep=d.nr_sklep)),
	(SELECT nip_wlasciciel from sklep s where s.nr_sklep=d.nr_sklep),
	(SELECT nazwa from hurtownia h where h.nr_hurtownia=d.nr_hurtownia),
	pobierz_adres_hurtownia(d.nr_hurtownia),
	(SELECT imie from wlasciciel w where w.NIP=(SELECT nip_wlasciciel from hurtownia h where h.nr_hurtownia=d.nr_hurtownia)),
	(SELECT nazwisko from wlasciciel w where w.NIP=(SELECT nip_wlasciciel from hurtownia h where h.nr_hurtownia=d.nr_hurtownia)),
	(SELECT nip_wlasciciel from hurtownia h where h.nr_hurtownia=d.nr_hurtownia)
	FROM faktura f 
	left join dostawa d USING (nr_dostawy);
		"""
		cur.execute(polecenie)
 
	# pobieranie danych
		tabelka = cur.fetchall()
		for elems in islice(tabelka,place_holder,place_holder+10):
			polecenie_towar = "SELECT * FROM towar WHERE nr_dostawy='%s';" % elems[0]
			cur.execute(polecenie_towar)
			towary = cur.fetchall()
			print"<div class=\"expander\"> %s  : %s zl: %s</div>" % (elems[0],elems[1],elems[2])
			print( """<div class= \"details\">
			<dl><dt>Sklep: %s</dt>
			    <dd>Adres: %s </dd> <br>
			    <dd>Wlasciciel: %s %s - NIP: %s </dd> <br>
			<dt>Hurtownia: %s </dt><br>
			<dd>Adres: %s </dd> <br>
			<dd>Wlasciciel: %s %s - NIP: %s </dd> <br>
			<dt>Towary:</dt> <br>""") % (elems[3],elems[4][6:-1],elems[5],elems[6],elems[7],elems[8],elems[9][6:-1],elems[10],elems[11],elems[12])
			for towar in towary:
				print "<dd>Nazwa: %s    " % (towar[1])
				print "| Data waznosci: %s </dd><br>" % (towar[2])
			print "</dl></div>"

		cur.close()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()
 
 
if __name__ == '__main__':
	print "Content-type: text/html\n"
	lista_faktur()