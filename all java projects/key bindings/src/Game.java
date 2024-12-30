import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class Game {
	
	JFrame frame;
	JLabel label;
	Action upAction;
	Action downAction;
	Action leftAction;
	Action rightAction;	

	Game(){
		frame = new JFrame("Key Binding using Action");
		frame.setDefaultCloseOperation(frame.EXIT_ON_CLOSE);
		frame.setSize(500,500);
		frame.setLayout(null);
		
		label = new JLabel();
		label.setBounds(110,110,150,150);
		label.setBackground(Color.blue);
		label.setOpaque(true);
		
		upAction = new UpAction();
		downAction = new DownAction();
		leftAction = new LeftAction();
		rightAction = new RightAction();
		
		label.getInputMap().put(KeyStroke.getKeyStroke("UP"), "UpAction");
		label.getActionMap().put("UpAction", upAction);
		
		label.getInputMap().put(KeyStroke.getKeyStroke("DOWN"), "DownAction");
		label.getActionMap().put("DownAction", downAction);
		
		label.getInputMap().put(KeyStroke.getKeyStroke("LEFT"), "LeftAction");
		label.getActionMap().put("LeftAction", leftAction);
		
		label.getInputMap().put(KeyStroke.getKeyStroke("RIGHT"), "RightAction");
		label.getActionMap().put("RightAction", rightAction);
		
		frame.add(label);
		frame.setVisible(true);
	}
	
	public class UpAction extends AbstractAction{

		@Override
		public void actionPerformed(ActionEvent e) {
			label.setLocation(label.getX(), label.getY()-10);
			
		}
	}
	
	public class DownAction extends AbstractAction{

		@Override
		public void actionPerformed(ActionEvent e) {
			label.setLocation(label.getX(),label.getY()+10);
			
		}
	}
	
	public class LeftAction extends AbstractAction{

		@Override
		public void actionPerformed(ActionEvent e) {
			label.setLocation(label.getX()-10,label.getY());
			
		}
	}
	
	public class RightAction extends AbstractAction{

		@Override
		public void actionPerformed(ActionEvent e) {
			label.setLocation(label.getX()+10,label.getY());
			
		}
	}
}
