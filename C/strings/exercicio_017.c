/* Exercício 3

Crie duas strings:
    char origem[] = "Programacao";
    char destino[50];

Copie a string origem para destino usando strcpy() e imprima o resultado. */

#include <stdio.h>
#include <string.h>

int main() {
    char origem[] = "Programacao";
    char destino[50];

    strcpy(destino, origem);
    printf("%s\n", destino);

    return 0;
}