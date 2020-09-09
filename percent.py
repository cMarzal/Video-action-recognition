import reader
import os
import numpy as np


if __name__ == '__main__':
    with open('log/p2_result.txt', "r") as f:
    #with open('log/p1_valid.txt', "r") as f:
        label = [int(line.strip()) for line in f.readlines()]

    lab3 = []
    lab3_pred = []
    dirs = []
    for lab in os.listdir('hw4_data/FullLengthVideos/labels/valid'):
        dirs.append(lab)
        with open('log/'+lab, "r") as f:
            # with open('log/p1_valid.txt', "r") as f:
            l = [int(line.strip()) for line in f.readlines()]
            lab3_pred.append(l)
        with open('hw4_data/FullLengthVideos/labels/valid/' + lab, "r") as f:
            # with open('log/p1_valid.txt', "r") as f:
            l = [int(line.strip()) for line in f.readlines()]
            lab3.append(l)
    '''
    collection = reader.getVideoList('hw4_data/TrimmedVideos/label/gt_valid.csv')
    act_label = collection['Action_labels']
    length = len(act_label)
    '''
    cor = 0
    acc = 0
    acc_tot = []
    cor_tot = 0
    len_tot = 0
    for i in range(7):
        cor = 0
        for e in range(len(lab3[i])):
            if lab3_pred[i][e] == int(lab3[i][e]):
                cor += 1
                cor_tot += 1
        acc += cor/len(lab3[i])
        acc_tot.append(cor / len(lab3[i]))
        len_tot += len(lab3[i])
    acc = acc/7
    total_acc = cor_tot/len_tot
    print('Mean Accuracy:', acc)
    print('Total Accuracy:', total_acc)
    for i in range(7):
        print('Accuracy of video', dirs[i], '=', acc_tot[i])
