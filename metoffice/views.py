from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from requests import get

# Create your views here.


@csrf_exempt
@api_view(['GET'])
def index(request):
    return HttpResponse("Hello, world. You're at the metoffice index.")


@api_view(['GET'])
def get_weather(request):
    params = request.GET.get('parameter', 'Tmin')
    state = request.GET.get('state', 'England')
    url = 'https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/' + \
        params + '/date/' + state + '.txt'
    # data = get(
    #     'https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Tmin/date/England.txt')
    data = get(url)

    lines = data.text.splitlines()

    headers = lines[5].split()

    key = []

    values = []
    for i in range(6, len(lines)-1):
        values.append(lines[i].split())

    data = {}
    for i in range(len(values)):
        data[int(values[i][0])] = values[i][1:]

    sum_50 = 0
    sum = 0
    for i in range(50):
        sum_50 += float(data[2022-i][16])

    for i in range(len(values)):
        sum += float(data[2022-i][16])

    print(sum_50/50)
    print(sum/len(values))

    coldest_annual_mean = 9999
    coldest_annual_mean_year = 0
    for i in range(len(values)):
        if float(data[2022-i][16]) < coldest_annual_mean:
            coldest_annual_mean = float(data[2022-i][16])
            coldest_annual_mean_year = 2022-i

    print(coldest_annual_mean)
    print(coldest_annual_mean_year)

    hottest_annual_mean = -100
    hottest_annual_mean_year = 0
    for i in range(len(values)):
        if float(data[2022-i][16]) > hottest_annual_mean:
            hottest_annual_mean = float(data[2022-i][16])
            hottest_annual_mean_year = 2022-i

    print(hottest_annual_mean)
    print(hottest_annual_mean_year)

    # count number of years where annual mean temperature was more than that of their previous year in last 50 years
    count = 0
    for i in range(1, 51):
        if float(data[2022-i][16]) > float(data[2022-i-1][16]):
            count += 1

    print(count)

    # coldest month of entire dataset
    coldest_month_temp = 9999
    coldest_month_year = 0
    coldest_month_month = 0

    for i in range(len(values)):
        for j in range(0, 12):
            # print(float(data[2022-i][j]))
            if float(data[2022-i][j]) < coldest_month_temp:
                coldest_month_temp = float(data[2022-i][j])
                coldest_month_year = 2022-i
                coldest_month_month = j

    print(coldest_month_temp)
    print(coldest_month_year)
    print(coldest_month_month)

    # hottest month of entire dataset
    hottest_month_temp = -100
    hottest_month_year = 0
    hottest_month_month = 0

    for i in range(len(values)):
        for j in range(0, 12):
            # print(float(data[2022-i][j]))
            if float(data[2022-i][j]) > hottest_month_temp:
                hottest_month_temp = float(data[2022-i][j])
                hottest_month_year = 2022-i
                hottest_month_month = j

    print(hottest_month_temp)
    print(hottest_month_year)
    print(hottest_month_month)

    # count number of years where annual mean temperature was more than that of their previous year in last 50 years

    if params == 'Tmin' or params == 'Tmax' or params == 'Tmean':
        result = {
            'coldest_annual_mean': coldest_annual_mean,
            'coldest_annual_mean_year': coldest_annual_mean_year,
            'hottest_annual_mean': hottest_annual_mean,
            'hottest_annual_mean_year': hottest_annual_mean_year,
            'mean_temp_more_than_previous_50': count,
            'coldest_month_temp': coldest_month_temp,
            'coldest_month_year': coldest_month_year,
            'coldest_month_month': coldest_month_month,
            'hottest_month_temp': hottest_month_temp,
            'hottest_month_year': hottest_month_year,
            'hottest_month_month': hottest_month_month,
            'data': data
        }
    elif params == 'Sunshine':
        result = {
            'sunniest_annual_mean': hottest_annual_mean,
            'sunniest_annual_mean_year': hottest_annual_mean_year,
            'sunniest_month_value': hottest_month_temp,
            'sunniest_month_year': hottest_month_year,
            'sunniest_month_month': hottest_month_month,
            'least_sunniest_annual_mean': coldest_annual_mean,
            'least_sunniest_annual_mean_year': coldest_annual_mean_year,
            'least_sunniest_month_value': coldest_month_temp,
            'least_sunniest_month_year': coldest_month_year,
            'least_sunniest_month_month': coldest_month_month,
            'data': data
        }
    elif params == 'Rainfall':
        result = {
            'rainiest_annual_mean': hottest_annual_mean,
            'rainiest_annual_mean_year': hottest_annual_mean_year,
            'rainiest_month_value': hottest_month_temp,
            'rainiest_month_year': hottest_month_year,
            'rainiest_month_month': hottest_month_month,
            'least_rainiest_annual_mean': coldest_annual_mean,
            'least_rainiest_annual_mean_year': coldest_annual_mean_year,
            'least_rainiest_month_value': coldest_month_temp,
            'least_rainiest_month_year': coldest_month_year,
            'least_rainiest_month_month': coldest_month_month,
            'data': data
        }
    elif params == 'Raindays1mm':
        result = {
            'rainiest_annual_mean': hottest_annual_mean,
            'rainiest_annual_mean_year': hottest_annual_mean_year,
            'rainiest_month_value': hottest_month_temp,
            'rainiest_month_year': hottest_month_year,
            'rainiest_month_month': hottest_month_month,
            'least_rainiest_annual_mean': coldest_annual_mean,
            'least_rainiest_annual_mean_year': coldest_annual_mean_year,
            'least_rainiest_month_value': coldest_month_temp,
            'least_rainiest_month_year': coldest_month_year,
            'least_rainiest_month_month': coldest_month_month,
            'data': data
        }
    elif params == 'AirFrost':
        result = {
            'least_airfrost_annual_mean': coldest_annual_mean,
            'least_airfrost_annual_mean_year': coldest_annual_mean_year,
            'least_airfrost_month_value': coldest_month_temp,
            'least_airfrost_month_year': coldest_month_year,
            'least_airfrost_month_month': coldest_month_month,
            'data': data
        }

    return JsonResponse(result)
