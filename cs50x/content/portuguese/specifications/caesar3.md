## Especificação

Projete e implemente um programa, `caesar`, que criptografa mensagens usando o cifra de César.

- Implemente seu programa em um arquivo chamado `caesar.c` em um diretório chamado `caesar`.
- Seu programa deve aceitar um único argumento de linha de comando, um inteiro não negativo. Vamos chamá-lo de `k` para fins de discussão.
- Se o seu programa for executado sem nenhum argumento de linha de comando ou com mais de um, seu programa deve imprimir uma mensagem de erro de sua escolha (com `printf`) e retornar de `main` um valor de `1` (que tende a significar um erro) imediatamente.
- Se qualquer um dos caracteres do argumento da linha de comando não for um dígito decimal, seu programa deve imprimir a mensagem `Usage: ./caesar key` e retornar de `main` um valor de `1`.
- Não assuma que `k` será menor ou igual a 26. Seu programa deve funcionar para todos os valores integrais não negativos de `k` menores que <code>2<sup>31</sup> - 26</code>. Em outras palavras, não é necessário se preocupar se o programa eventualmente quebrará se o usuário escolher um valor para `k` que seja grande demais ou quase grande demais para caber em um `int`. (Lembre-se de que um `int` pode estourar.) Mas, mesmo que `k` seja maior que 26, caracteres alfabéticos na entrada do seu programa devem permanecer caracteres alfabéticos na saída do seu programa. Por exemplo, se `k` for `27`, `A` não deve se tornar `\` mesmo que `\` esteja `27` posições distante de `A` em ASCII, de acordo com [asciitable.com](https://www.asciitable.com/); `A` deve se tornar `B`, já que `B` está `27` posições distante de `A`, desde que você retorne ao `Z` indo para `A`.
- Seu programa deve exibir `plaintext:` (com dois espaços, mas sem uma nova linha) e, em seguida, solicitar ao usuário uma `string` de texto simples (usando `get_string`).
- Seu programa deve exibir `ciphertext:` (com um espaço, mas sem uma nova linha), seguida do texto cifrado correspondente ao texto simples, com cada caractere alfabético do texto simples "rotacionado" por _k_ posições; caracteres não alfabéticos devem ser exibidos sem alteração.
- Seu programa deve preservar os caracteres em maiúscula e minúscula: as letras maiúsculas, mesmo rotacionadas, devem permanecer letras maiúsculas; as letras minúsculas, mesmo rotacionadas, devem permanecer letras minúsculas.
- Após exibir o texto cifrado, você deve imprimir uma nova linha. Seu programa deve então sair retornando `0` de `main`.

## Conselho

Como começar? Vamos abordar este problema uma etapa por vez.

### Pseudo-código

Primeiro, tente escrever uma função `main` em `caesar.c` que implementa o programa usando apenas pseudocódigo, mesmo que não tenha certeza de como escrevê-lo em código real.

<details><summary>Dica</summary><p>Há mais de uma maneira de fazer isso, então aqui está apenas uma!</p>

    int main(void)
    {
        // Verifique se o programa foi executado com apenas um argumento de linha de comando

        // Verifique se cada caractere em argv[1] é um dígito

        // Converta argv[1] de uma `string` para um `int`

        // Peça ao usuário o texto simples

        // Para cada caractere no texto simples:

            // Gere a rotação para o caractere, se for uma letra
    }

<p>Está tudo bem editar seu próprio pseudocódigo após ver o nosso aqui, mas não basta copiar/colar o nosso no seu!</p></details>
"