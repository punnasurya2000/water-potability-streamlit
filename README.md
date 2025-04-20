# 💧 Water Potability Prediction App

A machine learning-powered web application that predicts whether drinking water is **potable (safe)** or **non-potable** based on its physicochemical properties. Built using Streamlit and trained on real-world water quality data.

![App Screenshot](https://stateimpactcenter.org/images/general/_metadata/Issues-in-Focus-Ocean-Water-Policy-Safe-Drinking-Water-Act-Image.jpg)

---

## 🚀 Live Demo
👉 [Click here to try the app](https://share.streamlit.io/your-username/water-potability-streamlit/main/app.py)

---

## 🧠 ML Models Used
The notebook evaluates multiple models:
- Logistic Regression
- Support Vector Machine (SVM) ✅ *Best performer*
- Random Forest

The final app uses a tuned **SVM model with 92%+ accuracy**.

---

## 🔬 Features Used

The app takes the following inputs:

| Feature             | Description                             |
|---------------------|-----------------------------------------|
| pH                  | Acidity/alkalinity of water             |
| Hardness            | Mineral content (calcium & magnesium)  |
| Solids              | Total dissolved solids (TDS)            |
| Chloramines         | Chlorine + Ammonia compound             |
| Sulfate             | Sulfate concentration                   |
| Conductivity        | Ability to pass electric current        |
| Organic Carbon      | Organic pollutants                      |
| Trihalomethanes     | Disinfection byproducts                 |
| Turbidity           | Water clarity                           |

---

## 🛠 How to Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/your-username/water-potability-streamlit.git
cd water-potability-streamlit

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the Streamlit app
streamlit run app.py
