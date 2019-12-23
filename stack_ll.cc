// stack implemented as a linked list
#include <iostream>

using namespace std;

class Node {

  public:
     Node (int v):value(v),next(NULL){}
     int getValue () const {return value;}
     void setNext (Node* _next){next = _next;}
     Node* getNext(){return next;}

private:
  int value;
  Node* next;
};

class Stack {

public:
  Stack():head(NULL){}

  void push (int v){
    Node* n = new Node(v);
    if (head == NULL){
      head = n;
    } else {
      n->setNext(head);
      head = n;
    }
  }

  int pop(){
    if (head){
      int v = head->getValue();
      Node* next = head->getNext();
      delete head;
      head = next;
      return v;

    }else{
      return -1;
    }
  }

private:
  Node* head;
};


int main (){

  Stack* stack = new Stack();

  stack->push(5);
  stack->push(15);
  stack->push(25);
  cout << "pop: " << stack->pop() << endl;
  cout << "pop: " << stack->pop() << endl;
  cout << "pop: " << stack->pop() << endl;
  cout << "pop: " << stack->pop() << endl;


  return 0;
}
