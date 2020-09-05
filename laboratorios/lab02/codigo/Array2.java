  
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
public boolean no14(int[] nums) {
 boolean one=true, four=true;  
    for (int i : nums) {
        if(i==1) one = false;                
        if(i==4) four = false;  
    }
      return one || four;           
}
public boolean only14(int[] nums) {
    
     
    for (int i : nums) {
        if(i!=1&&i!=4){
          return false;
        }                 
       
    }
      return true;           
}
public boolean has22(int[] nums) {
    for(int i = 0; i < nums.length - 1; i++) {
        if(nums[i] == 2 && nums[i + 1] == 2)
            return true;
    }
                
    return false;
}
