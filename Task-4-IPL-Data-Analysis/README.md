# IPL Data Analysis Project

## Project Overview

This project analyzes historical IPL match data using Python. The main objective is to clean the dataset, calculate team performance statistics, and generate insights from past IPL matches.

Special analysis has been performed for **Kolkata Knight Riders (KKR)** to study their season-wise performance and toss decision outcomes.

This project was completed as part of an internship task to demonstrate skills in:

- Python
- Pandas
- Data Cleaning
- Data Analysis
- Data Visualization

---

## Objectives

The objectives of this project are:

- Clean and preprocess IPL match data
- Analyze overall IPL team performance
- Study KKR's performance across different IPL seasons
- Analyze the impact of toss decisions on KKR's match results
- Generate charts and a summary report

---

## Tools and Libraries Used

- Python
- Pandas
- Matplotlib

---

## Dataset Used

The project uses an IPL historical matches dataset located at:

```text
data/matches.csv
```

The dataset contains information such as:

- Teams playing each match
- Match winner
- Toss winner
- Toss decision
- Season
- Match venue
- Other match details

---

## Project Structure

```text
Task-4-IPL-Data-Analysis/
├── data/
│   ├── matches.csv
│   ├── cleaned_matches.csv
│   ├── team_win_stats.csv
│   ├── kkr_season_performance.csv
│   └── kkr_toss_decision_stats.csv
│
├── charts/
│   ├── team_win_rate_chart.png
│   ├── kkr_season_win_rate_chart.png
│   └── kkr_toss_decision_chart.png
│
├── reports/
│   └── analysis_summary.txt
│
├── ipl_analysis.py
└── README.md
```

---

## Analysis Performed

### 1. Data Cleaning

The dataset is cleaned by:

- Removing extra spaces from column names
- Standardizing old franchise names:
  - Delhi Daredevils → Delhi Capitals
  - Kings XI Punjab → Punjab Kings
  - Rising Pune Supergiant → Rising Pune Supergiants
- Removing rows with missing winners

Generated file:

```text
data/cleaned_matches.csv
```
### 2. Overall IPL Team Performance Analysis

The project calculates:

- Matches played by each team
- Total wins by each team
- Win rate percentage for each team

Generated file:

```text
data/team_win_stats.csv
```

Visualization:

```text
charts/team_win_rate_chart.png
```

---

### 3. KKR Season-wise Performance Analysis

For **Kolkata Knight Riders (KKR)**, the project calculates:

- Matches played per season
- Wins per season
- Losses per season
- Win rate percentage per season

Generated file:

```text
data/kkr_season_performance.csv
```

Visualization:

```text
charts/kkr_season_win_rate_chart.png
```

---

### 4. KKR Toss Decision Analysis

For matches where **KKR won the toss**, the project analyzes:

- Total matches after choosing to bat
- Total matches after choosing to field
- Wins, losses, and win rate for each toss decision

Generated file:

```text
data/kkr_toss_decision_stats.csv
```

Visualization:

```text
charts/kkr_toss_decision_chart.png
```

---

### 5. Summary Report Generation

The project generates a summary report containing:

- Top IPL team by win rate
- Top 3 teams by win rate
- KKR's best season
- KKR's worst season
- Total KKR matches and wins
- Better toss decision for KKR based on historical data

Generated file:

```text
reports/analysis_summary.txt
```

---

## Output Files Generated

### Data Files

- `data/cleaned_matches.csv`
- `data/team_win_stats.csv`
- `data/kkr_season_performance.csv`
- `data/kkr_toss_decision_stats.csv`

### Chart Files

- `charts/team_win_rate_chart.png`
- `charts/kkr_season_win_rate_chart.png`
- `charts/kkr_toss_decision_chart.png`

### Report File

- `reports/analysis_summary.txt`

---
## How to Run the Project

### Step 1: Install Required Libraries

Open Command Prompt in the project folder and run:

```text
pip install pandas matplotlib
```

### Step 2: Place the Dataset

Make sure the IPL dataset is available at:

```text
data/matches.csv
```

### Step 3: Run the Project

Execute:

```text
python ipl_analysis.py
```

### Step 4: View the Results

After the script finishes, check:

- `data/` for cleaned datasets and analysis CSV files
- `charts/` for generated charts
- `reports/` for the summary report

---

## Key Learning Outcomes

This project helped me practice:

- Data cleaning using Pandas
- Data preprocessing techniques
- Grouping and aggregation operations
- Sports data analysis
- Data visualization using Matplotlib
- Organizing project files into a professional folder structure
- Writing a complete Python project for GitHub

---

## Future Improvements

Some possible improvements to this project include:

- Adding player-wise performance analysis
- Creating interactive dashboards using Plotly
- Building a web interface using Streamlit
- Automating report generation in PDF format

---

## Author

**Sahil Patel**

---

## Conclusion

This project demonstrates how Python can be used to clean, analyze, and visualize real-world IPL match data. It also highlights how meaningful insights can be generated from historical sports datasets through data analysis techniques. The project is organized with a clear folder structure, reusable code, visualizations, and a summary report, making it suitable for showcasing on GitHub as part of an internship portfolio.