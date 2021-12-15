import os.path
import urllib.request
import PySimpleGUI as sg
import requests
from PIL import Image


def check_for_placeholder():
    placeholder_url = "https://ichef.bbci.co.uk/news/976/cpsprodpb/118B3/production/_117595817_hi059908781.jpg"
    if not os.path.exists("placeholder.png"):
        urllib.request.urlretrieve(placeholder_url, "placeholder.png")
        resize_placeholder = Image.open('placeholder.png')
        resize_placeholder.thumbnail((100, 100))
        resize_placeholder.save('placeholder.png')
def update_text():
    window['pg_bar'].update(3)
    window['a1_img'].update("temp.png")
    window['a2'].update("Success? = True")
    window['a3'].update("Lowest price sold 7 days = " + "$" + result_array["lowest_price"])
    window['a4'].update("Average price 7 weeks = " + "$" + result_array["average_price"])
    window['a5'].update("Highest price sold 7 days = " + "$" + result_array["highest_price"])
    window['a6'].update("Median Price = " + "$" + result_array["median_price"])
    window['a7'].update("Volume over 7 days = " + result_array["amount_sold"]+ "x")
    window['pg_bar'].update(4)
    window['pg_bar'].update(visible = False)
def resize_img():
    urllib.request.urlretrieve(result_array["icon"], "temp.png")
    img_resize = Image.open("temp.png")
    img_resize.thumbnail((100, 100))
    img_resize.save("temp.png")
check_for_placeholder()
sg.theme('DarkAmber')
layout = [
    [sg.Image("placeholder.png", size = (100, 100), key = 'a1_img')],
    [sg.ProgressBar(4,visible = False, style = "vista", size = (9,8), key = "pg_bar")],
    [sg.Text("Success? = ", key = 'a2')],
    [sg.Text("Lowest price sold 7 days = ", key = 'a3'), sg.Text("Average price 7 days = ", key = 'a4'),
     sg.Text("Highest price sold 7 days = ", key = 'a5')],
    [sg.Text("Median Price over 7 days = ", key = 'a6'), sg.Text("Volume over 7 days = ", key = 'a7')],
    [sg.Text('Manually input item')],
    [sg.InputText('Operation%20Riptide%20Case', size = (100, 1), key = 'input_name')],
    [sg.Submit(button_text = "CHECK", key = 'CHECK1', size = (35, 1)), sg.Button('EXIT', size = (35, 1)),
     sg.Text('Made by Kiil, Contact on discord: kiiloo#0420')]
    ]
window = sg.Window("ItemFinder", layout, resizable = False, margins = (20, 20))
while True:
    event, values = window.read()

    if event == 'CHECK1':
        window['pg_bar'].update(visible = True)
        window['pg_bar'].update(1)
        name_of_item = values['input_name']
        find_json = requests.get(
            "http://csgobackpack.net/api/GetItemPrice/?currency=USD&id=" + name_of_item + '&time=7&icon=1'
            )
        fjson = find_json.json()
        result = fjson['success']
        window['pg_bar'].update(2)
        if result == 'false':
            sg.Popup('Error')
        else:
            result_array = fjson
            resize_img()
            update_text()


    if event == "EXIT" or event == sg.WIN_CLOSED:
        break

window.close()
