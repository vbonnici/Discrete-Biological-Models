
# coding: utf-8

# # Recall

# In[15]:


s = 'agctaggaggatcgccagat'

def get_kmers(s, k):
    """ This function return the set of k-mers that occur in a given string s"""
    kmers = set()
    for i in range(len(s) - k +1):
        kmers.add(s[i:i+k])
    return kmers

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


# ---
# # Dictionary coverage
# 
# The sequence coverage of a dictionary $D$ over a genome $s$ is defined as the number of positions of the genome that are involved in at least one occurrence of the words of the dictionary.
# <br>
# For each word of the dictionary, we firstly need to find its occurrences within the genome, and then we need to keep trace of their positions and coverage. 
# <br>
# The function `get_positions` return the list of starting positions of the occurrences of a word $w$ in a string $s$.
# <br>
# An array of boolean is used to keep trace of the coverage of the occurrence. Initially, the array is filled with `False` values, subsequently it is filled with `True` values for each position covered by the word of the given dictionary.
# <br>
# A dictionary may contains words of different length, but this property does not influence the definition of sequence coverage.

# In[16]:


def get_positions(s,w):
    """
        Return the starting postions in a reference string s where a word w occurs
        ----
        Paramters:
            s (str) : the reference string
            w (str) : the searched word
        ----
        Returns:
            list[int] : the positions
    """
    positions = list()
    for i in range(len(s)):
        if s[i:i+len(w)] == w:
            positions.append(i)
    return positions

# s = 'agctaggaggatcgccagat'
dictionary = ['ga', 'ag', 'ca', 't', 'aaaa']

coverage = [False for _ in range(len(s))]

# coverage = [False] * len(s)

for w in dictionary:
    for pos in get_positions(s,w):
        for i in range(len(w)):
            coverage[pos + i] = True

print(s)
print(coverage)

print('sequence coverage:', coverage.count(True),'covered positions over a total of', len(s),'=', coverage.count(True)/len(s))


# <br>
# The positional coverage of a position within a given genome is defined as the number of occurrences of the word in a dictionary that cover the given genomic position.
# <br>
# The implementation of positional coverage is obtained by modification of the implementation of sequence coverage. The trace array is converted from a boolean vector to an array of integers. The array is initially filled with zero values. For each occurrence, the corresponding positions in the array are increased by a value equal to $1$.

# In[17]:


def get_positions(s,w):
    """
        Return the starting postions in a reference string s where a word w occurs
        ----
        Paramters:
            s (str) : the reference string
            w (str) : the searched word
        ----
        Returns:
            list[int] : the positions
    """
    positions = list()
    for i in range(len(s)):
        if s[i:i+len(w)] == w:
            positions.append(i)
    return positions

print(s)

dictionary = ['ga', 'ag', 'ca', 't']

coverage = [0 for _ in range(len(s)) ]
for w in dictionary:
    for pos in get_positions(s,w):
        for i in range(len(w)):
            coverage[pos + i] += 1

print(coverage)


# <br>
# The sequence coverage can also be retrieve from the integer array by counting the number of cells with a value that differs from zero.

# In[18]:


print('sequence coverage',(len(coverage) - coverage.count(0)),'/',len(coverage),'=', (len(coverage) - coverage.count(0))  / len(coverage))


# <br>
# And statistics regarding the positional coverage for all the positions of the genome can be computed.

# In[19]:


from statistics import mean, stdev

print('average positional coverage', mean(coverage))
print('standard deviation of positional coverage', stdev(coverage))


# <br>
# List comprehension can be used to calculate the mean positional coverage of only the covered positions.

# In[20]:


print('average positional coverage of covered positions', mean([ i for i in coverage if i > 0]))
print('standard deviation of positional coverage of covered positions', stdev([ i for i in coverage if i > 0]))


# ---

# ## Reading FASTA files
# FASTA file are textual files containing genomic sequences written with the FASTA format.
# Multiple sequences can be stored into a single file. Each sequence is preceded by a description line that starts with a `>` character.
# Sequences are split into multiple lines, usually having at most 80 characters per each.
# 
# <br>
# In python, file pointer are provided by the built-in `open` function, and they can be in reading or writing mode. The function returns and object that technically is a pointer to the file but it can also be used as an iterable object. The iteration is performed along the lines of the file.

# In[21]:


ifile = 'mycoplasma_genitalium_G37.fna'

s = ''

for line in open(ifile, 'r'):
    if line.strip()[0] != '>':
        s += line.strip()

print( len(s) )


# The `split` function remove multiple blank characters (spaces, tabulations and any other printable symbol that results into a black print) from the left and right of the string. 
# <br>
# The first use of `strip` is to ensure that the `>` symbol is checked even if spaces are inserted before.
# The second one is used to remove the new line character, namely `\n` from the read line. If the `strip` is not performed, the resultant genomic sequence will be a string with multiple lines concatenated by `\n` character. This means that the alphabet of the string will contain also the `\n` character. 
# <br>
# <br>
# The function presented above is a toy example because it do not deal with FASTA file containing more than one genomic sequences. In fact, if multiple sequences are contained, the resultant string will be the concatenation of them.

# ---
# # Informational indexes
# 
# The maximal repeat length (mrl) is defined as the length of the longest repeat. Starting from $k>1$, the search for the mrl checks for the existence of a repeat at word length $k$, and in positive case it scan forward to the next $k$. If no repeat are found at length $k$, then the procedure stops and the returned mrl value is $k-1$.

# In[22]:


def mrl(s):
    """ Calculate the maximal repeat length of a string s """
    k = 0
    mrl = 0
    next_k = True
    while next_k:
        k += 1
        next_k = False
        for kmer in get_kmers(s,k):
            mult = count_occurrences(s,kmer)
            if mult > 1:
                mrl = k
                next_k = True
    return mrl


mrl_s = mrl(s[:1000])
# redefining mrl as a varibale will overwrite the mrl funciotn definition
print('mrl', mrl_s)


# <br>
# A modfied version of the function returns the mrl value together with one of the repeats having such length. The multiplicity value is also returned.

# In[9]:


def mrl(s):
    """ Calculate the maximal repeat length of a string s """
    k = 0
    mrl = 0
    kmer_mrl = ''
    mult_mrl = 0
    next_k = True
    while next_k:
        #print(k, end='', sep=' ')
        k += 1
        next_k = False
        for kmer in get_kmers(s,k):
            mult = count_occurrences(s,kmer)
            if mult > 1:
                mrl = k
                kmer_mrl = kmer
                mult_mrl = mult
                next_k = True
    return mrl, kmer_mrl, mult_mrl


mrl_s, kmer_mrl, mult_mrl = mrl(s[:1000])
# redefining mrl as a varibale will overwrite the mrl funciotn definition


print('mrl', mrl_s, ', kmer', kmer_mrl, ', multiplicity', mult_mrl)


# <br>
# The search for the the minimum hapax length (mhl) is similar to the search for mrl. Starting from $k = 1$, the multiplicity of $k$-mers are examined and the value of $k$ is increased until the first hapax has not been found.

# In[10]:


def mhl(s):
    """ Calculate the minimal hapax length of a string s """
    k = 0
    mhl = 0
    kmer_mhl = ''
    mult_mhl = 0
    next_k = True
    while next_k:
        k += 1
        for kmer in get_kmers(s,k):
            mult = count_occurrences(s,kmer)
            if mult == 1:
                mhl = k
                kmer_mhl = kmer
                mult_mhl = mult
                next_k = False
    return mhl, kmer_mhl, mult_mhl


mhl_s, kmer_mhl, mult_mhl = mhl(s[:1000])

print('mhl', mhl_s, ', kmer', kmer_mhl, ', multiplicity', mult_mhl)


# <br>
# The minimum forbidden length is calculated by comparing the size of the effective set of k-mers occurring in a sequence with the size of the theoretical one. The first word lengh $k$ at which the two sizes differ is the wanted value.

# In[11]:


def get_alphabet(s):
    al = set()
    for c in s:
        al.add(c)
    return al

def mfl(s, alphabet = None):
    """ Calculate the minimal forbidden length of a string s """
    if alphabet == None:
        a = len(get_alphabet(s))
    else:
        a = len(alphabet)
        
    k = 0
    while True:
        k += 1
        kmers = get_kmers(s,k)
        if len(kmers) != a**k:
            return k
        
mfl_s = mfl(s)
print('mfl',mfl_s, ', mcl', mfl_s - 1)


# ---
# The reader may notice that in the previous examples the variable used to store the calculated indexes never have the same name of the function used to calculate it. This is due to the fact that if the same name is used, the declaration of the variable overwrites the declaration of the function, as it is shown in the following example.

# In[12]:


def my_funct():
    return 0

my_funct = my_funct()  # declaring a variable having the same name of a function declared before
print(my_funct)


# Python is a programming language which uses left-most derivation. This means that first the function is called, then the assignment of its returned values to the variable is performed. Since the variable is declared for the first time, its declaration is the last operation that is executed. For this instruction forward, the function is no more available. In fact, if it is called back, the python interpreted will throws an error because the int variable is not callable.

# In[13]:


my_funct = my_funct() 

print(my_funct)


# ---
# <br>
# An useful informational index is also the empirical $k$-entropy. Since entropy is defined only for discrete probability distributions, multiplicity of words must be converted to probabilisties (frequencies).

# In[14]:


import math

def k_entropy(s,k):
    """ Calculate the empirical entropy at word length k of a string s """
    
    t = 0.0
    for kmer in get_kmers(s,k):
        t += count_occurrences(s,kmer)
    
    e = 0.0
    for kmer in get_kmers(s,k):
        e += math.log(count_occurrences(s,kmer) / t, 2)
    return -e
    
k = 2
print(str(k)+'-entropy', k_entropy(s,k))


# ---
# # Informational laws and genomic complexity
# We implement the informational laws and the computation of the genomic complexity. Then, we verify it on real genomes.
# 
# 1. $LG(G) = LOG_4(|G|)$
# 2. $LX_{2LG}(G) = \frac{\sum_{\alpha \in D_{2LG(G)}(G)}{mult(\alpha)}}{|D_{2LG(G)}(G)|}  $
# 3. $AC(G) = 2LG(G) - E_{2LG}(G) $
# 4. $EC(G) = LG(G) - AC(G) $
# 5. $AF(G) = \frac{AC(G)}{LG(G)}$
# 6. $EH(G) = \frac{EC(G) - AC(G)}{LG}$
# 7. $BB =  AC^\gamma  \bigg( \frac{EC- AC}{LG} \bigg) ^{3\gamma + 2}$
