import java.awt.Color;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

import javax.swing.JFrame;

public class KeyListenerFrame extends JFrame implements KeyListener{

	public static void main(String[] args) {
		new KeyListenerFrame();
	}
	
	KeyListenerFrame(){
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		this.getContentPane().setBackground(Color.black);
		this.setSize(200,200);
		this.setBackground(Color.green);
		this.addKeyListener(this);
		this.setVisible(true);
		this.setLocationRelativeTo(null);
	}
//takes input in both case when a key is pressed and when a key is released
	@Override
	public void keyTyped(KeyEvent e) {
//		System.out.println("keyTyped: "+e.getKeyChar());
//		System.out.println("keyTyped: "+e.getKeyCode());
	}
//takes input when a key is pressed
	@Override
	public void keyPressed(KeyEvent e) {	//i think i prefer pressed over typed becase it only takes input when key is pressed
		System.out.println("keyPressed: "+e.getKeyChar());
		System.out.println("keyPressed: "+e.getKeyCode());
		
	}
//takes input when a key is released
	@Override
	public void keyReleased(KeyEvent e) {
//		System.out.println("keyReleased: "+e.getKeyChar());
//		System.out.println("keyReleased: "+e.getKeyCode());
		
	}
}
