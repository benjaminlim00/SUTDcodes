from sklearn.metrics import confusion_matrix

def get_metrics(actual_mat, pred_mat, labels):
    conf_metrics = confusion_matrix(actual_mat,pred_mat,labels)
    correct_pos = conf_metrics[1,1]
    correct_neg = conf_metrics[0,0]
    false_pos = conf_metrics[0,1]
    false_neg = conf_metrics[1,0]
    accuracy = (correct_pos + correct_neg)/(correct_pos + correct_neg + false_neg + false_pos)
    sensitivity = correct_pos / (correct_pos + false_neg)
    false_positive_rate = false_pos / (correct_neg + false_pos)
    dic = {}
    dic['confusion matrix'] = conf_metrics
    dic['total records'] = correct_pos + correct_neg + false_neg + false_pos
    dic['accuracy'] = accuracy
    dic['sensitivity'] = sensitivity
    dic['false positive rate'] = false_positive_rate
    return dic