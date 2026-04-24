import streamlit as st
import pandas as pd
import joblib
import os

# --- 1. MODEL LOADING (ONLY CHANGE THIS PART) ---
# This ensures it works on Streamlit Cloud using the compressed file
model_path = 'model.pkl'

@st.cache_resource # This keeps the 80MB model in memory so the app stays fast
def load_my_model():
    if os.path.exists(model_path):
        return joblib.load(model_path)
    else:
        st.error(f"Model file '{model_path}' not found in the repository!")
        st.stop()

model = load_my_model()

# --- 2. YOUR DASHBOARD CODE ---
# Keep all your st.title, st.sidebar, and st.number_input code exactly as it is.
# ... (Your existing UI code) ...

# --- 3. PREDICTION SECTION (ONLY CHANGE THE INPUT PART) ---
if st.button("Predict"):
    # 1. Create a dictionary with the EXACT column names from your training CSV
    # CRITICAL: These must match your training data column names exactly!
    feature_dict = {
        'Item_Weight': [val1],
        'Item_Fat_Content': [val2],
        'Item_Visibility': [val3],
        'Item_Type': [val4],
        'Item_MRP': [val5],
        'Outlet_Size': [val6],
        'Outlet_Location_Type': [val7],
        'Outlet_Type': [val8]
    }
    
    # 2. Convert to DataFrame
    input_df = pd.DataFrame(feature_dict)
    
    # 3. Predict using the DataFrame
    prediction = model.predict(input_df)
    
    # 4. Display result
    st.success(f"Predicted Sales: {prediction[0]:.2f}")