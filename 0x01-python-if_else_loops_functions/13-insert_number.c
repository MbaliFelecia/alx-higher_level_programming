#include "lists.h"

/**
 * insert_node -insert 1 new node
 * on a given position.
 * @head: head of the list.
 * @number: index of the list
 * where a node is added.
 * return: the address of the new node
 * or Null if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *h;
	listint_t *prev_h;

	h = *head;
	new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);

	while (h != NULL)
	{
		if (h->n > number)
			break;
		prev_h = h;
		h = h->next;
	}

	new->n = number;

	if (*head == NULL)
	{
		new->next = NULL;
		*head = new;
	}
	else
	{
		new->next = h;
		if (h == *head)
			*head = new;
		else
			prev_h->next = new;
	}

	return (new);
}
