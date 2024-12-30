import java.awt.Color;

import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JLayeredPane;

public class sahil{
	public static void main(String[] args) {
		JLabel label1 = new JLabel();
		label1.setBounds(50,50,150,150);
		label1.setBackground(Color.blue);
		label1.setOpaque(true);
		
		JLabel label2 = new JLabel();
		label2.setBounds(100,100,150,150);
		label2.setBackground(Color.red);
		label2.setOpaque(true);
		
		JLabel label3 = new JLabel();
		label3.setBounds(150,150,150,150);
		label3.setBackground(Color.green);
		label3.setOpaque(true);
		
		
		JLayeredPane layeredPane = new JLayeredPane();
		layeredPane.setBounds(0,0,500,500);
		
		layeredPane.add(label1, Integer.valueOf(0));
		layeredPane.add(label2, Integer.valueOf(1));
		layeredPane.add(label3, Integer.valueOf(3));
		
		JFrame frame = new JFrame(" create and add buttons to frame");
		frame.setDefaultCloseOperation(frame.EXIT_ON_CLOSE);
		frame.setLayout(null);
		frame.setSize(500,500);
		frame.setVisible(true);
		frame.add(layeredPane);
	}
}
