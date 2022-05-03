#include <stdio.h>

int main(void)
{
    int i;
    char c = getchar();
    for (i = 1; c != EOF; i++)
    {
        c = getchar();
    }

    printf("No. of charecters : %i\n .", i);
}