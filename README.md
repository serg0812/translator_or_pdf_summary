# translator_or_pdf_summary
Load pdf, and then query, translate or do whatever you want

you will need the following libraries installed:
-pickle
-langchain
-numpy
-flask
-flask_cors
-openai

Dont forget to put you OPENAI_API_KEY as env var

load your pdf file into pdf directory

run and create pcl file from your pdf: 
python3 pdf_ingestor.py 

launch your web server:

python3 appweb.py

open your main.html file

ask your question about loaded pdf

You can increase the prompt, recently OpenAI announced that they can accept larger number of tokens, you can change 
chunk_size in pdf_ingestor.py file

also you can change the model used in gpt4web.py
