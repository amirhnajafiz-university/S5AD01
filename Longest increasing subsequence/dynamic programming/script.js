function lis(arr, n)
{
	let lis = Array(n).fill(0);
	let i, j, max = 0;

	for(i = 0; i < n; i++)
		lis[i] = 1;
		
	for(i = 1; i < n; i++)
		for(j = 0; j < i; j++)
			if (arr[i] > arr[j] && lis[i] < lis[j] + 1)
				lis[i] = lis[j] + 1;

	for(i = 0; i < n; i++)
		if (max < lis[i])
			max = lis[i];

	return max;
}

let arr = [ 10, 22, 9, 33, 21, 50, 41, 60 ];
let n = arr.length;
document.write("Length of lis is " + lis(arr, n) + "\n");
