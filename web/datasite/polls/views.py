from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from pymongo import MongoClient


def index(request):
    connection_string = "mongodb://user1:1528@52.78.23.245/train"
    client = MongoClient(connection_string)

    db_handle = client['train']
    collection_name = db_handle['train']

    train1 = {
        "medicine_id": "RR000123456",
        "common_name": "Paracetamol",
        "scientific_name": "",
        "available": "Y",
        "category": "fever"
    }
    train2 = {
        "medicine_id": "RR000123456",
        "common_name": "Paracetamol",
        "scientific_name": "",
        "available": "Y",
        "category": "fever"
    }

    collection_name.insert_many([train1, train2])
    count = collection_name.count()

    names = ''
    med_details = collection_name.find({})
    for r in med_details:
        names = r["common_name"]

    return HttpResponse("Hello, world. You're at the polls index. count : " + str(count) + ", names : " + names)
