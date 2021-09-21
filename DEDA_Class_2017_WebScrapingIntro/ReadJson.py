"""
Description:
 - A simple demo to get json data from website by using json module

Usage: Executing this whole file in your IDE or from Terminal or executing line by line in iPython.

Author:
 - Junjie Hu, hujunjie@hu-berlin.de
 - Cathy Chen
Last modified date: 19-11-2017
"""

import requests
import json
import pprint

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    'Cookie': '_ntpc-x=a593a9ea-d199-4c25-954c-cc7265ca2499; __guid=167362475.-59793255998206210000.1632233217285.984; _ga=GA1.3.100058167.1632233218; _gid=GA1.3.251159113.1632233218; TS01232bc6=012479d1bf843e39162d2ab3a224a945ebc3c9661977965b80139bc877c5fa8e95d09d83081b979a322a38d8698a95fd1050f7f3a3bb3b862fcb1b2b0232483c091f7880d8; monitor_count=18',
    'Host': 'data.ntpc.gov.tw'
}
headers2 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
}

url = 'https://data.ntpc.gov.tw/api/datasets/71CD1490-A2DF-4198-BEF1-318479775E8A/json?page=0&size=100'
url2 = 'https://www.baidu.com'
response = requests.get(url2, headers=headers2)
print('niubi')
content = response.content
json_tree = json.loads(content)
pprint.pprint(json_tree)

for bike_rent_records in json_tree["result"]["records"]:
    leftRatio = float(bike_rent_records["sbi"]) / float(bike_rent_records["tot"]) * 100
    print("ID:{0} Left:{2:0.1f}% Name:{1}".format(bike_rent_records["sno"], bike_rent_records["aren"], leftRatio))
