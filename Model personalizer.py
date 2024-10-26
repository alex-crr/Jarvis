import ollama

'''model = "llama3.1:8b"
modeldetail = ollama.show(model)
modelfile_content = modeldetail['modelfile']
with open('mymodel.modelfile', "w") as f:
    f.write(modelfile_content)'''
    
with open('Jarvis.modelfile', 'r', encoding="utf-8") as f:
    model_file= f.read()
    
response = ollama.create(model='Jarvis', modelfile = model_file)
print(response)