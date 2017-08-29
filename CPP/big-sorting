/* Big-sorting
https://www.hackerrank.com/challenges/big-sorting/problem
Idea: Write your own sort function
*/
#include <bits/stdc++.h>
using namespace std;

bool sorter(const string &a, const string &b) {
    if(a.size() == b.size())
        return a<b;
    return a.size() < b.size();
}

int main(){
    int n;
    cin >> n;
    vector<string> unsorted(n);
    for(int unsorted_i = 0; unsorted_i < n; unsorted_i++){
       cin >> unsorted[unsorted_i];
    }
    // your code goes here
    sort(unsorted.begin(), unsorted.end(), sorter);
    for(int unsorted_i = 0; unsorted_i < n; unsorted_i++){
       cout<< unsorted[unsorted_i]<<"\n";
    }
    return 0;
}
