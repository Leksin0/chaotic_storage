package javaproject;

import java.awt.event.ActionListener;
import java.awt.event.WindowListener;

public interface SomeInterface extends ActionListener, WindowListener  {

	static int CONSTANT_NUMBER_ONE = 0;

	static int CONSTANT_NUMBER_TWO = 1;

	void setValue(int aValue);

	int getValue();	
}
