import requests
import json


input_data =  {"body": ["The sky is blue and beautiful.",
                  "Love this blue and beautiful sky!",
                  "The quick brown fox jumps over the lazy dog.",
                  "A king's breakfast has sausages, ham, bacon, eggs, toast and beans",
                  "I love green eggs, ham, sausages and bacon!",
                  "The brown fox is quick and the blue dog is lazy!",
                  "The sky is very blue and the sky is very beautiful today",
                  "The dog is lazy but the brown fox is quick!"    
            ]
        }


url = " "

r = requests.post(url, json=input_data)
print("result without securely key: ", r.json())















