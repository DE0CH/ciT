import pickle
with open('.github/workflows/file_changed.pkl', 'rb') as f:
  names = pickle.load(f)
print(names)