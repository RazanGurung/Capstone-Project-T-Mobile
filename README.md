📱 T-Mobile Churn Prediction – Capstone Project








🌐 Live Demo

🔗 Try the App on Render

📖 Project Overview

This project is a Capstone Machine Learning Solution focused on predicting customer churn for T-Mobile.

Designed a complete ML pipeline (data preprocessing → model training → evaluation → deployment).

Built a Flask API with endpoints for prediction and health checks.

Developed a user-friendly form interface for manual customer input and churn risk prediction.

Deployed the system seamlessly on Render Cloud Platform.

The project not only demonstrates technical ability in machine learning & full-stack deployment, but also highlights business impact by enabling telecom companies to proactively identify at-risk customers.

🚀 Features

✅ Machine Learning API – endpoints /predict, /predict_proba, /health

✅ Web Form – enter customer data manually for real-time predictions

✅ Threshold-based classification – optimized at 0.48 to balance Precision–Recall

✅ Performance evaluation – ROC–AUC, confusion matrix, metrics reporting

✅ Cloud Deployment – production-ready using Flask + Waitress + Render

📊 Model Performance








Detailed Metrics:

Metric	Value
Accuracy	74%
Precision (Churn class)	0.51
Recall (Churn class)	0.81
ROC–AUC	0.84

Test set size: 1,409 samples (374 churn, 1,035 non-churn)

Threshold chosen: 0.48 (optimized via precision–recall trade-off)

Confusion Matrix @ 0.48:

True Negatives = 740

False Positives = 295

False Negatives = 72

True Positives = 302

🛠️ Tech Stack

Programming: Python (3.9+)

ML Libraries: scikit-learn, pandas, numpy

Serving: Flask, Waitress

Frontend: HTML, CSS (form UI)

Deployment: Render Cloud

📂 Project Structure
Capstone_T_mobile_Churn_Prediction/
│
├── api/
│   ├── app.py          # Flask application (API + form routes)
│   ├── wsgi.py         # WSGI entrypoint for deployment
│   ├── templates/
│   │   └── form.html   # Frontend HTML form
│   └── static/         # (Optional) CSS/JS assets
│
├── models/             # Serialized ML model(s)
├── notebooks/          # Jupyter notebooks (EDA & experiments)
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation

📈 Business Impact

🎯 Early Risk Detection: Helps T-Mobile identify high-risk churn customers.

💡 Data-Driven Retention: Enables targeted offers and better resource allocation.

📉 Reduce Loss: Even a 5% churn reduction can save millions in revenue.

▶️ Getting Started (Local Run)

Clone the Repository

git clone https://github.com/<your-username>/t-mobile-churn-prediction.git
cd t-mobile-churn-prediction


Install Dependencies

pip install -r requirements.txt


Run with Waitress

python -m waitress --listen=127.0.0.1:5050 api.wsgi:app


Visit in Browser

http://127.0.0.1:5050/form

🧑‍💻 Author

Rajan Gurung
📍 Data Scientist | ML Engineer | AI Solutions Developer
🔗 LinkedIn:  | Portfolio | razangurung2147@gmail.com
