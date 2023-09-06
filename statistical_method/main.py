import os, time
import pandas as pd

from sklearn.tree import DecisionTreeClassifier 
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression as LogisticRegressionClassifier 
from sklearn.svm import SVC as SVMClassifier

from Assets.Log import Log
from Assets.Data_Conversion import Data_Conversion
from Assets.Data_Labeling import Data_Labeling
from Assets.Data_Preparation import Data_Preparation
from Assets.ML_Algoritms import ML_Algoritms

activations = {
    "Log_Parameters": False,
    "Data_Conversion": False,
    "Data_Labeling": False,
    "Data_Preparation": False,
    "ML_Algoritms": False
}
activations["Log_Parameters"] = True
activations['Data_Conversion'] = True
activations["Data_Labeling"] = True
activations["Data_Preparation"] = True
activations["ML_Algoritms"] = True

######### Main Parameters #########
# Get the directory containing the currently executing script
main_dir = os.path.dirname(os.path.abspath(__file__))
dataFolder_path = "Data"
resultFolder_path = "Results/No_drop"
dataFiles_names = ["Main_Data"]
number_of_splits = 5
random_state_numbers = [7, 42, 75, 101, 216]
data_labeling_rules = "R2B2"
preprocessing_methods = ["MinMax", "Standard"]
unWanted_columns = ["CompanyId",
                    "Return", "Beta"]
drop_columns = []
target_columns = ['r_dicho', 'b_dicho']
######### Main Parameters #########

######### Data_Conversion parameters #########
dc_input_path = dataFolder_path
dc_output_path = f'{resultFolder_path}/0_Converted_Data'
dc_delete_column = ["PersianYear"]
dc_groupBase_column = "CompanyId"
dc_singelValue_columns = ["Return", "Beta"]
######### Data_Conversion parameters #########

######### Data_Labeling Parameters #########
dl_input_path = dc_output_path
dl_output_path = f'{resultFolder_path}/1_Lebeled_Data'
######### Data_Labeling Parameters #########

######### Data_Preparation Parameters #########
dp_input_path = dl_output_path
dp_output_path = f'{resultFolder_path}/2_Prepared_Data'
######### Data_Preparation Parameters #########

######### ML_Algorithms Parameters #########
ml_input_path = dp_output_path
ml_output_path = f'{resultFolder_path}/3_Algorithms_Results'
ml_save_models_flag = False
ml_algorithms = {
    "DT": {
        "estimator": DecisionTreeClassifier(),
        "param_grid": {
            'max_features': ['sqrt', "log2", None],
            'max_depth': [2, 3, 5, 10, None],
            'min_samples_leaf': [1, 2, 3, 5, 7],
        }
    },
    "LR": {
        "estimator": LogisticRegressionClassifier(),
        "param_grid": {
            'penalty' : ['l1', 'l2', 'elasticnet', None],
            'C' :  [1, 0.1, 0.01],
            'solver': ['newton-cg', 'lbfgs'],
            'dual': [True, False],
            'tol': [0.1, 0.01, 0.001]
        }
    },
    "RF": {
        "estimator": RandomForestClassifier(),
        "param_grid": {
            'n_estimators': [10, 50, 100],
            'max_features': ['sqrt', "log2", None],
            'max_depth': [2, 3, 5, 10, None],
            'min_samples_leaf': [1, 2, 3, 5, 7],
        }
    },    
    "SVM":{
        "estimator": SVMClassifier(),
        "param_grid": {
            'kernel': ['linear', 'rbf'],
            'C': [1, 0.1, 0.01],
            'gamma': ['scale', 'auto'],
            'tol': [0.1, 0.01, 0.001],
            'probability': [True],
            'cache_size': [16384]
        }
    },
}
ml_score_names = [
    'cross_validation_accuracy_mean',
    'test_accuracy_mean','specificity_mean', 
    'sensitivity_mean','mcc_mean',
    'f1_mean', 'auc_roc_mean', 'aupr_mean'
]
ml_nJobs = -1
ml_scorer = 'accuracy'
######### Algorithms Parameters #########

if not os.path.isdir(resultFolder_path):
    os.makedirs(resultFolder_path)

# get the start time
start_time = time.time()
main_log = Log(resultFolder_path, "main_log")



if activations["Log_Parameters"]:
    ######### Log Parameters #########
    # Main
    main_log(F'\n..:: Log Parameters ::..')
    main_log(F'==> dataFolder_path: {dataFolder_path}')
    main_log(F'==> resultFolder_path: {resultFolder_path}')
    main_log(F'==> dataFiles_names: {dataFiles_names}')
    main_log(F'==> number_of_splits: {number_of_splits}')
    main_log(F'==> random_state_numbers: {random_state_numbers}')
    main_log(F'==> data_labeling_rules: {data_labeling_rules}')
    main_log(F'==> preprocessing_methods: {preprocessing_methods}')
    main_log(F'==> unWanted_columns: {unWanted_columns}')
    main_log(F'==> drop_columns: {drop_columns}')
    main_log(F'==> target_columns: {target_columns}')

    # Statistics
    main_log(F'==> dc_input_path: {dc_input_path}')
    main_log(F'==> dc_output_path: {dc_output_path}')
    main_log(F'==> dc_delete_column: {dc_delete_column}')
    main_log(F'==> dc_groupBase_column: {dc_groupBase_column}')
    main_log(F'==> dc_singelValue_columns: {dc_singelValue_columns}')

    # Data_Labeling
    main_log(F'==> dl_input_path: {dl_input_path}')
    main_log(F'==> dl_output_path: {dl_output_path}')

    # Preparing
    main_log(F'==> dp_input_path: {dp_input_path}')
    main_log(F'==> dp_output_path: {dp_output_path}')

    # Algorithms
    main_log(F'==> ml_input_path: {ml_input_path}')
    main_log(F'==> ml_output_path: {ml_output_path}')
    main_log(F'==> ml_algorithms: {ml_algorithms}')
    main_log(F'==> ml_score_names: {ml_score_names}')
    main_log(F'==> ml_scorer: {ml_scorer}')
    main_log(F'==> ml_nJobs: {ml_nJobs}')
    ######### Log Parameters #########

if activations['Data_Conversion']:
    DC = Data_Conversion(dc_input_path, dc_output_path, main_log, main_dir)

if activations["Data_Labeling"]:
    DL = Data_Labeling(dl_input_path, dl_output_path, main_log)

if activations["Data_Preparation"]:
    DP = Data_Preparation(dp_input_path, dp_output_path, main_log)

if activations["ML_Algoritms"]:
    ML = ML_Algoritms(
        ml_input_path, ml_output_path, ml_save_models_flag,
        ml_algorithms, ml_scorer, ml_score_names, ml_nJobs, main_log
    )

######### Main Loop #########
for file_name in dataFiles_names:
    input_file_path = os.path.join(main_dir, dataFolder_path, f"{file_name}.csv")
    df = pd.read_csv(input_file_path)
    main_log(f'\n==> \"{file_name}\" (Orginal) shape: {df.shape}')
    new_df = df.drop(drop_columns, axis=1)
    new_df = new_df.dropna()
    main_log(f'==> \"{file_name}_new\" (After droping drop_columns and Nan rows) shape: {new_df.shape}')
    out_file_path = os.path.join(main_dir, dataFolder_path, f'{file_name}_new.csv')
    new_df.to_csv(out_file_path, index=False)

    file_name = file_name+'_new'
    nRows, nColumns = new_df.shape
    number_of_features = (nColumns - len(unWanted_columns+dc_delete_column)+2)*4
    main_log(f'==> \"{file_name}_new\" number_of_features: {number_of_features}')

    # Data_Conversion
    if activations["Data_Conversion"]:
        DC(
            file_name, dc_delete_column, dc_groupBase_column,
            dc_singelValue_columns, unWanted_columns
        )

    # Data_Labeling
    if activations["Data_Labeling"]:
        DL(file_name, data_labeling_rules)

    for random_state in random_state_numbers:
        for preprocessing_method in preprocessing_methods: 

            shuffle_flag = True
            if random_state == None:
                shuffle_flag = False

            # Data_Preparation
            if activations["Data_Preparation"]:
                DP(
                    f'{file_name}_{data_labeling_rules}', number_of_features,
                    target_columns, unWanted_columns, preprocessing_method,
                    number_of_splits, shuffle_flag, random_state
                )  

            # ML_Algoritms
            if activations["ML_Algoritms"]:
                ML(
                    f'{file_name}_{data_labeling_rules}', number_of_features,
                    target_columns, preprocessing_method, number_of_splits,
                    shuffle_flag, random_state
                )

######### Main Loop #########

# get the end time
end_time = time.time()

# get the execution time
elapsed_time = end_time - start_time
main_log(f'\n==> Execution time: {elapsed_time} seconds')

main_log.write_log()
print("end")