import data_fetcher


def serialize_animal(animal):
    """Convert one animal dictionary into an HTML card."""
    output = ""
    output += '<li class="cards__item">\n'

    if "name" in animal:
        output += f'<div class="card__title">{animal["name"]}</div>\n'

    output += '<p class="card__text">\n'

    if "characteristics" in animal:
        characteristics = animal["characteristics"]

        if "diet" in characteristics:
            output += f'<strong>Diet:</strong> {characteristics["diet"]}<br/>\n'

        if "locations" in animal and animal["locations"]:
            output += f'<strong>Location:</strong> {animal["locations"][0]}<br/>\n'

        if "type" in characteristics:
            output += f'<strong>Type:</strong> {characteristics["type"]}<br/>\n'

    output += "</p>\n"
    output += "</li>\n"

    return output


def main():
    """Generate animals.html using data from the API."""

    animal_name = input("Enter a name of an animal: ")
    animals_data = data_fetcher.fetch_data(animal_name)

    with open("animals_template.html", "r") as file:
        html_template = file.read()

    if len(animals_data) == 0:
        output = f'<h2 style="color:deeppink; font-size:60px; text-align:center;">The animal "{animal_name}" doesn\'t exist.</h2>'
    else:
        output = ""

        for animal in animals_data:
            output += serialize_animal(animal)

    new_html = html_template.replace("__REPLACE_ANIMALS_INFO__", output)

    with open("animals.html", "w") as file:
        file.write(new_html)

    print("Website was successfully generated to the file animals.html.")

if __name__ == "__main__":
    main()