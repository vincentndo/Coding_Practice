import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class DataTypes {
	
    public static void main(String[] args) {
        int i = 4;
        double d = 4.0;
        String s = "HackerRank ";
		
        Scanner scan = new Scanner(System.in);

        /* Declare second integer, double, and String variables. */
        int integer;
        double real;
        String string;

        /* Read and save an integer, double, and String to your variables.*/
        // Note: If you have trouble reading the entire String, please go back and review the Tutorial closely.
        integer = scan.nextInt();
        real = scan.nextDouble();
        scan.nextLine();
        string = scan.nextLine();
        
        /* Print the sum of both integer variables on a new line. */
        System.out.println(i + integer);

        /* Print the sum of the double variables on a new line. */
        System.out.println(d + real);
		
        /* Concatenate and print the String variables on a new line; 
        	the 's' variable above should be printed first. */
        System.out.println(s + string);

        scan.close();
    }
}

