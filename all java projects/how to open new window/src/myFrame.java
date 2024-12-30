import java.awt.Color;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JLabel;

public class myFrame extends JFrame implements KeyListener{
	
	JLabel label;
	ImageIcon imageRocket;
	ImageIcon rocketImage;
	
	myFrame(){
		imageRocket = new ImageIcon("Images//1Emoji-Rocket.png");
		rocketImage = new ImageIcon("Images//1Rocket-Emoji.png");
		
		label = new JLabel();
		label.setBounds(190,350,100,100);
		label.setHorizontalAlignment(label.CENTER);
		label.setVerticalAlignment(label.CENTER);
		label.setIcon(imageRocket);
	//	label.setIcon(rocketImage);
		
		this.setDefaultCloseOperation(this.EXIT_ON_CLOSE);
		this.getContentPane().setBackground(Color.black);
		this.setTitle("KeyListener Interface");
		this.setSize(500,500);
		this.setLayout(null);
		this.add(label);	
		this.addKeyListener(this);
		this.setVisible(true);
		
	}

	@Override
	public void keyTyped(KeyEvent e) {
	//	System.out.println("you just typed a key: "+e.getKeyChar());
		
		switch(e.getKeyChar()){
		case 'w': label.setLocation(label.getX(),label.getY()-10);
		break;
		case 'a': label.setLocation(label.getX()-10,label.getY());
		break;
		case 's': label.setLocation(label.getX(),label.getY()+10);
		break;
		case 'd': label.setLocation(label.getX()+10 ,label.getY());
		break;
		case 'f': label.setLocation(190,350);
		}
	}

	@Override
	public void keyPressed(KeyEvent e) {
	//	System.out.println("you just pressed a key: "+e.getKeyCode());
		
		switch(e.getKeyCode()) {
		case 37: label.setLocation(label.getX()-10,label.getY());
		break;
		case 38: label.setLocation(label.getX(),label.getY()-10);
		break;
		case 39: label.setLocation(label.getX()+10,label.getY());
		break;
		case 40: label.setLocation(label.getX(),label.getY()+10);
		break;
		}
		
	}

	@Override
	public void keyReleased(KeyEvent e) {
		System.out.println("you just released a key: "+e.getKeyChar());
		System.out.println("you just released a key: "+e.getKeyCode());
	}
}