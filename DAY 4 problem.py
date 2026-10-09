string = """data science machine learning data analysis machine 
learning statistics data models data training data validation features
features labels preprocessing data augmentation models data optimization 
gradient descent neural networks data tensors matrices visualization 
exploration pandas numpy matplotlib seaborn scikitlearn tensorflow pytorch 
deployment inference production monitoring reproducibility experiments results 
metrics accuracy precision recall f1 cross validation data machine
"""

words = string.split()

count = {} 


for word in words:
    count[word]= count.get(word,0) +1  

for k,v in count.items():
    print(f"count of {k} is {v}")