import random

def greet():
    responses = ["Hello", "Hi there", "Welcome to an automated chatbot", "Welcome",
                 "Bienvenido", "Bonjur", "Ciao", "What's up?"]
    return random.choice(responses)

# Initialize conversation context
conversation_context = None
conversation_context_fact = None

def respond(message):
    global conversation_context
    global conversation_context_fact
    # list of facts  
    facts = [
        "The Great Wall of China is not a single continuous wall but a series of interconnected walls and fortifications built over centuries by various Chinese dynasties.",
        "Octopuses have three hearts. Two hearts pump blood to the gills, while the third heart pumps oxygenated blood to the rest of the body.",
        "The world's largest living organism is not a whale or an elephant but a fungus called Armillaria ostoyae, also known as the 'humongous fungus'. It covers an area of over 2,385 acres in Oregon's Malheur National Forest",
        "The deepest part of the ocean is the Mariana Trench, located in the western Pacific Ocean. Its deepest point, called the Challenger Deep, reaches a depth of about 36,070 feet (10,994 meters).",
        "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible.",
        "The probability of shuffling a deck of cards into an order that has never existed before in the history of the universe is virtually guaranteed. The number of possible combinations is approximately 8 x 10^67.",
        "The Eiffel Tower can be 15 cm taller during the summer due to thermal expansion. Metals expand when heated, causing the iron structure of the tower to expand slightly in warmer temperatures.",
        "The first computer virus was created in 1983 and was called the 'Elk Cloner.' It infected Apple II computers via floppy disks and displayed a poem to users after every 50th boot.",
        "The largest volcano in the solar system is Olympus Mons, located on Mars. It stands about 13.6 miles (22 kilometers) high, making it nearly three times the height of Mount Everest.",
        "The shortest war in history lasted only 38 minutes. It was the Anglo-Zanzibar War, which took place on August 27, 1896, between the United Kingdom and the Sultanate of Zanzibar.",
    ]
    # List of jokes
    jokes = [
        "Why did the chicken cross the road? To get to the other side faster",
        "What do you call a cow with no legs? Ground Beef.",
        "What did one ocean say to the other ocean? Nothing, they just waved at each other.",
        "What do you call a fake spaghetti? An impasta.",
        "Why don't scientists trust atoms? Because atoms always make up everything.",
        "Why couldn't the bicycle stand up by itself? It was two-tired.",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why don't skeletons fight each other? They don't have the guts.",
    ]
    
    # Check for greetings
    greetings = ["hello", "hi", "hey"]
    if any(greeting in message.lower() for greeting in greetings):
        conversation_context = "greeting"
        return "Hello! How can I help you?"
    
    # Check if user is continuing previous topic for jokes
    if conversation_context == "joke":
        if any(word in message.lower() for word in ["yes", "sure", "why not"]):
            return random.choice(jokes)
        elif any(word in message.lower() for word in ["that's funny", "oh wow", "haha", "nice"]):
            return "Do you want to hear another joke?"
        elif "no" in message.lower():
            conversation_context = None
            return "Okay, maybe next time!"
        else:
            return "I'm sorry, I didn't understand. Do you want to hear another joke?"
    
    if conversation_context_fact == "fact":
        if any(word in message.lower() for word in ["yes", "sure", "why not"]):
            return random.choice(facts)
        elif any(word in message.lower() for word in ["that's cool", "oh wow", "amazing", "nice", "impressive", "cool", "wow"]):
            return "Do you want to hear another fact?"
        elif "no" in message.lower():
            conversation_context_fact = None
            return "Okay, maybe next time!"
        else:
            return "I'm sorry, I didn't understand. Do you want to hear another fact?"
    


    # Simple responses based on keywords
    if "how are you" in message.lower():
        return "I'm good, thank you!"
    elif "name" in message.lower():
        return "I'm just a simple chatbot. What's yours?"
    elif "weather" in message.lower():
        return "I'm not sure about the weather. You might want to check a weather website."
    elif "joke" in message.lower():
        conversation_context = "joke"
        return random.choice(jokes)
    elif "thank you" in message.lower() or "thanks" in message.lower():
        return "You're welcome!"
    elif "fact" in message.lower():
        conversation_context_fact = "fact"
        return random.choice(facts)
    else:
        return "Sorry, I didn't understand that."
    
def main():
    print("Bot: " + greet())
    while True:
        user_input = input("You: ")
        if user_input == ("bye"):
            print("Bot: Goodbye!")
            break
        response = respond(user_input)

        print("Bot: " + response)


if __name__ == "__main__":
    main()
