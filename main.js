var xmlHttp;
var licz_faktur=0;
function choice1() {
    pobierz_liste("lista_dostawcow",".dostawca");
    document.getElementById("tit").innerHTML = "Wybierz dostawcę.";
	$(".reload_main").fadeIn();
     
}
function choice2() {
    $(".all").fadeOut();
	$(".reload_main").fadeIn();
    $(".dodaj").fadeIn();
    document.getElementById("tit").innerHTML = "Jaki element chcesz dodać?";
 
}
function choice3() {
    pobierz_liste("lista_faktur",".ksiegowosc",licz_faktur);
    licz_faktur=licz_faktur+10;
$(".details").fadeOut(); 
		$(".expander").click(function(){
      	$(this).next().slideToggle(200);});
    document.getElementById("tit").innerHTML = "Wykaz faktur.";
	$(".reload_main").fadeIn();
	
}

function lista_faktur_more(){
  pobierz_liste("lista_faktur",".ksiegowosc",licz_faktur);
  licz_faktur=licz_faktur+10;

$(".details").fadeOut(); 
		$(".expander").click(function(){
      	$(this).next().slideToggle(200);});

}

function pobierz_liste_dostaw(){
    document.getElementById("lista_dostaw").innerHTML = "";
    var e = document.getElementById("dostawca_select");
    var wybrane = e.options[e.selectedIndex].value;
    pobierz_liste("lista_dostaw",".dostawca",wybrane);
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


//------------------------------------------------------------------
function pobierz_liste(a,b,c=null)
{
    xmlHttp = getRequestObject() ;
    if (xmlHttp) {        
  try {
        var url = "../cgi-bin/project1/"+a+".py" ;
        var data = "designated_dostawca=" + encodeURIComponent(c) ;
        xmlHttp.onreadystatechange = function(){wstaw_liste(a,b);} ;
        xmlHttp.open("POST", url,false);
        xmlHttp.setRequestHeader("Content-Type","application/x-www-form-urlencoded") ;
        xmlHttp.send(data);
 
      }
      catch (e) {
        alert ("Nie mozna polaczyc sie z serwerem: " + e.toString()) ;
      }
    } else {
      alert ("Blad") ;
    }
}
function pobierz_liste_more(a,b,c)//chyba mozna bez tego
{
    xmlHttp = getRequestObject() ;
    if (xmlHttp) {        
  try {
        var url = "../cgi-bin/project1/"+a+".py" ;
        var data = "designated_dostawca=" + encodeURIComponent(c) ;
        xmlHttp.onreadystatechange = function(){wstaw_liste(a,b);} ;
        xmlHttp.open("GET", url,true);
        xmlHttp.setRequestHeader("Content-Type","application/x-www-form-urlencoded") ;
        xmlHttp.send(data);
      }
      catch (e) {
        alert ("Nie mozna polaczyc sie z serwerem: " + e.toString()) ;
      }
    } else {
      alert ("Blad") ;
    }
}
function wstaw_liste(a,b)   {
    myDiv = document.getElementById(a);
    if (xmlHttp.readyState == 4) {
         if ( xmlHttp.status == 200 )  {
            $(".all").fadeOut();
             response = xmlHttp.response;
             myDiv.innerHTML += response;
             $(b).fadeIn();

         }
    }  
}
//------------------------------------------------------------------


