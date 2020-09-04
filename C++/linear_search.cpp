#include <iostream>
using namespace std;

int linear_search(int arr[], int size,int ele){
    int i;
    for(i = 0; i<n; i++){
        if(arr[i] == x)
        return i;
    }
    return -1;
}

int main(){
    int arr[]={2, 3, 4, 10, 40, 65};
    int x = 40;
    int n = sizeof(arr)/sizeof(arr[0]);
    int result = linear_search(arr, n, x);
    cout<<"Position "<<i<<endl;
}
