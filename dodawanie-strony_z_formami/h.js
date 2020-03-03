var xmlHttp;

function h_start()
{
	pobierz_liste("lista_nipow");
	pobierz_liste("lista_adresow");
}
function d_start()
{
	pobierz_liste("sugerowany_numer_dostawy");
	pobierz_liste("lista_hurtownii");
	pobierz_liste("lista_sklepow");
	pobierz_liste("lista_dostawcow");
}

function f_start()
{
	pobierz_liste("lista_nr_dostaw_bez_faktury");
}
function t_start()
{
	pobierz_liste("lista_nr_dostaw");
}


function getRequestObject()      {
    if ( window.ActiveXObject)  {
         return ( new ActiveXObject("Microsoft.XMLHTTP")) ;
     } else if (window.XMLHttpRequest)  {
        return (new XMLHttpRequest())  ;
     } else {
        return (null) ;
     }
}

function pobierz_liste(a)
{
    xmlHttp = getRequestObject() ;
    if (xmlHttp) {        
  try {
        var url = "../../cgi-bin/project1/"+a+".py" ;
        xmlHttp.onreadystatechange = function(){wstaw_liste(a);} ;
        xmlHttp.open("POST", url,false);
        xmlHttp.setRequestHeader("Content-Type","application/x-www-form-urlencoded") ;
 		xmlHttp.send(null);
      }
      catch (e) {
        alert ("Nie mozna polaczyc sie z serwerem: " + e.toString()) ;
      }
    } else {
      alert ("Blad") ;
    }
}


function wstaw_liste(a)   {
    myDiv = document.getElementById(a);
    if (xmlHttp.readyState == 4) {
         if ( xmlHttp.status == 200 )  {
             response = xmlHttp.response;
             myDiv.innerHTML += response;
         }
    }  
}
