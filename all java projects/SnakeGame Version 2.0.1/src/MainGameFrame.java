import java.awt.Image;
import javax.swing.ImageIcon;
import javax.swing.JFrame;

public class MainGameFrame extends JFrame{

	public static void main(String[] args) {
		new MainGameFrame();
	}
	
	MainGameFrame(){
		Image image = new ImageIcon("Images//snake.png").getImage();
		this.setTitle("Snake Game Version 2.0.1");
		this.setIconImage(image);
		this.setDefaultCloseOperation(this.EXIT_ON_CLOSE);
		this.add(new FramePanel());
		this.setResizable(false);
		this.pack();
		this.setVisible(true);
		this.setLocationRelativeTo(null);
	}
}




