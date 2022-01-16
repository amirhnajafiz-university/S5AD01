function max(a,b) { return (a > b) ? a : b; }

function max(a,b,c) { return Math.max(Math.max(a, b), c); }


function maxCrossingSum(arr, l, m,h)
{
	let sum = 0;
	let left_sum = Number.MIN_VALUE;
	for (let i = m; i >= l; i--) {
		sum = sum + arr[i];
		if (sum > left_sum)
			left_sum = sum;
	}

	sum = 0;
	let right_sum = Number.MIN_VALUE;
	for (let i = m + 1; i <= h; i++) {
		sum = sum + arr[i];
		if (sum > right_sum)
			right_sum = sum;
	}

	return max(left_sum + right_sum, left_sum, right_sum);
}

function maxSubArraySum(arr, l,h)
{
	if (l == h)
		return arr[l];

	let m = parseInt((l + h) / 2, 10);

	return max(maxSubArraySum(arr, l, m),
			maxSubArraySum(arr, m + 1, h),
			maxCrossingSum(arr, l, m, h));
}


let arr = [ 2, 3, 4, 5, 7 ];
let n = arr.length;
let max_sum = maxSubArraySum(arr, 0, n - 1);
document.write("Maximum contiguous sum is " + max_sum);
