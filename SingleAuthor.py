import kivy
import ScanningNames
import csv
import os
import kivy
import ScanningNames
import csv
import os
import Pasring.ParsingAuthor

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.properties import StringProperty

authorLayout = Builder.load_file("singleAuthorPanel.kv")
infoAboutAuthorLayout = Builder.load_file("infoAboutAuthorLayout.kv")

infoAboutAuthorLayout = infoAboutAuthorLayout

class ProgramApp(App):
    def build(self):
        mainLayout = BoxLayout()
        mainLayout.add_widget(authorLayout)
        with open("./data.csv", encoding='utf-8') as r_file:
            # Создаем объект DictReader, указываем символ-разделитель ","
            file_reader = csv.DictReader(r_file)
            # Считывание данных из CSV файла
            count = 0
            for row in file_reader:
                if row['name'] == 'Марк Твен':
                    if count > 5:
                        break
                    count += 1
                    info = 'Имя: ' + row['name']
                    if row['careers']:
                        info += '\n' + 'Род деятельности: ' + ', '.join(row['careers'].split(','))
                    if row['date_of_birthday']:
                        info += '\n' + 'Дата рождения: ' + row['date_of_birthday']
                    if row['languages']:
                        info += '\n' + 'Языки произведений: ' + ', '.join(row['languages'].split(','))
                    if row['genres']:
                        info += '\n' + 'Жанры: ' + ', '.join(row['genres'].split(','))
                    lbl = Label(text=info)
                    infoAboutAuthorLayout.add_widget(lbl)
        mainLayout.add_widget(infoAboutAuthorLayout)
        return mainLayout


if __name__ == "__main__":
    ProgramApp().run()