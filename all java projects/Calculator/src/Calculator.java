import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class Calculator implements ActionListener{
	
	Font myFont = new Font("calibri",Font.BOLD,30);
	JFrame frame;
	JTextField textField;
	JPanel panel;
	JButton[] numberButtons = new JButton[10];
	JButton[] functionButtons = new JButton[9];
	JButton addButton,subButton,mulButton,divideButton,negativeButton;
	JButton decimalButton,equalButton,deleteButton,clearButton;
	
	double num1=0,num2=0,result=0;
	char operator;
	
	Calculator(){

		frame = new JFrame("Calculator");
		frame.setDefaultCloseOperation(frame.EXIT_ON_CLOSE);
		frame.setSize(410,550);
		frame.setLayout(null);
		frame.setResizable(false);
		
		textField = new JTextField();
		textField.setBounds(50,25,300,50);
		textField.setFont(myFont);
		textField.setEditable(false);
		
		addButton = new JButton("+");
		subButton = new JButton("-");
		mulButton = new JButton("*");
		divideButton = new JButton("/");
		decimalButton = new JButton(".");
		equalButton = new JButton("=");
		deleteButton = new JButton("Delete");
		clearButton = new JButton("Clear");
		negativeButton = new JButton("(+/-)");
		
		functionButtons[0] = addButton;
		functionButtons[1] = subButton;
		functionButtons[2] = mulButton;
		functionButtons[3] = divideButton;
		functionButtons[4] = decimalButton;
		functionButtons[5] = equalButton;
		functionButtons[6] = deleteButton;
		functionButtons[7] = clearButton;
		functionButtons[8] = negativeButton;

		for(int i =0;i<9;i++) {
			functionButtons[i].addActionListener(this);
			functionButtons[i].setFont(myFont);
			functionButtons[i].setFocusable(false);
		}

		for(int i = 0;i<10;i++) {
			numberButtons[i] = new JButton(String.format("%d", i)); //i used this because i wanted to see if it will work or not
		//	numberButtons[i] = new JButton(String.valueOf(i)); //this one was in the video and it works just fine
			numberButtons[i].addActionListener(this);
			numberButtons[i].setFont(myFont);
			numberButtons[i].setFocusable(false);
		}
		
		negativeButton.setBounds(50,430,100,50);
		deleteButton.setBounds(150,430,100,50);
		clearButton.setBounds(250,430,100,50);
		
		panel = new JPanel();
		panel.setBounds(50,100,300,300);
		panel.setLayout(new GridLayout(4,4,10,10));
		panel.add(numberButtons[1]);
		panel.add(numberButtons[2]);
		panel.add(numberButtons[3]);
		panel.add(functionButtons[0]);
		panel.add(numberButtons[4]);
		panel.add(numberButtons[5]);
		panel.add(numberButtons[6]);
		panel.add(functionButtons[1]);
		panel.add(numberButtons[7]);
		panel.add(numberButtons[8]);
		panel.add(numberButtons[9]);
		panel.add(functionButtons[2]);
		panel.add(functionButtons[5]);
		panel.add(numberButtons[0]);
		panel.add(functionButtons[4]);
		panel.add(functionButtons[3]);
		
		frame.add(panel);
		frame.add(negativeButton);
		frame.add(deleteButton);
		frame.add(clearButton);
		frame.add(textField);
		frame.setVisible(true);
	}

	public static void main(String[] args) {
		
		Calculator calculator = new Calculator();
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		for(int i = 0;i<10;i++) {
			if(e.getSource()==numberButtons[i]) {
				textField.setText(textField.getText().concat(String.valueOf(i))); //this one is from the video
			//	textField.setText(textField.getText().concat(String.format("%d", i))); //i added this myself not sure why
			}
		}
			if(e.getSource()==decimalButton) {
				textField.setText(textField.getText().concat("."));
			}
			if(e.getSource()==addButton) {
				num1 = Double.parseDouble(textField.getText());
				operator = '+';
				textField.setText(null);
			}
			if(e.getSource()==subButton) {
				num1 = Double.parseDouble(textField.getText());
				operator = '-';
				textField.setText(null);
			}
			if(e.getSource()==mulButton) {
				num1 = Double.parseDouble(textField.getText());
				operator = '*';
				textField.setText(null);
			}
			if(e.getSource()==divideButton) {
				num1 = Double.parseDouble(textField.getText());
				operator = '/';
				textField.setText(null);
			}
			
			if(e.getSource()==equalButton) {
				num2 = Double.parseDouble(textField.getText());
			//	textField.setText(null);
				
				switch(operator) {
				case '+': result = num1 + num2;
				break;
				case '-': result = num1 - num2;
				break;
				case '*': result = num1 * num2;
				break;
				case '/': result = num1 / num2;
				break;
				}
			//	textField.setText(String.format("%d",result)); //this line just breaks the entire code 
				textField.setText(String.valueOf(result));
			}
			
			if(e.getSource()==deleteButton) {
				String textFieldString = textField.getText();
				textField.setText(null);
				
				for(int i =0;i<textFieldString.length()-1;i++) {
					textField.setText(textField.getText()+textFieldString.charAt(i));
				}
			}
			if(e.getSource()==clearButton) {
				textField.setText(null);
			}
			if(e.getSource()==negativeButton) {
				double temp = Double.parseDouble(textField.getText());
				temp *= -1;
				textField.setText(String.valueOf(temp));
			}
	}
}
