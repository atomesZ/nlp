# Introduction to Natural Language Processing

-----------------------------

## Run locally

To run this project, you need at least Python 3.8.10 which can be checked with `python3 --version`

To install the dependencies: `pip3 install -r requirements.txt`



## Run with Docker

The project can be loaded in a docker with simply:
`docker-compose up`

The jupyter notebook architecture can be seen on [localhost:8887](localhost:8887)

(just be careful, modifications inside will only be applied inside the container and not the host machine)

And stopped with:
`docker-compose down`


----------

## Project

-----------------------------


### Naive Bayes classifier

The code is in gaussian_basics.ipynb 

We also reimplemented the code of the Naive Bayes in Hand_Bayesien.ipynb but we finally used the one from scikit-learn.


--------


### Logistic regression

The code is in logistic_regression.ipynb 


---------------

### FastText baseline

The code is in FastText.ipynb


###  Modules

* The code for the preprocessing is in preprocessing.py
* The code for the analysis of wrongly classified samples are in analyze.py

