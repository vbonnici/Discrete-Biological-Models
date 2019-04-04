
# coding: utf-8

# # Extraction of genomic dictionaries
# 
# Given a string $s$ we would like to understand if it is written in the genomic alphabet.
# <br>
# We can use the `set` data structure, that is a modifiable collection of elements with no repetitions.
# <br>
# We iterate over the positions of $s$ and extract the characters at the given position

# In[22]:


s = 'agctaggaggatcgccagat'

alphabet = set()
for i in range( len(s) ):
    alphabet.add( s[i] )
    
print("your alphabet is: ", alphabet)


# <br>
# Alternatively, since a string is an iterable object, we can iterate over the characters of $s$ with no indication about their position.

# In[23]:


alphabet = set()
for c in s:
    alphabet.add( c )
    
print("your alphabet is: ", alphabet)


# <br>
# The `set` data structure does not assure any specific order regarding the elements contained in it. Thus multiple runnings of the same source code can generate the same set but printing the symbols in a different order.
# <br>
# The `sorted` function returns a list of sorted elements.

# In[24]:


print("your sorted alphabet is: ", sorted(alphabet) )


# <br>
# The `sorted` function requires that there must exist an ordering relation between the elements of the input collection.
# <br>
# The following instructions generate an error because there is no defined ordering relation between string (or simple characters) and integers.

# In[25]:


myset = {'a', 0}
print(sorted(myset))


# <br>
# The way in which lists and sets (but more in general any built-in data structure) are printed is defined by python.
# <br>
# List are delimited by square brackets, while set are delimited by curly brackets, and elements are separated by commas.
# <br>
# However, we would like to personalize the print of our alphabet.
# <br>
# A first approach could be the creation of an empty string that will be concatenated to the symbols of the alphabet interleaved by a separator character.

# In[26]:


alpha_string = ''
for a in sorted(alphabet): # sets are iterable objects,thus they cna be used for cicling
    alpha_string = alpha_string + ',' + a
print('your sorted aplhabet is: ' + alpha_string)


# <br>
# Since the first comma is unwanted, we can extract the created string without the first character.

# In[27]:


print('your sorted aplhabet is: ' + alpha_string[1:])


# The same string can be obtained by using a function defined for the string object, called `join`. Given a string and a collection  of elements, the `join` function concatenate the element by putting a copy of the string between them.

# In[28]:


print( ','.join(alphabet) )


# ---

# ## List comprehension
# List comprehension provides a concise way to create lists.
# <br>
# The are in the form:

# In[ ]:


[ <generated values> <for, one or more> <filters> ]


# Values are generated in the middle block of the form (the one that contains the for statements), and filters can be applied to the generated values.
# <br>
# For example, we want to create a list which contains the numbers from 1 to 10

# In[12]:


[ i for i in range(1,11)]


# We can also generate the numbers multiples of 2 form 2 to 10:

# In[14]:


[i for i in range(2,11) if (i % 2) == 0]


# <br>
# We can use the `join` function as well.

# In[16]:


','.join( [ i for i in range(0,11)] )


# However, we need to remember that the function concatenates the given string with the elements. If those elements are not strings, then the concatenation operation between a string and any other type of object is not defined in python. Thus we need to explicitly cast the elements to be strings.

# In[18]:


','.join( [ str(i) for i in range(0,11)] )


# In[29]:


print("your sorted alphabet is: " + ','.join( [ str(a) for a in sorted(alphabet)] ) )


# ---

# ## Extraction for $k > 1$
# The extraction of the alphabet of a string correspond to the extraction of the 1-mers contained in the string. The procedure can be generalized to extract 2-mers in the following manner:

# In[31]:


words = set()
for i in range(len(s)):
    words.add( s[i:i+2] )
print( words )


# However, a problem arise. The extracted set of 2-mers contains a 1-mer, in the specific 't'.
# <br>
# The procedure can be represented as a sliding window, having size equal to two, and that starts from the first position fot he string extract the first 2-mer and, subsequently, extracted the other 2-mers by moving forward of one step.
# <br>
# An easy to visualize all the extracted windows is to append them to a list and then printing the list:

# In[32]:


words = list()
for i in range(len(s)):
    words.append( s[i:i+2] )
print(s)
print( words )


# <br>
# The last windows is positioned on the last character of the string and it extracts the character it self and an inexistent position that go over the string.
# Thus, the windows must be stopped one position before.

# In[33]:


words = list()
for i in range(len(s) - 1):
    words.append( s[i:i+2] )
print(s)
print( words )


# <br>
# We recall that, given a string $s$ the number of k-mers (with duplicates) that are contained in the string equals $|s| - k + 1$. 
# <br>
# Such a value is exactly the last available position form which a window of size $k$ does not exceed the right-most limit of the string.

# In[36]:


k = 2
words = list()
for i in range(len(s) -k +1): # the number of words of lenght k is |s|-k+1
    words.append( s[i:i+k] )
print( words )


# In[35]:


print( set(words) )


# ---
# ## Using functions
# 
# The generalized procedure for the extraction if k-mers from a string can be encapsulated into a function.
# <br>
# The function `get_kmers` takes as input the string $s$ and the word length $k$, and it returns the set of k-mers occurring in $s$.

# In[3]:


def get_kmers(s, k):
    """ This function return the set of k-mers that occur in a given string """
    kmers = set()
    for i in range(len(s) - k +1):
        kmers.add(s[i:i+k])
    return kmers

kmers = get_kmers(s,3)
print(kmers)


# <br>
# Functions are documented by writing a multi-line string immediately after the function signature.
# <br>
# Then, the documentation string is used by the `help` command to given information tot he user about the specific function.

# In[4]:


help(get_kmers)


# Additional information can also be retrieved via the `?` command.

# In[5]:


get_ipython().run_line_magic('pinfo', 'get_kmers')

