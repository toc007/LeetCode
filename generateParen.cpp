#include <iostream>
#include "vector"

using namespace std;
class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> result = vector<string>();
        result.push_back("Hello World");

        for(auto s:result) {
            cout << s << endl;
        }
        return result;
    }
};

int main() {
    Solution().generateParenthesis(3);
    return 1;
}