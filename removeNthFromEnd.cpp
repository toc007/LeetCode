struct ListNode {
     int val;
     ListNode *next;
     ListNode(int x) : val(x), next(NULL) {}
};  
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        return helper(head, &n);
    }
    
    ListNode* helper(ListNode* head, int* n) {
       if(head == NULL) {
           return head
       }
       ListNode* res = helper(head->next, n);
       if(*n == 0) {
           return res;
       }
       else if(*n > 0) {
           (*n)--;
           cout << *n << endl;
       }
    }
};