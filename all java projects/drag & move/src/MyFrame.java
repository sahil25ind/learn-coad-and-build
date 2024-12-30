import javax.swing.JFrame;

public class MyFrame extends JFrame{
	
	DragPanel dragPanel = new DragPanel();
	
	MyFrame(){
		this.setDefaultCloseOperation(this.EXIT_ON_CLOSE);
		this.setTitle("Move by Dragging");
		this.setSize(700,700);
		
		this.add(dragPanel);
		
		this.setVisible(true);
	}
}
