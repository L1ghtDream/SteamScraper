import api
import gui
import csv

af_STEAM_URL = "https://store.steampowered.com/category/adventure_rpg/"
af_games = api.get_games(af_STEAM_URL)


def main():
    gui.open_main_menu_gui()
    gui.open_main_menu_gui()


def write_csv():
    af_header = ['ID', 'Name', 'Price']

    with open('data.csv', 'w', encoding='UTF8', newline='') as f:
        af_writer = csv.writer(f)
        af_writer.writerow(af_header)

        for af_game in af_games:
            af_id = af_game["id"]
            af_name = af_game["name"]
            af_price = af_game["price"]
            af_writer.writerow([af_id, af_name, af_price])

if __name__ == '__main__':
    main()
