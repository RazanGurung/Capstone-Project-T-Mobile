T-Mobile Customer Churn Prediction








📊 Model Performance








🚀 Live Demo

🔗 Try the App Here

Endpoints available:

/health → API health check

/predict → JSON churn prediction

/predict_proba → churn probability

/form → interactive web form

✨ Key Features

🔎 Exploratory Data Analysis (EDA)

Identified churn trends across contract type, payment method, and monthly charges.

Discovered high-risk customer groups (e.g., month-to-month contracts, electronic check payments).

🧠 Machine Learning Models

Logistic Regression (final model), Random Forest, SVM, Gradient Boosting.

Balanced classes using SMOTE to avoid bias.

Final model achieved: ROC–AUC: 0.84, Recall: 0.81, Accuracy: 74%.

🛠 Production-Ready REST API

Health check, churn prediction, churn probability.

User-friendly web form for manual entry.

🎨 Web Form UI

Modern styled form for customer input.

Instant churn prediction results.

⚙️ Deployment on Render

Served with Gunicorn + Waitress for stability.

Scalable and cloud-ready.

📊 Insights from the Data

Customers on month-to-month contracts churn much more often than those with long-term plans.

Electronic check payments strongly correlate with churn.

Customers with short tenure (< 1 year) are most at risk.

Targeted retention (discounts, contracts, payment changes) could reduce churn by >20%.

🏗 Project Architecture
Capstone_T_mobile_Churn_Prediction/
│── api/
│   ├── app.py          # Flask app with endpoints
│   ├── wsgi.py         # Entry point for Gunicorn/Render
│   └── templates/      # HTML form
│── models/
│   └── churn_model.pkl # Trained Logistic Regression model
│── notebooks/
│   └── eda_modeling.ipynb # EDA + ML notebook
│── requirements.txt    # Dependencies
│── Procfile            # For Render deployment
│── README.md           # This file

⚡ Run Locally

Clone the repo:

git clone https://github.com/yourusername/Capstone_T_mobile_Churn_Prediction.git
cd Capstone_T_mobile_Churn_Prediction


Create & activate virtual environment:

python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows


Install dependencies:

pip install -r requirements.txt


Run API locally:

python -m waitress --listen=127.0.0.1:5050 api.wsgi:app


Access:

http://127.0.0.1:5050/form → Form UI

http://127.0.0.1:5050/predict → API

🔮 Future Enhancements

Add explainability with SHAP/LIME.

Build churn monitoring dashboards (Streamlit / Power BI).

Containerize with Docker for portability.

Automate retraining with fresh customer data.

🎯 Why This Project Matters

Telecom churn = multi-billion-dollar problem.
This project demonstrates:

End-to-end ML workflow: data → model → API → deployment.

Skills in data science, MLOps, and web development.

Business impact: targeted retention strategies = millions in saved revenue.

👨‍💻 Author

Rajan Gurung
Data Scientist | ML Engineer | Financial & Telecom Analytics Enthusiast

📌 LinkedIn • Portfolio • Email

⭐ If you found this project helpful, don’t forget to star the repo!
