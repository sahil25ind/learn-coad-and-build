import javax.swing.JFrame;

public class MyFrame extends JFrame{
	
	DragPanel dragPanel = new DragPanel();
	
	MyFrame(){
		this.setDefaultCloseOperation(this.EXIT_ON_CLOSE);
		this.setTitle("Drag it and Move it");
		this.setSize(800,800);
		
		this.add(dragPanel);
		
		this.setVisible(true);
	}

}
