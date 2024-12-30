import json
import streamlit as st

st.title("Gazların Özellikleri Testi")
secilenKonu = st.selectbox("Hangi konudan soru çözmek istersiniz?", ["Gazlar", "Asitler ve Bazlar", "Kimyasal Tepkimeler"])
zorluk = st.selectbox("Zorluk seviyesi seçiniz", ["Kolay", "Orta", "Zor"])
# JSON verisini bir değişkene yükle
soru_json = """
{
"soru": "Aşağıdakilerden hangisi gazların özelliklerinden **değildir**?",
"secenekler": {
    "A": "Gazlar bulundukları kabın şeklini ve hacmini alır.",
    "B": "Gazlar kolaylıkla sıkıştırılabilir.",
    "C": "Gazların belirli bir şekli ve hacmi vardır.",
    "D": "Gaz molekülleri arasındaki boşluklar katı ve sıvılara göre çok daha fazladır.",
    "E": "Gazlar akışkandır."
},
"dogru_cevap": "C"
}
"""

# JSON verisini Python sözlüğüne dönüştür
soru_data = json.loads(soru_json)

# Soruyu ve seçenekleri ekranda göster
cevap = st.radio(soru_data["soru"], soru_data["secenekler"].values())
 
if st.button("Cevabı Göster"):
    print(type(cevap.index.values))
    if cevap == soru_data["dogru_cevap"]:

        st.write(f"Doğru! {soru_data['dogru_cevap']} şıkkında verilen ifade gazlar için doğru değildir.")
        st.write(f"{soru_data['secenekler'][soru_data['dogru_cevap']]}")
    else:
        st.write(f"Yanlış. Doğru cevap {soru_data['dogru_cevap']} seçeneğidir.")
        st.write(f"{soru_data['secenekler'][soru_data['dogru_cevap']]}")