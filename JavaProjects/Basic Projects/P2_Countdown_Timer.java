import java.util.Scanner;

public class P2_Countdown_Timer {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the number of seconds for the countdown: ");
        int seconds = scanner.nextInt();

        System.out.println("Countdown starts now!");

        // Loop for the countdown
        for (int i = seconds; i >= 0; i--) {
            System.out.println("["+i+"]");
            // Delay for 1 second
            try {
                Thread.sleep(1000); // 1000 milliseconds = 1 second
            } catch (InterruptedException e) {
                System.out.println("Countdown was interrupted.");
            }
        }

        System.out.println("Time's up!");

        // Close the scanner
        scanner.close();
    }
}
