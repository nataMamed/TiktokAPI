import requests
import json


class TiktokAPI:

    def __init__(self, token) -> None:
        self.token = token


    def fetch_data(self, json_description:dict):

        headers = {
        'Access-Token': self.token,
        'Content-Type': 'application/json'
        }
        url = "https://business-api.tiktok.com/open_api/v1.2/reports/integrated/get"

        payload = json.dumps(json_description)
        response = requests.request("GET", url, headers=headers, data=payload)

        return response.json()['data']['list']



if __name__=="__main__":
    from datetime import datetime, timedelta

    yesterday  = datetime.now().date() - timedelta(days=1)
    start_date = yesterday - timedelta(days=30)
    token = ''
    api = TiktokAPI(token=token)

    payload = {
    "advertiser_id": '',
    "service_type": "AUCTION",
    "report_type": "BASIC",
    "data_level": "AUCTION_CAMPAIGN",
    "dimensions": [
        "campaign_id",
        "stat_time_day"
    ],
    "metrics": [
        "campaign_name",
        "clicks",
        "spend",
        "conversion",
        "impressions"
    ],
    "start_date": start_date.strftime('%Y-%m-%d'),
    "end_date": yesterday.strftime('%Y-%m-%d'),
    "page": 1,
    "page_size": 200
    }

    result= api.fetch_data(json_description=payload)
        

