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

