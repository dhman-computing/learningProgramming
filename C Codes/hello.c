#include <stdio.h>
//#include <cs50.h>

void prntn(int n);

int main(void)
{
  // printf("Hello, world.\n");
  int n = get_int("Enter n : ");
  prntn(n);
}

void pn(int n)
{
  for (int i = 1; i <= n; i++)
  {

    /*for (int k = n; k > i; k--)
    {
      printf(" ");
    }*/

    for (int j = i; j >= 1; j--)
    {
      printf("%i", j);
    }
    printf("\n");
  }

}
