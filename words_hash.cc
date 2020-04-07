#include <string>
#include <set>
#include <map>
#include <iostream>
#include <string.h>

#include <stdlib.h>

using namespace std;


typedef struct node *nodeptr;
typedef struct node {

    char *word;
    int count;
    nodeptr next;
} node;

#define NHASH 29989
#define MULT 31
nodeptr bin[NHASH];

unsigned int _hash (const char *p) {
    unsigned int h = 0;
    for (; *p; p++)
        h = MULT * h + *p;

    return h % NHASH;
}

void incword (const char *s) {

    unsigned int h = _hash(s);
    for (auto p = bin[h]; p != NULL; p = p->next)
        if (strcmp (s,p->word) == 0){
            (p->count)++;
            return;
        }
        

    nodeptr p = (nodeptr)malloc(sizeof(node));
    p->count = 1;
    p->word = (char *)malloc(strlen(s)+1);
    strcpy (p->word,s);
    p->next = bin[h];
    bin[h] = p;

}


int main() {

    string w;

    for (int i=0; i< NHASH; i++)
        bin[i] = NULL;


    while (cin >> w) {
        incword(w.c_str());
        
    }

    for (int i=0; i< NHASH; i++)
        for (auto p = bin[i]; p != NULL; p = p->next)
            cout << p->word << ":" << p->count << endl;


    return 0;
}