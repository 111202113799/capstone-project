import pickle
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from pathlib import Path
import streamlit_authenticator as stauth

def clear_cache():
    keys = list(st.session_state.keys())
    for key in keys:
        st.session_state.pop(key)

# --- USER AUTHENTICATION ---
names = ["Aditya Priadi Pradana", "Marchel Ferry Timoteus S", "Riski Nur Rohman", "Linda Septiana", "Monixca Fernandes Awangga Tirta"]
usernames = ["appradana", "mfsamosir", "rnrohman", "lsana", "mfatirta"]

# load hashed passwords
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

    
authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
    "SMS Fraud Detection", "abcdef", cookie_expiry_days=30)


name, authentication_status, username = authenticator.login("Login", "main")


if authentication_status == False:
   st.error("Username/password is incorrect")

if authentication_status == None:
   st.warning("Please enter your username and password")
 
if authentication_status: 
    st.sidebar.title(f"Welcome {name}")    
    st.title('Prediksi SMS Penipuan')

    # --- MAIN PROGRAM ---
    

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
    
    if st.button('Logout', on_click=clear_cache):
       st.cache_data.clear()  # Clear cache on logout
       st.cache_resource.clear()