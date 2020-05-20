class Solution {
public:
    bool backspaceCompare(string S, string T) {
        stack<char> A, B;
        for(int i=0;S[i]!='\0';i++)
        {
            if(S[i]!='#')
                A.push(S[i]);
            else
            {
                if(A.empty()==false)
                A.pop();
            }

        }
        for(int j=0;T[j]!='\0';j++)
        {
            if(T[j]!='#')
                B.push(T[j]);
            else
            {
                if(B.empty()==false)
                B.pop();
            }
        }
        bool flag= true;
        if(A.size() != B.size())
        {
            flag=false;
            return flag;
        }
        while(A.empty()==false)
        {
            if(A.top()== B.top())
            {
                A.pop();
                B.pop();
            }
            else
            {
                flag=false;
                break;
            }
        }
        return flag;
    }
};
