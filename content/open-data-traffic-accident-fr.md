Title: Open Data et carte des accidents de la route
Date: 2012-03-29 23:36
Category: Open Data
Tags: open-data, leaflet, python
Slug: open-data-traffic-accident
Author: Christophe Augier
lang: fr

L'[Open Data][1] ou les « Données Ouvertes » : une idée magnifique, rendre les
données publiques pour que tout un chacun puisse y accéder. Mais voilà derrière
cette idée honorable reste-t-il encore à créer les outils pour trier, recouper
et visualiser les données pertinentes sur un sujet.

C’est dans cette optique que j’ai voulu voir ce que mettait à disposition le
site de l’état : [data.gouv.fr][2]. Premier constat le site est ouvert depuis
quelques mois seulement et il y a déjà un grand nombre de jeux de données
disponibles. Pourtant en regardant de plus près on se rend compte que ces
données sont souvent déjà synthétisées au lieu de fournir des chiffres ou
résultats d’analyse bruts. Parfois même, les données sont hébergées sur le site
internet  du « producteur » et l’url pour y accéder est erronée.

Prenons par exemple le cas du [Rapport sur les programmes de surveillance 2010 –
Loire Bretagne][6]. L’url est incorrect, mais on peu en s’inscrivant sur le site
poser des questions sur le jeu de données. J’ai donc rapporté le problème mais
ce genre de problème risque de devenir embêtant si ces erreurs sont trop
fréquentes (ici une bonne partie de ces rapports sont inaccessibles) ou bien
lorsque l’on souhaite utiliser rapidement le service.

En attendant j’ai trouvé un jeu de données très intéressant : [Informations sur
la localisation des accidents corporels de la circulation sur 5 années –
France-Métropolitaine][7]. J’ai développé un script python pour extraire ces données
et les formater afin de pouvoir les afficher sur une carte via [Leaflet][3]. Plus
d’infos et la carte [ici][4], le tout sous licence [CC][5].

![Exemple sur le Morbihan]({filename}/images/opendata_map_traffic_accident.png)

J’ajouterai pour finir que bien que certains jeux de données sont uniquement
disponibles sous la forme de fichiers au format propriétaire la plupart du temps
ils sont accessibles sous forme de .csv ou .xml ou .ods. Il y a donc il
semblerait une réelle volonté d’utiliser des outils libres en plus de rendre les
données libres :-)

[1]: http://en.wikipedia.org/wiki/Open_data
[2]: http://www.data.gouv.fr
[3]: http://leaflet.cloudmade.com
[4]: http://tytouf.github.io/traffic-accident-map
[5]: http://creativecommons.org/licenses/by/3.0
[6]: https://www.data.gouv.fr/donnees/view/rapport-sur-les-programmes-de-surveillance-2010---Loire-Bretagne-30382042?xtmc=undefined&xtcr=2
[7]: http://www.data.gouv.fr/donnees/view/Informations-sur-la-localisation-des-accidents-corporels--de-la-circulation-sur-5-ann%C3%A9es---France-M%C3%A9-30379821?xtmc=accidents+corporels+circulation&xtcr=1
