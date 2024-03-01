#include "lists.h"

/**
 * check_cycle - checks the cycle in singly linked list
 * @list: the list to check
 * Return: its either zero or one
 */

int check_cycle(listint_t *list)
{
	int n;
	int k;
	listint_t *current;
	listint_t *temp;

	current = list;
	temp = list;
	n = 2;
	while (current != NULL)
	{
		k = n;
		while (k > 2)
		{
			if (current->next == temp)
				return (1);
			k--;
			temp = temp->next;
		}
		n++;
		temp = list;
		current = current->next;
	}
	return (0);
}

