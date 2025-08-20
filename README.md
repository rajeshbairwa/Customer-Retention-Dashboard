# Customer Retention Dashboard (Synthetic Project)

A **unique, analytics project** using a **synthetic e-commerce dataset**. It demonstrates how to go from **data → insights → visuals** with KPIs like **Monthly Revenue, Repeat Purchase Rate, Cohort Retention, CLV, and Churn proxy**.

## 📁 Project Structure
```
CustomerRetentionDashboard/
├─ data/
│  └─ synthetic_transactions.csv
├─ images/
│  ├─ monthly_revenue.png
│  ├─ repeat_purchase_rate.png
│  └─ cohort_retention.png
├─ src/
│  └─ analysis.py
├─ app_streamlit.py
├─ kpis.json
├─ requirements.txt
└─ README.md
```

## 🚀 Quickstart

### 1) Create & activate a virtual env (optional)
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Mac/Linux: source .venv/bin/activate
```

### 2) Install deps
```bash
pip install -r requirements.txt
```

### 3) Run the Streamlit app
```bash
streamlit run app_streamlit.py
```

### 4) Regenerate images (optional)
```bash
python src/analysis.py
```

## 📈 KPIs included
- **Monthly Revenue**
- **Repeat Purchase Rate**
- **Cohort Retention (first 6 months)** (see `images/cohort_retention.png`)
- **Churn Proxy** and **Average 6‑Month CLV** (precomputed in `kpis.json`)

## 🌐 Deploy to Streamlit Cloud (free)
1. Push this folder to GitHub (public repo).
2. Go to **share.streamlit.io** → “New app” → pick your repo.
3. Set **Main file path** to `app_streamlit.py`.
4. Add **requirements.txt** and click **Deploy**.

## 📸 Screenshots
See the `images/` folder (already generated) for ready-to-use visuals:
- `monthly_revenue.png`
- `repeat_purchase_rate.png`
- `cohort_retention.png`

