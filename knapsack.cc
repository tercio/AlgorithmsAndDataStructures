/*
    Knapsack problem
    Dynamic Programming with Memoization
    Complexity: O(n.W) (pseudo polynomial ?)

    Original: https://www.techiedelight.com/0-1-knapsack-problem/
*/

#include <vector>
#include <iostream>
#include <unordered_map>

using namespace std;

unordered_map<string,int> lookup;

int knapsack(const vector<int> &w, const vector<int> &v,int n, int W) {

    if (W < 0)
        return INT8_MIN;

    if (n < 0 || W == 0)
        return 0;

    string key = to_string(n) + "|" + to_string(W);

    if (lookup.find(key) == lookup.end()) {

        // Temos dois subproblemas:

        // o item atual deve ser incluido no ks e depois recur no item anterior
        int include = v[n] + knapsack(w,v,n - 1,W - w[n]);

        // o item atual NAO entra no ks e faço o recur no item atual
        int exclude = knapsack(w,v,n-1,W);

        lookup[key] = max(include,exclude);
    }

    return lookup[key];
}

int main () {

{
    int w[] = {3,2,5,1};
    int v[] = {1,4,2,6};
    int W = 10;
    int n = 4;

    vector<int> weights (w,w+4);
    vector<int> values (v,v+4);

    cout << knapsack(weights,values,n - 1,W) << endl;
}

{
    int v[] = { 20, 5, 10, 40, 15, 25 };
    int w[] = {  1, 2,  3,  8,  7, 4 };
    int W = 10;
    int n = 6;

    vector<int> weights (w,w+6);
    vector<int> values (v,v+6);

    cout << knapsack(weights,values,n - 1,W) << endl;
}

    return 0;
}