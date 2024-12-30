import streamlit as st

# Örnek bir soru ve cevap fonksiyonu
def sorugetir(konu, zorluk):
    # Örnek bir soru seti
    return {
        "soru": f"{konu} konusunda {zorluk} seviyesinde bir soru",
        "şıklar": ["A", "B", "C", "D"],
        "cevap": "B"
    }

# Uygulama başlığı
st.title("Sınav Hazırlık Uygulaması")

# 1. Kullanıcıdan konu ve zorluk seviyesi seçimi
konu = st.selectbox("Bir konu seçin:", ["Matematik", "Fizik", "Kimya"])
zorluk = st.selectbox("Zorluk seviyesi seçin:", ["Kolay", "Orta", "Zor"])

# 2. "Soru Getir" butonu ile durumu kontrol et
if st.button("Soru Getir"):
    # Soru ve durumları session_state'e kaydet
    soru_verisi = sorugetir(konu, zorluk)
    st.session_state.soru = soru_verisi["soru"]
    st.session_state.şıklar = soru_verisi["şıklar"]
    st.session_state.doğru_cevap = soru_verisi["cevap"]
    #st.session_state.kullanıcı_cevabı = None  # Cevap sıfırlanır

# 3. Soru ve şıkları göstermek
if "soru" in st.session_state:
    st.write(f"**Soru:** {st.session_state.soru}")

    # Kullanıcı cevabını seçer
    kullanıcı_cevabı = st.radio(
        "Cevabınızı seçin:",
        st.session_state.şıklar,
        index=-1 if st.session_state.kullanıcı_cevabı is None else st.session_state.şıklar.index(st.session_state.kullanıcı_cevabı),
        key="cevap_secimi"
    )

    # Kullanıcı cevabını kaydeder
    st.session_state.kullanıcı_cevabı = kullanıcı_cevabı

    # 4. Cevabı Göster Butonu
    if st.button("Cevabı Göster"):
        if st.session_state.kullanıcı_cevabı == st.session_state.doğru_cevap:
            st.success("Tebrikler! Doğru cevap.")
        else:
            st.error(f"Yanlış cevap. Doğru cevap: {st.session_state.doğru_cevap}")
