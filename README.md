# AI CURE
## Team Name : pip install win   
## aicure_pip-install-win
## Rank : 6 / 217 teams
# [Report](https://github.com/shoryasethia/aicure_pip-install-win/blob/main/Report_aicure_pip-install-win.pdf)
# [Certification](https://github.com/shoryasethia/Heart-Rate-Prediction/blob/main/Certificate.pdf)
# Autor
- [@shoryasethia](https://github.com/shoryasethia) **| IIT Bombay**
# Heart Rate Prediction Model
* [This](https://github.com/shoryasethia/aicure_pip-install-win) repository contains an `Random Forest Regressor Model` in [heartrate.ipynb](https://github.com/shoryasethia/aicure_pip-install-win/blob/main/heartrate.ipynb) for predicting an individual's heart rate based on diverse attributes derived from ECG recordings. The `train_data.csv` dataset used for training is provided [here](https://github.com/shoryasethia/aicure_pip-install-win/blob/main/train_data.csv).
+ Refer to the Jupyter notebook [heartrate.ipynb](https://github.com/shoryasethia/aicure_pip-install-win/blob/main/heartrate.ipynb) for details on data exploration, feature engineering, and model training.
## Acknowledgement
[Random Forest Regressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html)
[Algorithm](https://en.wikipedia.org/wiki/Random_forest)

# Running the Model
To predict heart-rates for `test_data.csv`, use [run.py](https://github.com/shoryasethia/aicure_pip-install-win/blob/main/run.py) python script. Run it by the following command
```
python run.py path_to_test_data.csv
```
If `run.py` and `test_data.csv` are in same directory, then run
```
python run.py test_data.csv
```
# Output
[run.py](https://github.com/shoryasethia/aicure_pip-install-win/blob/main/run.py) script gives `results.csv` as output

# MSE Value 
There exists a [mse-calc.py](https://github.com/shoryasethia/aicure_pip-install-win/blob/main/mse-calc.py) file used to check the mean squared error between the predicted data and the actual data 
>Run this script only after running the [run.py](https://github.com/shoryasethia/aicure_pip-install-win/blob/main/run.py) script
```
python mse-calc.py output_file_name.csv
```

# Clone the repository
```
git clone https://github.com/shoryasethia/Heart-Rate-Prediction
```
# Libraries for run.py
```
pip install -r requirements.txt
```
# License
This project is licensed under the [MIT License](LICENSE).
