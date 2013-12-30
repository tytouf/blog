Title: Open Data and a map of traffic accident (France)
Date: 2012-03-29 23:36
Category: Open Data
Tags: open-data, leaflet, python
Slug: open-data-traffic-accident
Author: Christophe Augier
lang: en

[Open Data][1] is a beautiful idea: make data public and available to anyone. Yet
while this idea is very honorable, without tools to sort, cross-reference, match
and visualize data it loses its meaning.

With this in my mind I went to see what kind of datasets and tools where
published on [data.gouv.fr][2], a website opened recently by the French government.
I found some interesting dataset related to traffic accident and decided to work
on a map to display the localization of the accidents. I developed a python
script to extract the data from the ODS files and format them  so that I can
display them on a map rendered using [Leaflet][3]. More details (sorry in French) and
the map [here][4], the tools are licensed under the [Creative Commons][5].

[1]: http://en.wikipedia.org/wiki/Open_data
[2]: http://www.data.gouv.fr
[3]: http://leaflet.cloudmade.com
[4]: http://opendata.tytouf.fr
[5]: http://creativecommons.org/licenses/by/3.0
