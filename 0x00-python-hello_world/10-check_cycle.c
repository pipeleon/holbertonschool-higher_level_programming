#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if theres a cycle
 * @list: pointer to list
 * Return: 1 if true 0 if false
 */
int check_cycle(listint_t *list)
{
	listint_t *temp, *current;

	temp = list;
	current = list->next;

	while (current)
	{
		if (temp == current)
			return (1);
		current = current->next;
	}

	return (0);
}
