#!/usr/bin/python3

import sys
import random
import numpy

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
from scipy import stats

import subprocess
import tempfile
import os


alpha_size = int(sys.argv[1])
seq_length = int(sys.argv[2])
ofile = sys.argv[3]

rtype = sys.argv[4]

#pouts = numpy.random.poisson(alpha_size,seq_lenth)

n_outcomes = list()

if rtype == "gauss":
	if len(sys.argv) > 4:
		sigma = float(sys.argv[5])
	else:
		sigma = 0.1
	print("sigma",sigma)
	vs =  numpy.random.normal(0,sigma,seq_length)
	for v in vs:
		n_outcomes.append(v)
	#for i in range(seq_length):
	#	n_outcomes.append(random.gauss(0,sigma))
elif rtype == "exp":
	for i in range(seq_length):
		n_outcomes.append(random.expovariate(0.1))
elif rtype == "pareto":
	for i in range(seq_length):
		n_outcomes.append(random.paretovariate(1) % alpha_size)
		#n_outcomes.append(1.0 / random.uniform(0.0,1.0))
elif rtype == "uniform":
	for i in range(seq_length):
		n_outcomes.append(random.uniform(0.0,1.0))
elif rtype == "piuniform":
	for i in range(seq_length):
		n_outcomes.append(random.randint(0,alpha_size-1))
elif rtype == "juniform":
	tmp = tempfile.NamedTemporaryFile(mode = 'w')
	#print(tmp.name)
	#subprocess.run(["java","RandomGen", str(alpha_size), str(seq_length),">",tmp.name], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
	subprocess.call("java "+" RandomGen "+str(alpha_size)+" "+str(seq_length)+" > "+tmp.name, shell=True)
	for i in open(tmp.name,'r'):
		#print(i)
		n_outcomes.append(int(i))
	#os.remove(tmp.name)
elif rtype == "runiform":
	tmp = tempfile.NamedTemporaryFile(mode = 'w')
	#print(tmp.name)
	#subprocess.run(["java","RandomGen", str(alpha_size), str(seq_length),">",tmp.name], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
	subprocess.call("Rscript "+" randomR.Rscript "+str(alpha_size)+" "+str(seq_length)+" "+tmp.name, shell=True)
	for i in open(tmp.name,'r'):
		#print(i)
		n_outcomes.append(int(i))
	#os.remove(tmp.name)
elif rtype == "chi2":
	k = int(sys.argv[5])
	vs =  numpy.random.chisquare(k,seq_length)
	for v in vs:
		n_outcomes.append(v)
elif rtype == "cauchy":
	#vs =  numpy.random.standard_cauchy(seq_length)
	vs = stats.cauchy.rvs(loc=0, scale=0.1, size=seq_length)
	for v in vs:
		n_outcomes.append(v)
elif rtype == "poisson":
	lam = float(sys.argv[5]) #1.0
	vs =  numpy.random.poisson(lam * alpha_size * alpha_size,seq_length)
	for v in vs:
		n_outcomes.append(v)
elif rtype == "gamma":
	alpha = float(sys.argv[5]) #3.0
	beta = float(sys.argv[6]) #1.0
	for i in range(seq_length):
		n_outcomes.append(random.gammavariate(alpha,beta))
elif rtype == "beta":
	alpha = float(sys.argv[5]) #0.5
	beta = float(sys.argv[6]) #0.5
	for i in range(seq_length):
		n_outcomes.append(random.betavariate(alpha,beta))
elif rtype == "lognorm":
	mu = float(sys.argv[5]) #0.0
	sigma = float(sys.argv[6]) #0.5
	for i in range(seq_length):
		n_outcomes.append(random.lognormvariate(mu,sigma))
elif rtype == "binomial":
	n = float(sys.argv[5]) #10
	p = float(sys.argv[6]) #0.1
	vs =  numpy.random.binomial(n * (alpha_size) * (alpha_size) ,p,seq_length)
	for v in vs:
		n_outcomes.append(v)
	#vs =  numpy.random.binomial(n * alpha_size,p,seq_length)
	#for i in range(seq_length):
	#	n_outcomes.append( numpy.random.binomial(n * alpha_size *alpha_size , p) )


#fig, axs = plt.subplots(1, 1, sharey=True, tight_layout=True)
#axs.hist(n_outcomes, bins=alpha_size)
#plt.show()
#quit()

min_n = min(n_outcomes)
max_n = max(n_outcomes)
bin_size = ((max_n - min_n) / alpha_size)


a_freqs = dict()

a_outcomes = list()
for n in n_outcomes:
	v = int((n+(0-min_n))/bin_size)
	if v >= alpha_size:
		v = alpha_size-1
	a_outcomes.append( v  )
	a_freqs[v] = a_freqs.get(v,0)+1


#for k,v in sorted(a_freqs.items()):
#	print(k,v)
#fig, axs = plt.subplots(1, 1, sharey=True, tight_layout=True)
#axs.hist(a_outcomes, bins=alpha_size)
#plt.show()
#quit()

with open(ofile,'w') as off:
	for n in a_outcomes:
		try:
			if n <= 25:
				s = str( chr( ord('A') + n))
			else:
				s = str( chr( ord('a') + (n - 25)))
			off.write(s)
		except ValueError as ex:
			pass
