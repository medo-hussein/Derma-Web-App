# 🧴 Derma - Skin Disease Diagnosis Web App

**Derma** is a Django-based web application that uses deep learning to assist in the preliminary diagnosis of skin diseases. Users can upload images of affected skin, and the system will analyze the image using an AI model to predict the likely condition.

> ⚠️ This app is for educational and demo purposes only. It is **not** intended for professional medical diagnosis.

---

## 📸 How It Works

1. The user uploads a photo of the affected skin area through the web interface.
2. The backend processes the image and passes it to a trained deep learning model.
3. The model predicts the possible skin disease based on the image.
4. The predicted result is displayed on the website.

---

## 🔧 Tech Stack

- **Backend:** Django (Python)
- **AI Model:** Trained with TensorFlow / PyTorch (custom model for skin disease classification)
- **Frontend:** HTML, CSS, JavaScript (Django Templates)
- **Image Processing:** Pillow / OpenCV
- **Model Input Format:** Image files (e.g. JPG, PNG)

---

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/derma.git
   cd derma
Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies
pip install -r requirements.txt
Run the server
python manage.py runserver
Access the app
Open your browser and go to http://127.0.0.1:8000

🧠 Model Details
Trained on a dataset of labeled skin disease images.

Supports classification of multiple common skin conditions.
