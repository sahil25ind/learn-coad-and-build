import javax.swing.*;

public class MyFrame extends JFrame{
	
	DrawOnPanel panel;
	
	MyFrame(){
		this.setDefaultCloseOperation(this.EXIT_ON_CLOSE);

		panel = new DrawOnPanel();
		this.add(panel);
		this.pack();
		this.setLocationRelativeTo(null);
		this.setVisible(true);
	}
}