#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>

int main(void)
{
    string word[2];
    word[0] = "hello";
    word[1] = "world";

    printf("%s, %s.\n", word[0], word[1]);
}