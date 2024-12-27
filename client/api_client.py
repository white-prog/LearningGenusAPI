import requests

def capital_first(value):
    return value[0].upper() + value[1:].lower()

def get_species_in_genus(genus):
    try:
        url = f"http://127.0.0.1:5000/species/{genus}"
        response = requests.get(url)
        response.raise_for_status()
        resp = response.json()
        if "error" in resp.keys():
            return [False,resp["error"]]
        return [True,resp["species"]]

    except:
        print(f"Error fetching species")
        return None

def main():
    while True:
        genus = capital_first(input("Enter genus name: "))
        if len(genus) == None:
            print("No input got")
        else:
            species_list = get_species_in_genus(genus)
            if species_list[0] == False:
                print(species_list[1])
            elif species_list[0] == True:
                print(f"Species in {genus}: ")
                for species in species_list[1]:
                    print(f"- {species}")
        back = input("Enter 'E' to exit: ")
        if back == 'E':
            break
        







if __name__ == "__main__":
    main()

