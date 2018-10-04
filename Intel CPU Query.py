import requests
import json


def cpuinfo(pNumber):
    """"Deze functie accepteerd 1 parameter; namelijk het nummer van de processor.
    Met dit nummer wordt de API request klaargemaakt voor de query. A.d.h.v. de query krijgt
    het programma daarna een JSON file terug met daarin """ # AANVULLEN!

    # Maakt de URL klaar voor de query, in combinatie met de input "pNumber"
    api_url = 'https://odata.intel.com/API/v1_0/Products/Processors()?&$select=CoreCount,ClockSpeedMhz,' \
              'ClockSpeedMaxMhz,ThreadCount,BornOnDate,ProductName&$filter=ProcessorNumber%20eq%20%27{}' \
              '%27&$format=json'.format(pNumber)

    # Voert de query uit met de requests module en slaat de output op in "response"
    response = requests.get(api_url)

    # Schrijft de output weg naar "output.json" voor de leesbaarheid. Heeft (nog) geen toegevoegde waarde.
    with open('output.json', 'w') as APIoutput:
        APIoutput.write(json.dumps(json.loads(response.text), indent=4, sort_keys=True))

    # Door middel van een Try - Except block wordt er gecheckt of het processornummer bekend is bij Intel.
    # Indien de processor niet bekend is wordt er via de exception "IndexError" een foutmelding gegeven, omdat
    # er dan geen list in het geheugen staat geschreven a.d.h.v. de output.
    while True:
        try:
            data = json.loads(response.text)
            corecount = '{} {}'.format("Corecount: ",
                                       data['d'][0]['CoreCount'])
            threadcount = '{} {}'.format("Threadcount: ",
                                         data['d'][0]['ThreadCount'])
            clockspeedmhz = '{} {}'.format("Clockspeed MHz: ",
                                         data['d'][0]['ClockSpeedMhz'])
            clockspeedmaxmhz = '{} {}'.format("Max Clockspeed MHz: ",
                                         data['d'][0]['ClockSpeedMaxMhz'])
            launchdate = '{} {}'.format("Launchdate: ",
                                        data['d'][0]['BornOnDate'])
            productname = '{} {}'.format("Productname: ",
                                         data['d'][0]['ProductName'])
            print('{}\n{}\n{}\n{}\n{}\n{}'.format(corecount, threadcount, clockspeedmhz, clockspeedmaxmhz,
                                                  launchdate, productname))

            break   # Hier stopt het Try block.

        except IndexError:
            print('Deze processor is niet bekend bij ons')

            break   # Hier stopt het Except block.


cpuinfo("i5-8400")  # Geef hier een CPU model op (c.q. i5-8400)
