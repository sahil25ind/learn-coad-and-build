import java.util.Scanner;
import javax.sound.sampled.*;
import java.io.File;

public class test{
    public static void main(String[] args)throws Exception {
        Scanner scanner = new Scanner(System.in);

        File audioFile = new File("i like the way you kiss me.wav");
        AudioInputStream audioStream = AudioSystem.getAudioInputStream(audioFile);
        Clip clip = AudioSystem.getClip();
        clip.open(audioStream);
        
        String choice = "";
        
        while(!choice.equals("Q")) {
        	System.out.println("P = play, S = stop, R = reset, Q = quit");
        	System.out.print("Enter your choice: ");
        	choice = scanner.next();
        	choice = choice.toUpperCase();
        	
        	switch(choice) {
        	case ("P"):	 clip.start();
        	break;
        	case ("S"):		clip.stop();
        	break;
        	case ("R"):		clip.setMicrosecondPosition(0);
        	break;
        	case ("Q"):		clip.close();
        	break;
        	default:	System.out.println("Invalid Input!");
        	}
        }
        System.out.println("Program is Closing...");
    }
}