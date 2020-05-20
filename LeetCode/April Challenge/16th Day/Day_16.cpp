class Solution {
public:
bool checkValidString(string s) {
      stack<int> open,ast;
      for(int i=0;i<s.length();i++)
      {
          if(s[i] == ')')
          {
              if(!open.empty()) open.pop();
              else if(!ast.empty()) ast.pop();
              else return false;
          }
          else if(s[i] == '(')   open.push(i);
          else ast.push(i);
      }
      while(!open.empty() && !ast.empty())
      {
         if(open.top() > ast.top()) return false;
         open.pop();
          ast.pop();
      }
        return open.empty();
    }
};
