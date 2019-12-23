#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define WORDMAX 100

int charcomp (const void *x, const void *y){return *(char*)x - *(char*)y;};

int main (int argc, char *argv) {

  FILE *fd;
  char word[WORDMAX], sign[WORDMAX];

  fd = fopen("dictionary.txt","r");

  while (fscanf(fd,"%s",word) != EOF) {
    //printf ("%s\n",word);
    strcpy(sign,word);
    qsort (sign, strlen(sign), sizeof(char), charcomp);
    printf ("%s %s\n",sign, word);
  }


}
