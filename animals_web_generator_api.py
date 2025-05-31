import requests
import json
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access the API key
api_key = os.getenv('API_KEY')
url = 'https://api.api-ninjas.com/v1/animals?name='
headers = {'X-Api-Key': api_key}

def load_html(file_name):
    """
    Load HTML content from a file.

    Args:
        file_name (str): The name of the file to load.

    Returns:
        str: The content of the file.
    """
    with open(file_name, 'r', encoding='utf-8') as fileobj:
        return fileobj.read()

def write_html(html, file_name):
    """
    Write HTML content to a file.

    Args:
        html (str): The HTML content to write.
        file_name (str): The name of the file to write to.
    """
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(html)

def serialize_animal(animal):
    """
    Convert an animal dictionary to HTML format.

    Args:
        animal (dict): The animal data.

    Returns:
        str: The HTML representation of the animal.
    """
    html = '<li class="cards__item">\n'
    html += f'  <div class="card__title">{animal["name"]}</div>\n'
    html += '  <p class="card__text">\n'

    characteristics = animal.get('characteristics', {})
    if 'diet' in characteristics:
        html += f'      <strong>Diet:</strong> {characteristics["diet"]}<br/>\n'

    if 'locations' in animal and animal['locations']:
        html += f'      <strong>Location:</strong> {animal["locations"][0]}<br/>\n'

    if 'type' in characteristics:
        html += f'      <strong>Type:</strong> {characteristics["type"]}<br/>\n'

    html += '  </p>\n'
    html += '</li>\n'
    return html

def generate_html(animals_data, template_html):
    """
    Generate the full HTML for all animals.

    Args:
        animals_data (list): A list of animal data.
        template_html (str): The HTML template to use.

    Returns:
        str: The full HTML content with animal data inserted.
    """
    output = ""
    for animal in animals_data:
        output += serialize_animal(animal)

    return template_html.replace("__REPLACE_ANIMALS_INFO__", output)

def fetch_animal_data(request_url):
    """
    Fetch animal data from the API.

    Args:
        request_url (str): The URL to fetch data from.

    Returns:
        list: A list of animal data.
    """
    response = requests.get(request_url, headers=headers)
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response.json()

def main():
    """
    Main function to fetch animal data and generate HTML.
    """
    print("Hello from zootopia!")
    user_input = input("Add name of animal to get information: ")
    request_url = url + user_input

    try:
        animals_data = fetch_animal_data(request_url)
        if len(animals_data) <= 0:
            write_html("Animal data currently not available", "animals.html")
            return

        animals_html = load_html('animals_template.html')
        final_output = generate_html(animals_data, animals_html)
        write_html(final_output, "animals.html")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
