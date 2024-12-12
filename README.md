## This is KIAM-Week-0 challenge

### Overview
The goal of this project was to perform Exploratory Data Analysis (EDA) on a solar radiation measurement data provided for 3 countries, Benin, Sierraleone and Togo. And based on the analysis, high-potential regions for solar installation are to be identified helping MoonLight Energy Solutions optimize their solar energy installation strategy.

Key activities include:

   * Cleaning and preprocessing the data.
   * Visualizing solar radiation patterns by region.
   * Analyzing seasonal variations and time-series trends.

### File Structure
The project is organized as follows:

* data/: Stores all data-related files.
* src/notebooks/: Contains Jupyter notebooks for interactive data analysis.
* scripts/: Python scripts for reusable code functions.
* results/figures: Contains visualizations generated through EDA.
* requirements.txt: Contains the necessary dependencies to run the project.

### Tools, Frameworks, and Libraries Used

#### Tools:
   * Jupyter Notebooks: Used for interactive analysis and visualization.
   * Git: Version control for managing changes.
   * Python: Primary programming language for data processing and analysis.

#### Frameworks & Libraries:
* Pandas: For data manipulation and cleaning (e.g., handling missing values, data transformation).
* NumPy: For numerical operations, especially when handling arrays and large datasets.
* Matplotlib: For creating static, animated, and interactive visualizations (e.g., bar charts, histograms).
* Seaborn: For statistical data visualization (e.g., heatmaps, box plots).
* Windrose: 

### User Guide: How to Run the Project
Before running the project, make sure you have Python 3.7+ , pip installed.

1. Clone the repository and navigate to the project
    ```
    https://github.com/selamasnake/kiam-week-0.git
    cd kiam-week-0
    ```
2. Install dependencies and the required Python libraries by using the requirements.txt
    ```
    pip install -r requirements.txt
    ```
3. Run the notebooks

    Navigate to the src/notebooks directory, which are divided by country.
   
    Go to each country's directory and start with the `data_preparation.ipynb` notebook to load the data and clean it.
   
    Then move to `data_anaysis.ipynb` notebook to perform the exploratory analysis.
   
    Visualizations will be generated at each step to interpret the data. 

5. Running Python Scripts
   
   Navigate to the scripts directory.
   
   Run the Python scripts directly `data_preparation.py` and `data_analysis.py` to execute parts of the data cleaning & analysis process.

