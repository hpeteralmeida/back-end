/* Exercício 10

Declare a string:
char palavra[] = "Computador";

Imprima a última letra usando índice. */

#include <stdio.h>
#include <string.h>

int main () {
    char palavra[] = "Computador";
    
    printf("%c", palavra[strlen(palavra) - 1]);

    return 0;
}