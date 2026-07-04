/* Exercício 27

Leia uma palavra e uma letra.
Informe quantas vezes essa letra aparece na palavra. */

#include <stdio.h>
#include <string.h>

int main() {
    char palavra[100];
    char letra;
    int contaLetra = 0;

    printf("Digite uma palavra: ");
    scanf("%s", palavra);

    printf("Escolha a letra para verificar a quantidade: ");
    scanf(" %c", &letra);

    for (int i = 0; palavra[i] != '\0'; i++) {
        if (palavra[i] == letra) {
            contaLetra++;
        }
    }

    printf("A letra '%c' aparece %d vezes na palavra.\n", letra, contaLetra);

    return 0;
}