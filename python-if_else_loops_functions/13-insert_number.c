#include "lists.h"
#include<stdlib.h>

/**
 * insert_node - inserting node in singly linked list
 * @head: the adress of head
 * @number: number to insert in the list
 * Return: return address to inserted node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;
	listint_t *temp;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	current = *head;
	while (current != NULL)
	{
		if (current->n >= number)
			break;
		temp = current;
		current = current->next;
	}
	if (*head == NULL || current == *head)
	{
		new->next = *head;
		*head = new;
	}
	else if (current == NULL)
	{
		temp->next = new;
	}
	else
	{
		temp->next = new;
		new->next = current;
	}
	return (new);
}
