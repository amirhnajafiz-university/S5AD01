<script>

function Solution(arr, n)
{
	if (n % 2 == 0)
	{
		var z = n / 2;
		var e = arr[z];
		var q = arr[z - 1];
		var ans = (e + q) / 2;
		return ans;
	} else {
		var z = Math.floor(n / 2);
		return arr[z];
	}
}

var arr1 = [ -5, 3, 6, 12, 15 ];
var arr2 = [ -12, -10, -6, -3, 4, 10 ];

var i = arr1.length;
var j = arr2.length;

var l = i+j;
const arr3 = arr1.concat(arr2);

arr3.sort(function(a, b) {
	return a - b;
});

document.write("Median = " + Solution(arr3, l));

</script>
