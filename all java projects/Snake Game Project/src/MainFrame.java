import java.awt.Image;

import javax.swing.ImageIcon;
import javax.swing.JFrame;

public class MainFrame extends JFrame{

	public static void main(String[] args) { //main method
		new MainFrame();
	}
	
	MainFrame(){
		Image icon = new ImageIcon("Images//snake.png").getImage(); //create game icon
		this.setTitle("Snake Game Practice Project"); //set game title
		this.setIconImage(icon); //set game icon
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		this.setResizable(false); //set Resizable to false
		this.add(new GamePanel()); //adding game panel
		this.pack(); //pack it all
		this.setVisible(true); //make it visible
		this.setLocationRelativeTo(null); //centering the frame
	}
}
/*
 * 	How to turn Source Code into Executable(.exe) windows application
 * 
 * 	1.download latest version java 
 * 	2.download Launch4j
 *  3.export jar file of the source code
 *  4.convert image to (.ico) file for icon
 *  5.Build Wrapper and app is ready to use if user device already have installed latest version java then app
 *    will run just fine if not then user cant run the app thats because java application requires
 *    JVM (java virtual machine) in order to run any java app so make sure you already complete the step.1	
 *    https://www.mediafire.com/file/jgfsiblhw09go4b/Snake+Game+Zip+File.zip/file
 */