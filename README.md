Animal Information Fetcher

This project fetches animal information from the API-Ninjas API and generates an HTML page with the details.

Installation

Clone the repository.
Navigate to the project directory.
Install the required dependencies: pip install requests python-dotenv.
Create a .env file in the root directory and add your API key: API_KEY=your_api_key_here.
Usage

Run the script: python script_name.py.
Enter the name of the animal when prompted.
The script will fetch the animal data and generate an HTML file named animals.html with the information.
Functions

load_html(file_name): Load HTML content from a file.
write_html(html, file_name): Write HTML content to a file.
serialize_animal(animal): Convert an animal dictionary to HTML format.
generate_html(animals_data, template_html): Generate the full HTML for all animals.
fetch_animal_data(request_url): Fetch animal data from the API.
main(): Main function to fetch animal data and generate HTML.
Contributing

Contributions are welcome! Please follow these steps:

Fork the repository.
Create a new branch: git checkout -b feature-branch.
Make your changes.
Commit your changes: git commit -am 'Add new feature'.
Push to the branch: git push origin feature-branch.
Create a new Pull Request.
