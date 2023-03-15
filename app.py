# Mengimpor library
import pandas as pd
import streamlit as st
import pickle

# Menghilangkan warning
import warnings
warnings.filterwarnings("ignore")

# Menulis judul
st.markdown("<h1 style='text-align: center; '>Model HPH #3 Level</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; '>Indonesia Power</h1>", unsafe_allow_html=True)
st.markdown('---'*10)


# Fungsi untuk prediksi
def final_prediction(values, model):
    global prediction
    prediction = model.predict(values)
    return prediction

# Ini merupakan fungsi utama
def main():
    
    # Nilai awal
    gmp = 192.75
    ttd = 0.34
    
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            ngmp = st.number_input('GENERATOR MEASURED POWER', value=gmp)
        with col2:
            ttd = st.number_input('TTD HPH #3', value=ttd)
    
    st.markdown('---'*10)
    
    data = {
        'GENERATOR MEASURED POWER': gmp,
        'TTD HPH #3': ttd
        }
    
    kolom = list(data.keys())
    
    df_final = pd.DataFrame([data.values()],columns=kolom)
    
    # load model
    my_model = pickle.load(open('model_regresi_hph_level3.pkl', 'rb'))
    
    # Predict
    result = round(float(final_prediction(df_final, my_model)),2)
    
    st.write('<center><b><h3>HPH #3 Level= ', result,'</b></h3>', unsafe_allow_html=True)
           
if __name__ == '__main__':
	main() 
