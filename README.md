# farmsetu-assignment

Working example : https://web-production-169d6.up.railway.app/metoffice/get_weather/?parameter=Tmax&state=UK

To access the api, make a get request to the deployed link and pass on the parameter, i.e., the value to be checked and the state, i.e. the location of that data.

Available parameters:

- Tmin
- Tmax
- Tmean
- Rainfall
- Sunshine
- Raindays1mm
- Airfrost

The data provided as a result in the api is given such that first I have created a few functions which provide a good amount of idea about how parameters are changing with time at a particular location.
These include highest and lowest value of that parameter and when did it occur.
The main data is avalable as a json with the format as given below in example:

```json
{
"id": 139,
"parameter": "Tmax",
"state": "UK",
"year": 1885,
"jan": 4.3,
"feb": 7.3,
"mar": 7.2,
"apr": 10.8,
"may": 11.8,
"jun": 17,
"jul": 19.4,
"aug": 16.8,
"sep": 15,
"oct": 9.3,
"nov": 7.5,
"dec": 5.9,
"win": 5.75,
"spr": 9.91,
"sum": 17.76,
"aut": 10.58,
"ann": 11.04
},
```
