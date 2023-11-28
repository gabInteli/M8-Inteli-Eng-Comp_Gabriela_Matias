from langchain.llms import Ollama
from langchain.schema import AIMessage, HumanMessage
import gradio as gr
import requests
import json

def chatLLM(prompt):
    url = "http://localhost:11434/api/generate" 
    post = {
        "model":"safety_guard",
        "prompt":prompt,
        "stream":False
    }
    response = requests.post(url, json=post)

    # Check the status code of the response
    if response.status_code == 200:
        print("Pergunta Enviada com Sucesso !")
        response_dict = vars(response)
        response_dict['_content'] = json.loads(response_dict["_content"].decode('utf-8'))
        print(response_dict['_content']['response'])
        return response_dict['_content']['response']
    
    else:
        print("POST request failed. Status code:", response.status_code)

with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()

    def respond(message, chat_history):
        answer = chatLLM(message)
        chat_history.append((message, answer))
        return "", chat_history

    msg.submit(respond, [msg, chatbot], [msg, chatbot])

demo.launch()