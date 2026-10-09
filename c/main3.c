#include <stdio.h>
#include <stdlib.h>
#include <string.h>


typedef struct Node{
	char symb;
	struct Node * next;
} Node;


void printlist(Node * node){
	while(node != NULL){
		printf("%c", node->symb);
		node = node->next;
	}
	printf("\n");
}

void freelist(Node * head){
	while(head != NULL){
		Node * temp = head;
		head = head->next;
		free(temp);
	}
}

void newnode(Node ** prev, char symb){
	Node * node = malloc(sizeof(Node));
	node->symb = symb;
	if(*prev != NULL){
		(**prev).next = node;}
	*prev = node;
}

int main(){
	char symb;
	char prsy = '\n';
	char lc[16];
	int len = 0;
	Node * head = NULL;
	Node * node = NULL;
	Node * prev = NULL;
	while((symb = getchar()) != EOF){
		if(symb != '\n'){
			if(!(prsy == ' ' && symb == ' ')){
				newnode(&prev, symb);
				len++;
			}
			if(prsy != ' ' && symb == ' '){
				len--;
				sprintf(lc, "%d", len);
				for(int i = 0; i < strlen(lc); i++){
					newnode(&prev, lc[i]);
				}
				len = 0;
				newnode(&prev, ' ');
			}
			if(head == NULL){
				head = prev;
			}
			prsy = symb;
		}
		else{
			if(prsy != ' '){
				newnode(&prev, ' ');
				sprintf(lc, "%d", len);
				for(int i = 0; i < strlen(lc); i++){
					newnode(&prev, lc[i]);
					len = 0;
				}
				newnode(&prev, ' ');
			}
			printlist(head);
			freelist(head);
			head = NULL;
			prev = NULL;
			prsy = '\n';
			len = 0;
		}
	}
	return 0;
}
