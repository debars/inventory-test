# project/tests/test_add_result.py

import requests
import datetime
from statistics import mean, stdev

def _add_result(count=9999):
    url = "http://localhost:8001/result/"
    data = {
        "resultType": count,
        "time": datetime.datetime.now().isoformat(),
        "probePort": count,
        "probeName": f"myProbeName_{count}",
        "probeId": f"myProbeId_{count}",
        "probeSerialNum": f"myProbeSerialNum_{count}",
        "config_id": 1,
        "calTimestamp": datetime.datetime.now().isoformat(),
        "probeParameter": 1000+count,
        "verifyMargin": 0.1234+count,
        "verifyStatus": count,
        "calStatus": count,
        "calType": count,
        "calNumStd": count,
        "username": f"User1_{count}",
        "sampleName": f"Sample1_{count}",
        "location": f"Timbuktu_{count}",
        "notes": f"noteshereandthere_{count}",
    }

    response = requests.post(url=url, json=data)
    assert response.status_code == 201
    result = response.json()

    url = "http://localhost:8001/float/"
    data = {
        "value": 0.321+count,
        "precisionType": count,
        "precision": count,
        "unitId": count,
        "formId": count,
        "result_id": result["id"],
        "standard": count,
        "ordinal": count,
    }
    response = requests.post(url=url, json=data)
    assert response.status_code == 201

    url = "http://localhost:8001/message/"
    data = {
        "messageType": count,
        "message": f"abcdefghijklmnopqrstuvwxyz_{count}",
        "result_id": result["id"],
        "ordinal": count,
    }
    response = requests.post(url=url, json=data)
    assert response.status_code == 201

    url = "http://localhost:8001/pt2pt/"
    data = {
        "slope": 0.5+count,
        "slopeUnits": count,
        "offset": count,
        "offsetUnits": count,
        "result_id": result["id"],
        "ordinal": count,
    }
    response = requests.post(url=url, json=data)
    assert response.status_code == 201


def test_add_result_100():
    url = "http://localhost:8001/measurement/100"
    response = requests.get(url=url)
    print(response.json())
    assert response.status_code == 201


def test_add_result_1000():
    url = "http://localhost:8001/measurement/1000"
    response = requests.get(url=url)
    print(response.json())
    assert response.status_code == 201

