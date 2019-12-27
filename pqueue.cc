// priority queue 
// location 3544 do livro Programming Pearls

#include <iostream>

using namespace std;

template<class T>
class priqueue{

private:
    int n, maxsize;
    T *x;
    void swap (int i, int j) {
        T t = x[i]; x[i] = x[j]; x[j] = t;
    }

public:
    priqueue(int m):maxsize(m) {
        x = new T[maxsize+1];
        n = 0;
    }

    void insert (T t) {
        int i,p; // p=parent of the node inserted
        x[++n] = t;
        for (i = n; i > 1 && x[p=i/2] > x[i]; i = p)
            swap(p,i);
    }

    T extractmin(){

        int i,c; //c = child
        T t = x[1];
        x[1] = x[n--];
        for (i = 1; (c = 2*i) <= n; i = c) {
            if (c+1 < n && x[c+1] < x[c]) 
                c++; // se o filho da direita é menor que o da esquerda, usa o menor
            if (x[i] <= x[c])
                break; // se o atual é menor ou igual ao filho, finaliza o loop
            swap(c,i);
        }
        return t;
    }

};


int main(){

    priqueue<int>* p = new priqueue<int>(50);

    p->insert(25);
    p->insert(15);
    p->insert(5);
    p->insert(4);
    p->insert(8);
    p->insert(1);

    cout << "extractmin: " << p->extractmin()<<endl; 
    cout << "extractmin: " << p->extractmin()<<endl; 
    cout << "extractmin: " << p->extractmin()<<endl; 

    return 0;
}
