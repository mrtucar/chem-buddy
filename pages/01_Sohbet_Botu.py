from chem_boddy.knowledge_base import build_knowledge_base, get_chroma_collection 
from chem_boddy.vector_db import summarize_collection 
from chem_boddy.chat_flow import RAG_LLM, generateAnswer
import streamlit as st


def main_interface():
    st.set_page_config(page_title="Sohbet Botu")
    st.title("⚛️ Sohbet Botu")
    
    # Giriş Metni ve Amacı
    st.write("""
        Merhaba değerli İzmir Atatürk Lisesi öğrencileri! Bu web sitesi, kimya dersinde sizlere destek olmayı, 
        öğrenme sürecinizi daha eğlenceli hale getirmeyi ve merak ettiğiniz sorulara cevap bulmanızı sağlamayı amaçlıyor.
        Burada, Kimya dersi konularını gözden geçirebilir, kavramları daha iyi kavrayabilir ve interaktif bir şekilde öğrenebilirsiniz.
        """)
        # Bölümler ve Navigasyon
    
    st.markdown("---")
    st.subheader("Merak Ettiğin Konuları Sorabilirsin.:")
    
    # Load knowledge base
    if "knowledge_base" not in st.session_state :
        st.session_state.knowledge_base = get_chroma_collection()
   
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # React to user input
    if prompt := st.chat_input("Write your query here..."):
        # Display user message in chat message container
        st.chat_message("user").markdown( prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content":  prompt})

        response = generateAnswer(RAG_LLM, st.session_state.knowledge_base, prompt)

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main_interface()
