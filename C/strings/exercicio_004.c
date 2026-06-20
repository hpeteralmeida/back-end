/* Exercício 4

Faça um programa em C que declare uma string com uma palavra e
 imprima a primeira, a segunda e a terceira letra separadamente. */

 #include <stdio.h>

 int main() {
    char palavra[50];

    printf("Digite uma palavra: ");
    scanf("%s", &palavra);

    printf("A primeira letra da palavra é: %c\n", palavra[0]);
    printf("A segunda letra da palavra é: %c\n", palavra[1]);
    printf("A terceira letra da palavra é: %c\n", palavra[2]);

    return 0;
}