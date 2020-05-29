public class Solution {
    public int threeSumClosest(ArrayList<Integer> A, int B) {
        int min = Integer.MAX_VALUE;
        int sum = Integer.MAX_VALUE;
        int arr[] = new int[A.size()];
        int  l = 0; 
        for(int m : A){
            arr[l++] = m;
        }
        Arrays.sort(arr);
        if(arr.length == 3)
            return arr[0] + arr[1] +arr[2];
        for(int i = 0;i<A.size()-2;i++)
        {
            int j = i+1;
            int k = A.size() - 1;
            while(j<k)
            {
              int sum1 = arr[i] + arr[j] + arr[k];
              int diff = Math.abs(sum1 - B);
              if(diff == 0)
                  return B;
              if(diff<min)
              {
                  min = diff;
                  sum = sum1;
              }
              if(sum1<B)
                j++;
              else
                k--;
            }
        }
        return sum;
    }
}
