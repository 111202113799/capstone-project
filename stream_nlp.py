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
                                    "SMS Fraud Detection", "abcdef", cookie_expiry_days=1)

# Add a guest login option
guest_mode = st.button("Continue as Guest" )
if guest_mode:
    authentication_status = "guest"  # Set a unique value for guest login
else:
    name, authentication_status, username = authenticator.login("Login", "main")


if authentication_status == False:
   st.error("Username/password is incorrect")

if authentication_status == None:
   st.warning("Please enter your username and password")
 
if authentication_status or authentication_status == "guest": 
        
        # Valid user login, proceed with full functionality
    if authentication_status == "guest":
        st.sidebar.title(f"Welcome guest")
        st.title('Prediksi SMS Penipuan')    
        
    else:
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
    
    authenticator.logout("Logout", "sidebar")
    if authentication_status == "Logout":
        st.cache_data.clear()  # Clear cache on logout
        st.cache_resource.clear()