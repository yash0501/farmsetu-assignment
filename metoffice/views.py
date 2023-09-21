from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from requests import get
from .models import Combination, APIData
from django.core.serializers import serialize
import json
from .serializers import APIDataSerializer
from django.db.models import Min, Max

# Create your views here.


@csrf_exempt
@api_view(['GET'])
def index(request):
    return HttpResponse("Hello, world. You're at the metoffice index.")


@api_view(['GET'])
def get_weather(request):
    parameter = request.GET.get('parameter', 'Tmin')
    state = request.GET.get('state', 'England')

    # if not present, then fetch data from metoffice website and store in Combination table
    # else fetch data from Combination table

    params = [
        'Tmin',
        'Tmax',
        'Tmean',
        'Sunshine',
        'Rainfall',
        'Raindays1mm',
        'AirFrost'
    ]

    states = [
        'UK',
        'England',
        'Wales',
        'Scotland',
        'Northern_Ireland',
        'England_and_Wales',
        'England_N',
        'England_S',
        'Scotland_N',
        'Scotland_E',
        'Scotland_W',
        'England_E_and_NE',
        'England_NW_and_N_Wales',
        'Midlands',
        'East_Anglia',
        'England_SW_and_S_Wales',
        'England_SE_and_Central_S'
    ]

    if parameter not in params:
        print(params)
        return HttpResponse('Invalid parameter')

    if state not in states:
        print(state)
        return HttpResponse('Invalid state')

    # check if params and state are present in Combination table or not

    combination = Combination.objects.filter(parameter=parameter, state=state)

    if len(combination) == 0:
        # fetch data from metoffice website and store in APIData table

        url = 'https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/' +            parameter + '/date/' + state + '.txt'
        response = get(url)

        data = response.text.split('\n')[7:-2]

        api_data_list = []

        for row in data:
            row_data = row.split()
            # convert row_data to float
            for i in range(1, len(row_data)):
                if row_data[i] == '---':
                    row_data[i] = None
                row_data[i] = float(row_data[i])

            api_data = APIData(parameter=parameter, state=state, year=row_data[0], jan=row_data[1], feb=row_data[2], mar=row_data[3], apr=row_data[4], may=row_data[5], jun=row_data[6], jul=row_data[7], aug=row_data[8], sep=row_data[9], oct=row_data[10], nov=row_data[11], dec=row_data[12], win=row_data[13], spr=row_data[14], sum=row_data[15], aut=row_data[16], ann=row_data[17])
            api_data_list.append(api_data)

        APIData.objects.bulk_create(api_data_list)

        add_combination = Combination.objects.create(
            parameter=parameter, state=state)
        add_combination.save()

    # fetch data from APIData table
    fetched_data = APIData.objects.filter(parameter=parameter, state=state)
    serialized_data = APIDataSerializer(fetched_data, many=True)

    # coldest annual mean year
    coldest_annual_mean_year = APIData.objects.filter(
        parameter=parameter, state=state).order_by('ann').first()

    # hottest annual mean year
    hottest_annual_mean_year = APIData.objects.filter(
        parameter=parameter, state=state).order_by('-ann').first()

    if parameter == 'Tmin' or parameter == 'Tmax' or parameter == 'Tmean':
        result = {
            'coldest_annual_mean': coldest_annual_mean_year.ann,
            'coldest_annual_mean_year': coldest_annual_mean_year.year,
            'hottest_annual_mean': hottest_annual_mean_year.ann,
            'hottest_annual_mean_year': hottest_annual_mean_year.year,
            'data': serialized_data.data
        }
    elif parameter == 'Sunshine':
        result = {
            'sunniest_annual_mean': hottest_annual_mean_year.ann,
            'sunniest_annual_mean_year': hottest_annual_mean_year.year,
            'data': serialized_data.data
        }
    elif parameter == 'Rainfall':
        result = {
            'rainiest_annual_mean': hottest_annual_mean_year.ann,
            'rainiest_annual_mean_year': hottest_annual_mean_year.year,
            'least_rainiest_annual_mean': coldest_annual_mean_year.ann,
            'least_rainiest_annual_mean_year': coldest_annual_mean_year.year,
            'data': serialized_data.data
        }
    elif parameter == 'Raindays1mm':
        result = {
            'rainiest_annual_mean': hottest_annual_mean_year.ann,
            'rainiest_annual_mean_year': hottest_annual_mean_year.year,
            'least_rainiest_annual_mean': coldest_annual_mean_year.ann,
            'least_rainiest_annual_mean_year': coldest_annual_mean_year.year,
            'data': serialized_data.data
        }
    elif parameter == 'AirFrost':
        result = {
            'least_airfrost_annual_mean': coldest_annual_mean_year.ann,
            'least_airfrost_annual_mean_year': coldest_annual_mean_year.year,
            'data': serialized_data.data
        }
    else:
        result = {}

    return JsonResponse(result, safe=False)
