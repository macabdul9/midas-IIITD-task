import os
import pickle
def accuracy(path='meld/val'):
  with open('README.txt', '+r') as f:
  
    data = f.readlines()
  
  predictions = dict([(each.split(', ')[0],each.split(', ')[1].split('\n')[0]) for each in data ])
  
  correct_prediction=0
  for cls in os.listdir(path):
    for file in os.listdir(path+'/'+cls):
      if predictions[file]==cls:
        correct_prediction += 1
  return correct_prediction/len(predictions)
