import java.awt.Image;
import javax.swing.*;

public class MainFrame extends JFrame{

	public static void main(String[] args) {
		new MainFrame();
	}
	
	MainFrame(){
		Image imageIcon = new ImageIcon("Images//snake.png").getImage();
		this.setTitle("Snake Game Practice Project");
		this.setIconImage(imageIcon);
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		this.add(new GamePanel());
		this.pack();
		this.setResizable(false);
		this.setVisible(true);
		this.setLocationRelativeTo(null);
	}
}
