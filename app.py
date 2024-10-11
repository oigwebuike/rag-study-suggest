import streamlit as st
import math
from collections import Counter
from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

# Load environment variables
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# Function to convert text to a word frequency vector
def text_to_vector(text):
    words = text.lower().split()  # Split text into words
    return Counter(words)

# Function to calculate cosine similarity between two sentences
def cosine_similarity_sentence(sentence1, sentence2):
    vector1 = text_to_vector(sentence1)
    vector2 = text_to_vector(sentence2)
    
    common_words = set(vector1.keys()).intersection(set(vector2.keys()))
    dot_product = sum(vector1[word] * vector2[word] for word in common_words)
    
    magnitude1 = math.sqrt(sum([value**2 for value in vector1.values()]))
    magnitude2 = math.sqrt(sum([value**2 for value in vector2.values()]))
    
    if magnitude1 == 0 or magnitude2 == 0:
        return 0.0
    return dot_product / (magnitude1 * magnitude2)

# Function to compare query against a list of sentences
def document_similarity(query, sentences):
    similarities = [cosine_similarity_sentence(query, sentence) for sentence in sentences]
    return max(similarities), sentences[similarities.index(max(similarities))]

# Streamlit App UI
st.title("Document Similarity Checker with Study Recommendation")

# Text input or file upload
document_body = st.text_area("Enter document text or paste multiple sentences (one per line):")
uploaded_file = st.file_uploader("Or upload a text file", type="txt")

# User input for query
user_query = st.text_input("Enter a query to compare against the document:")

# Add a submit button
if st.button("Submit"):
    if uploaded_file:
        document_body = uploaded_file.read().decode("utf-8")

    if document_body and user_query:
        sentences = document_body.split('\n')
        sim_value, relevant_document = document_similarity(user_query, sentences)
        
        st.write(f"Most relevant document: {relevant_document}")
        st.write(f"Cosine similarity score: {sim_value:.4f}")

        # ChatGroq model setup for recommendations
        llm = ChatGroq(
            model="llama-3.1-70b-versatile",
            temperature=0,
            groq_api_key=groq_api_key,
            max_tokens=None,
            timeout=None,
            max_retries=2,
        )

        prompt_extract = PromptTemplate.from_template(
           """
           You are a chat bot making recommendation for studies. A recommended subject course is: {sim}.
           Given a query: {query}
           Compile a recommended subject course for the user, which is based on the user's query.  
           """
        )

        json_parser = JsonOutputParser()
        chain = prompt_extract | llm
        response_chain = chain.invoke(input={"sim": relevant_document, "query": user_query})

        # Display the LLM response
        st.write("Recommended study course:")
        st.write(response_chain.content)
    else:
        st.write("Please provide both document text and a query.")
