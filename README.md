# Cardiac Disease prediction using Machine Learning, Flask and MongoDB

This repository contains for a simple flask application that uses ML algorithm to classify whether a person has cardiac disease or not. 

## Dataset

Dataset can be collected from [UCL ML Repository](https://archive.ics.uci.edu/ml/datasets/heart+disease).

## Data preprocessing
The Data has to preprocessed extensively. As some information cannot be easily inputted some of the columns were dropped.

## Training & Testing
Various ML algorithms were used for training. Currently SVM is used in this application. The model performs moderately with around 72 % accuracy.

## Flask Application
A Simple Flask application was created with a UI so as collect the response from the user. Once collected it goes into the app.py file through which the ML algorithm will predict whether the person is having Cardiac disease or not.

## Backend
MongoDB is the backend here. All the data gets stored into Mongo Cluster in the cloud. In this way the data can used for retraining and other evaluation purpose.

## Deployment
The application was deployed in Heroku. However taken down now due to some updates in their server.

## App Overview

![alt text](https://github.com/wanderer799/cuddly-succotash/blob/master/app.PNG?raw=true)
