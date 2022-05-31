class Bowling{
	public static void main(String[] args) {
		int nums[] = new int[]{-3,1,1,9,9,2,5,5};
		int B[] = new int[nums.length+1];
		int n = nums.length;
		B[n] = 0;
		for ( int i=n-2; i>=0;i--){
			B[i] = Math.max(B[i+1], (B[i+1]+nums[i]));
			B[i] = Math.max(B[i], (B[i+2]+nums[i]*nums[i+1]));
		}
		System.out.println(B[0]);
	}
}
