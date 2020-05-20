/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        int n=0;
        ListNode* temp;
        temp=head;
        while(temp != NULL)
        {
            n++;
            temp=temp->next;
        }
        for(int i=1;i<=(n/2);i++)
            head=head->next;
        
        return head;
    }
};
