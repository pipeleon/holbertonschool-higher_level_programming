#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to head of list
 * @number: new number to insert
 * Return: pointer to new list
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *temp, *ant;
	int flag = 0;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	temp = *head;

	while (temp)
	{
		if (temp->n > number)
		{
			new->n = number;
			new->next = ant->next;
			ant->next = new;
			flag = 1;
			break;
		}
		ant = temp;
		temp = temp->next;
	}

	if (flag == 0)
	{
		free(new);
		return (NULL);
	}

	return (new);
}
