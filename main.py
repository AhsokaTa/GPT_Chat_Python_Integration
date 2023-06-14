
import openai
from config import API_KEY, MAX_TOKENS, N, TEMPERATURE
 
def gpt3_response(question):

    openai.api_key =API_KEY

    response = openai.Completion.create(
                                        engine = "text-davinci-003",
                                        prompt = question,
                                        max_tokens = MAX_TOKENS,
                                        n = N,
                                        stop = None,
                                        temperature = TEMPERATURE)
    
    return response.choices[0].text.strip() 

while True:

    input_text = input("\nIntroduce una pregunta: (exit para salir)  ")
    if input_text.lower() == "exit":
        break
    answer = gpt3_response(input_text)
    print(answer)