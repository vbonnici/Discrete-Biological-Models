
# coding: utf-8

# ---
# # Suffix arrays
# The suffix array is a most-used data structure to index texts (strings over any alphabet) such that operations like the search of a substring are made more efficiently witch respect to on-line approaches that do no use indexing structures.
# <br>
# Given a string $s$ and the set of all the suffixes of $s$, the suffix array reports the starting position of the i-th suffix in the lexicographical order.
# <br>
# <br>
# We recall that, the lexicographical order between two strings $a$ and $b$ is defined as:
# - if $|a| = |b|$ then let $i$ being the left-most position where $a$ and $b$ differ, then $a<b  $   if    $  a[i] < b[i]$
# - else $a<b$  if $a$ is a prefix of $b$
# 
# In general, this is not a well-order, even if the alphabet is well-ordered, this is the reason why the quasi-lexicographical order is user (it states that $a<b$ if $|a|<|b|$).
# However, for the purpose regarding the construction of a suffix array we are not interested in quasi-lexicographical order. 

# Given a string $s$, the set if its suffixes can be extracted in the following manner:

# In[1]:


s = 'agctagctagctagtttagct'

suffixes = list()

for i in range(len(s)):
    suffixes.append(s[i:])

for suff in suffixes:
    print(suff)


# Then, the suffixes can be lexicographically sorted via the python function `sorted`.

# In[2]:


for suff in sorted(suffixes):
    print(suff)


# NOTE: the quasi-lexicographical order can be obtained by using the parameter `key` of the function `sorted`. In this manner, the  words are sorted by following the order driven by the function specified in the parameter, and in case of equality the lexicographical order is used.

# In[3]:


qllist = ['a','b','ab','ac','bb','abc', 'bba','bbc']

for suff in sorted(qllist, key = len):
    print(suff)


# A trivial and inefficient way to construct the suffix array is to build a list of pairs, where the first element of the pair is one the suffixes and the second element is its starting position. Because starting position are all different, the `sorted` function sorts the pairs by the lexicographical order of the suffixes.

# In[4]:


s = 'agctagctagctagtttagct'

pairs = list()

for i in range(len(s)):
    pairs.append( (s[i:] ,i) ) 

for p in sorted(pairs):
    print(p)


# Once the pairs are sorted, the suffix array is built by iterating the sorted pairs and by extracting their starting position (namely the second element of the pair).

# In[5]:


print('suffixes'+ ' '*(len(s) - len('suffixes')) + 'suffix_array' )

for p in sorted(pairs):
    print(p[0] + ' '*(p[1]) ,p[1])  
    # a given number of space characters (' '*(p[1])) is added 
    # such that the elements of the suffix array are print on the same column


# <br>
# Actually, we are not interested in storing the ordered set of suffixes, but only in storing the resultant suffix array.
# Thus, the function `get_suffix_array` receives in input a string $s$ and returns only the array.

# In[6]:


def get_suffix_array(s):
    """
    Construct the suffix array of the string s.
    """
    pairs = list()
    for i in range(len(s)):
        pairs.append( (s[i:],i) ) 
    sa = list()
    for p in sorted(pairs):
        sa.append(p[1])
    return sa

sa = get_suffix_array(s)


# <br>
# The list of sorted suffixes can be obtained by iterating over the suffix array an by extracting on the fly the suffix corresponding to the given  starting position given by array. Let $sa$ being the suffix array of a string $s$, then the $i$-th ordered suffix starts in position $sa[i]$, and the suffix corresponds to $s[i:]$. A padding of extra space characters `' '*(sa[i])` is added to the suffix for a well print format.

# In[7]:


def print_suffix_array(s, sa):
    for i in range(len(sa)):
        print(s[sa[i]:] + ' '*(sa[i]), sa[i])
        
print_suffix_array(s,sa)


# ---
# ## LCP intervals and enhanced suffix arrays (ESA)
# Indexing structures based on suffix arrays are enhanced by means of a further array reporting the length of the longest common prefix (LCP) between two consecutive suffixes in the lexicographical order.The LCP value of the first suffix is set to be 0.

# In[8]:


def longest_prefix_length(s, i, j):
    """
        Calculate the length of the longest common prefix between two suffixes, 
        the one in position i and the other in position j, of s
    """
    l = 0
    while (i+l < len(s)) and (j+l < len(s)):
        if s[i+l] != s[j+l]:
            break
        l += 1
    return l


def get_lcp(s,sa):
    """
        Construct the LCP array associated tot he suffix array (sa) of the string s.
        The LCP value of the first suffix is set to be 0.
    """
    lcp = list()
    lcp.append(0)
    for i in range(1,len(sa)):
        lcp.append( longest_prefix_length(s, sa[i], sa[i-1]) )
    return lcp


lcp = get_lcp(s,sa)


# <br>
# The print of the ordered suffixes together with the suffix array is extended to report the lcp values.

# In[9]:


def print_sa_lcp(s,sa,lcp):
    print('index', 'suffixes' + ' '*(len(s)-len('suffixes')), 'SA', 'LCP', sep='\t')
    print('-'*45)
    for i in range(len(sa)):
        print(i, s[sa[i]:] + ' '*(sa[i]), sa[i], lcp[i], sep='\t')

print_sa_lcp(s,sa,lcp)


# <br>
# <br>
# An LCP $k$-interval is defined as a contiguous region of the LCP array, defined by two indexes $i$ and $j$ (with $1 \leq i \leq j \leq |s|$) 
# such that for $ i < x \leq j$, $LCP[x] \geq k$.
# Moreover, $LCP[i-1] < k$ and $LCP[j+1] < k$.
# <br>
# LCP intervals are useful in enumerating the  k-mers occurring in a given string. In fact, for $k=1$ all and only the suffixes starting with the symbol `a` are contiguous listed in he first positions of the suffix array. Moreover, such suffixes have a lcp value grater than 1, except for the first one. starting for the second suffix, the first position where the lcp value is less than 1 is the one identified by the suffix `ct`. More in general an lcp value of 0 occurs each time the corresponding suffix has the first character different from the previous suffix.
# <br>
# In the previous example, the four nucleobases $A,C,G,T$ are recognized by 4 lcp 1-intervals that are $[0,4]$,$[5,8]$,$[9,13]$ and $[14,20]$. Within each interval, the lcp value i greater or equal to 1, except for the first element that has an lcp value of 0 and that identifies the end of the previous interval and the start of the current one.

# An algorithm to retrieve lcp k-intervals uses two indexes, $i$ and $j$, to identified the bounds of the current interval. The $i$ index is the start, and the $j$ index is the end  (not included).
# <br>
# The algorithm start with $i=0$ and $j=1$, increases the value of $j$ until $lcp[j] \geq k$ (and until $j$ is a valid index, namely it is less than the length of the array). When $lcp[j] < k$, the algorithm stops and return the interval $[i,j]$. Subsequently, $i$ is set to be the current value of $j$, $j$ is increased by 1 and the search in repeated. The algorithm continues until $i$ is less then the length of the array. 

# In[10]:


def print_sa_lcp_region(s,sa,lcp, i,j):
    print('-'*40)
    print('interval')
    for x in range(i,j):
        print(x,s[sa[x]:] +' '*(sa[x]), sa[x], lcp[x], sep='\t')
    #print('.'*40)


k = 1
i = 0
while i < len(s):
    j = i + 1
    while (j < len(s)) and (lcp[j] >= k):
        j += 1
        
    print_sa_lcp_region(s,sa,lcp, i,j)
    print('k-mer:', s[ sa[i]:sa[i]+k] )
    
    i = j


# <br>
# The above algorithm results not suitable for value of $k$ grater than 1, in fact when it is applied to extract 2-mers unwanted intervals, thus unwanted words, are retrieved.
# In particular, the 1-mer $t$ is produced, which is due to the fact that the algorithm extracts prefixes that are shorter than the given value of $k$.
# 

# In[11]:


k = 2
i = 0
while i < len(s):
    j = i + 1
    while (j < len(s)) and (lcp[j] >= k):
        j += 1
        
    print_sa_lcp_region(s,sa,lcp, i,j)
    print('k-mer:', s[ sa[i]:sa[i]+k] )
    
    i = j


# <br>
# In order to avoid the extraction of such extra intervals, the algorithm has to take into account the the right .intervals are not contiguous but they are interleaved with intervals tat must be discarded. The condition for the discarding of such intervals is given by the check of their proximity with the end of the string. 
# 

# In[12]:


k = 2
i = 0
while i < len(s):
    while (i < len(s)) and  (sa[i] > len(s) - k - 1): # check
        i += 1
    if i == len(s): # there are no more valid intervals
        break
        
    j = i + 1
    while (j < len(s)) and (lcp[j] >= k):
        j += 1
        
    print_sa_lcp_region(s,sa,lcp, i,j)
    print('k-mer:', s[ sa[i]:sa[i]+k] )
    
    i = j


# ---
# ## Some notes on the enhanced suffix array
# 1. Due to the lexicographically construction of the suffix array, the enumeration of k-mer via lcp k-intervals implicitly follows the lexicographical order on enumerating the k-mers.
# 2. The enhanced suffix array implicitly contains the complete set $D(s)$, which includes every $k$-mer occurring in $s$ for $1 \leq k \leq |s|$.

# ---
# ## Informational genomics via ESA (and NELSA)
# Usually, sequenced genomes present an extra symbol, coded with an `N`, which represent an ambiguity in determining a specific nucleotided at a given position of the genome.
# The execution of the previous approach on such sequences produces k-mers that may contain `N` symbols.
# However, is it desirable to skip such k-mers from the enumeration.
# <br>
# The issue is solved with an approach similar to the one used to discard k-mers shorter than the desired word length $k$.
# A modified algorithm discards suffixes which have a symbol `N` within the initial $k$ characters.
# <br>
# In order to increase the efficiency in time complexity, a further array is computed. The array, called `NS`, takes trace of the distance from the starting position of the suffix to the closest `N` character on the right of such position.

# In[13]:


def distance_to_n(s,i):
    j = i
    while (j<len(s)) and (s[j] != 'N'):
        j += 1
    return j - i

def get_ns_array(s,sa):
    return [  distance_to_n(s,sa[i]) for i in range(len(s)) ]
    

def print_sa_lcp_ns(s,sa,lcp, ns):
    print('index', 'suffixes' + ' '*(len(s)-len('suffixes')), 'SA', 'LCP', 'NS', sep='\t')
    print('-'*60)
    for i in range(len(sa)):
        print(i, s[sa[i]:] + ' '*(sa[i]), sa[i], lcp[i], ns[i], sep='\t')

        
        
s = 'agctagNctagctagNtttagctN'


sa = get_suffix_array(s)
lcp = get_lcp(s,sa)
ns = get_ns_array(s,sa)


print_sa_lcp_ns(s,sa,lcp,ns)
print('-'*60)


# Two further conditions are included on enumerating k-mers.
# <br>
# The first one is due to a modification of the definition of the lcp k-interval such that it is extended by the condition $LCP[x] \geq k$. This ensures that interval do not contains k-mers having a `N` character in the initial $k$ positions.
# <br>
# The second condition is applied to discard unwanted intervals that interleave valid ones.

# In[14]:


def print_sa_lcp_ns_region(s,sa,lcp,ns, i,j):
    print('-'*60)
    print('interval')
    for x in range(i,j):
        print(x,s[sa[x]:] +' '*(sa[x]), sa[x], lcp[x], ns[x], sep='\t')
   

k = 3
i = 0
while i < len(s):
    while  (i < len(s)) and  ( (sa[i] > len(s) - k - 1)  or (ns[i] < k) ): # second further condition
        i += 1
    if i == len(s):
        break
        
    j = i+1
    while (j < len(s)) and (lcp[j] >= k) and (ns[i] >= k): # first further condition
        j += 1
        
    print_sa_lcp_ns_region(s,sa,lcp,ns, i,j)
    print('k-mer:', s[ sa[i]:sa[i]+k] )
    i = j


# <br>
# The following code povides a faster implementation of the construction fo the N array. It costructs and inverse suffix array, such that for each poistion $i$in the string, the corresponding position of the $i$-th suffix in the suffix array is obtanined in constant time. Then, starting form the end of the string, it takes traces of the last poisiotn, ont he right, where the symbol N has been found, thus it assigns the distance between the current position and the last right occurrence of the N.

# In[16]:


def fast_get_ns_array(s, sa):
    inv_sa = [0 for _ in range(len(sa))]
    for i in range(len(sa)):
        inv_sa[ sa[i] ] = i
    
    ns = [0 for _ in range(len(sa))]
    lastn = len(s)
    for i in range(len(s)-1,-1,-1):
        if s[i] == 'N':
            lastn = i
        ns[ inv_sa[i] ] = lastn - i
    return ns
                               
                               
fns = fast_get_ns_array(s, sa)
print(len(fns), fns)

ns = get_ns_array(s, sa)
print(len(ns), ns)

assert ns == fns


# ---
# ## Implementing an iterator
# In python, iterators can be implemented in several ways. We focus on defining iterator b objects.
# Iterators are special types of objects which implement the `__iter__` and `__next__` methods. Iterators maintain an internal state which refers to the current iterated element. 
# <br>
# The following examples illustrates how to build an iterator that iterates over the integer numbers starting from 1. The internal state is represented by the internal variable `__i`. Each time the method `next` is called on the iterator, the internal state is update with a forward operation and the element resulting form such operation is returned. 
# 

# In[17]:


class my_iterator:
    __i = 0
    
    def __init__(self):
        self.__i = 0
        
    def __next__(self):
        self.__i += 1
        return self.__i
    
it = my_iterator()
print(next(it))
print(next(it))


# One important thing to notice and to remember is that the method `next` is called in order to retrieve the elements of the iteration. This means that, after the creation of the iterator, the first element is retrieved only after a call of the `next` method. For this reason, in order to start the iteration form the value 1, the initial state is set to 0. <vr>
# <br>
#     
# The given implementation is still not suitable to be used in `for` statements because the `__iter__` method has to be defined. The simplest way to defined the method is shown below.

# In[18]:


class my_iterator:
    __i = 0
    
    def __init__(self):
        self.__i = 0
        
    def __iter__(self):
        return self
        
    def __next__(self):
        self.__i += 1
        return self.__i

it = my_iterator()
for n in it:
    print(n)
    if n > 10:
        break


# The object provides an iteration over integer numbers without any limit. In fact, it can iterate up to infinite. The method `__next__` has to raise a `StopIteration` exception in order to stop the interaction at a specific state. For example, an iterator to enumerate integers from 1 to 10 is the following one.

# In[19]:


class my_iterator:
    __i = 0
    __limit = 10
    
    def __init__(self):
        self.__i = 0
        
    def __iter__(self):
        return self
        
    def __next__(self):
        self.__i += 1
        if self.__i <= self.__limit:
            return self.__i
        else:
            raise StopIteration

it = my_iterator()
for n in it:
    print(n)


# The raise of a `StopIteraction` exception is a special event that, in case of iterator objects, is not threaded like a common exception raise. In fact, it is not cached by the try-except statement.

# In[20]:


it = my_iterator()
try:
    for n in it:
        print(n)
except:
    print('an exception has been arised')


# In[21]:


def m_function():
    raise StopIteration

try:
    my_function()
except:
    print('an exception has been arised')


# ---
# ## Implementing a k-mer iterator
# According to the method shown before for the enumeration of k-mers based on enhanced suffix arrays, a k-mer iterator has four internal fixed parameters that are the indexed string, the suffix array, the LCP array and the word length $k$. The variables of the internal state are the start and the end of the current LPC k-interval, identified by the private variables $i$ and $j$ respectively. Each time the `next` method is called on the iterator, the search for the successive interval starts. If two valid limits for the next interval are found, the iterator pauses the iteration and return the k-mer corresponding to the found interval. If no more intervals are found, the iterator rises a `StopIteration` exception. 
# <br>
# In addition, the iterator informs about the multiplicity of the current k-mer and the starting position of its occurrences along the string. The information is provided b the two methods `multiplicity` and `positions`, respectively.
# We recall, that the multiplicity is given by the size of the k-interval on the LCP array, and the set of occurring positions is the corresponding slice on the suffix array. Since the suffix array only ensures the lexicographical order of the suffix, the positions are not sorted. 

# In[22]:


class ESAIterator:
    __s = None
    __k = 0
    __sa = None
    __lcp = None
    __i = 0
    __j = 0
    
    def __init__(self, s, k, sa = None, lcp = None):
        self.__s = s
        self.__k = k
        
        if sa == None:
            self.build_sa()
        else:
            self.__sa = sa
            
        if lcp == None:
            self.build_lcp()
        else:
            self.__lcp = lcp

    def build_sa(self):
        print("building suffix array...")
        suffixes = list()
        for i in range(len(self.__s)):
            suffixes.append( (self.__s[i:] + self.__s[:i] ,i) ) 
        self.__sa = list()
        for suff in sorted(suffixes):
            self.__sa.append(suff[1])
        print('done')
        
        
    def longest_prefix_length(s, i, j):
        l = 0
        while (i+l < len(s)) and (j+l < len(s)):
            if s[i+l] != s[j+l]:
                break
            l += 1
        return l

    def build_lcp(self):
        print('building lcp array...')
        self.__lcp = list()
        self.__lcp.append(0)
        for i in range(1,len(self.__sa)):
            self.__lcp.append( ESAIterator.longest_prefix_length(self.__s, self.__sa[i], self.__sa[i-1]) )
        print('done')
    
    def get_sa(self):
        return self.__sa
    
    def get_lcp(self):
        return self.__lcp
        
    def __iter__(self):
        return self
    def __next__(self):
        if self.__i < len(self.__s):
            self.__i = self.__j
            
            while (self.__i < len(self.__s)) and  (self.__sa[self.__i] > len(self.__s) - self.__k - 1):
                self.__i += 1
            if self.__i == len(self.__s):
                raise StopIteration
            self.__j = self.__i+1
            while ( self.__j < len(self.__s) ) and (self.__lcp[self.__j] >= self.__k):
                self.__j += 1
            ret = self.__s[ self.__sa[self.__i] : self.__sa[self.__i] + self.__k ]
            #self.__i = self.__j #!!!!!!
            return ret
        else:
            raise StopIteration
            
    def multiplicity(self):
        return self.__j - self.__i
    
    def positions(self):
        return self.__sa[self.__i : self.__j]
    
    
it = ESAIterator('agctagctagctagtttagct', 3, sa=None, lcp=None)

for kmer in it:
    print(kmer, it.multiplicity(), it.positions())


# In addition, the iterator builds by it self the suffix and the LCP arrays if they are not proved by the user. The construction of the arrays is an expensive step, thus, this is not a good practice if multiple iterators has to be launched on the same strings, even with different values of $k$ .

# In[23]:


s = 'agctagctagctagtttagct'

k = 2
it = ESAIterator(s, k, sa=None, lcp=None)

sa = it.get_sa()
lcp = it.get_lcp()

print(str(k)+"-mers")
for kmer in it:
    print(kmer, it.multiplicity(), it.positions())
 

k = 3
it = ESAIterator(s, k, sa, lcp)

print(str(k)+"-mers")
for kmer in it:
    print(kmer, it.multiplicity(), it.positions())  


# There are many more efficient ways to built the suffix array and the LCP array. One of them is provided by the module `pysuffixarray`, that can be installed by the command `pip install pysuffixarray`.

# In[24]:


from pysuffixarray.core import SuffixArray
sa_obj = SuffixArray(s)
sa_sa = sa_obj.suffix_array()
lcp_sa = sa_obj.longest_common_prefix()

print_sa_lcp(s,sa_sa,lcp_sa)


# In[25]:


from pysuffixarray.core import SuffixArray
sa_obj = SuffixArray(s)
sa_sa = sa_obj.suffix_array()[1:]
lcp_sa = sa_obj.longest_common_prefix()[1:]

k = 3
it = ESAIterator(s, k, sa_sa, lcp_sa)

print(str(k)+"-mers")
for kmer in it:
    print(kmer, it.multiplicity(), it.positions()) 


# <br>
# Similarly, an iterator based on the NESA data structure is implemented.

# In[26]:


class NESAIterator:
    __s = None
    __k = 0
    __sa = None
    __lcp = None
    __ns = None
    __i = 0
    __j = 0
    
    def __init__(self, s, k, sa = None, lcp = None, ns = None):
        self.__s = s
        self.__k = k
        
        if sa == None:
            self.build_sa()
        else:
            self.__sa = sa
            
        if lcp == None:
            self.build_lcp()
        else:
            self.__lcp = lcp
            
        if ns == None:
            self.build_ns()
        else:
            self.__ns = ns

    def get_k(self):
        return self.__k
    
    def reset(self):  #<--------------------------------------------------------------------------------
        self.__i = 0
        self.__j = 0
            
    def build_sa(self):
        print("building suffix array...")
        suffixes = list()
        for i in range(len(self.__s)):
            suffixes.append( (self.__s[i:] + self.__s[:i] ,i) ) 
        self.__sa = list()
        for suff in sorted(suffixes):
            self.__sa.append(suff[1])
        print('done')
        
        
    def longest_prefix_length(s, i, j):
        l = 0
        while (i+l < len(s)) and (j+l < len(s)):
            if s[i+l] != s[j+l]:
                break
            l += 1
        return l

    def build_lcp(self):
        print('building lcp array...')
        self.__lcp = list()
        self.__lcp.append(0)
        for i in range(1,len(self.__sa)):
            self.__lcp.append( NESAIterator.longest_prefix_length(self.__s, self.__sa[i], self.__sa[i-1]) )
        print('done')
    
    def build_ns(self):
        print('building ns array...')
        inv_sa = [0 for _ in range(len( self.__sa))]
        for i in range(len(self.__sa)):
            inv_sa[  self.__sa[i] ] = i

        self.__ns = [0 for _ in range(len( self.__sa))]
        lastn = len(self.__s)
        for i in range(len(self.__s)-1,-1,-1):
            if self.__s[i] == 'N':
                lastn = i
            self.__ns[ inv_sa[i] ] = lastn - i
        print('done')
        
    def get_sa(self):
        return self.__sa
    
    def get_lcp(self):
        return self.__lcp
    
    def get_ns(self):
        return self.__ns
        
        
    def __iter__(self):
        return self
    def __next__(self):
        if self.__i < len(self.__s):
            self.__i = self.__j
            
            while (self.__i < len(self.__s)) and  ( (self.__sa[self.__i] > len(self.__s) - self.__k - 1) or (self.__ns[self.__i] < self.__k) ):
                self.__i += 1
            if self.__i == len(self.__s):
                raise StopIteration
            self.__j = self.__i+1
            while ( self.__j < len(self.__s) ) and (self.__lcp[self.__j] >= self.__k) and (self.__ns[self.__i] >= self.__k) :
                self.__j += 1
            ret = self.__s[ self.__sa[self.__i] : self.__sa[self.__i] + self.__k ]
            #self.__i = self.__j #!!!!!!
            return ret
        else:
            raise StopIteration
            
    def multiplicity(self):
        return self.__j - self.__i
    
    def positions(self):
        return self.__sa[self.__i : self.__j]
    
    
it = NESAIterator('agctagctagNctagtttagctN', 3, sa=None, lcp=None, ns = None)

print('iterating '+str(it.get_k())+'-mers...')
for kmer in it:
    print(kmer, it.multiplicity(), it.positions())


# An useful operation with which to extend the iterator is the `reset` function, which restores the internal state to the initial value.

# In[27]:


print('reiterating '+str(it.get_k())+'-mers...')
it.reset() #<--------------------------------------------------------------------------------
kmer = next(it) #<--------------------------------------------------------------------------------
print("first: ",kmer, it.multiplicity(), it.positions())

for kmer in it:
    print(kmer, it.multiplicity(), it.positions())

