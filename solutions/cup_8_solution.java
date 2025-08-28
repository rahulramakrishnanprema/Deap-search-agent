// Auto-generated java solution for CUP-8
    // Generated: 2025-08-28 19:55:18
    // Requirement: Write a Java function that takes two integer arguments and returns their sum.  Handle potential integer overflow.

    import java.math.BigInteger;

public class IntegerAdder {

    /**
     * Adds two integers, handling potential integer overflow.
     *
     * @param a The first integer.
     * @param b The second integer.
     * @return The sum of a and b, or null if overflow occurs.
     */
    public static BigInteger addIntegers(int a, int b) {
        try {
            return BigInteger.valueOf(a).add(BigInteger.valueOf(b));
        } catch (ArithmeticException e) {
            return null; // Indicate overflow
        }
    }


    public static void main(String[] args) {
        int a = Integer.MAX_VALUE;
        int b = 1;

        BigInteger sum = addIntegers(a, b);

        if (sum != null) {
            System.out.println("Sum: " + sum);
        } else {
            System.out.println("Integer overflow occurred.");
        }


        a = Integer.MIN_VALUE;
        b = -1;
        sum = addIntegers(a,b);
        if (sum != null) {
            System.out.println("Sum: " + sum);
        } else {
            System.out.println("Integer overflow occurred.");
        }

        a = 10;
        b = 20;
        sum = addIntegers(a,b);
        if (sum != null) {
            System.out.println("Sum: " + sum);
        } else {
            System.out.println("Integer overflow occurred.");
        }
    }
}

    // End of generated code for CUP-8
    