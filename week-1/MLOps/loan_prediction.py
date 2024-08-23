# Importing the required packages
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
import joblib  # Assuming it will be used for saving the models
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from matplotlib import pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn import metrics
from tabulate import tabulate  # For generating markdown tables
import mlflow
import os

# Set MLFlow tracking URI
# mlflow.set_tracking_uri("http://127.0.0.1:5001")
# mlflow.set_tracking_uri("http://0.0.0.0:5001/")

os.environ["MLFLOW_TRACKING_URI"] = "https://gitlab-codecamp24.obss.io/api/v4/projects/119/ml/mlflow/"
os.environ["MLFLOW_TRACKING_TOKEN"] = "glpat-_dUQ_1yxg6soUHDoenPp"

# load the dataset
dataset = pd.read_csv("train.csv")
numerical_cols = dataset.select_dtypes(include=['int64','float64']).columns.tolist()
categorical_cols = dataset.select_dtypes(include=['object']).columns.tolist()
categorical_cols.remove('Loan_Status')
categorical_cols.remove('Loan_ID')

# Filling categorical columns with mode
for col in categorical_cols:
    dataset[col].fillna(dataset[col].mode()[0], inplace=True)

# Filling Numerical columns with median
for col in numerical_cols:
    dataset[col].fillna(dataset[col].median(), inplace=True)

# Take care of outliers
dataset[numerical_cols] = dataset[numerical_cols].apply(lambda x: x.clip(*x.quantile([0.05, 0.95])))

# Log Transforamtion & Domain Processing
dataset['LoanAmount'] = np.log(dataset['LoanAmount']).copy()
dataset['TotalIncome'] = dataset['ApplicantIncome'] + dataset['CoapplicantIncome']
dataset['TotalIncome'] = np.log(dataset['TotalIncome']).copy()


# Dropping ApplicantIncome and CoapplicantIncome
dataset = dataset.drop(columns=['ApplicantIncome','CoapplicantIncome'])

# Label encoding categorical variables
for col in categorical_cols:
    le = LabelEncoder()
    dataset[col] = le.fit_transform(dataset[col])

# Encode the target columns
dataset['Loan_Status'] = le.fit_transform(dataset['Loan_Status'])

# Train test split
X = dataset.drop(columns=['Loan_Status', 'Loan_ID'])
y = dataset.Loan_Status
RANDOM_SEED = 5

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=RANDOM_SEED)

# Define RandomForest parameters
rf = RandomForestClassifier(random_state=RANDOM_SEED)
param_grid_forest = {
    'n_estimators': [200, 400, 700],
    'max_depth': [10, 20, 30],
    'criterion': ["gini", "entropy"],
    'max_leaf_nodes': [50, 100]
}

grid_forest = GridSearchCV(
        estimator=rf,
        param_grid=param_grid_forest, 
        cv=5, 
        n_jobs=-1, 
        scoring='accuracy',
        verbose=0
    )
model_forest = grid_forest.fit(X_train, y_train)

# Define Logistic Regression parameters
lr = LogisticRegression(random_state=RANDOM_SEED)
param_grid_log = {
    'C': [150, 10, 1.0, 0.2, 0.05],
    'penalty': ['l1', 'l2'],
    'solver': ['liblinear']
}

grid_log = GridSearchCV(
        estimator=lr,
        param_grid=param_grid_log, 
        cv=5,
        n_jobs=-1,
        scoring='accuracy',
        verbose=0
    )
model_log = grid_log.fit(X_train, y_train)

# Define DecisionTree parameters
dt = DecisionTreeClassifier(random_state=RANDOM_SEED)
param_grid_tree = {
    "max_depth": [3, 5, 7, 9, 11, 13],
    'criterion': ["gini", "entropy"],
}

grid_tree = GridSearchCV(
        estimator=dt,
        param_grid=param_grid_tree, 
        cv=5,
        n_jobs=-1,
        scoring='accuracy',
        verbose=0
    )
model_tree = grid_tree.fit(X_train, y_train)

mlflow.set_experiment("Loan_prediction")

# Model evaluation metrics
def eval_metrics(actual, pred):
    accuracy = metrics.accuracy_score(actual, pred)
    f1 = metrics.f1_score(actual, pred, pos_label=1)
    fpr, tpr, _ = metrics.roc_curve(actual, pred)
    auc = metrics.auc(fpr, tpr)
    plt.figure(figsize=(8,8))
    plt.plot(fpr, tpr, color='blue', label='ROC curve area = %0.2f' % auc)
    plt.plot([0, 1], [0, 1], 'r--')
    plt.xlim([-0.1, 1.1])
    plt.ylim([-0.1, 1.1])
    plt.xlabel('False Positive Rate', size=14)
    plt.ylabel('True Positive Rate', size=14)
    plt.legend(loc='lower right')
    # Save plot
    os.makedirs("plots", exist_ok=True)
    plt.savefig("plots/ROC_curve.png")
    # Close plot
    plt.close()
    return accuracy, f1, auc

def save_model_report(metrics, params, name, report_path="metrics_report.md"):
    report = []
    if os.getenv('MLFLOW_TRACKING_URI'):
        if os.getenv('GITLAB_CI'):
            ci_job_id = os.getenv('CI_JOB_ID')
    else:
        ci_job_id = "Undefined"
    
    if os.path.exists(report_path):
        with open(report_path, "r") as f:
            report = f.readlines()
            
    report.append(f"\n\n# Model Report for {name}\n\n")
    report.append(f"#### CI Job ID: {ci_job_id}\n\n")
    report.append("## Model Parameters\n\n")
    for key, value in params.items():
        report.append(f"- **{key}** : {value}\n")
    report.append("\n\n## Metrics\n\n")
    
    # Ensure metrics_data is a dictionary
    if isinstance(metrics, dict):
        metrics_list = [metrics]
    else:
        metrics_list = metrics

    report.append(tabulate(metrics_list, headers="keys", tablefmt="pipe"))

    with open(report_path, "w") as f:
        f.write("".join(report))

    return report_path

def mlflow_logging(model, X, y, name):
    with mlflow.start_run() as run:
        run_id = run.info.run_id
        mlflow.set_tag("run_id", run_id)
        if os.getenv('GITLAB_CI'):
            mlflow.set_tag('gitlab.CI_JOB_ID', os.getenv('CI_JOB_ID'))
        
        pred = model.predict(X)
        # Metrics
        accuracy, f1, auc = eval_metrics(y, pred)
        
        metrics_data = {
            "Mean CV score": model.best_score_,
            "Accuracy": accuracy,
            "f1-score": f1,
            "AUC": auc
        }
        params = model.best_params_
        
        # Logging best parameters from GridSearchCV
        mlflow.log_params(params)
        mlflow.log_params({"Class": name})
        # Log the metrics
        mlflow.log_metrics(metrics_data)
        
        # Logging artifacts and model
        mlflow.log_artifact("plots/ROC_curve.png")
        
        # Save and log model report
        report_path = save_model_report(metrics_data, params, name)

        mlflow.sklearn.log_model(model, name) 

        mlflow.end_run()

mlflow_logging(model_tree, X_test, y_test, "DecisionTreeClassifier")
mlflow_logging(model_log, X_test, y_test, "LogisticRegression")
mlflow_logging(model_forest, X_test, y_test, "RandomForestClassifier")
