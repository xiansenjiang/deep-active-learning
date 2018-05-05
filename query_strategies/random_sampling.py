import numpy as np
from .strategy import Strategy

class RandomSampling(Strategy):
	def __init__(self, X, Y, idxs_lb, args):
		super(RandomSampling, self).__init__(X, Y, idxs_lb, args)

	def query(self, n):
		return np.random.choice(np.where(self.idxs_lb==0)[0], n)

	def update(self, idxs_lb):
		self.idxs_lb = idxs_lb