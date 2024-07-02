import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree



# prints the path of the decesion tree for a particular decision and anlow plots it
def show_decision(dtc,X,feature_names = None,class_name = None):   
    feature = dtc.tree_.feature
    threshold = dtc.tree_.threshold
    node_indicator = dtc.decision_path(X)
    leaf_id = dtc.apply(X)

    # Using sample 0 by default as this is only made for a dataset containing a single row

    sample_id = 0

    # obtain ids of the nodes `sample_id` goes through, i.e., row `sample_id`

    node_index = node_indicator.indices[
        node_indicator.indptr[sample_id] : node_indicator.indptr[sample_id + 1]
    ]
    node_index = node_index.tolist()

    for node_id in node_index:

        # continue to the next node if it is a leaf node
        if leaf_id[sample_id] == node_id:
            continue

        if X.iloc[sample_id, feature[node_id]] <= threshold[node_id]:
            threshold_sign = "<="
        else:
            threshold_sign = "=>"

        print(
            "decision node {node} : {col} = {value}) "
            "{inequality} {threshold})".format(
                node=node_id,
                # sample=sample_id,
                col = X.columns[feature[node_id]] ,
                # feature=feature[node_id],
                value=X.iloc[sample_id, feature[node_id]],
                inequality=threshold_sign,
                threshold=threshold[node_id],
            )
        )
    # Setting a figure size
    fig = plt.figure(figsize=(10,10))
    # The complete decision tree plot
    plott = plot_tree(dtc,feature_names=feature_names,class_names=class_name,fontsize=10)
    # Making each and every tree node invisible
    plt.setp(plott[:],visible = False)
    #Going thru all the nodes that are in the prediction path and making them visible
    for i in node_index:
        if i >= 2 : 
            i = i+1
        plt.setp(plott[i],visible = True)

    # Can also be saved in .svg or .png and a lot of formats
    plt.savefig('decison.pdf')
    plt.show()


if __name__ == "__main__" :

    dummy_tree = DecisionTreeClassifier()

    dummy_feature_names = ["a","b"] # Names of all the features of the dataset (Unique Column names)

    dummy_class_names = ["c","d"] # Names of the all the classes that the model can predict

    x = pd.DataFrame() # A dataframe that contains the data that you want to predict on

    show_decision(dummy_tree,X = x,feature_names=dummy_feature_names,class_name=dummy_class_names)


