class StockSpanner {
public:
    vector<pair<int, int>> vec;
    StockSpanner() {
        
    }
    
    int next(int price) {
        int count = 1;
        while(vec.size()>0 && vec[vec.size()-1].first<=price)
        {
            count+=vec[vec.size()-1].second;
            vec.pop_back();
        }
        vec.push_back(make_pair(price,count));
        
        return count;
    }
};

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner* obj = new StockSpanner();
 * int param_1 = obj->next(price);
 */
