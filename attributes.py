import random

traits = [
    # Intellectual traits
    ["Analytisk", "Skarpsinnig", "Logisk", "Lärd", "Uppfinningsrik", "Disträ",
     "Strategisk", "Klurig", "Vis", "Snabbtänkt", "Förutseende", "Teknisk"],

    # Personality traits
    ["Vänlig", "Känslig", "Modig", "Generös", "Empatisk", "Mystisk", "Naiv",
     "Stolt", "Lojal", "Svekfull", "Manipulativ", "Hemlighetsfull"],

    # Emotional traits
    ["Lättretlig", "Tålamodig", "Passionerad", "Oberörd", "Kylig", "Impulsiv",
     "Försiktig", "Temperamentsfull", "Ödmjuk", "Självsäker", "Oförutsägbar",
     "Dramatisk"],

    # Physical traits
    ["Uthållig", "Smidig", "Stark", "Svag", "Snabb", "Trög", "Klumpig", "Elegant",
     "Vig", "Skadad (t.ex. blind på ett öga)"],

    # Social traits
    ["Karismatisk", "Övertygande", "Charmig", "Tystlåten", "Respektlös", "Högljudd",
     "Tillbakadragen", "Skämtsam", "Sarkastisk", "Snäll", "Skrämmande", "Respektingivande"],

    # Moral traits
    ["Ädel", "Självisk", "Rättvis", "Oärlig", "Girig", "Hämndlysten", "Medlidsam",
     "Tveksam", "Opportunistisk", "Disciplinerad", "Anarkistisk", "Pragmatisk"],

    # Supernatural traits
    ["Kan se framtiden", "Har en förbannelse över sig", "Är odödlig", "Kan tala med djur",
     "Kan förändra sitt utseende", "Läser andras tankar", "Kan kontrollera eld/vatten/jord/luft",
     "Har en magisk artefakt", "Har en demonisk sida", "Kan återuppstå efter att ha dött"]
]

# Lista med förnamn
first_names = [
    "Elias", "Anna", "Johannes", "Sofia", "Liam", "Emma", "Oskar", "Elin", "Hugo", "Maja", 
    "William", "Isabelle", "Lucas", "Alice", "Noah", "Julia", "Alfred", "Clara", "Max", "Greta", 
    "Felix", "Frida", "Axel", "Lily", "Sigrid", "Oliver"
]

# Lista med efternamn
last_names = [
    "Thornfield", "Johansson", "Andersson", "Lundberg", "Svensson", "Karlsson", "Nilsson", 
    "Olsson", "Persson", "Bergström", "Jönsson", "Pettersson", "Fransson", "Berg", "Larsson", 
    "Mårtensson", "Eriksson", "Hansson", "Gustafsson", "Jonasson"
]

def get_random_trait():
    random_trait_list = random.choice(traits)
    return random.choice(random_trait_list)

def get_random_name():
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    return f"{first_name} {last_name}"


def get_random_age():
    return random.randint(1, 100)
