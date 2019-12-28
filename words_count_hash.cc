#include <iostream>
#include <string.h>

using namespace std;

typedef struct node *nodeptr;
typedef struct node {
    char *word;
    int count;
    nodeptr next;
} node;

#define NHASH 60649
#define MULT 31
nodeptr bin[NHASH];
int count = 0;

unsigned int myhash(const char *p) {

    unsigned int h = 0;
    for (;*p;p++)
        h = MULT * h + *p;
    
    return h % NHASH;
}


void incword (const char *s) {

    unsigned int h = myhash(s);
    
    nodeptr p;
    
    //cout << "hash: " << h << endl;
    for (p=bin[h]; p != NULL; p = p->next) {
        if (strcmp(s,p->word) == 0) {
            p->count ++;
            return;
        }
    }
    p = (nodeptr)malloc(sizeof(node));
    p->count = 1;
    p->word = (char *)malloc(strlen(s)+1);
    strcpy(p->word,s);
    p->next = bin[h];
    bin[h] = p;

    
}

int main () {

    string t;

    for (int i=0; i< NHASH; i++)
        bin[i] = NULL;


    while (cin >> t)
        incword(t.c_str());

    for (int i=0; i<NHASH; i++)
        for (nodeptr p=bin[i]; p!= NULL; p=p->next) {
            //if (p->next)count++; // collisions ?
            cout << p->word << "\t" << p->count << endl;
        }

    //cout << "collisions:" << count << endl;

    return 0;
}