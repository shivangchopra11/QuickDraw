import numpy as np
import json

def parse_line(arr):
    total_points = arr.shape[0]
    np_ink = np.zeros((total_points, 3), dtype=np.float32)
    np_ink[:,0] = arr[:,0]
    np_ink[:,1] = arr[:,1]
    np_ink[:,2] = 0
    np_ink[-1, 2] = 1  # stroke_end
  # Preprocessing.
  # 1. Size normalization.
    lower = np.min(np_ink[:, 0:2], axis=0)
    upper = np.max(np_ink[:, 0:2], axis=0)
    scale = upper - lower
    scale[scale == 0] = 1
    np_ink[:, 0:2] = (np_ink[:, 0:2] - lower) / scale
  # 2. Compute deltas.
    np_ink[1:, 0:2] -= np_ink[0:-1, 0:2]
#   print np_ink.shape
    np_ink = np_ink[1:, :]
#   print np_ink.shape
    return np_ink