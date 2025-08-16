from flask import Flask, request, jsonify, render_template
from werkzeug.exceptions import BadRequest
import joblib
import json
import pandas as pd
import os

# ---------- Load artifacts ----------
MODEL_PATH = os.getenv("MODEL_PATH", "models/final_logreg_smote_pipeline.joblib")
THRESH_PATH = os.getenv("THRESH_PATH", "models/threshold.json")

pipe = joblib.load(MODEL_PATH)
with open(THRESH_PATH, "r") as f:
    THRESHOLD = float(json.load(f).get("threshold", 0.5))

# Columns expected by the pipeline (same as training features BEFORE preprocessing)
# Adjust this list to match your X_train columns order in the notebook.
EXPECTED_COLUMNS = [
    "gender", "SeniorCitizen", "Partner", "Dependents", "tenure",
    "PhoneService", "MultipleLines", "InternetService", "OnlineSecurity",
    "OnlineBackup", "DeviceProtection", "TechSupport", "StreamingTV",
    "StreamingMovies", "Contract", "PaperlessBilling", "PaymentMethod",
    "MonthlyCharges", "TotalCharges",
    # engineered features created in FeatureEngineer.transform():
    "tenure_group", "avg_monthly_spend", "has_fiber", "num_addons",
    "auto_payment", "has_streaming"
]

app = Flask(__name__)


# ---------- Helpers ----------
def _ensure_dataframe(payload):
    """
    Accepts:
      - {"data": {...}} for a single record (dict)
      - {"data": [{...}, {...}]} for batch (list of dicts)
    Returns: pandas.DataFrame with EXPECTED_COLUMNS (missing cols filled with NA)
    """
    if "data" not in payload:
        raise BadRequest("JSON must contain a 'data' key with a dict or list of dicts.")

    data = payload["data"]
    if isinstance(data, dict):
        df = pd.DataFrame([data])
    elif isinstance(data, list):
        if not all(isinstance(r, dict) for r in data):
            raise BadRequest("'data' must be a list of JSON objects.")
        df = pd.DataFrame(data)
    else:
        raise BadRequest("'data' must be a dict or list of dicts.")

    # Add any missing expected columns
    for col in EXPECTED_COLUMNS:
        if col not in df.columns:
            df[col] = pd.NA
    # Keep only expected columns (order matters for some pipelines)
    df = df[EXPECTED_COLUMNS]
    return df


# ---------- JSON API Routes ----------
@app.route("/", methods=["GET"])
def root():
    """
    Render a minimal HTML form to input one customer and get a prediction.
    Place templates/form.html and templates/result.html under api/templates/.
    """
    return render_template("form.html", threhold=THRESHOLD)

@app.route("/health", methods=["GET"])
def health():
    try:
        _ = pipe  # ensure loaded
        return jsonify({"status": "healthy"}), 200
    except Exception as e:
        return jsonify({"status": "unhealthy", "error": str(e)}), 500


@app.route("/predict_proba", methods=["POST"])
def predict_proba():
    """
    Returns churn probability for each record.
    """
    payload = request.get_json(silent=True)
    if payload is None:
        raise BadRequest("Invalid JSON body.")

    df = _ensure_dataframe(payload)
    probs = pipe.predict_proba(df)[:, 1].tolist()

    return jsonify({
        "threshold": THRESHOLD,
        "probabilities": probs
    })


@app.route("/predict", methods=["POST"])
def predict():
    """
    Returns class prediction (0/1) using saved threshold.
    """
    payload = request.get_json(silent=True)
    if payload is None:
        raise BadRequest("Invalid JSON body.")

    df = _ensure_dataframe(payload)
    probs = pipe.predict_proba(df)[:, 1]
    preds = (probs >= THRESHOLD).astype(int).tolist()

    return jsonify({
        "threshold": THRESHOLD,
        "predictions": preds,
        "probabilities": probs.tolist()
    })


# ---------- Simple Web Form UI ----------



@app.route("/predict_form", methods=["POST"])
def predict_form():
    """
    Handle form submission, cast types, ensure expected columns/order,
    and render a human-readable result page.
    """
    # Read fields from the HTML form
    form_data = {k: v for k, v in request.form.items()}
    df = pd.DataFrame([form_data])

    # Safely cast numeric fields used by the model/engineer
    numeric_cols = [
        "tenure", "MonthlyCharges", "TotalCharges",
        "avg_monthly_spend", "num_addons", "has_fiber",
        "auto_payment", "has_streaming", "SeniorCitizen"
    ]
    for c in numeric_cols:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors="coerce").fillna(0)

    # Ensure all expected columns exist and are ordered
    for col in EXPECTED_COLUMNS:
        if col not in df.columns:
            df[col] = pd.NA
    df = df[EXPECTED_COLUMNS]

    # Predict
    proba = float(pipe.predict_proba(df)[:, 1][0])
    pred = int(proba >= THRESHOLD)

    return render_template(
        "result.html",
        proba=round(proba, 3),
        pred=pred,
        threshold=THRESHOLD
    )


# ---------- Error handling ----------
@app.errorhandler(BadRequest)
def handle_bad_request(e):
    return jsonify({"error": str(e)}), 400
