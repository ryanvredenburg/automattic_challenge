### Bonus Points Round 1:  
-  Guessed which city each color represents on the map 
### Bonus Points Round 2:
- Guessed which city EVERY dot represents on the map
### Bonus Points Round 3:
- Modified the map to display city names for each point as they are placed

# Bonus Points Round: 1
To guess which city each color represents on the map, I checked the source of the web page and found the following:

```sh
dcss["dfw"] = new Array(255,255,255); //	#FFFFFF White
dcss["dca"] = new Array(240,163,255); // 	#F0A3FF	Amethyst
dcss["lax"] = new Array(0,117,220); // 	#0075DC Blue
dcss["ord"] = new Array(153,63,0); // 	#993F00	Caramel
dcss["sjc"] = new Array(76,0,92); // 	#4C005C	Damson
dcss["UND"] = new Array(25,25,25); // 	#191919	Ebony - too hard to see on black bg
dcss["mxp"] = new Array(0,92,49); // 	#005C31	Forest
dcss["nrt"] = new Array(43,206,72); // 	#2BCE48	Green
dcss["arn"] = new Array(255,204,153); // 	#FFCC99	Honeydew
dcss["atl"] = new Array(128,128,128); // 	#808080	Iron
dcss["jnb"] = new Array(148,255,181); // 	#94FFB5	Jade
dcss["sea"] = new Array(143,124,0); // 	#8F7C00	Khaki
dcss["bur"] = new Array(157,204,0); // 	#9DCC00	Lime
dcss["ams"] = new Array(194,0,136); // 	#C20088	Mallow
dcss["ewr"] = new Array(0,51,128); // 	#003380	Navy
dcss["sat"] = new Array(255,164,5); // 	#FFA405	Orpiment
dcss["hkg"] = new Array(255,168,187); // 	#FFA8BB	Pink
dcss["syd"] = new Array(66,102,0); // 	#426600	Quagmire
dcss["lhr"] = new Array(255,0,16); // 	#FF0010	Red
dcss["fra"] = new Array(94,241,242); // 	#5EF1F2	Sky
dcss["den"] = new Array(0,153,143); // 	#00998F	Turquoise
dcss["mad"] = new Array(224,255,102); // 	#E0FF66	Uranium
dcss["kix"] = new Array(116,10,255); // 	#740AFF	Violet
dcss["cdg"] = new Array(153,0,0); // 	#990000	Wine
dcss["vie"] = new Array(255,255,128); // 	#FFFF80	Xanthin
dcss["mia"] = new Array(255,255,0); // 	#FFFF00	Yellow
dcss["gru"] = new Array(255,80,5); // 	#FF5005	Zinnia
dcss["bom"] = new Array(191,255,0); // 	#BFFF00	Light Lime
dcss["tpe"] = new Array(220,20,60); // 	#DC143C	Crimson
dcss["yyz"] = new Array(255,127,80); // #FF7F50	Coral
dcss["sin"] = new Array(252,15,192); // #FC0FC0 Hot Pink
```

Recognizing that these were major serving IAT airport codes I looked them up. I thought about writing a python script to look them up for me, but decided there weren't enough items to justify it for a one off script. However, I thought it would be much more interesting to determine the city for EVERY dot on the map and how far away from the Automattic HQ it was. 

|City|Color|
| ------ | ------ |
|Dallas|#FFFFFF White|
|Washington D.C.| #F0A3FFAmethyst|
|Los Anageles| #0075DC Blue|
|Chicago| #993F00Caramel|
|San Jose| #4C005CDamson|
|Grand Forks| #191919Ebony - too hard to see on black bg|
|Milan| #005C31Forest|
|Tokyo| #2BCE48Green|
|Stockholm| #FFCC99Honeydew|
|Atlanta| #808080Iron|
|Johannesburg| #94FFB5Jade|
|Seattle| #8F7C00Khaki|
|Holleywood Burbank| #9DCC00Lime|
|Amsterdam| #C20088Mallow|
|Newark| #003380Navy|
|San Antonio| #FFA405Orpiment|
|Hong Kong| #FFA8BBPink|
|Sydney| #426600Quagmire|
|London| #FF0010Red|
|Frankfurt| #5EF1F2Sky|
|Denver| #00998FTurquoise|
|Madrid| #E0FF66Uranium|
|Kansai| #740AFFViolet|
|Paris| #990000Wine|
|Vienna| #FFFF80Xanthin|
|Miami| #FFFF00Yellow|
|São Paulo| #FF5005Zinnia|
|Mumbai| #BFFF00Light Lime|
|Taipei| #DC143CCrimson|
|Toronto| #FF7F50Coral|
|Singapore| #FC0FC0 Hot Pink|


# Bonus Points Round: 2

Using a python script and Google's Geocode API, I made a json request for the data sources the original map was using. I calculated the distance of every point on the map back to Automattic HQ. I also found the city name of nearly every point on the map (unfortunately the geocode API didn't have answers for everything). You can see that script [dotToCity.py] and the resulting output [cities.txt] . 


# Bonus Points Round: 3

Because text results weren't that exciting, I modified the code of the original map to list the city names. Dots were being added so quickly that I also added a scrolling "history" of the last 4 cities added in addition to the current city. That modification can be seen live here: [map]


   [dotToCity.py]: <https://github.com/ryanvredenburg/automattic_challenge/tree/master/dotToCity.py>
   [cities.txt]: <https://github.com/ryanvredenburg/automattic_challenge/tree/master/cities.txt>
   [map]: <https://ryanvredenburg.github.io/automattic_challenge/map.html>

   
