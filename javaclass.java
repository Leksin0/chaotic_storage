package javaproject;

import java.awt.event.WindowAdapter;
import java.awt.event.ActionEvent;
import java.io.IOException;

public class SomeClass extends WindowAdapter implements SomeInterface {

	private int _classMember; // prefix a member with "_"

// prefix a method's formal arguments with "a"
	public SomeClass(int aFirstValue, int aSecondValue)  {
		setValue(aValue);
	}

	public void actionPerformed(ActionEvent aEvent)  {
		usefulMethod();
	}

	public void setValue(int aValue)  {
		if (CONSTANT_NUMBER_ONE == aValue)  { // put a constant first in comparison
			usefulMethod();
    		} else  {
			usefulMethod();
	    	}
	}

	public int getValue()  {
		int returnValue = 0;

		switch (_classMember)  {
		        case CONSTANT_NUMBER_ONE:
				returnValue = CONSTANT_NUMBER_ONE;
	                	break;
			case CONSTANT_NUMBER_TWO:
				returnValue = CONSTANT_NUMBER_TWO;
			        break;
		        default:
		      		returnValue = -1;
	        }
	        return returnValue;
	}

	private void usefulMethod()  {
		try  {
			usefulMethodWhoThrowsExceptions();
	    	} catch (IOException aIOE)  {
	        	// fix it - not to leave uncaught
	    	} catch (ClassCastException aCCE)  {
	        	// fix it - not to leave uncaught
	    	}
	}

	private void usefulMethodWhoThrowsExceptions() throws IOException,
								ClassCastException  {
		throw new IOException("I cannot find anything");
    }
}