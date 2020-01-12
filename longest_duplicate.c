/*
 * Exemplo de suffix matrix do livro Programming Pearls
 * Location 3792 no Kindle
 * Complexidade: O(n log n)
 *
 * Suffix array representam cada sufixo na string principal usando a propria string e
 * n adicional ponteiros (ver c e *a abaixo)
 */

#include <stdlib.h>
#include <string.h>
#include <stdio.h>

#define M 1
#define  MAXN  5000000
char c[MAXN],*a[MAXN];


int pstrcmp(const void *x, const void *y) {
	return strcmp(*(char**)x, *(char**)y);
}


int comlen(char *p,char *q){

	int i=0;
	while  (*p &&(*p++==*q++)){
		i++;
	}

	return i;
}

int main(){

	int maxlen=-1;
	int maxi; 
	int ch,n=0; 

	/*
	 * Temos a string onde a frase é colocada: c
	 * Temos um vetor de ponteiros "a" onde cada entrada aponta para
	 * a próxima letra inserida em c
	 * ex.:  c = banana
	 *       a[0] = banana (ponteiro para c[0]
	 *       a[1] = anana  (ponteiro para c[1]
	 *       a[2] = nana   (etc...
	 * */
	while ((ch=getchar())!=EOF){
		a[n]=&c[n];
		c[n++]=ch;
	}
	c[n]=0;


	qsort(a,n,sizeof( char *),pstrcmp);

	//for (int i=0; i< n; i++)
	//	printf ("suffix: sorted: %s\n",a[i]);

	int clen = 0;
	for (int i=0;i<n-M;i++){ // testa a string atual com a próxima
		if ((clen = comlen(a[i],a[i+M])) > maxlen){ // se o len aqui, for maior que maxlen (o maior len até agora)
			maxlen = clen;
			maxi=i; // posição onde a maior string repetida foi encontrada
		}
	}

	char *dup;
	dup = malloc(maxlen+1);
	strncpy(dup,a[maxi],maxlen);
	dup[maxlen+1] = '\0';

	printf("%d : %s\n",maxi,dup);

	return 0;
}
