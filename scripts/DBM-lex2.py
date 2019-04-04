
# coding: utf-8

# # Recall

# In[25]:


s = 'agctaggaggatcgccagat'

def get_kmers(s, k):
    """ This function return the set of k-mers that occur in a given string s"""
    kmers = set()
    for i in range(len(s) - k +1):
        kmers.add(s[i:i+k])
    return kmers


# ---

# # Word multiplicity
# 
# In what follows, a function to count the number of characters `c` within a string $s$ is given. The function scans every position of $s$ and update the counter in case a `c` symbols occurs in a position.
# <br>
# The procedure equals the built-in `count` function defined for python strings.

# In[6]:


def count_C(s):
    count_c = 0 
    for a in s:
        if a == 'c':
            count_c += 1
    return count_c

nof_c = count_C(s)

print(s)
print(nof_c)
print(s.count('c'))


# <br>
# Python functions can return multiple values. For example the following function counts the number of `c` and `g`, and return the two separated values. 

# In[7]:


def count_CG(s):
    """Count the number of c and g in a given string and return the countings
    --------
    Parameters:
        s (str) : the input string
    --------
    Returns:
        int : the count of c
        int : the count of g
    """
    count_c, count_g = 0,0
    for a in s:
        if a == 'c':
            count_c += 1
        elif a == 'g':
            count_g += 1
    return count_c, count_g 

nof_c, nof_g = count_CG(s)

print(s)
print(nof_c, nof_g)
print(s.count('c'), s.count('g'))


# <br>
# Functions receives multiple input parameters and return multiple values, and python is not a typed programming language. The understanding of the correct value to be pass to the function, as well as the meaning and the type of its return values may result difficult for the final developer who wants to use the function. 
# <br>
# Thus, documentation of the function plays a crucial role in the usability of python. The code shown above gives an example of out to document input parameters and return values of a function. 
# <br>
# For what concerns input parameters, the name, the type and a brief description are provided.
# <br>
# Regarding return values, they do not have names thus the type and the description are given. However, the order in which they are return is crucial for they correct use.

# In[8]:


help(count_CG)


# <br>
# An examples of the practical use of the function is the calculation of the CG content of a string, that corresponds to the sum of the number of `c` and `g` characters divided by the total length of the string.

# In[9]:


print("the CG content of " + s + " is " + str((nof_c + nof_g)/len(s)) )
print(str((nof_c + nof_g))+" of " +str(len(s)) +" positions")


# ---
# ## Counting words
# 
# The previous example showed hot to count for specific single characters, however the counting of longer words (k-mers) is often wanted.
# <br>
# <br>
# The `count_occurrences` function counts the number of occurrences of a word $w$ in a string $s$. For each position of $s$ it verifies if an occurrence of $w$ starts form that position. The verification is made by comparing one by one the characters of $w$ with those occurring in the sibling positions of $s$.
# <br>
# <br>
# The built-in python library already provides a string function to count the occurrences of a substring. However, this exercise wants to emphasize the complexity of such a searching approach. It requires to nested for loops, which result in a time requirement that is of size $|s|$ times $|w|$.
# <br>
# <br>
# More in general, the reader is encouraged to understand the complexity of the built-in functions when they are used, because they can conceal an unexpected complexity in time or space. Conversely, the function given as example is the most trivial way to count for substring occurrences and more powerful methods exists which can be used by the library and that can increase the knowledge of a curious user. 

# In[10]:


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
        #if s[i:i+len(w)] == w:
        #    count += 1
    return count

print(count_occurrences(s,'ga'))
print(s.count('ga'))


# <br>
# One a function to count the number of occurrences of a single word has been defined, the multiplicity of all k-mers occurring in a string can be done. The example uses the multiplicity information to inform about the repetitiveness of all 2-mers (and more in general k-mers) of the string $s$. The k-mer are distinguished in hapaxes and repeats, and repeates are further verified for the duplex nature (they occur only twice). 

# In[11]:


k = 2
kmers = get_kmers(s,k)
for kmer in kmers:
    m = count_occurrences(s,kmer)
    if m == 1:
        print(kmer + " is an hapax")
    else:
        print(kmer + " is a repeat")
        if m == 2:
            print(kmer + " is a duplex")


# <br>
# The procedure is modified such that the multiplicity information is not just printed, but words are bucket depending on their occurrence property. The operation is performed by representing buckets as sets. 

# In[12]:


k = 2
kmers = get_kmers(s,k)

hapaxes = set()
repeats= set()
duplexes = set()

for kmer in kmers:
    m = count_occurrences(s,kmer)
    if m == 1:
        hapaxes.add(kmer)
    else:
        repeats.add(kmer)
        if m == 2:
            duplexes.add(kmer)

print('hapaxes', len(hapaxes), sorted(hapaxes))
print('repeats', len(repeats), sorted(repeats))
print('duplexes', len(duplexes), sorted(duplexes))


# By definition, the set of duplexes is contained within the complete set of repeats. A way to retrieve the set of repeats that occur more than twice is to use the built-in python set-theoretic operations, in this case the set difference denoted by the symbol `-`.

# In[13]:


nodupl = repeats - duplexes
print("repeats not duplexes", len(nodupl), sorted(nodupl))


# ---
# # ! WARNING !
# The built-it method `count` does not count overlapping occrrences !!!

# In[1]:


s = 'aaaaaaa'
count_occurrences(s,'aa')
s.count('aa')


# ---

# ## Searching for nullomers

# Nullomers are k-mers belonging to the complete set of word of length $k$, that can be built of a specific alphabet, but that do not appear in a given string. Thus, to search for nullomer, firstly a way to generate the complete set of words is necessary. Then, the presence of the k-mers can be verified. 
# <br>
# The complete set can be computed via a recursive function. It extends word of length $x$ to length $x+1$ in a combinatorial way by elonging them with all the symbols of the alphabet. This means that, given a word $\alpha$, it generates $\{\alpha A, \alpha C, \alpha G,\alpha T\}$, then it recursively extends such elongations until words of length $k$ are formed. The initial string is set to be the empty string. The base case, namely the stop condition of the recursion, is reached when the formed word has length equal to $k$.

# In[14]:


def list_words(prefix, k, alphabet):
    if len(prefix) == k:
        print(prefix)
    else:
        for a in alphabet:
            list_words(prefix + a, k, alphabet)

nuc_alphabet = ['a','c','g','t']

list_words('', 1, nuc_alphabet)


# In[15]:


list_words('', 2, nuc_alphabet)


# The function is modified such that instead of just printing the k-mer, they are added to an output set. 

# In[16]:


def list_words_2(prefix, k, nuc_alphabet, words):
    if len(prefix) == k:
        words.add(prefix)
    else:
        for a in nuc_alphabet:
            list_words_2(prefix + a, k, nuc_alphabet, words)
            
kmers = set()
list_words_2('',2, nuc_alphabet, kmers)
print(kmers)


# <br>
# Once a way to enumerate all the possible k-mers has made, it can be used to identify the set of nullomers of a string. For each k-mer, if its multiplicity within the string is equal to zero it means that it is not occurring in the string, thus it is a nullomer.

# In[18]:


k = 2
kmers = set()
list_words_2('',k,nuc_alphabet,kmers)

nullomers = set()
for kmer in kmers:
    if count_occurrences(s,kmer) == 0:
        nullomers.add(kmer)
        
print(s)
print(nullomers)


# <br>
# The mere presence of a single occurrence can be searched for, alternatively to the counting for all the occurrences of a k-mer. If on average k-mer appear more than twice, the just-presence method reduce the time requirement of the procedure since it stops to the first occurrence and does not search for the others. 
# <br>
# <br>
# Python provides a built-in operator, that is inclusion operator `in`, to check for presence of an elements within a set. The operator can also be combined with the logical `not` operator.

# In[19]:


A = {'a','b','c'}
print('a' in A)
print('a' not in A)


# When the `in` operator is applied to strings, it searches whenever a string is contained into another.

# In[26]:


k = 2
kmers = set()
list_words_2('',k,nuc_alphabet,kmers)

nullomers = set()
for kmer in kmers:
    if kmer not in s:
        nullomers.add(kmer)
        
print(s)
print('nullomers:', nullomers)


# ---
# ## Itertools
# 
# Python provides a set of built-in functions to built combinatorial elements. The library is called `itertool` and its documentation is given at https://docs.python.org/3/library/itertools.html .
# <br>
# <br>
# It can be used to perform Cartesian products.

# In[21]:


import itertools 

alphabet = 'acgt'

itertools.product(alphabet, repeat = 2) # cartesian product, equivalent to a nested for-loop

for i in itertools.product(alphabet, repeat = 2):
    print(i)


# That can be converted to combinatorial strings, such as the ones computed in the previous examples. 

# In[22]:


for i in itertools.product(alphabet, repeat = 2):
    print( ''.join(i) )


# And many other combinatorial operations can be performed.

# In[23]:



for i in itertools.product(alphabet, repeat = 2):
    print(''.join(i), end=' ')
print()

# r-length tuples, all possible orderings, no repeated elements
for i in itertools.permutations(alphabet, 2):
    print(''.join(i), end=' ')
print()

# r-length tuples, in sorted order, no repeated elements
for i in itertools.combinations(alphabet, 2):
    print(''.join(i), end=' ')
print()

# r-length tuples, in sorted order, with repeated elements
for i in itertools.combinations_with_replacement(alphabet,2):
    print(''.join(i), end=' ')
print()

