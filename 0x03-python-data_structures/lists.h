#include <stdio.h>
#include <stdlib.h>

/* Definition of a node in the linked list */
typedef struct listint_t {
    int data;
    struct listint_t* next;
} listint_t;

/* Function to check if a linked list is a palindrome */
int is_palindrome(listint_t** head);
/* Function to create a new node in the linked list */
listint_t* create_node(int data);
/* Function to insert a new node at the beginning of the linked list */
void insert_node(listint_t** head, int data);
/* Function to print the linked list */
void print_list(listint_t* head);
