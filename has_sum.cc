#include <unordered_set>
#include <iostream>
#include <vector>

using namespace std;


bool hasPairWithSum(const vector<int>& data, int sum) {

    unordered_set<int> comps;

    for (int value : data) {

        if (comps.find(value) != comps.end()) {
            return true;
        } else {
            comps.insert(sum - value);
        }

    }

    return false;
}


int main() {

    int my_ints[] = {1,2,4,9};
    vector<int> v1(my_ints,my_ints+5);

    cout << hasPairWithSum(v1,8) << endl;

    int my_ints2[] = {1,2,4,4};
    vector<int> v2(my_ints2,my_ints2+5);
    cout << hasPairWithSum(v2,8) << endl;

    vector<int> v3;
    cout << hasPairWithSum(v3,8) << endl;

    return 0;
}