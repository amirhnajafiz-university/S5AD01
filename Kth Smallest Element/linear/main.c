#include <stdio.h>

int kth_element(int size_a, int size_b, int A[size_a], int B[size_b], int k)
{
	if (size_a + size_b < k)
		return -1;
	
	int i = 0, j = 0, t = 0;
	while(i < size_a && j < size_b)
	{
		if (t == k)
			return A[i] < B[j] ? A[i] : B[j];
		if (A[i] > B[j])
			j++;
		else 
			i++;
		t++;
	}
	
	if (i == size_a)
	{
		while(j < size_b)
		{
			if (t == k)
				return B[j];
			j++;
			t++;
		}
	} else 
	{
		while(i < size_a)
		{
			if (t == k)
				return A[i];
			i++;
			t++;
		}
	}
	
	return -1;
}


int main()
{
	int A[] = {1, 2, 3, 4, 5, 6, 7, 8};
	int B[] = {9, 10, 11, 12, 13, 14, 15};
	
	int SA = sizeof(A) / sizeof(A[0]);
	int SB = sizeof(B) / sizeof(B[0]);
	
	int k = 10;
	
	printf("%d", kth_element(SA, SB, A, B, k));
}