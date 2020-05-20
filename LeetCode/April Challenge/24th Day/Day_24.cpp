class LRUCache {
public:
    int cap;
    list<int>key_list; //stores only keys
    unordered_map<int,int>mp; // stores keys and corresponding values.
	
	
    LRUCache(int capacity) {
        ios::sync_with_stdio(false);
        cin.tie(nullptr);
        cout.tie(nullptr);
        cap = capacity;
    }
    
    int get(int key) {
         if(mp.find(key) == mp.end() )
             return -1;
        else{
            key_list.remove(key);
            key_list.push_back(key);
            return mp[key];
        }
        
    }
    
    void put(int key, int value) {
        if(mp.find(key) != mp.end() ){
            mp.erase(key);
            key_list.remove(key);
        }
        if(key_list.size() == cap){
           int temp = key_list.front();
            key_list.pop_front();
            mp.erase(temp);
        }
        mp[key] = value;
        key_list.push_back(key);
    }
};
