import requests

url = "https://uselessfacts.jsph.pl/random.json?language=en"

def get_random_tech_fact():
    response=requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"Did you know? {data['text']}")

    else:
        print("Failed to retrieve a fact. Please try again later.")

while True:
    user_input = input("press 'Enter' to get a random tech fact or type 'q' to quit: ")
    if user_input.lower() == 'q':
      print("Goodbye!")
    break
            
get_random_tech_fact()