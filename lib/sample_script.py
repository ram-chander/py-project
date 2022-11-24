import requests
import json

BASE_URL="https://storecare.crm-nightly-new.cc.capillarytech.com/"
def getUrl():
    url=BASE_URL+"add/deviceHeartbeat"
    return url

def getHeaders():
    headers={
        'Content-Type':'application/json',
        'Authorization': 'Basic Y3B2LnRpbGw6MjAyY2I5NjJhYzU5MDc1Yjk2NGIwNzE1MmQyMzRiNzA='
    }
    return headers

def getParams():
    return None

def getBody():
    sample_json=json.dumps({
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
    return sample_json

def sample_request():
    url=getUrl()
    headers=getHeaders()
    params=getParams()
    payload=getBody()
    print(url,headers,params,payload)
    response = requests.post(url, headers=headers, data=payload)
    print(response)
    print(response.status_code)
    print(response.text)
    # print(json.loads(response.text))
    return response.text

if __name__ == '__main__':
    sample_request()