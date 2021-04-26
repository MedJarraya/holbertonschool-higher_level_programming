#include "lists.h"

/**
* check_cycle - cycle
* @list: list
* Return: 1
*/
int check_cycle(listint_t *list)
{
listint_t *fp = list;
listint_t *sp = list;
if (list == NULL || list->next == NULL)
return (0);
while (fp && fp->next && fp->next->next)
{
sp = sp->next;
fp = fp->next->next;
if (sp->n == fp->n)
return (1);
}
return (0);
}