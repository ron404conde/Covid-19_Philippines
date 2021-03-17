import json
from urllib.request import urlopen

def get_covid_cases():
    with urlopen("https://api.apify.com/v2/key-value-stores/lFItbkoNDXKeSWBBA/records/LATEST?disableRedirect=true") as response:
        source = response.read()
        data = json.loads(source)

        print("Country: ", json.dumps(data['country']))
        print("Infected: ", json.dumps(data['infected']))
        print("Tested: ", json.dumps(data['tested']))
        print("Recovered: ", json.dumps(data['recovered']))
        print("Deaths: ", json.dumps(data['deceased']))
        print("Active Cases: ", json.dumps(data['activeCases']))

# call
# main call
if __name__ == "__main__":
    get_covid_cases()