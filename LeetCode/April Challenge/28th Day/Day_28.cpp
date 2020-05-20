class FirstUnique {
public:
    deque <int> dq;
    map <int, int> look;
    FirstUnique(vector<int>& nums) {
        
        for(auto i : nums)
            add(i);
    }
    
    int showFirstUnique() {
        if(dq.size()==0)
            return -1;
        
        while( dq.size()>0 && look.find(dq[0]) != look.end() && (look.find(dq[0])->second) >= 2)
            dq.pop_front();
        
        if(dq.size()==0)
            return -1;
        
        return dq[0];
    }
    
    void add(int value) {
        if(look.find(value) != look.end())
            look[value]+=1;
        else
            look[value]=1;
        
        dq.push_back(value);
    }
};

/**
 * Your FirstUnique object will be instantiated and called as such:
 * FirstUnique* obj = new FirstUnique(nums);
 * int param_1 = obj->showFirstUnique();
 * obj->add(value);
 */
