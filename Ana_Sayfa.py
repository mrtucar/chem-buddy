#pip install rag-kmk
#pip install streamlit
#streamlit run test.py
__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
from chem_boddy.knowledge_base import build_knowledge_base, get_chroma_collection 
from chem_boddy.vector_db import summarize_collection 
from chem_boddy.chat_flow import RAG_LLM, generateAnswer
import streamlit as st


def main_interface():
    st.set_page_config(page_title="Ana Sayfa",
                       layout="wide")
    
    st.title("⚛️ Kimya Konularını Keşfet ve Başarıya Ulaş!",
             )
    
    st.write("""
        Merhaba değerli İzmir Atatürk Lisesi öğrencileri! Bu web sitesi, kimya dersinde sizlere destek olmayı, 
        öğrenme sürecinizi daha eğlenceli hale getirmeyi ve merak ettiğiniz sorulara cevap bulmanızı sağlamayı amaçlıyor.
        Burada, Kimya dersi konularını gözden geçirebilir, kavramları daha iyi kavrayabilir ve interaktif bir şekilde öğrenebilirsiniz.
        """)
    
    st.markdown("---")
    st.subheader("Keşfedebileceğiniz Alanlar:")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**❓ Soru Çözümleri ve Testler**")
        st.write("Kimya konularıyla ilgili soru çözümleri ve pratik testlerle kendinizi sınayın.")
        st.button("Soru Çözümlerine Git", key="soru_button")

    with col2:
        st.markdown("**🤖 Kimya Sohbet Botu**")
        st.write("Kimya dersi ile ilgili merak ettiğiniz soruları sohbet botumuza sorabilirsiniz.")
        if st.button("Sohbet Botuna Git", key="chat_button"):
            st.switch_page("pages/chatpage.py")

    # # Load knowledge base
    # if "knowledge_base" not in st.session_state :
    #     st.session_state.knowledge_base = get_chroma_collection()
   
    # # Initialize chat history
    # if "messages" not in st.session_state:
    #     st.session_state.messages = []

    # # Display chat messages from history on app rerun
    # for message in st.session_state.messages:
    #     with st.chat_message(message["role"]):
    #         st.markdown(message["content"])

    # # React to user input
    # if prompt := st.chat_input("Write your query here..."):
    #     # Display user message in chat message container
    #     st.chat_message("user").markdown( prompt)
    #     # Add user message to chat history
    #     st.session_state.messages.append({"role": "user", "content":  prompt})

    #     response = generateAnswer(RAG_LLM, st.session_state.knowledge_base, prompt)

    #     # Display assistant response in chat message container
    #     with st.chat_message("assistant"):
    #         st.markdown(response)
    #     # Add assistant response to chat history
    #     st.session_state.messages.append({"role": "assistant", "content": response})

 



if __name__ == "__main__":
    main_interface()

