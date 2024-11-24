import os
import streamlit as st
import faiss
from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
)
from llama_index.vector_stores.faiss import FaissVectorStore
from llama_index.llms.openai import OpenAI
from llama_index.core.memory import ChatMemoryBuffer

# Set up OpenAI API key
os.environ["OPENAI_API_KEY"] = st.secrets['OPENAI_API_KEY']

def load_data():
    """Load documents from the specified directory and create a Faiss index."""
    doc_path = os.path.expanduser("docs")
    if not os.path.exists(doc_path):
        print(f"Directory {doc_path} does not exist. Please check the path.")
        return None
    
    documents = SimpleDirectoryReader(doc_path).load_data()

    d = 1536  # dimensions of text-ada-embedding-002
    faiss_index = faiss.IndexFlatL2(d)
    vector_store = FaissVectorStore(faiss_index=faiss_index)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    
    return VectorStoreIndex.from_documents(
        documents, storage_context=storage_context
    )

vector_index = load_data()

def setup_chat_engine(vector_index):
    """Set up the chat engine"""
    if vector_index is None:
        return None
    
    llm = OpenAI(model="gpt-4o", temperature=0.0, max_tokens=2000)
    memory = ChatMemoryBuffer.from_defaults(token_limit=3900)
    
    return vector_index.as_chat_engine(
        chat_mode="condense_plus_context",
        memory=memory,
        llm=llm,
        context_prompt=(
            "You are a helpful chatbot. Use the previous chat history and the "
            "context provided to answer the user's questions."
            "Here are the relevant documents for the context:\n"
            "{context_str}"
            "\nInstruction: Use the previous chat history, or the context above, "
            "to interact and help the user."
        ),
        streaming=True,  # Enable streaming
        verbose=True,
    )

# Set up chat engine
chat_engine = setup_chat_engine(vector_index)

def main():
    """Create the Streamlit app"""
    st.title("LlamaIndex Chatbot")
    st.write("Ask me anything about the loaded documents!")

    if chat_engine is None:
        st.error("Failed to initialize chat engine. Please check your document path.")
        return

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.chat_input("what is your question?"
    # Accept user input
    if prompt: 
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate assistant response
        # Generate assistant response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        response = chat_engine.chat(prompt)
        print("final answer ----------", response)
        
        # Display the response on the Streamlit UI
        message_placeholder.markdown(response.response)

# Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response.response})

        # Add assistant response to chat history
        # st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()
