public static void main(String[] args){
}

public boolean linearIn(int[] outer, int[] inner) {
int count = 0;
  for(int j = 0; j < inner.length; j++){
    for(int i = 0; i < outer.length; i++){
      if(outer[i] == inner[j]){
        count++;
        break;
      }
      }
    }
    return count >= inner.length;
  }

public boolean canBalance(int[] nums){
   int total1 = 0;
  
  for (int i = 0; i < nums.length; i++) {
    total1 += nums[i];
    int total2 = 0;
    for (int j = nums.length-1; j > i; j--) {
      total2 += nums[j];
    }
    if (total1 == total2)
      return true;
  }
  return false;
}

public int maxSpan(int[] nums) {
  int m = 0;
    for(int i = 0; i < nums.length; i++) {
      int j = nums.length - 1;
      while(nums[i] != nums[j])
        j--;
        int s = j - i + 1;
        if(s > m)
          m = s;
  }
  return m;
}

public int[] fix45(int[] nums) {
  int i = 0;
  int j = 0;
  while(j < nums.length && nums[j] != 5)
    j++;
    while(i < nums.length) {
      if(nums[i] == 4) {
        int t = nums[i+1];
        nums[i+1] = nums[j];
        nums[j] = t;
        while((j < nums.length && nums[j] != 5) || j == i + 1)
          j++;
      }
      i++;
  }
  return nums;
}

public int[] fix34(int[] nums) {
  int i = 0;
  while(i < nums.length && nums[i] != 3)
    i++;
  int j = i + 1;
  while(j < nums.length && nums[j] != 4)
    j++;
  while(i < nums.length) {
    if(nums[i] == 3) {
      int temp = nums[i+1];
      nums[i+1] = nums[j];
      nums[j] = temp;
      while(j < nums.length && nums[j] != 4)
        j++;
      }
      i++;
  }
  return nums;
}
