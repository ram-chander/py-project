import sys
sys.path.append("../")
from lib.sample_script import *
# from unittest.mock import MagicMock

def test_getUrl():
    url = getUrl()
    assert url=="https://storecare.crm-nightly-new.cc.capillarytech.com/add/deviceHeartbeat"

def test_getHeaders():
    headers=getHeaders()
    correctHeaders={
        'Content-Type':'application/json',
        'Authorization': 'Basic Y3B2LnRpbGw6MjAyY2I5NjJhYzU5MDc1Yjk2NGIwNzE1MmQyMzRiNzA='
    }
    #we cannot compare the headers, we have ensure it has all the keys required atleast
    assert json.dumps(headers,sort_keys=True) == json.dumps(correctHeaders,sort_keys=True)

def test_getParams():
    params = getParams()
    assert params == None

def test_getBody():
    body=getBody()
    correctBody=json.dumps({
            "orgId": "783",
            "tillId": "15000375",
            "zoneId": "15000380",
            "storeId": "15001861",
            "source": "till",
            "tillName": "kn.0034",
            "storeName": "KNIGHT_STOER_SERVER",
            "timestamp": 1531825994198,
            "configs": [
                {
                    "key": "ffc_setup",
                    "deviceId": 202481602221173,
                    "deviceName": "",
                    "heartbeat": 1531825631788,
                    "lastEventTime": 1531825746768,
                    "ffcRunningStatus": "Running",
                    "cpuUsage": "279.0",
                    "diskSpaceLeft": "2.0G",
                    "temperature": "79C",
                    "memoryUsage": {
                        "vailable": "587",
                        "used": "179",
                        "free": "67"
                    }
                }
            ]
        })
    assert body == correctBody


def test_sample_request(mocker):
    mocker.patch('lib.sample_script.getUrl',return_value="randomurl")
    mocker.patch('lib.sample_script.getHeaders',return_value={"randomheaders":"random"})
    mocker.patch('lib.sample_script.getParams',return_value="randomparams")
    mocker.patch('lib.sample_script.getBody',return_value=json.dumps({"randombody":"random"}))
    mock_requests = mocker.patch('lib.sample_script.requests.post')
    mock_requests.return_value.ok = True
    mock_requests.return_value.status_code=200
    mock_requests.return_value.text="sampleresponse"

    response = sample_request()
    mock_requests.assert_called_with("randomurl",headers={"randomheaders":"random"},data=json.dumps({"randombody":"random"}))
    assert response == "sampleresponse"