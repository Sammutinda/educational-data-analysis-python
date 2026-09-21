# From Student Data to Actionable Insights

## Educational Data Analysis Portfolio Project

**Author:** Samson Mutinda  
**Focus:** Data Analysis, Educational Analytics, AI Data Work  
**Dataset:** Synthetic demonstration dataset (240 student records)

### Project overview

This project demonstrates a complete data-analysis workflow using a synthetic educational dataset. The objective is to show how raw student-level observations can be cleaned, summarized, visualized, and translated into practical insights.

The project is intentionally designed as a portfolio artifact for data-analysis and AI-training opportunities. **No real student personally identifiable information is used.**

### Questions explored

1. Which learning areas have the highest and lowest average scores?
2. How does performance vary across grades?
3. Is attendance associated with overall performance?
4. Is weekly study time associated with overall performance?
5. How are students distributed across performance bands?
6. What actions could an educator investigate based on the observed patterns?

### Dataset

The dataset contains 240 synthetic student records with:

- `student_id`
- `grade`
- `gender`
- `attendance_pct`
- `weekly_study_hours`
- `reading_score`
- `math_score`
- `english_score`
- `science_score`
- `overall_score`
- `performance_band`

### Methodology

The workflow follows a standard analytical process:

**1. Data generation and validation**
- Created a reproducible synthetic dataset.
- Checked data types and missing values.
- Applied reasonable ranges to percentage and study-time variables.

**2. Feature construction**
- Calculated `overall_score` as the mean of four learning-area scores.
- Classified students into five performance bands.

**3. Exploratory analysis**
- Calculated descriptive statistics.
- Compared learning areas and grades.
- Examined relationships between attendance, study time, and performance.

**4. Visualization**
- Bar charts for subject and grade comparisons.
- Scatter plots for relationships between behavioral variables and achievement.

**5. Interpretation**
- Findings are treated as associations, not proof of causation.
- Recommendations are framed as areas for further investigation rather than claims about individual students.

### Key findings

Using the synthetic dataset:

- The learning-area averages differ, indicating that instructional attention could be prioritized by subject rather than assuming uniform performance.
- Grade-level averages vary, suggesting that cohort-level analysis can reveal patterns hidden by an overall school average.
- Attendance and overall performance show a positive association in this simulated dataset (correlation: **0.41**).
- Weekly study time and overall performance also show a positive association (correlation: **0.64**).
- These relationships should **not** be interpreted as causal effects because the dataset is synthetic and observational.

### Practical implications

A school analytics workflow could use this type of analysis to:

- identify learning areas requiring additional support;
- flag cohorts for closer instructional review;
- monitor attendance alongside academic outcomes;
- design targeted interventions;
- track performance over time;
- produce concise reports for teachers and administrators.

### Limitations

This project has important limitations:

1. The dataset is synthetic.
2. It does not represent a statistically sampled population.
3. Correlation does not establish causation.
4. The model does not account for socioeconomic, instructional, or other contextual variables.
5. The results should not be used to make decisions about real students.

### Reproducibility

Python was used with:

- pandas
- NumPy
- Matplotlib

Run:

```bash
python analysis.py
```

The analysis script reads `student_performance_dataset.csv` and produces summary statistics and visualizations.

### Repository structure

```text
mindrift-data-analysis/
├── README.md
├── analysis.py
├── student_performance_dataset.csv
├── grade_summary.csv
├── subject_summary.csv
├── performance_bands.csv
├── 01_subject_performance.png
├── 02_grade_performance.png
├── 03_attendance_relationship.png
└── 04_study_relationship.png
```

### Skills demonstrated

- Data cleaning and validation
- Exploratory data analysis (EDA)
- Descriptive statistics
- Feature engineering
- Correlation analysis
- Data visualization
- Insight generation
- Analytical communication
- Reproducible Python workflows
- Responsible interpretation of data

### Portfolio note

This project is a demonstration of analytical methodology. The dataset is synthetic and should be clearly labeled as such wherever the project is published.
