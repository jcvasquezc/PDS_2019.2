import numpy as np

	
def delay_noise(signal):
	delay=np.random.randint(2*len(signal),10*len(signal),1)
	return np.hstack((np.zeros(delay),signal,np.zeros(5*len(signal))))+np.random.normal(0,1,delay+len(signal)+5*len(signal))
	
