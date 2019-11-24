/*
BankAccount created by ZXx_Neto_xXZ
An OOP code that creates and implements bank accounts
*/
public class BankAccount {
	/*
	Declaring the instance variables for the class
	@param finalBalance holds the total money of the object bank account
	@param interestRate is passed to the interest method and is always constant
	*/
	private double finalBalance; 
	private final double interestRate = .075;
	/*
	creating an empty BankAccount object and setting its finalBalance to 0
	@param finalBalance is set automatically to 0 when no other parameters are inputted.
	*/
	public BankAccount() {
		finalBalance = 0; // if the object of Bank Account class is empty its initial value is 0
	}
	/*
	creating a BankAccount object with an initial balance
	@param iniBal is the given initial balance inputed by the user when creating the object
	@param finalBalance is set to the given input
	*/
	public BankAccount(double iniBal) {
		finalBalance = iniBal; 
	}
	/*
	method for updating the finalBalance instance variable when new balance is added
	@param amount is the input to be added to the finalBalance
	*/
	public void deposit(double amount) { 
		finalBalance += amount;
	}
	/*
	method for updating the finalBalance instance variable when balance is subtracted
	@param amount is the input to be subtracted to the finalBalance
	*/
	public void withdraw(double amount) {
		finalBalance -= amount; // method for subtracting a value from the current value of the bank account
	}
	/*
	method for updating the finalBalance instance variable when balance is subtracted
	@param amount is the input to be subtracted to the finalBalance
	*/
	public double getBalance() {
		return finalBalance; // returns the actual value of the object
	}
	/*
	method for calculating and updating the finalBalance for an invested amount of balance with interest
	@param amount is to be applied the interest
	@param term is the time period or frequency of the applied interest
	@param intest performs the calculations for the interest
	@param total gets the actual value to be added to the bank account
	*/
	public void interest(double term, double amount) {
		double intest = (Math.pow((1+(interestRate/term)), term)) - 1;
		double total = intest*amount;
		this.deposit(total); //implicit variable
	}
}
