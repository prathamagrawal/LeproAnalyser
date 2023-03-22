#include <iostream>
using namespace std;

// void print_name(string name,int n,int count){
//     if(n==count){
//         return;
//     }
//     cout<<name<<endl;
//     count++;
//     print_name(name,n,count);
// }

void oneToN(int count,int n){
    if(count>n){
        return;
    }
    cout<<count;
    count++;
    oneToN(count,n);
}

int sumtoN(int count,int n,int temp){
    if(count<n){
        return temp;
    }
    temp=temp+count;
    count++;
    sumtoN(count,n,temp);
}

int main(){
    int count=0;
    int n;
    cin>>n;
    // string name="Pratham ";
    // print_name(name,n,count);
    // oneToN(count,n);

    cout<<sumtoN(count,n,0);

}