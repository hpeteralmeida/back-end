/* Exercício 12

Leia uma palavra e mostre quantas letras ela possui sem usar strlen(). */

#include <stdio.h>
#include <string.h>

int length(char palavra[]) {
    int contador = 0, i = 0;

    while (palavra[i] != '\0') {
        contador++;
        i++;
    }

    return contador;
}

int main() {
    char palavra[50];
    int tamanho = 0;

    printf("Digite uma palavra: ");
    scanf("%s", palavra);

    tamanho = length(palavra);

    printf("Sua palavra tem %d letras \n", tamanho);

    return 0;
}