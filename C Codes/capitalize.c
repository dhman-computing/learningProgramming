#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>

int main(void)
{
    string s = get_string("Enter Text : ");

    for (int i = 0; i < strlen(s); i++)
    {
        if (islower(s[i]))
        {
            printf("%c", toupper(s[i]));
        }
        else if (isupper(s[i]))
        {
            printf("%c", s[i]);
        }
        else
        {
            printf("%c", s[i]);
        }
    }
    printf("\n");
}