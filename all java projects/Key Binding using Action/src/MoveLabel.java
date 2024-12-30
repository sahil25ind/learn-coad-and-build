import java.awt.Color;
import java.awt.event.ActionEvent;

import javax.swing.AbstractAction;
import javax.swing.Action;
import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.KeyStroke;

public class MoveLabel {
	
	JFrame frame;
	JLabel label;
	Action upAction;
	Action downAction;
	Action leftAction;
	Action rightAction;
	Action resetAction;
	ImageIcon RocketImage;
	
	MoveLabel(){
		RocketImage = new ImageIcon("Images//1Rocket-Emoji.png");
		

		frame = new JFrame("KeyBinding Using Action Key");
		frame.setDefaultCloseOperation(frame.EXIT_ON_CLOSE);
		frame.setSize(700,700);
		frame.getContentPane().setBackground(Color.black);
		frame.setLocationRelativeTo(label);
		frame.setLayout(null);
		
		label = new JLabel();
		label.setBounds(330,550,100,100);
		label.setIcon(RocketImage);
	//	label.setBackground(Color.red);
	//	label.setOpaque(true);
		
		upAction = new UpAction();
		downAction = new DownAction();
		leftAction = new LeftAction();
		rightAction = new RightAction();
		resetAction = new ResetAction();
		
		label.getInputMap().put(KeyStroke.getKeyStroke("UP"), "UpAction");
		label.getActionMap().put("UpAction", upAction);
		
		label.getInputMap().put(KeyStroke.getKeyStroke("DOWN"), "DownAction");
		label.getActionMap().put("DownAction", downAction);
		
		label.getInputMap().put(KeyStroke.getKeyStroke("LEFT"), "LeftAction");
		label.getActionMap().put("LeftAction", leftAction);
		
		label.getInputMap().put(KeyStroke.getKeyStroke("RIGHT"), "RightAction");
		label.getActionMap().put("RightAction", rightAction);
		
		label.getInputMap().put(KeyStroke.getKeyStroke('f'), "ResetAction");
		label.getActionMap().put("ResetAction", resetAction);


		label.getInputMap().put(KeyStroke.getKeyStroke('w'), "UpAction");
		label.getActionMap().put("UpAction", upAction);
		
		label.getInputMap().put(KeyStroke.getKeyStroke('s'), "DownAction");
		label.getActionMap().put("DownAction", downAction);
		
		label.getInputMap().put(KeyStroke.getKeyStroke('a'), "LeftAction");
		label.getActionMap().put("LeftAction", leftAction);
		
		label.getInputMap().put(KeyStroke.getKeyStroke('d'), "RightAction");
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
			label.setLocation(label.getX(), label.getY()+10);
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
	
	public class ResetAction extends AbstractAction{
		
		@Override
		public void actionPerformed(ActionEvent e) {
			label.setLocation(330,550);
		}
	}
}
