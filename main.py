from nicegui import ui
import attributes

class Character:
    def __init__(self, name : str, age : int, gender : str, race : str, profession : str, traits : list[str]):
        self.name = name
        self.age = age
        self.gender = gender
        self.race = race
        self.profession = profession
        self.traits = traits

random_character = Character("", 0, "", "", "", [])

def generate_character():
    random_character = Character("", 0, "", "", "", [])
    random_character.name = attributes.get_random_name()
    random_character.age = attributes.get_random_age()
    random_character.traits.append(attributes.get_random_trait())
    random_character.traits.append(attributes.get_random_trait())

    name_label.text = random_character.name
    age_label.text = random_character.age

    traits = ""
    for trait in random_character.traits:
        traits += trait + ", "

    trait_label.text = traits

with ui.column().classes("self-center items-center"):
    ui.html('Karaktärskaparen 3000', tag='h1').classes("text-2xl")
    ui.button('Skapa Karaktär', on_click=lambda: generate_character())

    with ui.grid(columns=2).classes("w-full"):
        ui.label("Namn:").classes("font-bold")
        name_label = ui.label()

        ui.label("Ålder:").classes("font-bold")
        age_label = ui.label()

        ui.label("Egenskaper:").classes("font-bold")
        trait_label = ui.label()

dark = ui.dark_mode()
dark.enable()

ui.colors(dark_page="#181c21")
ui.run(native=True)
