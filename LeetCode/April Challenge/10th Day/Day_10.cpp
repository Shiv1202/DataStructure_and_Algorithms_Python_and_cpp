class MinStack {
public:
    /** initialize your data structure here. */
    stack<int> s;
    vector<int> min;
    MinStack() {
    }
    void push(int x) {
        s.push(x);
        if(min.empty()||min.back()>=x)
            min.push_back(x);
    }
    void pop() {
        if(s.top()==min.back())
            min.pop_back();
        s.pop();
    }
    int top() {
        return s.top();
    }
    int getMin() {
        return min.back();
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(x);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
