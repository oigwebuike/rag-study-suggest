**RAG on LLMs: Document Similarity and Study Recommendation**
=====================================================

**Overview**
------------

This project demonstrates the integration of Retrieval-Augmented Generation (RAG) with Large Language Models (LLMs). It allows users to compare a user query with a document or a set of sentences and suggests relevant study courses based on the query. The core features include document similarity checking using cosine similarity and generating recommendations using a language model like `Llama` via a `ChatGroq` API.


**Features**
------------

* **Cosine Similarity Computation**: Computes Cosine Similarity between a query and a user-defined document corpus.
* **Interactive Document Input**: Users can either paste text directly into a text area or upload a `.txt` file.
* **Real-Time Analysis**: Displays the most relevant document based on similarity scores as soon as a query is provided.
* **User-Friendly Interface**: Built with Streamlit, the app is interactive and easy to use.
* **Document Similarity Checker**: Uses cosine similarity to find the most relevant document/sentence from a given set of text or uploaded document based on the user's query.
* **RAG Integration**: Combines information retrieval (similarity checking) with LLM-based generation, leveraging the retrieved information to augment the recommendations.
* **Study Course Recommendation**: Once a relevant document is identified, the system generates a study recommendation for the user based on their query using the Llama model via ChatGroq.
* **Dynamic Input Options**: Users can either paste document text directly or upload a .txt file to compare their query against.

**Requirements**
---------------

* **Python 3.8+**: The project is compatible with Python 3.8 and later versions.
* **Streamlit**: Required for building the interactive UI.
* **python-dotenv**: Used for managing environment variables.
* **Langchain**: For chaining LLMs with prompts and APIs.
* **Groq API Key**: Required to access the Llama model via ChatGroq.
* **Math, Counter**: For cosine similarity computation.

**Installation**
------------

1. Clone the repository:

   ```bash
   git clone <repository_url>
2. Navigate to the project directory:

   ```bash
   cd document_similarity_checker
3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
5. Create a `.env` file in the project root and add your API keys:
   ```plaintext
   GROQ_API_KEY=<your_groq_api_key>
   LANGSMITH_API_KEY=<your_langsmith_api_key>

Replace `<your_groq_api_key>` and `<your_langsmith_api_key>` with your actual API keys.


**Usage**
---------------

1. To run the application, use the following command:
   ```bash
   streamlit run app.py
**How It Works**
----------------

1. The user either uploads a `.txt` file or inputs a document corpus directly into a text area.
2. The user then inputs a query in the text box.
3. The app computes the **cosine similarity** of the query against the provided document corpus.
4. The **most relevant document** and its **similarity score** are displayed.

**Project Structure**
---------------------
1. The project struncture
   ```bash
   .
   ├── app.py                  # Streamlit application file
   ├── requirements.txt        # Project dependencies
   ├── README.md               # Project documentation
   └── .env                    # Environment variables (not included in the repo)



**Dependencies**
----------------

- `streamlit`
- `python-dotenv`

**Future Improvements**
-----------------------

* Add more sophisticated NLP models for better sentence representation.
* Allow users to upload their own document corpus in different file formats (e.g., CSV, JSON).

**License**
-----------

This project is licensed under the **MIT License**.

**Acknowledgments**
-------------------

This project was inspired by the work of the Streamlit and NLP community.
