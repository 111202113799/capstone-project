import pickle
import streamlit as st 
from sklearn.feature_extraction.text import TfidfVectorizer
from pathlib import Path
import streamlit_authenticator as stauth

# --- USER AUTHENTICATION ---
names = ["Aditya Priadi Pradana", "Marchel Ferry Timoteus S", "Riski Nur Rohman", "Linda Septiana", "Monixca Fernandes Awangga Tirta"]
usernames = ["appradana", "mfsamosir", "rnrohman", "lsana", "mfatirta"]

# load hashed passwords
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
    "Prediksi SMS Penipuan", "abcdef", cookie_expiry_days=30)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == None:
    st.warning("Silahkan masukkan username dan password")
    
if authentication_status:
    
    # --- MAIN PROGRAM ---
        
    # Proceed with app functionality after successful login
        authenticator.logout("Logout", "sidebar")
        st.sidebar.title(f"Welcome {name}")
        st.title('Prediksi SMS Penipuan')
                
    # Streamlit App
            
    # load save model
        model_fraud = pickle.load(open('model_fraud.sav', 'rb'))

        tfidf = TfidfVectorizer

        loaded_vec = TfidfVectorizer(decode_error="replace", vocabulary=set(pickle.load(open("new_selected_feature_tf-idf.sav", "rb"))))

    # judul halaman
        clean_teks = st.text_input('Masukkan Teks SMS')

        fraud_detection = ''

        if st.button('Hasil Deteksi'):
            predict_fraud = model_fraud.predict(loaded_vec.fit_transform([clean_teks]))
                    
            if (predict_fraud == 0):
                fraud_detection = 'SMS Normal'
            elif (predict_fraud == 1):
                fraud_detection = 'SMS Penipuan'
            else :
                fraud_detection = 'SMS Promo'
        st.success(fraud_detection)
        