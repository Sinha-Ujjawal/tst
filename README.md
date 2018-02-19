## tst(Ternary Search Trie)
>'Trie' comes from the word 'Re**trie**val'. In computer science, a **ternary search tree** is a type of **trie** (sometimes called a **prefix tree**) where nodes are arranged in a manner similar to a **binary search tree**, but with up to **three children** rather than the binary tree's limit of two. Like other prefix trees, a ternary search tree can be used as an associative map structure with the ability for incremental string search. However, ternary search trees are more space efficient compared to standard prefix trees, at the cost of speed. Common applications for ternary search trees include **spell-checking** and **auto-completion**. For more information visit https://en.wikipedia.org/wiki/Ternary_search_tree.

##### How to use:

  *description*: **`tst()`**
  
  *Space-Complexity*: **`O(nk)`** *where **n** is the no of keys in the tree and **k** is the avg length of the keys*
  
  ```python
  import tst
  
  ob = tst.tst() 
  # Now u cud add keys and values/data to the dictionary object ob
  ```
  
##### insert:

  *description*: **`insert(k, data = None)`** *it **inserts k, data (by default None)** to the dictionary*
  
  *Time-Complexity*: **`O(|k|)`** *where **|k|** is the length of the key **k*** 
  
  ```python
  ob.insert('1001', 'apple') # or ob['1001'] = 'apple'
  ob.insert('1002', 'banana')
  ob.insert('1003') # or ob['1003'] = None
  ob.insert('1004', 'orange')
  ob.insert('2001', 'pen')
  ob.insert('2002', 'pencil')
  ```

##### delete:

  *description*: **`delete(k)`** *it **deletes k** from the dictionary, also returns **data** at that key, if no such key then raises a **KeyError** exception*
  
  *Time-Complexity*: **`O(|k|)`** *where **|k|** is the length of the key **k*** 
  
  ```python
  ob.delete('1001') # will remove and return 'apple'
  # or del ob['1001'], but this will not return anything
  ```

##### getData:

  *description*: **`getData(k)`** *it returns **data** at key **k**, if no such key then raises a **KeyError** exception*
  
  *Time-Complexity*: **`O(|k|)`** *where **|k|** is the length of the key **k*** 
  
  ```python
  print(ob.getData('1001')) # or print(ob['1001'])
  # will print 'apple' on the console
  ```
  
##### member:

  *description*: **`member(k)`** *it returns **True** if the key **k** is present in the tree*
  
  *Time-Complexity*: **`O(|k|)`** *where **|k|** is the length of the key **k*** 
  
  ```python
  print(ob.member('1001'))
  # will print True on the console
  ```
  
##### min:

  *description*: **`min()`** *it returns **min(k, data)** as **tuple***
  
  *Time-Complexity*: **`O(|k|)`** *where **|k|** is the length of the key **k*** 
  
  ```python
  print(ob.min())
  # will print ('1001', 'apple') on the console
  ```
  
##### extractMin:

  *description*: **`extractMin()`** *it returns and removes **min(k, data)** as **tuple***
  
  *Time-Complexity*: **`O(|k|)`** *where **|k|** is the length of the key **k*** 
  
  ```python
  print(ob.extractMin())
  # will print and remove ('1001', 'apple')
  ```
  
##### max:

  *description*: **`max()`** *it returns **max(k, data)** as **tuple***
  
  *Time-Complexity*: **`O(|k|)`** *where **|k|** is the length of the key **k*** 
  
  ```python
  print(ob.max())
  # will print ('2002', 'pencil') on the console
  ```
  
##### extractMax:

  *description*: **`extractMax()`** *it returns and removes **max(k, data)** as **tuple***
  
  *Time-Complexity*: **`O(|k|)`** *where **|k|** is the length of the key **k*** 
  
  ```python
  print(ob.extractMax())
  # will print and remove ('2002', 'pencil')
  ```
  
##### getKeyCount:

  *description*: **`getKeyCount()`** *it returns the no of keys in the dictionary*
  
  *Time-Complexity*: **`O(1)`**
  
  ```python
  print(ob.getKeyCount()) # or print(len(ob))
  # will print 6 on the console
  ```

##### isEmpty:

  *description*: **`isEmpty()`** *it returns **True** if the tree is empty, otherwise returns **False***
  
  *Time-Complexity*: **`O(1)`**
  
  ```python
  print(ob.isEmpty())
  # will print False on the console
  ```

##### getAll:

  *description*: **`getAll(decreasing = False)`** *it returns a **generator** that generate **(k, data)** as **tuples**, if **decreasing** is **True** then generate in decreasing order*
  
  *Time-Complexity*: **`O(n|k|)`** *where **n** is the no of keys in the tree and **|k|** is the avg length of the keys* 
  
  ```python
  for i in ob.getAll():
      print(i)
  # will print
  # ('1001', 'apple')
  # ('1002', 'banana')
  # ('1003', None)
  # ('1004', 'orange')
  # ('2001', 'pen')
  # ('2002', 'pencil')
  ```
  
##### printAll:

  *description*: **`printAll(decreasing = False)`** *it just uses **getAll()** and print the generated items, if **decreasing** is **True** then prints in decreasing order*
  
  *Time-Complexity*: **`O(n|k|)`** *where **n** is the no of keys in the tree and **|k|** is the avg length of the keys* 
  
  ```python
  ob.printAll()
  # will print
  # ('1001', 'apple')
  # ('1002', 'banana')
  # ('1003', None)
  # ('1004', 'orange')
  # ('2001', 'pen')
  # ('2002', 'pencil')
  ```

##### delAll:

  *description*: **`delAll()`** *it just deletes all the keys from the tree*
  
  *Time-Complexity*: **`O(n|k|)`** *where **n** is the no of keys in the tree and **|k|** is the avg length of the keys* 
  
  ```python
  ob.delAll()
  # will delete
  # ('1001', 'apple')
  # ('1002', 'banana')
  # ('1003', None)
  # ('1004', 'orange')
  # ('2001', 'pen')
  # ('2002', 'pencil')
  ```

##### startsWith:

  *description*: **`startsWith(k, decreasing = False)`** *it returns a **generator** that generate **(k1, data)** as **tuples**, here **k1** has the prefix **k**, if **decreasing** is **True** then generate in decreasing order*
  
  *Time-Complexity*: **`O(n|k|)`** *where **n** is the no of keys with prefix **k** in the tree and **|k|** is the avg length of the keys* 
  
  ```python
  for i in ob.startsWith('100'):
      print(i)
  # will print
  # ('1001', 'apple')
  # ('1002', 'banana')
  # ('1003', None)
  # ('1004', 'orange')
  ```
  
##### printStartsWith:

  *description*: **`printStartsWith(decreasing = False)`** *it just uses **startsWith()** and print the generated items, if **decreasing** is **True** then prints in decreasing order*
  
  *Time-Complexity*: **`O(n|k|)`** *where **n** is the no of keys in the tree and **|k|** is the avg length of the keys* 
  
  ```python
  ob.printStartsWith('100')
  # will print
  # ('1001', 'apple')
  # ('1002', 'banana')
  # ('1003', None)
  # ('1004', 'orange')
  ```
  
##### successor:

  *description*: **`successor(k)`** *it **returns k1, data** as **tuple** where **k1** is the **successor** of **k***
  
  *Time-Complexity*: **`O(|k|)`** ***|k|** is the length of **k*** 
  
  ```python
  print(ob.successor('1000'))
  # will print
  # ('1001', 'apple')
  print(ob.successor('1001'))
  # will print
  # ('1002', 'banana')
  ```

##### predecessor:

  *description*: **`predecessor(k)`** *it **returns k1, data** as **tuple** where **k1** is the **predecessor** of **k***
  
  *Time-Complexity*: **`O(|k|)`** ***|k|** is the length of **k*** 
  
  ```python
  print(ob.predecessor('2000'))
  # will print
  # ('1004', 'orange')
  print(ob.predecessor('1003'))
  # will print
  # ('1002', 'banana')
  ```

##### __iter__:

  *description*: **`__iter__()`** *the tst object is **iterable***
  
  *Time-Complexity*: **`O(n|k|)`** *where **n** is the no of keys in the tree and **|k|** is the avg length of the keys* 
  
  ```python
  for i in ob:
      print(i)
  # will print
  # ('1001', 'apple')
  # ('1002', 'banana')
  # ('1003', None)
  # ('1004', 'orange')
  # ('2001', 'pen')
  # ('2002', 'pencil')
  ```

##### __repr__:

  *description*: **`__repr__()`**
  
  *Time-Complexity*: **`O(n|k|)`** *where **n** is the no of keys in the tree and **|k|** is the avg length of the keys* 
  
  ```python
  print(ob)
  # will print
  # tst([('1001', 'apple'), ('1002', 'banana'), ('1003', None), ('1004', 'orange'), ('2001', 'pen'), ('2002', 'pencil')])
  ```
