#include <stdio.h>

int getMedian(int ar1[], int ar2[], int n, int m)
{
	int i = 0; 
	int j = 0; 
	int count;
	int m1 = -1, m2 = -1;

	if ((m + n) % 2 == 1) {
		for (count = 0; count <= (n + m)/2; count++) {
			if(i != n && j != m) {
				m1 = (ar1[i] > ar2[j]) ? ar2[j++] : ar1[i++];
			} else if(i < n){
				m1 = ar1[i++];
			} else {
				m1 = ar2[j++];
			}
		}
		return m1;
	} else {
		for (count = 0; count <= (n + m)/2; count++) {
			m2 = m1;
			if (i != n && j != m) {
				m1 = (ar1[i] > ar2[j]) ? ar2[j++] : ar1[i++];
			} else if(i < n) {
				m1 = ar1[i++];
			} else{
				m1 = ar1[j++];
			}
		}
		return (m1 + m2)/2;
	}
}

int main()
{
	int ar1[] = {900};
	int ar2[] = {5, 8, 10, 20};

	int n1 = sizeof(ar1)/sizeof(ar1[0]);
	int n2 = sizeof(ar2)/sizeof(ar2[0]);
	
	printf("%d", getMedian(ar1, ar2, n1, n2));
	getchar();
	
	return 0;
}
