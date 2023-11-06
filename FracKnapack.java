
import java.util.Arrays;
import java.util.*;

public class FracKnapack {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int capacity=sc.nextInt();
        int n=sc.nextInt();
        int weight[]=new int[n]; 
        int value[]={10,15,10,12,8};
        double ratio[]=new double[value.length];

        //calculate value/weight
        for(int i=0;i<weight.length;i++){
            ratio[i]=value[i]/weight[i];
        }

        //Sort the ratio
        Arrays.sort(ratio);

        //Highest ratio add to knapsack
        double maxvalue=0;
        for(int i=0;i<ratio.length;i++){
            if(capacity==0){
                break;
            }

            if(weight[i]<capacity){
                maxvalue=maxvalue+value[i];
                capacity=capacity-weight[i];
            }else{
                double fraction=capacity/weight[i];
                maxvalue=maxvalue+fraction*value[i];
                capacity=0;
            }
        }
        System.out.println("Max Value is :"+maxvalue);
    }
}