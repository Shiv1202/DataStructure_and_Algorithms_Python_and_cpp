class Trie {
public:
    /** Initialize your data structure here. */
    unordered_map<char,Trie*> children;
    bool isEndOfword;
    public:
    Trie() {
        isEndOfword=false;
        for(int i=0;i<26;i++)
        {
            children.insert({NULL,NULL});
        }
    }
    
    /** Inserts a word into the trie. */
    void insert(string word) {
        Trie* curr= this;
        for(auto i: word)
        {
            if(curr->children.find(i)==curr->children.end())
            {
                Trie* temp=new Trie();
                curr->children.insert({i,temp});
            }
            curr=curr->children[i];
        }
        curr->isEndOfword=true;
    }
    
    /** Returns if the word is in the trie. */
    bool search(string word) {
        Trie* curr=this;
        for(auto i: word)
        {
            if(curr->children.find(i)==curr->children.end())
                return false;
            curr=curr->children[i];
        }
        return curr->isEndOfword;
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string prefix) {
        Trie* curr=this;
        for(auto i: prefix)
        {
            if(curr->children.find(i)==curr->children.end())
                return false;
            curr=curr->children[i];
        }
        return true;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */
