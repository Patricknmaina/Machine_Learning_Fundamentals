# 📊 Machine Learning Fundamentals: Regression Analysis
This repository aims to explore fundamental concepts of Machine Learning, with a strong focus on regression techniques using Scikit-Learn for making housing prices predictions.

## 📁 Project Structure
- `data/`: Contains the [Boston Housing dataset](https://www.kaggle.com/datasets/altavish/boston-housing-dataset) from StatsLib, as well as a cleaned version of the dataset.

- `Data Preprocessing/`: Contains notebooks for data preprocessing, as well as Exploratory Data Analysis.

- `Models`: Contains `regression.ipynb` that contains the regression models used to make predictions and performance evaluation.

- `README.md`: Overview of the repository, installation instructions, and usage guide.

## 🧰 Tools implemented:
- `Python 3.11`
- `Scikit-Learn`: Regression modeling, data splitting, predictions & model performance
- `Numpy`: Numerical computations
- `Matplotlib & Seaborn`: visualization and EDA
- `StatsModels`: Measuring statistical significance.
- `Pandas`: Loading the dataset & data cleaning

## ⚒️ Installation
To run the notebooks locally:
1. Clone the repo:
```
git clone https://github.com/Patricknmaina/Regression_Techniques.git
cd Regression_Techniques
```

2. Create a virtual environment:
```
python -m venv venv
venv\Scripts\activate # On Linux, use: source venv/bin/activate
```

3. Install the dependencies:
```
pip install -r requirements.txt
```
Or manually:
```
pip install numpy pandas matplotlib seaborn scikit-learn statsmodels
```

4. Launch the notebook
```
jupyter notebook models/regression.ipynb
```

## 📝 TODO
- [ ] Data Cleaning & Preprocessing
- [ ] Exploratory Data Analysis
- [ ] Model Predictions
- [ ] Model Deployment (Streamlit)
- [ ] Docker Implementation
- [ ] CI/CD pipeline

## 📚 References
1. [IBM Machine Learning definition](https://www.ibm.com/think/topics/machine-learning)
2. [UC Berkeley: What is ML?](https://ischoolonline.berkeley.edu/blog/what-is-machine-learning/)
3. [Scikit-Learn Documentation](https://scikit-learn.org/stable/index.html)

## 📃 License
This repository is under the [MIT License](https://github.com/Patricknmaina/Regression_Techniques/blob/main/LICENSE).
