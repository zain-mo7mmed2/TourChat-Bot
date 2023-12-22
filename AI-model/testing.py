import openai
from colorama import Fore
from dotenv import load_dotenv
import os
load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

def chat_with_model(user_input, conversation, chatbot):
    conversation.append({"role": "user", "content": user_input})
    messages_input = conversation.copy()
    messages_input.insert(0, {"role": "system", "content": chatbot})

    completion = openai.ChatCompletion.create(
        model='ft:gpt-3.5-turbo-0613:personal::8Y5Vj6oL',
        messages=messages_input,
        temperature=0.7,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    chat_response = completion['choices'][0]['message']['content']

    conversation.append({"role": "assistant", "content": chat_response})

    # Print the chatbot's response in color
    print_colored("ChatBot1", chat_response)

    return chat_response

# Function to print text in color
def print_colored(agent, text):
    agent_colors = {
        "User": Fore.GREEN,
        "ChatBot1": Fore.CYAN,
    }
    colored_text = agent_colors.get(agent, Fore.RESET) + text + Fore.RESET
    print(colored_text)

conversation = []
tour_prompt = "You are a helpful assistant and a skilled trip advisor experienced in planning trips and providing details for tourists to enhance their experience. You possess knowledge about famous places, traditional food in each city, and the optimal times to visit. so provide me or us the specific times, places, and detailed recommendations for things I should do during my trip"
chat_response = chat_with_model(tour_prompt, conversation, "")

# Start the chat loop
while True:
    user_input = input("User: ").strip()
    if user_input.lower() in ("exit", "quit", "stop"):
        print("ChatBot1: Goodbye!")
        break
    chat_response = chat_with_model(user_input, conversation, chat_response)



