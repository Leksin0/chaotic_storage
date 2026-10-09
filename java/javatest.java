package javaproject;

import junit.framework.TestCase;
import junit.framework.Test;
import junit.framework.TestSuite;

// Test's classname is prefixed with "test"
public class testSomeClass extends TestCase {

	private auxTestClass _testClass;

	public testSomeClass(String aTestName)  {
		super(aTestName);
	}

	public void setUp()  {
		// some setup code
	}

	public void tearDown()  {
		// tear down code
	}


// Implementing suite() is obligatory
	public static Test suite() {
		return new TestSuite(testSomeClass.class);
	}

// Making a test runnable alone is obligatory
	public static void main(String [] args)  {
		junit.textui.TestRunner.run(testSomeClass.class);
	}
}
