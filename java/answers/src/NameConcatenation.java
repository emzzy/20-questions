import java.util.Scanner;

public class NameConcatenation {
    public static void main(String[] myArgs){
        Scanner userInput = new Scanner(System.in);

        System.out.println("Enter your first name, last name, and age: ");

        String firstName = userInput.nextLine();
        String lastName = userInput.nextLine();
        int age = userInput.nextInt();

        System.out.printf("Welcome, %s %s born %d", firstName, lastName, age);
        System.out.println("What is your gender?\nEnter Male/Female or Other: ");

        String gender = userInput.nextLine();



    }
}
