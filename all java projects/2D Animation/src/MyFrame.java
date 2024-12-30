import javax.swing.JFrame;

public class MyFrame extends JFrame{

	MyPanel panel;
	
	MyFrame(){
		this.setDefaultCloseOperation(this.EXIT_ON_CLOSE);
		this.setTitle("2D Animation Using Timer and ActionListener and fuck you!");
		panel = new MyPanel();
		this.add(panel);
		this.pack();
		this.setLocationRelativeTo(null);
		this.setVisible(true);
	}
}
