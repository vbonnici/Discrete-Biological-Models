
# coding: utf-8

# # Recall

# In[3]:


s = 'agctaggaggatcgccagat'

def get_kmers(s, k):
    """ This function return the set of k-mers that occur in a given string """
    kmers = set()
    for i in range(len(s) - k +1):
        kmers.add(s[i:i+k])
    return kmers

def get_positions(s,w):
    positions = list()
    for i in range(len(s)):
        if s[i:i+len(w)] == w:
            positions.append(i)
    return positions

def count_occurrences(s,w):
    """
        Count the number of occurences of w in s
        --------
        Parameters:
            s (str)
            w (str)
    """
    count = 0
    for i in range(len(s) -len(w) +1):
        for j in range(len(w)):
            if s[i+j] != w[j]:
                break
        else:
            count += 1
    return count


def k_entropy(s,k):
    """
        Calculate the empirical k-entropy on k-mers in s
    """
    t = 0.0
    for kmer in get_kmers(s,k):
        t += count_occurrences(s,kmer)
    
    e = 0.0
    for kmer in get_kmers(s,k):
        e += math.log(count_occurrences(s,kmer) / t, 2)
    return -e


ifile = 'mycoplasma_genitalium_G37.fna'
mg37 = ''
for line in open(ifile, 'r'):
    if line.strip()[0] != '>':
        mg37 += line.strip()


# ---
# # Genomic distributions

# ## Word multiplicity distribution
# 
# The word multiplicity distribution (WMD) is a function that assigns to words their corresponding multiplicity in a given string. <br>
# For example, one may wnat to assign to each symbol of the alphabet the number of its occurrences within a string.

# In[28]:


nuc_alphabet = ['a','c','g','t']
for n in nuc_alphabet:
    print(n, count_occurrences(s,n))


# Generally, a specific word length  $k$ is chosen, and the distribution is retrieved for the set of  $k$-mers.The complete set of  $k$-mers, even if they not occur in the string, can be used as domain of the distribution, or only those occurring in the string can be taken into account.

# In[29]:


kmers = get_kmers(s, k = 2)
for kmer in kmers:
    print(kmer, count_occurrences(s,kmer))


# ---
# ### Python key-value collections (dictionaries)
# Distributions are injective functions that assign values to a set of domain objects. In python, a data structure which maps values to keys in an injective way is called dictionary. Such data structure is a modifiable collection of pairs in the form $(key,value)$. 
# <br>
# Dictionaries can be declared statically by specifying an initial set of pairs, or can be declared without an explicit initial collection.
# <br>
# The single-slice operator allows to access the value associated with a specific key, as well as the updated of the value.

# In[30]:


D = {1:'one', 2:'two'} 

print(D[1])
print(D[2])

D[3] = 'three'

print(D[3])


# <br>
# There is not restriction on the type of keys and values.

# In[31]:


D['four'] = 4

print(D['four'])


# <br>
# The built-in functions `items`, `keys` and `values` are used to iterate the collection.

# In[32]:


for p in D.items():
    print(p)


# In[33]:


for k in D.keys():
    print(k,'-', D[k])


# In[34]:


for k,v in D.items():
    print(k,'-',v)


# ---
# ### WMD as key-value collection
# The development of the word multiplicity distribution result into a python dictionary which assigns multiplicity values (integers) to a set of key k-mers (strings).

# In[35]:


WMD = dict() # multiplicity distribution 
kmers = get_kmers(s,2)
for kmer in kmers:
    WMD[kmer]  = count_occurrences(s,kmer)

for kmer in WMD.keys():
    print(kmer,  WMD[kmer])


# Technically speaking, there is no assumption to the order in which keys, or pairs, are iterate because it depends on the internal data structure used by the specific python version to implement the dictionary. Thus, in case the user wants to output the distribution by the lexicographical order of the k-mers, an explicit sorting must be performed.

# In[36]:


for kmer in sorted(WMD.keys()):
    print(kmer, WMD[kmer])


# In[37]:


for kmer,mult in sorted(WMD.items()):
    print(kmer, mult)


# ---
# Retrieving the set of k-mers and then searching for their multiplicity results in a redundant combination of steps, that can be merged together. The distribution can be built while scanning for k-mers in the string and, at the same time, by updating their multiplicity values.

# In[38]:


WMD = dict() 
k = 2
for i in range(len(s) -k +1):
        w = s[i:i+k]  # extraction of the k-mer at position i
        WMD[w] += 1  # update of the occurrence of the k-mer w


# The single-slice operator of `dict` can only be used to access pairs that have been previously inserted in the collection. Thus, using it to access a key not yet present will cause an error.
# <br>
# A possible way to solve the problem is to firstly check for the presence of the key, and in case of absence making a first insertion of it. The operator `in` allows to check for the existence of a key in a dictionary.

# In[39]:


WMD = dict() 
k = 2
for i in range(len(s) -k +1):
        w = s[i:i+k]
        if w in WMD: 
            WMD[w] += 1
        else:
            WMD[w] = 1

for kmer in WMD.keys():
    print(kmer,  WMD[kmer])


# Alternatively, the built-in `get` function can be used. It allows to specify a default value that is returned in case of a missing key, without causing any error.
# <br>
# In the example, the default value of zero is used such that if $w$ has not yet inserted as a key, the `get` operation returns $0$ and the final counter is set to $1$. Conversely, if $w$ already exists within the collection, the operation return it current counter that will be updated by one.

# In[40]:


WMD = dict() 
k = 2
for i in range(len(s) -k +1):
        w = s[i:i+k]
        WMD[w] = WMD.get(w, 0) + 1

for kmer in WMD.keys():
    print(kmer,  WMD[kmer])


# Once a working code has been written, it can be also encapsulated in a function.

# In[5]:


def get_multiplicity_distribution(s,k):
    """
        Return the word multiplciity distribution of k-mers occurrig in the string s
         ------
        Parameters:
            s (str) : the input string
            k (int) : the length of the k-mers 
        -------
        Returns:
            dict[str,int] : a dictionary which associates multiplicity values to the k-mers in s
    """
    WMD = dict()
    for i in range(len(s) -k +1):
        w = s[i:i+k]
        WMD[w] = WMD.get(w,0) + 1
    return WMD
        
WMD = get_multiplicity_distribution(s,2)

for k,v in sorted(WMD.items()):
    print(k,v)


# <br>
# The given WMD implementation speeds the calculation of some of the informational indexes up.

# In[42]:


import math

def k_entropy(s,k):
    """
        Calculate the empirical k-entrpy on k-mers in s
    """
    t = 0.0
    for kmer in get_kmers(s,k):
        t += count_occurrences(s,kmer)
    
    e = 0.0
    for kmer in get_kmers(s,k):
        e += math.log(count_occurrences(s,kmer) / t, 2)
    return -e


def fast_k_entropy(s,k):
    """
        Calculate the empirical k-entrpy on k-mers in s
    """
    distr = get_multiplicity_distribution(s,k)
    t = sum(distr.values())
    e = 0.0
    for v in distr.values():
        e += math.log(v / t, 2)
    return -e
    
k = 2

import time

start_time = time.time()
print(str(k)+'-entropy', k_entropy(mg37,k))
print('seconds:', time.time() - start_time)

print()

start_time = time.time()
print(str(k)+'-entropy', fast_k_entropy(mg37,k))
print('seconds:', time.time() - start_time)


# ---
# ## Word length distribution
# The word length distribution (WLD) assigns to each word lenght $k$ the number of $k$-mers of $G$, namely the size of $D_k(G)$.

# In[44]:


def wld(s, k_start, k_end):
    """
        Calculate the word lenght distribution of the string s for the given range of values of word length k
        ----
        Paramters:
            s (str) : the input string
            k_start (int) : the initial word length
            k_end (int) : the final word length
        ----
        Returns:
            dict[int,int] : a dictionary which associates wolrd lengths (key) to the number of k-mers at each length (value)
    """
    wld = dict()
    for k in range(k_start,k_end):
        wld[k] = len(get_kmers(s,k))
    return wld

k_start = 1
k_end = 20
wld = wld(mg37, k_start, k_end)

import matplotlib.pyplot as plt
bar_values = [v for k,v in sorted(wld.items())]
plt.rcParams['figure.figsize'] = [20, 6]
plt.bar(range(k_start,k_end), bar_values)
plt.xticks(range(k_start,k_end), range(k_start,k_end))
plt.ylabel('|D_k(G)|')
plt.xlabel('k')
plt.title('Word length distribution')
plt.show()


# ---
# ## Average multiplcity distribution
# The average multiplcity distribution (AMD) assigns to each word lenght $k$ the average multiplcity of the k-mers of $G$.

# In[45]:


import statistics 

def amd(s, k_start, k_end):
    """
        Calculate the average multiplcity distribution of the string s for the given range of values of word length k
        ----
        Paramters:
            s (str) : the input string
            k_start (int) : the initial word length
            k_end (int) : the final word length
        ----
        Returns:
            dict[int,int] : a dictionary which associates word lengths (key) to the average multiplicity at the specific word length (value)
    """
    amd = dict()
    for k in range(k_start,k_end):
        amd[k] = statistics.mean( get_multiplicity_distribution(s,k).values() )
    return amd

k_start = 1
k_end = 20
amd = amd(mg37, k_start, k_end)

#for k,v in amd.items():
#    amd[k] = math.log(v)

#k_start = 12

import matplotlib.pyplot as plt
bar_values = [v for k,v in sorted(amd.items())]
plt.rcParams['figure.figsize'] = [20, 6]
plt.bar(range(k_start,k_end), bar_values)
plt.xticks(range(k_start,k_end), range(k_start,k_end))
plt.ylabel('Average multiplicity')
plt.xlabel('k')
plt.title('Average multiplicity distribution')
plt.show()


# ---
# ## Empirical entropy distribution
# The empirical entropy distribution (EED) assigns to each word length $k$ the value of the k-entropy.

# In[46]:


def eed(s, k_start, k_end):
    """
        Calculate the empirical entropy distribution of the string s for the given range of values of word length k
        ----
        Paramters:
            s (str) : the input string
            k_start (int) : the initial word length
            k_end (int) : the final word length
        ----
        Returns:
            dict[int,int] : a dictionary which associates word lengths (key) to the empirical entropy at the specific word length (value)
    """
    eed = dict()
    for k in range(k_start,k_end):
        eed[k] = fast_k_entropy(s,k)
    return eed

k_start = 1
k_end = 20
eed = eed(mg37[:10000], k_start, k_end)

#for k,v in amd.items():
#    amd[k] = math.log(v)

#k_start = 12

import matplotlib.pyplot as plt
bar_values = [v for k,v in sorted(eed.items())]
plt.rcParams['figure.figsize'] = [20, 6]
plt.bar(range(k_start,k_end), bar_values)
plt.xticks(range(k_start,k_end), range(k_start,k_end))
plt.ylabel('k-entropy')
plt.xlabel('k')
plt.title('Empirical entropy distribution')
plt.show()


# ---
# ##  Word co-multiplicity distribution
# Given a value of $k$, the word multiplicity distribution (WMD) reports for each value of multiplicity the number of word having such multiplicity

# In[9]:


def wcmd(s,k):
    """
        Calculate the word co-multiplicity distribution of the string s for the given value of word length k
        ----
        Paramters:
            s (str) : the input string
            k (int) : the word length
        ----
        Returns:
            dict[int,int] : a dictionary which associates a multiplicity value (key) to the number of k-mers having such multiplicity (value)
    """
    distr = dict()
    mdistr = get_multiplicity_distribution(s,k)
    for m in mdistr.values():
        distr[m]= distr.get(m,0) + 1
    return distr

k = 6
wcmd = wcmd(mg37[:100000],k)
# add missing multiplicity values
for i in range(1,max(wcmd.keys())):
    wcmd[i] = wcmd.get(i,0) + 0

import matplotlib.pyplot as plt
bar_values = [v for k,v in sorted(wcmd.items())]
plt.rcParams['figure.figsize'] = [20, 6]
plt.bar(sorted(wcmd.keys()), bar_values, width=1.0)
plt.ylabel('Number of words')
plt.xlabel('Multiplicity')
plt.title('Word co-multiplicity distribution')
plt.show()

