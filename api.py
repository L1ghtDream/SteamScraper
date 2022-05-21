import json

import requests

"""
Gets a steam game ID and returns its 
"""


def get_steam_price(id):
    af_response = requests.get(f"https://store.steampowered.com/api/appdetails?filters=price_overview&appids={id}")
    af_data = af_response.json()[id]
    return af_data["data"]["price_overview"]["final_formatted"]


"""
Get a stram url and returns a list of all the games on the page with their ids, names and prices
"""


def get_games(url):
    af_response = requests.get(url)
    af_raw_data = af_response.text
    af_upper_cut = af_raw_data.split("GStoreItemData.AddStoreItemDataSet( ")[1]
    af_lower_cut = af_upper_cut.split(" );")[0]

    af_data = json.loads(af_lower_cut)["rgApps"]
    af_output = []

    for af_id in af_data.keys():
        af_game = {}
        af_game["id"] = af_id
        af_game["name"] = af_data[af_id]["name"]

        try:
            af_price_upper_cut = af_data[af_id]["discount_block"].split("class=\"discount_final_price\">")[1]
            af_price_lower_cut = af_price_upper_cut.split("</div>")[0]
            af_game["price"] = af_price_lower_cut
        except:
            af_game["price"] = "Not Released"
        af_output.append(af_game)

    return af_output
