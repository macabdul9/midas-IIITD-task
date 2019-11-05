import os
import pickle
def accuracy(path='meld/val'):
  '''
    we have stored the true labels and predicted labels for test
    we will read it and calculate the accruacy
  '''
  with open('actual.pkl', 'rb') as fp:
    actual = pickle.load(fp)
  with open('predicted.pkl', 'rb') as fp:
    predicted = pickle.load(fp)
  
  
  correct = 0
  for i in range(len(actual)):
    if actual[i] == predicted[i]:
      correct += 1
  return (correct/len(actual))*100