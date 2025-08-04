import requests
import random

# figured out these APIs work pretty well
fact_apis = {
    "random": "https://uselessfacts.jsph.pl/random.json?language=en",
    "cats": "https://catfact.ninja/fact", 
    "numbers": "http://numbersapi.com/random?json",
    "advice": "https://api.adviceslip.com/advice"
}

def get_fact(api_type):
    url = fact_apis[api_type]
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            
            # each API has different json structure, had to figure this out
            if api_type == "random":
                return data['text']
            elif api_type == "cats": 
                return data['fact']
            elif api_type == "numbers":
                return data['text']
            elif api_type == "advice":
                return data['slip']['advice']
        else:
            return "couldn't get fact right now"
            
    except:
        return "something went wrong with the API call"

def main():
    print("Random Facts from Different APIs")
    print("Press enter for random fact, or type category (random/cats/numbers/advice)")
    
    while True:
        choice = input("\n> ").strip().lower()
        
        if choice == 'quit' or choice == 'q':
            break
            
        if choice == '' or choice not in fact_apis:
            # pick random API if they just hit enter or invalid choice
            api_choice = random.choice(list(fact_apis.keys()))
            print(f"Getting {api_choice} fact...")
        else:
            api_choice = choice
            
        fact = get_fact(api_choice)
        print(f"\n{fact}")

if __name__ == "__main__":
    main()