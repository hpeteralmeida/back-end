/* Exercício 18

Leia nome e sobrenome separadamente.

Monte o nome completo usando strcpy() e strcat().*/

#include <stdio.h>
#include <string.h>

int main() {
    char nome[50], sobrenome[50], nomeCompleto[100];

    printf("Digite o seu nome: ");
    scanf("%s", nome);

    printf("Digite o seu sobrenome: ");
    scanf("%s", sobrenome);

    strcpy(nomeCompleto, nome);
    strcat(nomeCompleto, " ");
    strcat(nomeCompleto, sobrenome);

    printf("Nome completo: %s\n", nomeCompleto);

    return 0;
}

