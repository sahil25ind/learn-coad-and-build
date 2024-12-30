import java.awt.FlowLayout;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;

import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JLabel;

public class myFrame extends JFrame implements MouseListener{
	
	JLabel label;
	ImageIcon SmirkFaceEmoji;
	ImageIcon FearfulFaceEmoji;
	ImageIcon HuggingFaceEmoji;
	ImageIcon SurprisedFaceEmoji;
	ImageIcon ThinkingEmoji;
	
	myFrame(){
		SmirkFaceEmoji = new ImageIcon("Images//SmirkFaceEmoji.png");
		FearfulFaceEmoji = new ImageIcon("Images//FearfulFaceEmoji.png");
		HuggingFaceEmoji = new ImageIcon("Images//HuggingFaceEmoji.png");
		SurprisedFaceEmoji = new ImageIcon("Images//SurprisedFaceEmoji.png");
		ThinkingEmoji = new ImageIcon("Images//ThinkingEmoji.png");
		
		label = new JLabel();
	//	label.setBackground(Color.green);
	//	label.setOpaque(true);
		label.setIcon(SmirkFaceEmoji);
		label.addMouseListener(this);
		
		this.setDefaultCloseOperation(this.EXIT_ON_CLOSE);
		this.setTitle("MouseListener Interface");
		this.setSize(500,500);
		this.setLayout(new FlowLayout());
		this.setLocationRelativeTo(null);
		this.add(label);
		this.pack();
		this.setVisible(true);
	}

	@Override
	public void mouseClicked(MouseEvent e) {
		label.setIcon(SurprisedFaceEmoji);
		
	}

	@Override
	public void mousePressed(MouseEvent e) {
		label.setIcon(ThinkingEmoji);
		
	}

	@Override
	public void mouseReleased(MouseEvent e) {
		label.setIcon(FearfulFaceEmoji);
		
	}

	@Override
	public void mouseEntered(MouseEvent e) {
		label.setIcon(HuggingFaceEmoji);
		
	}

	@Override
	public void mouseExited(MouseEvent e) {
		label.setIcon(SmirkFaceEmoji);
		
	}
}