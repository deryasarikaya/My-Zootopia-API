import json


def load_data(file_path):
    """Load animal data from a JSON file."""
    with open(file_path, "r") as handle:
        return json.load(handle)


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
    """Generate animals.html from the animal data and HTML template."""
    animals_data = load_data("animals_data.json")

    with open("animals_template.html", "r") as file:
        html_template = file.read()

    output = ""

    for animal in animals_data:
        output += serialize_animal(animal)

    new_html = html_template.replace("__REPLACE_ANIMALS_INFO__", output)

    with open("animals.html", "w") as file:
        file.write(new_html)


if __name__ == "__main__":
    main()