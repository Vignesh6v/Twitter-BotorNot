# Twitter-BotorNot

Machine Learning Coursework Project

Aimed at analyzing the effectiveness and performance of different machine learning algorithms in its ability to classify twitter accounts as bots or humans. For obvious reasons, this is treated as classification problem. We evaluated the generalization performance and the predictive performance of all the models on future data. Based on the results we find the best suited machine learning algorithm for the given hypothesis space. 

BaseLine 
----
For baseline, Majority class classifier was used which had an accuracy of 0.5037.


 Decision Tree
 -------
Decision tree classifier was trained with the training set consisting of the features considered from RFE approach namely followers count, friends count, listed count, favorites count, verified, tweet count.  The decision tree classifier was able to predict with an accuracy of 0.864

Choosen Parameters:
* criterion: gini 
* max depth: 6
* max features: 6
* min impurity split: 1e-08
* min samples leaf: 8

Tree Structure: 
![Alt text](https://github.com/Vignesh6v/Twitter-BotorNot/blob/master/Image.jpeg "Tree Visualization") 


Neural Network
 -------
Parameters:
* solver = lbfgs
* alpha = 0.001
* layer = [17,10]
* activation = tanh


Random Forest
-------
Parameters:
* criterion= gini
* max_depth= 6
* max_features= 21
* min_impurity_split=1e-07
* min_samples_leaf=5
* min_samples_split=30


Comparing Different Models
![Alt text](https://github.com/Vignesh6v/Twitter-BotorNot/blob/master/Result.jpeg "Result") 


Project Team
-------

* Revanth Mattapalli
* Varun Elango
* Vignesh Ramesh
