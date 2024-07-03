import java.util.*;

public class P1_Number_Guessing_Game {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int bestScore = Integer.MAX_VALUE; // Initialize bestScore to a high value
        
        System.out.println(" ------------------------------------------");
        System.out.println("| Guess The Right Number To Break The Loop |");
        System.out.println(" ------------------------------------------");
        
        String ans = "yes";
        
        while (ans.equalsIgnoreCase("yes")) {
            int guess = 0;
            int attempt = 0;

            System.out.print("Enter the maximum number for random generation: ");
            int maxNumber = scan.nextInt();

            Random rand = new Random();
            int r = rand.nextInt(maxNumber) + 1;

            while (guess != r) {
                System.out.print("Enter Your Guess : ");
                guess = scan.nextInt();
                attempt++;

                if (guess < r) {
                    System.out.println("======== Too low! Try again. ========");
                } else if (guess > r) {
                    System.out.println("======== Too high! Try again. ========");
                } else {
                    System.out.println("Congratulations! You guessed the correct number.");
                    System.out.println("Your Score : " + attempt);

                    // Update bestScore if the current attempt is better
                    if (attempt < bestScore) {
                        bestScore = attempt;
                    }

                    System.out.println("Best Score : " + bestScore);
                }
            }

            System.out.print("Want to play again? (yes or no) : ");
            scan.nextLine(); // Clear the newline character from the buffer
            ans = scan.nextLine();

            if (ans.equalsIgnoreCase("no")) {
                System.out.println(" -----------------------------");
                System.out.println("| Thanks For Playing The Game |");
                System.out.println(" -----------------------------");
            }
        }

        scan.close();
    }
}
