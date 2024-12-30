import java.io.File;
import javax.sound.sampled.*;
import java.util.Scanner;

public class audioPlayerOnTerminal{
	public static void main(String[] args)throws Exception {
		Scanner scanner = new Scanner(System.in);
		File audioFile = new File("i like the way you kiss me.wav");
		System.out.println(audioFile.getAbsolutePath());
		AudioInputStream audioStream = AudioSystem.getAudioInputStream(audioFile);
		Clip audioClip = AudioSystem.getClip();
		audioClip.open(audioStream);
		
		String choice = "";
				
		while(!choice.equals("Q")) {
		System.out.println("P = play, S = stop, R = reset, Q = quit");
		System.out.print("Enter your choice: ");
		choice = scanner.next();
		choice = choice.toUpperCase();
		
		switch(choice) {
		case ("P"):		audioClip.start();
		break;
		case ("S"):		audioClip.stop();
		break;
		case ("R"):		audioClip.setMicrosecondPosition(0);
		break;
		case ("Q"): 	audioClip.close();
		break;
		default:	System.out.println("Not a Valid Input!");
			}
		}
		System.out.println("Program is Closing...");
	}
}
