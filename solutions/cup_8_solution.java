// Auto-generated java solution for CUP-8
    // Generated: 2025-08-28 19:56:14
    // Requirement: Write a Java program that takes two integer inputs from the user, adds them, and prints the sum to the console.  Handle potential `NumberFormatException`.

    import java.util.Scanner;

public class Adder {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int num1 = 0;
        int num2 = 0;

        try {
            System.out.print("Enter the first integer: ");
            num1 = Integer.parseInt(scanner.nextLine());

            System.out.print("Enter the second integer: ");
            num2 = Integer.parseInt(scanner.nextLine());

        } catch (NumberFormatException e) {
            System.err.println("Invalid input. Please enter integers only.");
            scanner.close();
            return;
        }

        int sum = num1 + num2;
        System.out.println("The sum is: " + sum);
        scanner.close();
    }
}

    // End of generated code for CUP-8
    