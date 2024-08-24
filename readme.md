LlamaIndex Chatbot
This is a Streamlit-based chatbot application that uses LlamaIndex, Faiss, and OpenAI to interact with users by answering questions based on a set of loaded documents. The app leverages vector-based search with Faiss for efficient information retrieval and utilizes OpenAI's GPT model to generate responses.

Features
Document-Based Q&A: The chatbot answers questions using context from pre-loaded documents.
Streaming Responses: The chatbot provides streaming responses for a more interactive experience.
Chat History: The app maintains a chat history to provide context for better responses.
Installation
Clone the Repository:


Install Required Packages:

Ensure you have Python 3.8 or above. Install the required dependencies:

```
pip install streamlit faiss-cpu llama-index openai
```

Set Up OpenAI API Key:

Replace "your OpenAI API key" in the code with your actual OpenAI API key.

Prepare Your Documents:

Place the documents you want the chatbot to use in the following directory:

```
~/Desktop/personal/python/projects/doc
```

Ensure the path is correct, or modify the doc_path in the code to point to your document directory.

Usage
Run the Streamlit App:

```
streamlit run app.py
```
Interact with the Chatbot:

Once the app is running, you can ask the chatbot questions through the Streamlit interface. The chatbot will provide responses based on the content of the loaded documents.

Configuration
Model Configuration: The chatbot is configured to use the gpt-4o model from OpenAI with a temperature of 0.0 and a maximum token limit of 2000. These settings can be modified in the setup_chat_engine() function.
Streaming: The chatbot is set to stream responses for better interactivity.
Document Path: The document path is set to ~/Desktop/personal/python/projects/doc. Ensure that this path is correct or modify it as needed.
Troubleshooting
Document Path Issues: If the app cannot find the documents, ensure the path specified in the load_data() function is correct.
OpenAI API Errors: Make sure your OpenAI API key is valid and you have sufficient quota.
Faiss Indexing Issues: Ensure that Faiss is properly installed and compatible with your system.
License
This project is licensed under the MIT License.

Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

Contact
For any issues or inquiries, please contact kriti.sam@gmail.com
