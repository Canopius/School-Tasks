class Main {
    public static void main(String[] args) {
        int[] ToSearch = {1,4,6,10,23,106,255,500,5002,50064};
        int ToFind = 1;
        int ub, lb, mid, len;
        len = ToSearch.length;
        ub = len;
        lb = 0;

        while (true){ // Bad I know but it works
            mid = lb + (ub - lb) / 2;

            if (ub < lb){
                System.out.println(ToFind + " not found.");
                return;
            }

            if (ToSearch[mid] > ToFind){
                ub = mid - 1;
            } else if(ToSearch[mid] < ToFind){
                lb = mid + 1;
            } else{
                System.out.println(mid);
                return;
            }
        }
    }
  }