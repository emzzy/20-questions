import java.util.Scanner;

public class NameConcatenation {
    public static void main(String[] myArgs){
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter your first name: ");
        String firstName = scanner.nextLine();

        System.out.print("Enter your last name: ");
        String lastName = scanner.nextLine();

        System.out.print("Enter your age: ");
        int userAge = scanner.nextInt();
        scanner.nextLine();
        int age = 2025 - userAge;

        System.out.printf("Welcome, %s %s born %d", firstName, lastName, age);

        System.out.println("\nWhat is your gender?\nEnter Male/Female or Other: ");
        String gender = scanner.nextLine();
        String role = "";

        if (gender.equalsIgnoreCase("male")){
            role = "son";
        } else if (gender.equalsIgnoreCase("female")) {
            role = "daughter";
        }
        System.out.printf("%s, %s of %s %d", firstName, role, lastName, age);

        scanner.close();
    }
}
