#include <stdio.h>
#include <cs50.h>

//This code draws a triangle with numbers

void prntn(int n);
int get_n();

int main(void)
{
    int n = get_n();
    prntn(n);
}

void prntn(int n)
{
    //This function takes an integer as an input and draws the triangle
    for (int i = 1; i <= n; i++)
    {
        for (int k = n; k > i; k--)
        {
            printf(" ");
        }
        for (int j = i; j >= 1; j--)
        {
            printf("%i", j);
        }
        //printf(" ");
        for (int j = 1; j <= i; j++)
        {
            printf("%i", j);
        }

        for (int k = n; k > i; k--)
        {
            printf(" ");
        }
        printf("\n");
    }
}

int get_n()
{
    //this function recieves a number between 1 and 9 from the user
    //if any other number is given then it prompts again with an qoute
    int i;
    printf("Enter a number between 1 and 9.\n");
    do
    {
        i = get_int("Enter n: ");
        if (i < 1)
        {
            printf("Give a number greater than 1.\n");
        }
        else if (i > 9)
        {
            printf("Give a number less than 9.\n");
        }
    }
    while (i < 1 || i > 9);
    return i;
}
