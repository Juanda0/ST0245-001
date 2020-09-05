  
public static void main(String[] args){
}

public int matchUp(int[] nums1, int[] nums2) {
  int i = 0;
  int count = 0;
  int con = 0;
  while(i<nums1.length){
    con = nums1[i]-nums2[i];
    if( con <= 2 && con >= -2 && con != 0){
      count++;
    }
    i++;
    }
    return count;
  }

public boolean has77(int[] nums) {
  int i = 0;
  while(i<=nums.length-2){
    if(nums[i] == 7){
      if (nums[i+1] == 7){
        return true;
      }else if (i+2 < nums.length && nums[i+2] == 7){
        return true;
      }
      }
      i++; 
    }
  return false;
}
