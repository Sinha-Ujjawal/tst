class _tst_node:
	def __init__(self, k):
		'''a tst node containing
				[k, data]           
				/   |   \           
				l   m   r           
		k is the split character of the key
		data is the data stored in the node
		l, m and r are the left, middle and right fields respectively
		'''
		self.k = k
		self.key = None
		self.data = None
		self.count = 1 if k == chr(0) else 0
		self.middle = self.right = self.left = None
		
	def __del__(self):
		del self.k, self.key, self.data, self.middle, self.left, self.right, self.count
		
	def isLeftNone(self):
		return self.left == None
		
	def isMiddleNone(self):
		return self.middle == None
		
	def isRightNone(self):
		return self.right == None
		
	def isEmpty(self):
		return self.isLeftNone() and self.isMiddleNone() and self.isRightNone()
		
class tst:
	def __init__(self):
		'''creates a tst object
		'''
		self._root = None
		self._key_count = 0
		
	def __repr__(self):
		A = []
		for i in self:
			A.append(i)
		return 'tst({})'.format(A)
		
	def __iter__(self):
		return self.getAll()
		
	@property
	def key_set(self):
		A = []
		for i in self:
			A.append(i[0])
		return A
		
	@property
	def key_value_set(self):
		A = []
		for i in self:
			A.append(i)
		return A
		
	def __getitem__(self, k):
		return self.getData(k)
		
	def __setitem__(self, k, data):
		self.insert(k, data)
		
	def __delitem__(self, k):
		self.delete(k)
		
	def __len__(self):
		return self.getKeyCount()
		
	def __del__(self):
		self.delAll()
		del self._root, self._key_count
	
	def __getNode(self, k):
		return _tst_node(k)
		
	def __validateInput(self, k, typelist, msg):
		if not isinstance(k, typelist):
			raise TypeError(msg)
	
	def getKeyCount(self):
		'''returns no of keys in the tst trie
		'''
		return self.__getCount(self._root)
	
	def isEmpty(self):
		'''checks if the trie is empty or not
		'''
		return self._root == None
		
	def __getCount(self, root):
		if root:
			return root.count
		return 0
	
	def __insertUtil(self, i, k, len_k, data, root):
		if i < len_k:
			j = k[i]
		else:
			j = chr(0)
		new_node_created = False
		if root == None:
			new_node_created = True
			root = self.__getNode(j)
		
		if j == chr(0) and root.k == chr(0):
			root.key = k
			root.data = data
			return root, new_node_created
		
		if ord(j) < ord(root.k):
			root.left, t = self.__insertUtil(i, k, len_k, data, root.left)
		elif ord(j) > ord(root.k):
			root. right, t = self.__insertUtil(i, k, len_k, data, root.right)
		else:
			root.middle, t = self.__insertUtil(i + 1, k, len_k, data, root.middle)
		if t:
			root.count += 1
		return root, t
	
	def insert(self, k, data = None):
		'''inserts k, data(by default None) pair in the trie
		'''
		self.__validateInput(k, str, 'key k can only be of type str')
		self._root, t = self.__insertUtil(0, k, len(k), data, self._root)
		
	def __restructure(self, root):
		if root != None:
			if root.isMiddleNone():
				if root.isLeftNone():
					t = root.right
					del root
					return t
				elif root.isRightNone():
					t = root.left
					del root
					return t
				else:
					if root.left.isRightNone():
						t = root.left
						t.right = root.right
						del root
						return t
					elif root.right.isLeftNone():
						t = root.right
						t.left = root.left
						del root
						return t
			return root
		
	def __deleteUtil(self, i, k, len_k, root):
		if i < len_k:
			j = k[i]
		else:
			j = chr(0)
		
		if root == None:
			return None, None, False
			
		data = None
		
		if j == chr(0) and root.k == chr(0):
			p = root.right
			data = root.data
			del root
			return p, data, True
	
		if ord(j) < ord(root.k):
			root.left, data, t = self.__deleteUtil(i, k, len_k, root.left)
		elif ord(j) > ord(root.k):
			root. right, data, t = self.__deleteUtil(i, k, len_k, root.right)
		else:
			root.middle, data, t = self.__deleteUtil(i + 1, k, len_k, root.middle)
		if t:
			root.count -= 1
		return self.__restructure(root), data, t
	
	def delete(self, k):
		'''deletes k from the trie and returns data of that key, if no such key then raises KeyError exception
		'''
		self.__validateInput(k, str, 'key k can only be of type str')
		self._root, data, t = self.__deleteUtil(0, k, len(k), self._root)
		if t:
			return data
		else:
			raise KeyError('key {} not in the tree'.format(k))
	
	def __getDataUtil(self, i, k, len_k, root):
		if i < len_k:
			j = k[i]
		else:
			j = chr(0)
		
		if root == None:
			return None
		
		if j == chr(0) and root.k == chr(0):
			return k, root.data
		
		if ord(j) < ord(root.k):
			return self.__getDataUtil(i, k, len_k, root.left)
		elif ord(j) > ord(root.k):
			return self.__getDataUtil(i, k, len_k, root.right)
		else:
			return self.__getDataUtil(i + 1, k, len_k, root.middle)
		
	def getData(self, k):
		'''return data of the key k in the trie, if no such key then raises KeyError exception
		'''
		self.__validateInput(k, str, 'key k can only be of type str')
		t = self.__getDataUtil(0, k, len(k), self._root)
		if t:
			return t[1]
		else:
			raise KeyError('key {} not in the tree'.format(k))
			
	def member(self, k):
		'''checks if the key k is in the trie or not
		'''
		try:
			self.getData(k)
			return True
		except KeyError:
			return False
	
	def __startsWithUtil(self, i, k, len_k, root):
		if i < len_k:
			j = k[i]
		else:
			j = chr(0)
			
		if root == None:
			return None
			
		if j == chr(0):
			return root
		
		if ord(j) < ord(root.k):
			return self.__startsWithUtil(i, k, len_k, root.left)
		elif ord(j) > ord(root.k):
			return self.__startsWithUtil(i, k, len_k, root.right)
		else:
			return self.__startsWithUtil(i + 1, k, len_k, root.middle)
		
	def startsWith(self, k, decreasing = False):
		'''yields all k1, data pair as tuples in sorted order
		with k1 having prefix as k
		'''
		self.__validateInput(k, str, 'key k can only be of type str')
		xnode = self.__startsWithUtil(0, k, len(k), self._root)
		return self.__getAllUtil(xnode, decreasing)
		
	def countStartsWith(self, k):
		'''returns the total no of string that has prefixes k
		'''
		self.__validateInput(k, str, 'key k can only be of type str')
		xnode = self.__startsWithUtil(0, k, len(k), self._root)
		return self.__getCount(xnode)
		
	def printStartsWith(self, k, decreasing = False):
		'''loop over startsWith() and print all k, data
		'''
		if not self.isEmpty():
			for i in self.startsWith(k, decreasing):
				print(i)
		
	def __getAllUtil(self, root, decreasing = False):
		if root != None:
		
			if root.k == chr(0):
				yield root.key, root.data
				
			if not decreasing:
				yield from self.__getAllUtil(root.left, decreasing)
				yield from self.__getAllUtil(root.middle, decreasing)
				yield from self.__getAllUtil(root.right, decreasing)
			else:
				yield from self.__getAllUtil(root.right, decreasing)
				yield from self.__getAllUtil(root.middle, decreasing)
				yield from self.__getAllUtil(root.left, decreasing)
			
	def getAll(self, decreasing = False):
		'''yields all k, data pair as tuples in sorted order
		'''
		return self.__getAllUtil(self._root, decreasing)
		
	def printAll(self, decreasing = False):
		'''loop over getAll() and print all k, data
		'''
		for i in self.getAll(decreasing):
			print(i)
			
	def __delAllUtil(self, root):
		if root != None:
			if root.k == chr(0) and root.right == None:
				del root
				return None
				
			root.left = self.__delAllUtil(root.left)
			root.middle = self.__delAllUtil(root.middle)
			root.right = self.__delAllUtil(root.right)
			
			if root.isEmpty():
				del root
				return None
	
	def delAll(self):
		'''empties the trie
		'''
		self._root = self.__delAllUtil(self._root)
			
	def __minUtil(self, root):
		if root != None:
			if root.left != None:
				return self.__minUtil(root.left)
			if root.k == chr(0):
				return root.key, root.data
			return self.__minUtil(root.middle)
	
	def min(self):
		'''returns min k, data pair as tuple
		'''
		if not self.isEmpty():
			return self.__minUtil(self._root)
			
	def __extractMinUtil(self, root):
		if root != None:
			if root.left != None:
				root.left, minn = self.__extractMinUtil(root.left)
				root.count -= 1
				return self.__restructure(root), minn
			if root.k == chr(0):
				minn = root.key, root.data
				t = root.right
				del root
				return t, minn
			root.middle, minn = self.__extractMinUtil(root.middle)
			root.count -= 1
			return self.__restructure(root), minn
			
	def extractMin(self):
		'''returns and remove min k, data pair as tuple
		'''
		if not self.isEmpty():
			self._root, minn = self.__extractMinUtil(self._root)
			return minn
		
	def __maxUtil(self, root):
		if root != None:
			if root.right != None:
				return self.__maxUtil(root.right)
			if root.k == chr(0):
				return root.key, root.data
			return self.__maxUtil(root.middle)
	
	def max(self):
		'''returns min k, data pair as tuple
		'''
		if not self.isEmpty():
			return self.__maxUtil(self._root)
			
	def __extractMaxUtil(self, root):
		if root != None:
			if root.right != None:
				root.right, maxx = self.__extractMaxUtil(root.right)
				root.count -= 1
				return self.__restructure(root), maxx
			if root.k == chr(0):
				maxx = root.key, root.data
				t = root.right
				del root
				return t, maxx
			root.middle, maxx = self.__extractMaxUtil(root.middle)
			root.count -= 1
			return self.__restructure(root), maxx
			
	def extractMax(self):
		'''returns and remove max k, data pair as tuple
		'''
		if not self.isEmpty():
			self._root, maxx = self.__extractMaxUtil(self._root)
			return maxx
			
	def __successorUtil(self, i, len_k, k, root):
		if i < len_k:
			j = k[i]
		else:
			j = chr(0)
		if root != None:
			t = None
			if j != chr(0):
				if ord(j) < ord(root.k):
					t = self.__successorUtil(i, len_k, k, root.left)
				elif ord(j) > ord(root.k):
					t = self.__successorUtil(i, len_k, k, root.right)
				else:
					t = self.__successorUtil(i + 1, len_k, k, root.middle)
			if t == None:
				if ord(j) <= ord(root.k):
					if root.k != j:
						return self.__minUtil(root.middle)
					else:
						return self.__minUtil(root.right)
			return t
				
	def successor(self, k):
		'''returns the successor of k as k1, data pair tuple
		'''
		self.__validateInput(k, str, 'key k can only be of type str')
		if not self.isEmpty():
			return self.__successorUtil(0, len(k), k, self._root)
			
	def __predecessorUtil(self, i, len_k, k, root):
		if i < len_k:
			j = k[i]
		else:
			j = chr(0)
		if root != None:
			t = None
			if j != chr(0):
				if ord(j) < ord(root.k):
					t = self.__predecessorUtil(i, len_k, k, root.left)
				elif ord(j) > ord(root.k):
					t = self.__predecessorUtil(i, len_k, k, root.right)
				else:
					t = self.__predecessorUtil(i + 1, len_k, k, root.middle)
			if t == None:
				if root.k == chr(0) and j != chr(0):
					return k[:i], root.data
				if ord(j) >= ord(root.k):
					if root.k != j:
						return self.__maxUtil(root.middle)
					else:
						return self.__maxUtil(root.left)
			return t
				
	def predecessor(self, k):
		'''returns the predecessor of k as k1, data pair tuple
		'''
		self.__validateInput(k, str, 'key k can only be of type str')
		if not self.isEmpty():
			return self.__predecessorUtil(0, len(k), k, self._root)
