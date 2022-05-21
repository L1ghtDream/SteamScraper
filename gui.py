import copy

import PySimpleGUI as gui

import main

af_default_layout = [
    [
        gui.Button("Back to Main Menu"),
        gui.Button("Exit")
    ],
]


def open_main_menu_gui():
    af_layout = [
        [
            gui.Button("Retrieve Data"),
            gui.Button("Create Graph"),
            gui.Button("Display Matrix"),
            gui.Button("Save to Excel File"),
            gui.Button("Exit")
        ]
    ]

    af_window = gui.Window("Technologies for e-Business", af_layout, size=(900, 500))

    while True:
        af_event, af_values = af_window.read()
        if af_event == "Retrieve Data":
            af_window.close()
            open_games_list_gui()
            break
        if af_event == "Create Graph":
            af_window.close()
            open_graph_gui()
            break
        if af_event == "Display Matrix":
            af_window.close()
            open_matrix_gui()
            break
        if af_event == "Save to Excel File":
            af_window.close()
            main.write_csv()
            break
        if af_event == "Exit" or af_event == gui.WIN_CLOSED:
            af_window.close()
            break


def open_games_list_gui():
    af_layout = copy.deepcopy(af_default_layout)

    af_column_layout = []

    for af_game in main.af_games:
        af_id = af_game["id"]
        af_name = af_game["name"]
        af_price = af_game["price"]

        af_column_layout.append([gui.Text(f"Game '{af_name}' ({af_id}) = {af_price}")])

    af_layout.append(
        [gui.Column(af_column_layout, scrollable=True, vertical_scroll_only=True, size=(900, 500))]
    )

    af_window = gui.Window("Technologies for e-Business", af_layout, size=(900, 500))
    while True:
        af_event, af_values = af_window.read()
        if af_event == "Back to Main Menu":
            af_window.close()
            open_main_menu_gui()
            break
        if af_event == "Exit" or af_event == gui.WIN_CLOSED:
            af_window.close()
            break


def open_graph_gui():
    af_layout = copy.deepcopy(af_default_layout)

    af_BAR_WIDTH = 8
    af_BAR_SPACING = 9
    af_EDGE_OFFSET = 3
    af_GRAPH_SIZE = (900, 500)
    af_DATA_SIZE = (900, 500)
    af_bcols = ['blue', 'red', 'green']

    af_graph = gui.Graph(af_GRAPH_SIZE, (0, 0), af_DATA_SIZE)

    af_layout.append(
        [af_graph],
    )

    af_window = gui.Window("Technologies for e-Business", af_layout, size=(900, 500))

    af_window.Finalize()

    af_games_sorted = main.af_games
    af_games_sorted.sort(key=sort_games)

    for i in range(len(af_games_sorted)):
        af_game = af_games_sorted[i]

        af_price = af_game["price"]

        try:
            af_price_no_format = round(float(af_price.replace("€", "").replace(",", ".")))
        except:
            af_price_no_format = 0

        af_price_no_format += 9

        af_graph.draw_rectangle(top_left=(i * af_BAR_SPACING + af_EDGE_OFFSET, af_price_no_format * 6),
                                bottom_right=(i * af_BAR_SPACING + af_EDGE_OFFSET + af_BAR_WIDTH, 0),
                                fill_color=af_bcols[i % 3])

    while True:
        af_event, af_values = af_window.read()
        if af_event == "Back to Main Menu":
            af_window.close()
            open_main_menu_gui()
            break
        if af_event == "Exit" or af_event == gui.WIN_CLOSED:
            af_window.close()
            break


def sort_games(af_game):
    af_price = af_game["price"]
    try:
        af_price_no_format = round(float(af_price.replace("€", "").replace(",", ".")))
    except:
        af_price_no_format = 0
    return af_price_no_format


def open_matrix_gui():
    af_data = []

    for af_game in main.af_games:
        af_id = af_game["id"]
        af_name = af_game["name"]
        af_price = af_game["price"]
        af_data.append(
            [af_id, af_name, af_price]
        )

    af_headings = ['ID', 'Name', 'Price']

    af_layout = copy.deepcopy(af_default_layout)

    # noinspection PyTypeChecker
    af_layout.append([
        [
            gui.Table(
                values=af_data,
                headings=af_headings,
                max_col_width=50,
                auto_size_columns=True,
                justification='right',
                num_rows=10,
                key='-TABLE-',
                row_height=35,
            )
        ]
    ])

    af_window = gui.Window("Technologies for e-Business", af_layout, size=(900, 500))
    while True:
        af_event, af_values = af_window.read()
        if af_event == "Back to Main Menu":
            af_window.close()
            open_main_menu_gui()
            break
        if af_event == "Exit" or af_event == gui.WIN_CLOSED:
            af_window.close()
            break
