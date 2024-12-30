import java.awt.Color;
import java.awt.Image;

import javax.swing.ImageIcon;
import javax.swing.JFrame;

public class MainFrame extends JFrame{

	public static void main(String[] args) {
		new MainFrame();
	}
	
	MainFrame(){
		Image image = new ImageIcon("Images//snake.png").getImage();
		this.setTitle("Snake Game v2");
		this.setIconImage(image);
//		this.setSize(700,700);
//		this.getContentPane().setBackground(Color.red);
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		this.add(new GamePanel());
		this.pack();
		this.setLocationRelativeTo(null);
//		this.setResizable(false);
		this.setVisible(true);
	}

}
