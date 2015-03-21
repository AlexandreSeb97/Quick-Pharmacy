from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
	text="""<!DOCTYPE html>
		 <html>
		 <head>
			<meta charset="utf-8"/>
			<title>Bienvenue sur PharmaOnline</title>
			<link rel="stylesheet" type="text/css" href="base.css" />
		 </head>
		 <body>
			<h1>QuickPharma</h1>
			<form method="GET" action={% url "page2.html" %} accept-charset="UTF-8">
			<input type="text" placeholder="Besoin d'un medicament?" name="search_entry" />
			<br>
			<input type="submit" value="recherche" />
			</form>

		 <p id="para1">Bonjour et bienvenue sur pharmaOnline !
		 Ce site a été créé pour aider les gens dans le besoin à trouver les medicaments et les pharmacies
		 qui vendent ces medicaments. Cependant pour certains de ces medicaments il vous faudra une recommendation
		 d'un medecin.
		 </p> 

		 </body>

		 </html>"""
	return HttpResponse(text)
def resultats(request):
	text="""<!DOCTYPE html>
		 <html>
		 <head>
			<meta charset="utf-8"/>
			<title> Resultats de la recherche</title>
			<link rel="stylesheet" type="text/css" href="base.css" />
		 </head>
		 <body>
			<h1 id="one"> QuickPharma </h1>
			<p><Dans cette page vous retrouverez les resultats de votre recherche</p>
		</body>
		</html>"""
	return HttpResponse(text)