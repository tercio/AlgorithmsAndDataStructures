#include <iostream>

using namespace std;

template<class T>
class Element{

public:
  Element(const T& value):next(NULL),data(value){}
  ~Element(){cout<<"Element::~Element called..."<<endl;}

  const T& value()const {return data;}
  void setNext(Element<T>* n){next = n;}
  Element<T>* getNext()const {return next;}

private:
  T data;
  Element<T> *next;
};

template <class T>
class LinkedList{

public:
  LinkedList():head(NULL){}
  ~LinkedList(){}

  void insertIntoFront(Element<T>* elem){
    if (head != NULL) {
        elem->setNext(head);
    }
    head = elem;
  }

  void traverse(){
    Element<T>* temp = head;
    while (temp) {
      cout << temp->value() << endl;
      temp = temp->getNext();
    }
  }

private:
  Element<T>* head;

};

int main () {

  LinkedList<int>* ll = new LinkedList<int>();

  ll->insertIntoFront(new Element<int>(5));
  ll->insertIntoFront(new Element<int>(15));
  ll->insertIntoFront(new Element<int>(25));
  ll->insertIntoFront(new Element<int>(35));
  ll->insertIntoFront(new Element<int>(45));

  ll->traverse();

  return 0;
}
