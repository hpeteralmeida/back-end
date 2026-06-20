/* Exercício 9

Declare a string:
char palavra[] = "Computador";

Imprima apenas a primeira letra. */

#include <stdio.h>

int main () {
    char palavra[] = "Computador";

    printf("%c", palavra[0]);
    
    return 0;
}