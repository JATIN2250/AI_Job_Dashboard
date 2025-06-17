# 📊 Global Job Market Dashboard

An interactive Streamlit dashboard that visualizes job trends using a dataset from Kaggle. This project helps users understand various aspects of the global job market such as top job titles, hiring trends, salary insights, remote work adoption, and required skills.

---

## 🚀 Features

- 💼 **Top 10 High-Paying Job Titles**  
  Discover which roles offer the highest salaries across industries.

- 🌍 **Top 5 Hiring Company Locations**  
  Identify countries with the most hiring opportunities.

- 🧠 **Most Required Skills**  
  Analyze the most frequently listed technical and soft skills.

- 📈 **Top Hiring Companies Over the Years (Animated)**  
  Explore how hiring trends have changed across companies over time.

- 🏠 **Remote Work Trends**  
  Visualize the rise or decline of remote jobs over different years.

- 👥 **Experience Level vs Employment Type**  
  Compare job types based on required experience levels.

- 🧾 **Filtered Industry Donut Chart**  
  See the proportion of selected industry jobs versus all job openings.

- 💬 **Feedback Form**  
  Users can submit feedback directly from the dashboard.

---

## 📁 Project Structure

job_dashboard_project/
├──src
  └──app.py # Main Streamlit app
   └──AI_Job_visual_jupyter_notebook # Jupter Notebook work
├── requirements.txt # Python package dependencies
├── README.md # This file
├── dataset/
│ └── ai_job_dataset.csv # Input dataset


---

## 📦 Installation & Setup

### 🔧 Prerequisites
- Python 3.8 or above
- `pip` package manager

### ⚙️ Steps to Run Locally

1. **Clone the repo:**
   ```bash
        git clone https://github.com/yourusername/job-dashboard.git

        cd job-dashboard 
    ```
2. **Install required packages:**
    ```bash
        pip install -r requirements.txt
    ``` 
3. **Run the Streamlit app:**
    ```bash
        streamlit run app.py
    ```

4. **The dashboard will open in your browser at http://localhost:8501.**

## 🌐 Deployment (Streamlit Cloud)
To deploy on Streamlit Cloud:

1. Push your code to a public GitHub repo.

2. Go to streamlit.io/cloud

3. Click "New App" > connect your GitHub > select repo > deploy!

## 📊 Dataset
This dashboard uses job-related data from Kaggle.

Source: [https://www.kaggle.com/datasets/uom190346a/ai-powered-job-market-insights]

Columns Used: job title, salary, experience level, location, required skills, etc.

## ✉️ Feedback
We value your input! You can leave feedback directly in the app using the built-in form at the bottom of the page.

Alternatively, contact us via:

📧 Email: jitintulswani1@gmail.com


## 📄 License
This project is open-source under the MIT License


