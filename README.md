# 📊 Statistical Plots & Distribution Analysis

A Python-based data analysis project that uses statistical visualization techniques to understand numerical data distributions, compare groups, detect outliers, and analyze skewness and spread.

## 📌 Project Overview

This project performs **exploratory statistical analysis** using histograms, KDE plots, and boxplots. It analyzes the distribution of sales data and compares sales between different regions.

The project demonstrates how data visualization can be used to identify:

* Distribution patterns
* Central tendency
* Data spread and variability
* Outliers
* Skewness
* Differences between groups

---

## 🎯 Objectives

The main objectives of this project are:

1. Create histograms to understand frequency distributions.
2. Create KDE plots to visualize the shape of distributions.
3. Create boxplots to identify outliers and compare spread.
4. Compare distributions between different groups such as Region A and Region B.
5. Calculate skewness and statistical spread.
6. Detect outliers using the **Interquartile Range (IQR)** method.
7. Export statistical plots as image files.
8. Generate statistical summary results for further analysis.

---

## 🛠️ Technologies Used

| Technology | Purpose                                  |
| ---------- | ---------------------------------------- |
| Python     | Programming language                     |
| Pandas     | Data loading and analysis                |
| NumPy      | Numerical operations                     |
| Matplotlib | Data visualization                       |
| Seaborn    | Statistical visualization                |
| SciPy      | KDE calculation and statistical analysis |

---

## 📂 Project Structure

```text
Statistical-Plots-Distribution-Analysis/
│
├── sales_data.csv
├── analysis.py
│
├── sales_histogram.png
├── sales_histogram_kde.png
├── region_kde.png
├── region_boxplot.png
│
│
└── README.md
```

---

## 📈 Visualizations

### 1. Sales Histogram

The histogram shows the frequency distribution of sales values and helps identify the range where most observations occur.

### 2. Histogram with KDE

Combines a histogram with a Kernel Density Estimate (KDE) curve to provide a smoother view of the underlying distribution.

### 3. Region A vs Region B KDE

The KDE comparison shows how the sales distributions differ between Region A and Region B.

### 4. Regional Boxplot

The boxplot displays the median, quartiles, overall spread, and potential outliers for each region.

---

## 🔍 Statistical Analysis

### Skewness

Skewness is calculated to determine the asymmetry of the sales distribution.

```python
skewness = df["Sales"].skew()
```

Interpretation:

* `Skewness > 0.5` → Right/positive skew
* `Skewness < -0.5` → Left/negative skew
* Between `-0.5` and `0.5` → Approximately symmetric

### Outlier Detection

The project uses the **IQR method**:

```python
Q1 = df["Sales"].quantile(0.25)
Q3 = df["Sales"].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR
```

Values outside these limits are identified as potential outliers.

---

## 📊 Regional Comparison

The project calculates the following statistics for each region:

* Count
* Mean
* Median
* Standard deviation
* Minimum
* Maximum

Example:

```text
Region A
--------
Mean
Median
Standard Deviation
Minimum
Maximum

Region B
--------
Mean
Median
Standard Deviation
Minimum
Maximum
```

This allows the distributions to be compared using both visual and numerical methods.

---

## 📤 Output Files

After running the analysis, the following visualization files are generated:

```text
sales_histogram.png
sales_histogram_kde.png
region_kde.png
region_boxplot.png
```

The regional statistical summary is exported as:

```text
regional_statistics.csv
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Statistical-Plots-Distribution-Analysis.git
```

Move into the project directory:

```bash
cd Statistical-Plots-Distribution-Analysis
```

Install the required libraries:

```bash
pip install pandas numpy matplotlib seaborn scipy
```

---

## ▶️ How to Run

Run the Python analysis script:

```bash
python analysis.py
```

The program will:

1. Load the dataset.
2. Display basic dataset information.
3. Calculate descriptive statistics.
4. Generate histograms.
5. Generate KDE plots.
6. Generate regional comparison plots.
7. Detect potential outliers.
8. Calculate skewness.
9. Calculate statistical spread.
10. Export plots and regional statistics.

---

## 📝 Interpretation

The statistical plots provide an overview of the distribution and variability of sales values. The histogram shows how frequently different sales ranges occur, while the KDE plot provides a smoothed representation of the distribution. The boxplot helps identify the median, spread, and potential outliers using the interquartile range. The regional comparison provides a visual way to examine differences in sales distributions between Region A and Region B. Skewness is used to determine whether the distribution is approximately symmetric or shifted toward higher or lower values. Together, these statistical techniques provide a useful exploratory analysis of the dataset.

---

## 💡 Key Concepts Demonstrated

* Exploratory Data Analysis (EDA)
* Statistical visualization
* Histograms
* Kernel Density Estimation (KDE)
* Boxplots
* Outlier detection
* Interquartile Range (IQR)
* Skewness
* Standard deviation
* Grouped statistical analysis
* Data distribution comparison
* Data visualization with Python

---

## 🔮 Future Improvements

Possible improvements include:

* Add interactive Plotly visualizations.
* Add additional datasets.
* Create an automated statistical report.
* Add correlation analysis.
* Add Q-Q plots for normality checking.
* Create a Streamlit dashboard.
* Add automated outlier reporting.
* Compare multiple numerical variables.
* Export a complete PDF analysis report.

---

## 👨‍💻 Author

**Ankit Chauhan**

### Project

**Project 2 – Statistical Plots & Distribution Analysis**

### Purpose

Academic / Data Science Practice Project

---

## 📄 License

This project is intended for educational and learning purposes.
