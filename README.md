<img src="https://raw.githubusercontent.com/KasperJuunge/mlcutter/main/mlcutter.png" align="right">


Project structure template for developing machine learning models as packages.



## How to get started?
[Cookiecutter](https://github.com/cookiecutter/cookiecutter) is used to generate the PyTorch model package template. So first install cookiecutter with pip:

``` bash
pip install cookiecutter
```
Generate the template:
``` bash
python -m cookiecutter https://github.com/KasperJuunge/pytorch-package-template
```



## The Project Structure You'll Get

```
├── LICENSE
├── README.md                           <- The top-level README for developers using this project.
├── data_storage                        <- Data storage directory.
│   ├── raw
│   ├── utils        
│   └── dataset      
│        ├── train
│        ├── val
│        └── test
│
├── trained_models                      <- Trained serialized models.
│
├── notebooks                           <- Jupyter notebooks.
│
├── references                          <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports                             <- Directory for analysis and reports.
│   └── figures                         <- Generated graphics and figures to be used in reporting.
│
├── src                                 <- Source code for use in this project.
│   └── model_name
│       │
│       ├── __init__.py                 <- Makes model_name a Python module.
│       │        
│       ├── model_name.py               <- Main model class that ties all functions together <3
│       │
│       ├── config                      <- Module containing configuration settings, such as hyperparameters.
│       │   ├── __init__.py
│       │   └── hyperparams.py
│       │ 
│       ├── data                        <- Scripts to get raw data. The raw data should be placed in ~/data/raw/ in the project root.
│       │   ├── __init__.py
│       │   └── get_model_data.py
│       │
│       ├── features                    <- Scripts to turn raw data into features for modeling.     
│       │   ├── __init__.py
│       │   └── build_features.py
│       │
│       ├── model                       <- Scripts to define PyTorch Model, train it and make predictions.  
│       │   ├── __init__.py
│       │   ├── Network.py
│       │   ├── train_model.py
│       │   └── predict.py
│       │
│       ├── performance                 <- Scripts to measure performance of trained models.     
│       │   ├── __init__.py
│       │   └── measure_performance.py
│       │
│       └── visualization               <- Scripts to write reproducible and insightful data visualizations :p
│           ├── __init__.py
│           └── visualize.py
│
├── requirements.txt                    <- The requirements file for reproducing the analysis environment. 
│                                       
└── setup.py                            <- makes project pip installable (pip install -e .) so src can be imported.
```



## Workflow

When the template is initialized it creates a project structure that is ready for developing your very own PyTorch model 🔥

My typical workflow using this project structure is the following:

#### 1. Get Raw Data

First, get the data. Write the get_model_data() function to get the raw data for modeling. Place the raw data in ~/data_storage/raw/

#### 2. Data Exploration

Now we need to get our hands dirty! Explore the data, analyze the problem, make some plots, remove outliers and try to come up with some input features. This process is carried out using Jupyter Notebooks which should be placed in ~/notebooks/

#### 3. Build Features

When the data exploration phase is done, write the build_features() function that turns the raw data into juicy features. The function should also split the dataset in train, validation and test set and place it in ~/data_storage/dataset/

#### 4. Train Model

Now we're ready to train the model. In this phase ...



### Credits

This template is inspired by the [DrivenData Data Science Template](https://github.com/drivendata/cookiecutter-data-science). Thanks!



