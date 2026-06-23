Aula 4 — Biblioteca <string.h>

Antes de usar essas funções, precisamos incluir:
    #include <string.h>
    As 4 funções mais importantes para começar são:
        strlen() → tamanho da string
        strcmp() → comparar strings
        strcpy() → copiar strings
        strcat() → concatenar strings


1. strlen()
    Retorna a quantidade de caracteres da string.

        char nome[] = "Pedro";
        printf("%lu", strlen(nome));

        Saída: 5

    Lembre-se:
    strlen("Pedro") = 5
    porque não conta o \0.

    Exemplo

        char palavra[] = "Computador";
        int tamanho = strlen(palavra);
        printf("%d", tamanho);

        Saída: 10

2. strcmp()
    Em C não podemos comparar strings usando:
        if(nome1 == nome2)
    Isso compara endereços de memória, não o conteúdo.

    Errado:
        char a[] = "Pedro";
        char b[] = "Pedro";

        if(a == b)

    Para comparar conteúdo usamos: strcmp()

    Exemplo:
        char a[] = "Pedro";
        char b[] = "Pedro";

        if(strcmp(a, b) == 0)
        {
            printf("Iguais");
        }

        Saída: Iguais
    
    Como interpretar o retorno
    strcmp(a, b)

    Retorna:
    0  -> iguais
    <0 -> primeira vem antes alfabeticamente
    >0 -> primeira vem depois alfabeticamente

    Exemplo:

    strcmp("Ana", "Pedro")

    Retorna valor negativo, porque Ana vem antes de Pedro

3. strcpy()
    Serve para copiar strings.

    Errado:
        char destino[50];
        destino = "Pedro";

    Isso não funciona.

    Correto:
        char destino[50];
        strcpy(destino, "Pedro");

    Exemplo
        char nome[50];
        char origem[] = "Pedro";

        strcpy(nome, origem);

        printf("%s", nome);

        Saída: Pedro

4. strcat()
    Serve para juntar strings.

    Exemplo:
        char nome[50] = "Pedro";
        strcat(nome, " Almeida");
        printf("%s", nome);

        Saída: Pedro Almeida

    Atenção

    O vetor deve ter espaço suficiente.

    Funciona:
        char nome[50] = "Pedro";

    Perigoso:
        char nome[6] = "Pedro";

    porque não sobra espaço para adicionar nada.

    Resumo
    Função	       Faz o quê?
    _____________________________
    strlen() |	Conta caracteres
    strcmp() | 	Compara strings
    strcpy() |	Copia strings
    strcat() |	Junta strings

exercicios 15 - 21