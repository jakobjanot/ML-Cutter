# PyTorch Model Package Template
Project structure template for packaging PyTorch models.


### How to use it?
[Cookiecutter](https://github.com/cookiecutter/cookiecutter) is used to generate the PyTorch model package template. So first install cookiecutter with pip:

``` bash
pip install cookiecutter
```
Generate the template:
``` bash
python -m cookiecutter https://github.com/KasperJuunge/pytorch-package-template
```

### Project Structure
The directory structure of your new project looks like this: 

```
├── LICENSE
├── README.md                           <- The top-level README for developers using this project.
├── data                                <- Raw data, utility data and 
│   ├── raw
│   ├── utils        
│   └── dataset      
│        ├── train
│        ├── val
│        └── test
│
├── trained_models                      <- Trained serialized models.
│   └── model_x                             <- Example of a trained model directory (not required, only a suggestion)
│       ├── state_dict.pt                       <- Trained model weights, serialized with torch.save()
│       ├── log.pt                              <- Training log file, serialized with torch.save()
│       └── events.out.tfevents                 <- TensorBoard events
│
├── notebooks                           <- Jupyter notebooks.
│
├── references                          <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports                             <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures                         <- Generated graphics and figures to be used in reporting
│
├── src                                 <- Source code for use in this project.
│   └── repo_name
│       │
│       ├── __init__.py                 <- Makes model_name a Python module
│       │        
│       ├── repo_name.py                <- Main model class that ties all functions together <3
│       │
│       ├── config                      <- Module containing configuration settings, such as hyperparameters.
│       │   │                 
│       │   ├── __init__.py
│       │   └── hyperparams.py
│       │ 
│       ├── data                        <- Scripts to get raw data. The raw data should be placed in ~/data/raw/ in the project root.
│       │   │                 
│       │   ├── __init__.py
│       │   └── get_model_data.py
│       │
│       ├── features                    <- Scripts to turn raw data into features for modeling.
│       │   │                 
│       │   ├── __init__.py
│       │   └── build_features.py
│       │
│       ├── model                       <- Scripts to define PyTorch Model, train it and make predictions.
│       │   │                 
│       │   ├── __init__.py
│       │   ├── Network.py
│       │   ├── train_model.py
│       │   ├── predict.py
│       │   └── train_model.py
│       │
│       ├── performance                 <- Scripts to measure performance of trained models.
│       │   │                 
│       │   ├── __init__.py
│       │   └── measure_performance.py
│       │
│       └── visualization               <- Scripts to reproducible data visualizations.
│           │                 
│           ├── __init__.py
│           └── visualize.py
│
├── requirements.txt                    <- The requirements file for reproducing the analysis environment, e.g.
│                                       generated with `pip freeze > requirements.txt`
│
└── setup.py                            <- makes project pip installable (pip install -e .) so src can be imported
```

### Workflow

Something about the workflow.

### Credits

This template is inspired by the [DrivenData Data Science Template](https://github.com/drivendata/cookiecutter-data-science). Thanks!



