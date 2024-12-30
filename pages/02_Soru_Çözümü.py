import streamlit as st
from chem_boddy.chat_flow import RAG_LLM, generateAnswer,SoruUretici,generateQuestion
import json

st.set_page_config(page_title="Soru Çözümü",
                   layout="wide")

def soruOlustur(soru_json,panel):
    soru_data = json.loads(soru_json.replace("```json", "").replace("```", ""))
    print(soru_data)
    # JSON verisini Python sözlüğüne dönüştür
    with panel:
        # Soruyu ve seçenekleri ekranda göster
        cevap = st.radio(soru_data["soru"], soru_data["secenekler"].values())

        if st.button("Cevabı Göster"):
            print(cevap)
            dogru_cevap = soru_data["dogru_cevap"]
            dogru_cevap =dogru_cevap.replace("A) ","").replace("B) ","").replace("C) ","").replace("D) ","").replace("E) ","")
            if cevap == dogru_cevap or cevap == soru_data["dogru_cevap"]:
                st.success(f"Doğru!")
                #st.write(f"{soru_data['secenekler'][soru_data['dogru_cevap']]}")
            else:
                st.error(f"Yanlış. Doğru cevap {soru_data['dogru_cevap']} seçeneğidir.")
                #st.write(f"{soru_data['secenekler'][soru_data['dogru_cevap']]}")

            st.write(f"Açıklama : {soru_data['aciklama']}")


def main_interface():
    if "soru" not in st.session_state:
        st.session_state.soru = ""

    col1, col2 = st.columns(2)
    with col1:
        secilenKonu = st.selectbox("Hangi konudan soru çözmek istersiniz?", 
                                   ["Kuantum Sayıları",
                                    "Yükseltgenme Basamakları",
                                    "Gaz Yasaları",
                                    "Thomson Atom Modeli",
                                    "Karışımlarda Ayrıştırma ve Saflaştırma Teknikleri",
                                    "Periyodik Özellikler",
                                    "Katılar",
                                    "Kimyanın Temel Kanunları"])
        zorluk = st.selectbox("Zorluk seviyesi seçiniz", ["Kolay", "Orta", "Zor"])
        if st.button("Soruyu Getir"):  
            mesaj = f"{secilenKonu} konusundan {zorluk} seviyesinde bir soru üretebilir misin?"
            st.session_state.soru =""
            if st.session_state.soru == "":
                response = generateQuestion(SoruUretici, mesaj)
                st.session_state.soru = response.text
            else:
                response = st.session_state.soru
            
            #print(response.text)
            
        if (st.session_state.soru != ""):
            soruOlustur(st.session_state.soru,col2)

if __name__ == "__main__":
    main_interface()