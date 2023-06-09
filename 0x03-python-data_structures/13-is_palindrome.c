#include "lists.h"

/* Function to check if a linked list is a palindrome */
int is_palindrome(listint_t** head) {
    // Check for empty list
    if (*head == NULL) {
        return 1;
    }

    // Find the middle of the linked list using the two-pointer technique
    listint_t* slow = *head;
    listint_t* fast = *head;
    while (fast != NULL && fast->next != NULL) {
        slow = slow->next;
        fast = fast->next->next;
    }

    // Reverse the second half of the linked list
    listint_t* prev = NULL;
    listint_t* curr = slow;
    listint_t* next;
    while (curr != NULL) {
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }

    // Compare the reversed second half with the first half of the linked list
    listint_t* first = *head;
    listint_t* second = prev;
    while (second != NULL) {
        if (first->data != second->data) {
            return 0;  // Not a palindrome
        }
        first = first->next;
        second = second->next;
    }

    return 1;  // Palindrome
}

/* Function to create a new node in the linked list */
listint_t* create_node(int data) {
    listint_t* new_node = (listint_t*)malloc(sizeof(listint_t));
    new_node->data = data;
    new_node->next = NULL;
    return new_node;
}

/* Function to insert a new node at the beginning of the linked list */
void insert_node(listint_t** head, int data) {
    listint_t* new_node = create_node(data);
    new_node->next = *head;
    *head = new_node;
}

/* Function to print the linked list */
void print_list(listint_t* head) {
    listint_t* temp = head;
    while (temp != NULL) {
        printf("%d ", temp->data);
        temp = temp->next;
    }
    printf("\n");
}

/* Main function */
int main() {
    // Create a sample linked list
    listint_t* head = NULL;
    insert_node(&head, 1);
    insert_node(&head, 2);
    insert_node(&head, 3);
    insert_node(&head, 2);
    insert_node(&head, 1);

    // Print the linked list
    printf("Linked List: ");
    print_list(head);

    // Check if the linked list is a palindrome
    int palindrome = is_palindrome(&head);
    if (palindrome) {
        printf("The linked list is a palindrome.\n");
    } else {
        printf("The linked list is not a palindrome.\n");
    }

    // Free the memory allocated for the linked list
    listint_t* temp;
    while (head != NULL) {
        temp = head;
        head = head->next;
        free(temp);
    }

    return 0;
}
