// Longest Common Subsequence
// Memoized Version
// https://www.techiedelight.com/longest-common-subsequence/

#include <string>
#include <iostream>
#include <unordered_map>

using namespace std;

int lcs (string s1, string s2,int m, int n, unordered_map<string,int> &lookup) {

    if (m == 0 || n == 0)
        return 0;

    string key = to_string(m) + "|" + to_string(n);

    if (lookup.find(key) == lookup.end()) {

        if (s1[m - 1] == s2[n - 1]) {
            lookup[key] = lcs(s1,s2,m-1,n-1,lookup) + 1;
        } else {
            lookup[key] = max(lcs(s1,s2,m-1,n,lookup),
                                lcs(s1,s2,m,n-1,lookup));
        }

    }

    return lookup[key];
}

int main () {

    unordered_map<string,int> lookup;

    string s1 = "abcbdab";
    string s2 = "bdcaba";
    int m = s1.size();
    int n = s2.size();
    cout << "LCS for " << s1 << " & " << s2 << " is: " << lcs(s1,s2,m,n,lookup) << endl;

    s1 = "sao paulo";
    s2 = "em sao paulo sp";
    m = s1.size();
    n = s2.size();
    cout << "LCS for " << s1 << " & " << s2 << " is: " << lcs(s1,s2,m,n,lookup) << endl;

    return 0;

}