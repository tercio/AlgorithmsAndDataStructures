#include <stdio.h>
#include <string.h>

#define WORDMAX 100

int main(int argc,char *argv){

  char sign[WORDMAX], word[WORDMAX], oldsign[WORDMAX];
  int linenum = 0;

  strcpy (oldsign,"");

  while (scanf("%s %s",sign,word) != EOF) {

    if (strcmp(sign,oldsign) != 0 && linenum > 0)
      printf ("\n");
    strcpy(oldsign,sign);
    linenum ++;
    printf ("%s ",word);

  }


  return 0;
}
