# 3MTT-Knowledge-Showcase
To **run the phishing email detection app** (built with Streamlit) on your local machine or in the cloud, follow one of the options below:

---

## ✅ Option 1: **Run Locally on Your PC**

### Requirements:

* Python installed
* Your `.py` Streamlit app file (e.g., `app.py`)
* All necessary Python libraries installed

### 🔧 Steps:

1. **Install Streamlit (if not yet installed):**

```bash
pip install streamlit
```

2. **Navigate to your project folder**:

```bash
cd path/to/your/app
```

3. **Run the app**:

```bash
streamlit run app.py
```

4. It will open in your browser at:

```
http://localhost:8501
```

---

## ✅ Option 2: **Run in the Cloud (No Installation Needed)**

Use [Streamlit Community Cloud](https://streamlit.io/cloud) — perfect for sharing!

### 🔧 Steps:

1. Push your app code to GitHub in a public repo.

   * Include:

     * `app.py`
     * `requirements.txt` (list libraries used like `pandas`, `sklearn`, `streamlit` etc.)

2. Go to: [https://streamlit.io/cloud](https://streamlit.io/cloud)

3. Sign in with GitHub and click **“New App”**.

4. Connect your repo and choose the branch and Python file.

5. Click **“Deploy”** — Streamlit will set it up and give you a live link.

---

## ✅ Sample `requirements.txt`:

Here’s a basic version for your phishing email detector:

```
streamlit
pandas
scikit-learn
nltk
```

---

# 3MTT-Knowledge-Showcase
