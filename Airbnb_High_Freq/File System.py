"""
File System
Write a file system class, which has two functions: create, and get 
create("/a",1)
get("/a") 
create("/a/b",2)
get("/a/b") 
create("/c/d",1) //Error, because "/c" is not existed 
get("/c") //Error, because "/c" is not existed
"""

class Trie():
    def __init__(self):
        self.paths = {}
        self.content = None
        self.call_back = None
        
    def add(self,directory,content):
        trie = self
        n = len(directory)
        for dir in directory[:-1]:
            if dir not in trie.paths:
                return False
            trie = trie.paths[dir]
            if trie.call_back:
                 trie.call_back()
        trie.paths[directory[-1]] = trie.paths.get(directory[-1],Trie())
        trie = trie.paths[directory[-1]]
        trie.content = content
        return True
        
class File():
    def __init__(self):
        self.trie = Trie()
        
    def create(self,directory,content):
        direct = directory.split('/')[1:]
        if not self.trie.add(direct,content):
            raise Exception('Error')
        
    def get(self,directory):
        direct = directory.split('/')[1:]
        trie = self.trie
        for dir in direct:
            if dir not in trie.paths:
                raise Exception('Error')
            trie = trie.paths[dir]
        return trie.content
    
   def watch(self,directory,function):
        direct = directory.split('/')[1:]
        trie = self.trie
        for dir in direct:
            if dir not in trie.paths:
                raise Exception('Error')
            trie = trie.paths[dir]
        trie.call_back = function
        
"""
def func1():
    print 'haha'
def func2():
    print 'yes'
    
f = File()
f.create("/a",1)
f.get("/a") 
f.create("/a/b",2)
f.get("/a/b") 
f.watch('/a',func1)
f.watch('/a/b',func2)
f.create('/a/b/c',4)
"""

class HashFileSystem():
    def __init__(self):
        self.paths = {}
        self.callPaths = {}
        
    def create(self,path,value):
        last_slash = path.rfind('/')
        if path[:last_slash] and path[:last_slash] not in self.paths:
            raise Exception('Error')
        dir = path.split('/')[1:]
        cur_dir = ''
        for d in dir:
            cur_dir += '/' + d
            if cur_dir in self.callPaths:
                self.callPaths[cur_dir]()
        self.paths[last_slash] = value
        
    def get(self,path):
        if path not in self.paths:
            raise Exception('Error')
        return self.paths[path]
    
   def watch(self,path,function):
        if path not in self.paths:
            raise Exception('Error')
        self.callPaths[path] = function
        
        