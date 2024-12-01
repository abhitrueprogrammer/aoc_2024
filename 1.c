#include <stdio.h>
#include <stdlib.h>
void qsort();
#define MAX 1000
#define MAXSIZE 1024

void qIForgotCHadItsOwnImplementationSort(int *a, int l, int r);

int main(void)
{
    int a1[MAX] = {0};
    int a2[MAX] = {0};
    int a, b;
    FILE *f = fopen("input", "r");
    char buf[MAXSIZE];
    int input_size = 0;
    while (fgets(buf, MAXSIZE, f) != NULL)
    {
  
        sscanf(buf, "%d %d", &a, &b);

        a1[input_size] = a;
        a2[input_size] = b;
        input_size++;
    } 
    printf("%d %d\n", a1[input_size -1 ], a2[input_size -1]);
    qIForgotCHadItsOwnImplementationSort(a1, 0, input_size -1);
    qIForgotCHadItsOwnImplementationSort(a2, 0, input_size -1);
    int total_diff = 0;
    for (int i = 0; i < input_size ; i++)
    {
        int diff = a1[i] - a2[i];
        diff = diff > 0 ? diff : -diff;
        total_diff += diff;
    }
    printf("%d\n", total_diff);
}





int partition(int *a, int l, int r);
void qIForgotCHadItsOwnImplementationSort(int *a, int l, int r)
{
    if (l < r)
    {
        int pi = partition(a, l, r);

        qIForgotCHadItsOwnImplementationSort(a, l, pi - 1);
        qIForgotCHadItsOwnImplementationSort(a, pi + 1, r);
    }
}
void swap(int *arr, int l, int r);
int partition(int *a, int l, int r)
{
    int mid = (l + r) / 2;
    int pivot = a[mid];
    swap(a, mid, r);

    int pi = l - 1;
    for (int i = l; i < r; i++)
    {
        if (a[i] < pivot) // basically arr[r] but readable
        {
            pi = pi + 1;
            swap(a, pi, i);
        }
    }
    swap(a, pi + 1, r);
    return pi + 1;
}

void swap(int *arr, int l, int r)
{
    int temp = arr[l];
    arr[l] = arr[r];
    arr[r] = temp;
}