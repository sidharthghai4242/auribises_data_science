import java.util.*;
public class recursion{
    public static void main(String[] args) {
        Stack<Integer> stack=new Stack<>();
        for(int i=0;i<=Integer.MAX_VALUE;i++){
            stack.add(i);
            System.out.println(i);
        }
        // System.out.println(stack.peek());
    }
    public static void series(int a,int b,int c){
        if(c==0){
            return;
        }
        
        int d=a+b;
        System.out.print(d+" ");
        a=b;
        b=d;
        series(a, b, c-1);
    }
}