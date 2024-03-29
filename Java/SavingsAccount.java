/*
BankAccount created by ZXx_Neto_xXZ
An OOP code that extends the BankAccount class and adds interest
*/
public class SavingAccounts extends BankAccount {

    /*
    @param interestRate is passed to the amountInterest method and is always constant
    @param interestRate2 is passed to the addInterest method
    */
    private final double interestRate = .075;
    private double interestRate2;

    public SavingAccounts(double rate) {
        interestRate2 = rate;
    }

    /*
   	method for adding an interest to the account
  	method for calculating and updating the finalBalance for an invested amount of balance with interest
	@param amount is to be applied the interest
	@param term is the time period or frequency of the applied interest
	@param intest performs the calculations for the interest
	@param total gets the actual value to be added to the bank account
    */

	public void amountInterest(double term, double amount) {
		double intest = (Math.pow((1+(interestRate/term)), term)) - 1;
		double total = intest*amount;
		this.deposit(total); //implicit variable
    }

    /*
    method for adding an interest to the account
    and updating the finalBalance for an invested amount of balance with interest
    */
    public void addInterest() {
		double interest = getBalance()*interestRate2 / 100;
		this.deposit(interest); //implicit variable
    }
}
