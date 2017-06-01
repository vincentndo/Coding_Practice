import java.util.*;
import java.math.*;

public class Operators {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        double mealCost = scan.nextDouble(); // original meal price
        int tipPercent = scan.nextInt(); // tip percentage
        int taxPercent = scan.nextInt(); // tax percentage
        scan.close();
      
        // Write your calculation code here.
        double all = mealCost * (1 + tipPercent / 100.0 + taxPercent / 100.0);
      
        // cast the result of the rounding operation to an int and save it as totalCost 
        int totalCost = (int) Math.round(all);
      
        // Print your result
        System.out.println("The total meal cost is " + totalCost + " dollars.");
    }
}
