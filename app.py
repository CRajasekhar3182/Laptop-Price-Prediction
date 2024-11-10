import streamlit as st
import numpy as np
import joblib

# Apply custom CSS for styling
st.markdown("""
    <style>
    body {
        background-color: #f5f5f5;
        font-family: 'Arial', sans-serif;
    }
    .main {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
    }
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 20px;
        border-radius: 10px;
        border: none;
        font-size: 18px;
    }
    .stButton > button:hover {
        background-color: #45a049;
    }
    .stMarkdown h1 {
        color: #333;
        font-size: 36px;
        text-align: center;
        padding-bottom: 20px;
    }
    .prediction-text {
        font-size: 22px;
        font-weight: bold;
        color: #0b5563;
    }
    </style>
""", unsafe_allow_html=True)

# Loading the model (ensure the model file is in the same directory or correct path)
model = joblib.load("model.joblib")  # Replace with your trained model file name

# Title of the app
st.markdown("<h1>💻 Laptop Price Prediction</h1>", unsafe_allow_html=True)
st.image("ai.webp", caption="Laptop Price Prediction App", width=600)
# Using markdown with custom CSS to control both width and height
st.markdown(
    """
    <style>
    .resized-image {
        width: 600px; /* Set width */
        height: 300px; /* Set height */
        object-fit: cover; /* Adjust to fit the container */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Embedding the image with CSS for custom dimensions
st.markdown('<img src="ai.webp" class="resized-image" alt="Laptop Price Prediction App">', unsafe_allow_html=True)


# User inputs
st.markdown("### Please provide your laptop details:")

# Company selection with the provided list
company = st.selectbox("🏢 Select Company", ['Apple', 'HP', 'Acer', 'Asus', 'Dell', 'Lenovo', 'Chuwi', 'MSI',
       'Microsoft', 'Toshiba', 'Huawei', 'Xiaomi', 'Vero', 'Razer',
       'Mediacom', 'Samsung', 'Google', 'Fujitsu', 'LG'])

# Type Name selection with the provided list
type_name = st.selectbox("💼 Select Type Name", ['Ultrabook', 'Notebook', 'Gaming', '2 in 1 Convertible',
       'Workstation', 'Netbook'])

# CPU selection with the provided list
cpu = st.selectbox("💻 Select CPU", ['Intel Core i5', 'Intel Core i7', 'Intel Core i3', 'Intel Celeron'])

# Memory selection with the provided list
memory = st.selectbox("📦 Select Memory", ['128GB', '256GB', '512GB', '500GB', '1TB', '128GB 1TB',
       '256GB 256GB', '64GB', '32GB', '256GB 1TB', '256GB 2TB', '2TB',
       '1 0TB', '512GB 1TB', '256GB 500GB', '128GB 2TB', '512GB 512GB',
       '16GB', '512GB 256GB', '512GB 2TB', '64GB 1TB', '180GB', '1TB 1TB',
       '', '240GB', '8GB', '508GB', '512GB 1 0TB', '256GB 1 0TB'])

# Other inputs remain the same
inches = st.number_input("📐 Inches (screen size in inches)", min_value=10.0, max_value=18.0, step=0.1)
ram = st.number_input("💾 RAM (GB)", min_value=4, max_value=64, step=1)

# GPU selection with the provided list
gpu = st.selectbox("🎮 Select GPU", [
    'Intel Iris Plus Graphics 640', 'Intel HD Graphics 6000', 'Intel HD Graphics 620', 'AMD Radeon Pro 455',
    'Intel Iris Plus Graphics 650', 'AMD Radeon R5', 'Intel Iris Pro Graphics', 'Nvidia GeForce MX150', 
    'Intel UHD Graphics 620', 'Intel HD Graphics 520', 'AMD Radeon Pro 555', 'AMD Radeon R5 M430', 
    'Intel HD Graphics 615', 'AMD Radeon Pro 560', 'Nvidia GeForce 940MX', 'Nvidia GeForce GTX 1050',
    'AMD Radeon R2', 'AMD Radeon 530', 'Nvidia GeForce 930MX', 'Intel HD Graphics', 'Intel HD Graphics 500', 
    'Nvidia GeForce 930MX', 'Nvidia GeForce GTX 1060', 'Nvidia GeForce 150MX', 'Intel Iris Graphics 540', 
    'AMD Radeon RX 580', 'Nvidia GeForce 920MX', 'AMD Radeon R4 Graphics', 'AMD Radeon 520', 
    'Nvidia GeForce GTX 1070', 'Nvidia GeForce GTX 1050 Ti', 'Intel HD Graphics 400', 'Nvidia GeForce MX130',
    'AMD R4 Graphics', 'Nvidia GeForce GTX 940MX', 'AMD Radeon RX 560', 'Nvidia GeForce 920M', 
    'AMD Radeon R7 M445', 'AMD Radeon RX 550', 'Nvidia GeForce GTX 1050M', 'Intel HD Graphics 515', 
    'AMD Radeon R5 M420', 'Intel HD Graphics 505', 'Nvidia GTX 980 SLI', 'AMD R17M-M1-70', 'Nvidia GeForce GTX 1080', 
    'Nvidia Quadro M1200', 'Nvidia GeForce 920MX', 'Nvidia GeForce GTX 950M', 'AMD FirePro W4190M', 
    'Nvidia GeForce GTX 980M', 'Intel Iris Graphics 550', 'Nvidia GeForce 930M', 'Intel HD Graphics 630', 
    'AMD Radeon R5 430', 'Nvidia GeForce GTX 940M', 'Intel HD Graphics 510', 'Intel HD Graphics 405', 
    'AMD Radeon RX 540', 'Nvidia GeForce GT 940MX', 'AMD FirePro W5130M', 'Nvidia Quadro M2200M', 
    'AMD Radeon R4', 'Nvidia Quadro M620', 'AMD Radeon R7 M460', 'Intel HD Graphics 530', 'Nvidia GeForce GTX 965M',
    'Nvidia GeForce GTX 1080', 'Nvidia GeForce GTX 1050 Ti'])

# Operating System selection
os = st.selectbox("🖥 Operating System", ["Windows", "MacOS", "Linux"])

# Weight input
weight = st.number_input("⚖ Weight (kg)", min_value=0.5, max_value=3.0, step=0.1)

# Button for prediction
if st.button("🔍 Predict Price"):
    # Encoding the selected company
    company_value = {
        'Apple': 0, 'HP': 1, 'Acer': 2, 'Asus': 3, 'Dell': 4, 'Lenovo': 5, 'Chuwi': 6, 
        'MSI': 7, 'Microsoft': 8, 'Toshiba': 9, 'Huawei': 10, 'Xiaomi': 11, 'Vero': 12, 
        'Razer': 13, 'Mediacom': 14, 'Samsung': 15, 'Google': 16, 'Fujitsu': 17, 'LG': 18
    }[company]

    # Encoding the selected type name
    type_name_value = {
        'Ultrabook': 0, 'Notebook': 1, 'Gaming': 2, '2 in 1 Convertible': 3,
        'Workstation': 4, 'Netbook': 5
    }[type_name]

    # Encoding the selected CPU type
    cpu_value = {
        'Intel Core i5': 0, 'Intel Core i7': 1, 'Intel Core i3': 2, 'Intel Celeron': 3
    }[cpu]

    # Encoding the selected memory
    memory_value = {
        '128GB': 0, '256GB': 1, '512GB': 2, '500GB': 3, '1TB': 4, '128GB 1TB': 5,
        '256GB 256GB': 6, '64GB': 7, '32GB': 8, '256GB 1TB': 9, '256GB 2TB': 10, '2TB': 11,
        '1 0TB': 12, '512GB 1TB': 13, '256GB 500GB': 14, '128GB 2TB': 15, '512GB 512GB': 16,
        '16GB': 17, '512GB 256GB': 18, '512GB 2TB': 19, '64GB 1TB': 20, '180GB': 21, '1TB 1TB': 22,
        '': 23, '240GB': 24, '8GB': 25, '508GB': 26, '512GB 1 0TB': 27, '256GB 1 0TB': 28
    }[memory]

    # Encoding the selected GPU
    gpu_value = {
        'Intel Iris Plus Graphics 640': 0, 'Intel HD Graphics 6000': 1, 'Intel HD Graphics 620': 2, 
        'AMD Radeon Pro 455': 3, 'Intel Iris Plus Graphics 650': 4, 'AMD Radeon R5': 5,
        'Intel Iris Pro Graphics': 6, 'Nvidia GeForce MX150': 7, 'Intel UHD Graphics 620': 8, 'Intel HD Graphics 520': 9,
        'AMD Radeon Pro 555': 10, 'AMD Radeon R5 M430': 11, 'Intel HD Graphics 615': 12, 'AMD Radeon Pro 560': 13, 
        'Nvidia GeForce 940MX': 14, 'Nvidia GeForce GTX 1050': 15, 'AMD Radeon R2': 16, 'AMD Radeon 530': 17, 
        'Nvidia GeForce 930MX': 18, 'Intel HD Graphics': 19, 'Intel HD Graphics 500': 20, 'Nvidia GeForce 930MX': 21
    }[gpu]

    # Encoding the selected operating system
    os_value = {
        'Windows': 0, 'MacOS': 1, 'Linux': 2
    }[os]

    # Making prediction
    features = np.array([[company_value, type_name_value, cpu_value, memory_value, gpu_value, inches, ram, weight, os_value]])
    prediction = model.predict(features)

    st.markdown(f"### Predicted Laptop Price: ₹ {prediction[0]:,.2f}", unsafe_allow_html=True)