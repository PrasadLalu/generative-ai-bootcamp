import time
import streamlit as st
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

# Title
st.title("Chat With AI Tools")

if "messages" not in st.session_state:
    st.session_state.messages = []
    
        
# Chat input
if query := st.chat_input("What's in your mind?"):
    # Add user message to chat history
    user_timestamp = time.strftime("%H:%M")
    st.session_state.messages.append({
        "role": "user", 
        "content": query, 
        "timestamp": user_timestamp
    })
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(query)
        st.caption(user_timestamp)
        
    llm = init_chat_model("groq:openai/gpt-oss-20b")
    with st.spinner("🔍 Processing your query..."):
        response = llm.invoke(query)

    assistant_timestamp = time.strftime("%H:%M")
    
    if response:
        st.markdown(response.content)
        st.caption(assistant_timestamp)
            
        # Add assistant message to chat history
        st.session_state.messages.append({
            "role": "assistant", 
            "content": response.content, 
            "timestamp": assistant_timestamp
        })
    else:
        with st.chat_message("assistant"):
            st.error("⚠️ Error found")
            st.caption(assistant_timestamp)
    