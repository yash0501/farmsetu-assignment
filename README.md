# farmsetu-assignment

Base URL : https://farmsetu-assignment.vercel.app

Working example : https://farmsetu-assignment.vercel.app/metoffice/get_weather/?parameter=Raindays1mm&state=UK

To access the api, make a get request to the deployed link and pass on the parameter, i.e., the value to be checked and the state, i.e. the location of that data.

Available parameters:

- Tmin
- Tmax
- Tmean
- Rainfall
- Sunshine
- Raindays1mm

The data provided as a result in the api is given such that first I have created a few functions which provide a good amount of idea about how parameters are changing with time at a particular location.
These include highest and lowest value of that parameter and when did it occur.
The main data is avalable as a json with the format as given below in example:

```json
"1884": [ // year
"2.7", // jan
"1.4", // feb
"1.8", // mar
"2.2", // apr
"5.0", // may
"7.9", // jun
"10.3", // jul
"10.5", // aug
"9.0", // sep
"4.9", // oct
"1.8", // nov
"0.9", // dec
"---", // winter
"3.01", // spring
"9.59", // summer
"5.24", // autumn
"4.88" // annual
],
```
