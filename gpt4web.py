import os
import openai
import datetime
import pickle
import logging

GPT_MODEL = "gpt-3.5-turbo"
openai.api_key = os.getenv("OPENAI_API_KEY")

def setup_logger():
    date = datetime.date.today().isoformat() # get today's date in YYYY-MM-DD format
    time = datetime.datetime.now().time().isoformat(timespec='seconds') # get current time in HH:MM:SS format
    filename = f'logs/log_{date}_{time}.txt' # file name with date and time

    # Create a custom logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # Check if the log file already exists
    if not os.path.exists(filename):
        # If the log file doesn't exist, create it
        open(filename, 'w').close()

    # Create handlers
    handler = logging.FileHandler(filename)
    handler.setLevel(logging.INFO)

    # Create formatters and add it to handlers
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(handler)

    return logger

def generate_response(user_query, doc_chunk):
    logger = setup_logger()
    combined_query = user_query + " " + doc_chunk
    logger.info(f'Query: {combined_query}') # log the query

    response = openai.ChatCompletion.create(
        model=GPT_MODEL,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": combined_query},
        ],
        temperature=0.3,
    )
    generated_response = response['choices'][0]['message']['content']
    logger.info(f'Response: {generated_response}') # log the response

    return generated_response

# Load the list of Document objects
with open('docs.pkl', 'rb') as file:
    docs = pickle.load(file)

# Create a generator that yields elements from docs
def doc_generator(docs):
    for doc in docs:
        yield doc.page_content

doc_gen = doc_generator(docs)
