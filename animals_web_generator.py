import json

def load_data(file_name):
    with open(file_name, 'r') as fileobj :
        return json.load(fileobj)

def load_html(file_name):
    with open(file_name, 'r', encoding='utf-8') as fileobj :
        return fileobj.read()

def write_html(html, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        # Write the content to the file
        file.write(html)


def main():
    print("Hello from zootopia!")
    animals_data = load_data('animals_data.json')
    animals_html = load_html('animals_template.html')
    print(animals_html)
    #print(animals_data)

    output = ""
    for animal in animals_data:
        output += '<li class="cards__item">\n'
        output += f'  <div class="card__title">{animal["name"]}</div>\n'
        output += '  <p class="card__text">\n'

        if 'diet' in animal['characteristics']:
            output += f'      <strong>Diet:</strong> {animal["characteristics"]["diet"]}<br/>\n'

        if 'locations' in animal and animal['locations']:
            output += f'      <strong>Location:</strong> {animal["locations"][0]}<br/>\n'

        if 'type' in animal['characteristics']:
            output += f'      <strong>Type:</strong> {animal["characteristics"]["type"]}<br/>\n'

        output += '  </p>\n'
        output += '</li>\n'

    #print(output)
    final_output = animals_html.replace("__REPLACE_ANIMALS_INFO__", output)
    #print(final_output)
    write_html(final_output, "animals.html")


if __name__ == "__main__":
    main()
