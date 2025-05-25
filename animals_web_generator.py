import json

def load_data(file_name):
    with open(file_name, 'r') as fileobj :
        return json.load(fileobj)



def main():
    print("Hello from zootopia!")
    animals_data = load_data('animals_data.json')
    print(animals_data)
    for animal in animals_data:
        print(f"Name: {animal['name']}")

        if 'diet' in animal['characteristics']:
            print(f"Diet: {animal['characteristics']['diet']}")

        if 'locations' in animal and animal['locations']:
            print(f"Location: {animal['locations'][0]}")

        if 'type' in animal['characteristics']:
            print(f"Type: {animal['characteristics']['type']}")

        print()


if __name__ == "__main__":
    main()
