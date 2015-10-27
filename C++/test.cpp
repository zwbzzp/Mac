#include<iostream>
#include<map>
#include<stdlib.h>
#include<vector>
#include<queue>
#include<math.h>
#include<set>
using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if(nums.size()==0)
            return 0;
        int count=0;
        
    }
};

int main(){
	Solution s;
    // ListNode* a = new ListNode(-9);
    // ListNode* b = new ListNode(5);
    // ListNode* headb = b;
    // ListNode* heada = a;
    // a->next = new ListNode(3);
    // b->next = new ListNode(7);
    // b = b->next;
    // b->next = new ListNode(10);
    // while(head!=NULL){
    //     cout<<head->val<<endl;
    //     head = head->next;
    // }
    // string ss = "AA";
    // s.titleToNumber(ss);
    int a[]={1,2};
    vector<int> nums(a,a+2);
    s.removeDuplicates(nums);
    vector<int>::iterator it;
    for(it=nums.begin();it!=nums.end();it++){
        cout<<*it<<endl;
    }

    return 0;	
}