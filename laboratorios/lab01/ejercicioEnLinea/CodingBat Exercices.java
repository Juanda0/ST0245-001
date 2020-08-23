class Main {
  // Main
  public static void main(String[] args) {
     //Espacio para pruebas
  }
  // Recursion 1
  //1
  public static int factorial(int n) {
    if (n == 1){
    return 1;
  }
  return n * factorial(n-1);
  }
  //2
  public static int bunnyEars(int bunnies) {
  if (bunnies == 0){
      return 0;
    }
    return 2 + bunnyEars(bunnies-1);
  }
  //3
  public static int fibonacci(int n) {
  if (n == 0){
    return 0;
  }
  if (n == 1){
    return 1;
  }
  return fibonacci(n-1)+fibonacci(n-2);
  }
  //4
  public static int bunnyEars2(int bunnies) {
    if (bunnies == 0){
      return 0;
    }
    if (bunnies % 2 == 0){
      return 3 + bunnyEars2(bunnies-1);
    }else{
      return 2 + bunnyEars2(bunnies-1);
    }
  }
  //5
  public static int triangle(int rows) {
  if (rows == 0){
    return 0;
  }
  return rows+triangle(rows-1);
  }
  //Recursion 2
  //1
  public static boolean groupSum6(int start, int[] nums, int target) {
     if(start == nums.length){
       if (target == 0){ 
         return true;
       }else{
         return false;
       }
     }
     if(nums[start] == 6){
       return (groupSum6(start + 1, nums, target - nums[start]));
     }else{
       return (groupSum6(start + 1, nums, target - nums[start]) || groupSum6(start + 1, nums, target));
     }
  }
  //2
  public  static boolean groupSumClump(int start, int[] nums, int target){
     if(target==0) {
         return true;
     }else if(start>= nums.length) {
         return false;
     }else{
         int end = start;
         while (end< nums.length && nums[end]==nums[start]) {
           end ++;
         }
         int length = end-start;
         return groupSumClump(end, nums,target) || groupSumClump(end, nums, target-nums[start]*length);
      }
   }
  //3
  public static boolean groupSum5(int start, int[] nums, int target) {
     if(start == nums.length){
       if (target == 0){ 
         return true;
       }else{
         return false;
       }
     }else{
       if(nums[start] % 5 == 0){
         if(start + 1 < nums.length && nums[start+1] == 1)
             return (groupSum5(start + 2, nums, target - nums[start]));
         else{
             return (groupSum5(start + 1, nums, target - nums[start]));
         }
       }
     return (groupSum5(start + 1, nums, target - nums[start]) || groupSum5(start + 1, nums, target));
     }
  }
  //4
  public static boolean groupNoAdj(int start, int[] nums, int target){
     if (target == 0){
        return true;
     }else if(start >= nums.length){
        return false;
     }else{
        return (groupNoAdj(start + 1, nums, target) || groupNoAdj(start + 2, nums, target-nums[start]));
     }
  }
  //5.1
  public boolean splitArray(int[] nums){
     return splitArrayAux(0, nums, 0, 0);
   }
  //5.2
  public boolean splitArrayAux(int start, int[] nums, int suma1, int suma2){
     if(start >= nums.length){
       return suma1 == suma2;
     }                            
     return splitArrayAux(start+1, nums, suma1 + nums[start], suma2) || splitArrayAux(start+1, nums, suma1, suma2 + nums[start]);
   }
}
