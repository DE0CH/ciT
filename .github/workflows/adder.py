import sys
import pickle
with open('.github/workflows/file_changed.pkl', 'wb') as f:
  print(sys.argv[1:])
  pickle.dump(sys.argv[1:], f)


