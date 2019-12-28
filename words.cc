// mostra palavras que estão em um texto. Não repete
// location 3686  Programming Pearls

#include <iostream>
#include <set>

using namespace std;

int main () {

    set<string> S;
    set<string>::iterator j;
    string t;

    while (cin >> t) {
        S.insert(t);
    }

    for (j = S.begin(); j != S.end(); j++)
        cout << *j << endl;


    return 0;
}