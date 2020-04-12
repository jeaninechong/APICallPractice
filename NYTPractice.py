import requests
import requests_cache
import json

requests_cache.install_cache()


def getArticlesforMonthYear(month, year):
    dict = {}
    strmonth = month.__str__()
    stryear = year.__str__()
    url = 'https://api.nytimes.com/svc/archive/v1/' + stryear + '/' + strmonth + '.json'
    params = {
        'api-key': 'REDACTED'
    }
    r = requests.get(url, params=params).json()
    length = len(r['response']['docs'])

    i = 0
    while i < length:
        keywordArray = []
        j = 0
        headline = json.dumps(r['response']['docs'][i]['headline']['main'], sort_keys=True, indent=4)
        lenkeywords = len(r['response']['docs'][i]['keywords'])
        while j < lenkeywords:
            keywordArray.append(json.dumps(r['response']['docs'][i]['keywords'][j]['value'], sort_keys=True, indent=4).lower())
            j += 1
        keywordArray.sort()
        dict[i] = {'headline': headline, 'keywords': keywordArray}
        print(dict[i]['keywords'])
        i += 1

    return dict

def returnArticlesFromPeriod(begYear, begMonth, endYear, endMonth):
    return 0

testDict = getArticlesforMonthYear(11, 2009)

