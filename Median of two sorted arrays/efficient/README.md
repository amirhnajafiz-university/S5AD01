Let’s take an example to understand this
Input :arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10},
brr[] = { 11, 12, 13, 14, 15, 16, 17, 18, 19 }
Dry Run of the code:
Recursive call 1:
smaller array[] = 1 2 3 4 5 6 7 8 9 10, mid = 5
larger array[] = 11 12 13 14 15 16 17 18 19 , mid = 15

5 < 15
Discard first half of the first array and second half of the second array

Recursive call 2:
smaller array[] = 11 12 13 14 15, mid = 13
larger array[] = 5 6 7 8 9 10, mid = 7

7 < 13
Discard first half of the second array and second half of the first array

Recursive call 3:
smaller array[] = 11 12 13 , mid = 12
larger array[] = 7 8 9 10 , mid = 8

8 < 12
Discard first half of the second array and second half of the first array

Recursive call 4:
smaller array[] = 11 12
larger array[] = 8 9 10

Size of the smaller array is 2 and the size of the larger array is odd
so, the median will be the median of max( 11, 8), 9, min( 10, 12)
that is 9, 10, 11, so the median is 10.

Output:10.000000