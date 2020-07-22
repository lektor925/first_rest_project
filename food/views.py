import requests
from django.http import Http404

# Create your views here.
from django.views.generic import TemplateView
from rest_framework.decorators import api_view
from rest_framework.response import Response


def get_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()


foodboxes = get_data('https://stepik.org/media/attachments/course/73594/foodboxes.json')
recipients = get_data('https://stepik.org/media/attachments/course/73594/recipients.json')


class MainView(TemplateView):
    template_name = 'food/index.html'


@api_view(http_method_names=['GET'])
def food_boxes_list(request):
    result = []

    if request.query_params:
        min_price = request.query_params.get('min_price')
        min_weight = request.query_params.get('min_weight')

        if min_price:
            for foodbox in foodboxes:
                if int(foodbox['price']) >= int(min_price):
                    result.append(foodbox)
        elif min_weight:
            for foodbox in foodboxes:
                if int(foodbox['weight_grams']) >= int(min_weight):
                    result.append(foodbox)
        else:
            raise Http404

    else:
        result = foodboxes

    return Response(result)


@api_view(http_method_names=['GET'])
def food_boxes_detail(request, pk):
    response = None

    for foodbox in foodboxes:
        if foodbox['inner_id'] == int(pk):
            response = foodbox

    if response:
        return Response(response)
    else:
        raise Http404


@api_view(http_method_names=['GET'])
def recipients_list(request):
    return Response(recipients)


@api_view(http_method_names=['GET'])
def recipient_detail(request, pk):
    if int(pk) <= len(recipients):
        return Response(recipients[int(pk)])
    else:
        raise Http404
