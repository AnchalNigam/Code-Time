class TrieNode:
  def __init__(self):
    self.children = [None] * 26
    self.isEndOfWord = False

class Trie:
  def __init__(self):
      self.root = self.initializeTrieNode()
  def initializeTrieNode(self):
    return TrieNode()
  def getIndex(self, char):
    return ord(char)-ord('a')
  # o(len(word))
  def insert(self, word):
    temp = self.root
    for char in word:
      index = self.getIndex(char)
      if(not temp.children[index]):
        temp.children[index] = self.initializeTrieNode()
      temp = temp.children[index]
    temp.isEndOfWord = True
  # o(len(wordToSearch))  
  def search(self, wordToSearch):
    temp = self.root
    for char in wordToSearch:
      index = self.getIndex(char)
      if not temp.children[index]:
        return False
      temp = temp.children[index]
    return temp.isEndOfWord
  # o(len(prefix))  
  def startsWith(self, prefix):
    temp = self.root
    for char in prefix:
      index = self.getIndex(char)
      if not temp.children[index]:
        return False
      temp = temp.children[index]
    return True

      



trie = Trie()
trie.insert("apple")
trie.insert("apps")
trie.insert("bac")

print(trie.startsWith("ap"))


# I have understood trie...basically it is of linkedlist node type...where characters or acc
# to questn we store chars and then one is to track end of word/entity. we start making trie
# by storng refernce of new trie ..children[index] store reference to next trienode..
# in tis way we connect chars using trie node and end me true kr dete h to track its end of word
# for better understading check striver trie playlist - https://www.youtube.com/watch?v=dBGUmUQhjaM&list=PLgUwDviBIf0pcIDCZnxhv0LkHf5KzG9zp&index=1