import PySimpleGUIWeb as psg


def gui_attributes():
    optionRace = ["American Indian", "Asian", "Black", "Hispanic", "White"]
    optionGender = ["Male", "Female", "Other"]

    # Options inside gui
    layout = [
        [psg.Text("Race"), psg.Combo(optionRace)],
        [psg.Text("Gender"), psg.Combo(optionGender)],
        [psg.Text("History knowledge:     "), psg.Slider(range=(0, 100), orientation='h', resolution=5, key="HistorySlider", enable_events=True),
         psg.Text('', key='historyValue')],
        [psg.Text("Film knowledge:  "), psg.Slider(range=(0, 100), orientation='h', resolution=5, key="FilmSlider", enable_events=True),
         psg.Text('', key='filmValue')],
        [psg.Text("Sport knowledge: "), psg.Slider(range=(0, 100), orientation='h', resolution=5, key="SportsSlider", enable_events=True),
         psg.Text('', key='sportsValue')],
         [psg.Text('Progress: ', key='progressValue')],
        [psg.Button("Done")]
        ]

    window = psg.Window("Attribute Questions", layout)

    inputs = []

    add = 0
    event, values = window.read()
    values['HistorySlider'] = 0
    values['FilmSlider'] = 0
    values['SportsSlider'] = 0
    while True:
        event, values = window.read()

        window['historyValue'].Update(value=values['HistorySlider'])
        window['filmValue'].Update(value=values['FilmSlider'])
        window['sportsValue'].Update(value=values['SportsSlider'])
        add = int(values["HistorySlider"]) + int(values["FilmSlider"]) + int(values["SportsSlider"])
        window['progressValue'].Update(value=("Total: " + str(add) + "%"))

        if event in (None, "Done"):  # only activates once done or exit is pressed
            if add == 100:
                for i in values:
                    inputs.append(values[i])
                break

    window.close()

    return inputs



