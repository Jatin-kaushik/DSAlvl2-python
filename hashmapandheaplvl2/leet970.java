import java.util.ArrayList;
import java.util.HashSet;
import java.util.Scanner;
import java.lang.Math;

public class leet970{
    public static void main(String[] args){
        Scanner scn = new Scanner(System.in);
        int x = scn.nextInt();
        int y = scn.nextInt();
        int bound = scn.nextInt();
        ArrayList<Integer> arr = solve(x,y,bound);
        scn.close();
        System.out.println(arr);
    }

    public static ArrayList<Integer> solve(int x, int y, int bound){
        HashSet<Integer> set = new HashSet<>();
        for(int i =0 ; i<bound; i++){
            for(int j = 0; j<bound; j++){
                int pf = (int)(Math.pow(x,i) + Math.pow(y,j));
                if (pf <= bound) set.add(pf);
                else break;
            }
        }
        // System.out.println(set);
        ArrayList<Integer> arr = new ArrayList<>();
        arr.addAll(set);
        return arr;
    }
}