import openai
from colorama import Fore
import os

openai.api_key = '-------------> Our API Key <-------------'

# Function to interact with the chatbot model
def chat_with_model(user_input, conversation, chatbot):
    print("User : ", end=""),
    print_colored('User', user_input)
    conversation.append({"role": "user", "content": user_input})
    messages_input = conversation.copy()
    messages_input.insert(0, {"role": "system", "content": chatbot})

    completion = openai.chat.completions.create(
        model='-------------> MODEL TOKEN <-------------',
        messages=messages_input,
        temperature=0.7,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    chat_response = completion.choices[0].message.content.strip()

    conversation.append({"role": "assistant", "content": chat_response})

    # Print the chatbot's response in color
    print("TourChat : ", end=""),
    print_colored('ChatBot', chat_response)

    return chat_response

# Function to print text in color
def print_colored(agent, text):
    agent_colors = {
        "User": Fore.GREEN,
        "ChatBot": Fore.CYAN,
    }
    colored_text = agent_colors.get(agent, Fore.RESET) + text + Fore.RESET
    print(colored_text)

conversation = []
chatbot_prompt = "You are a helpful assistant and a skilled trip advisor experienced in planning trips and providing details for tourists to enhance their experience. You possess knowledge about famous places, traditional food in each city, and the optimal times to visit. so provide me or us the specific times, places, and detailed recommendations for things I should do during my trip"
