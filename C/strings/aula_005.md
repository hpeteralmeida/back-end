Aula 5 — Contando caracteres dentro de uma string

A ideia é percorrer a string e verificar cada caractere.
Esse conceito será usado para:
    - contar vogais
    - contar consoantes
    - contar números
    - contar espaços
    - verificar palíndromos
    - validar senhas
    - processar textos

Exemplo 1 — Contar letras 'a'
    #include <stdio.h>

    int main() {
        char palavra[100];
        fgets(palavra, sizeof(palavra), stdin);
        int contador = 0;

        for(int i = 0; palavra[i] != '\0'; i++) {
            if(palavra[i] == 'a') {
                contador++;
            }
        }

        printf("%d\n", contador);

        return 0;
    }

    Entrada: banana
    Saída: 3

Exemplo 2 — Contar espaços
    if(palavra[i] == ' ') {
        contador++;
    }

    Entrada: Pedro Almeida Silva
    Saída: 2
    
Exemplo 3 — Contar vogais
    Uma vogal pode ser:

    a e i o u

    Logo:
        if( 
            palavra[i] == 'a' ||
            palavra[i] == 'e' ||
            palavra[i] == 'i' ||
            palavra[i] == 'o' ||
            palavra[i] == 'u'
        ){
            contador++;
        }

    Entrada: computador
    Saída: 4

Exemplo 4 — Contar um caractere informado pelo usuário
    char letra;
    int contador = 0;

    Usuário digita: a

    Percorremos a string:
    if(palavra[i] == letra) {
        contador++;
    }
    Técnica importante

    Quase todos os exercícios dessa aula seguem esta estrutura:

        for(int i = 0; string[i] != '\0'; i++){
            if(condicao){
                contador++;
            }
        }

    Guarde isso.

    Você vai usar dezenas de vezes.

exercicios 20 - 30
