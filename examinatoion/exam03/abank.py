
from bank import Bank
class ABank(Bank):
    def __init__(self, bankname: str) -> None:
        super().__init__(bankname)
        self.__loanmount = float
        self.__loanyear = float
        self.__loanrate = float
        self.interest = ''
        self.monthlypay = ''

    @property
    def loanmount(self):
        return self.__loanmount

    @loanmount.setter
    def loanmount(self,value):
        self.__loanmount = value

    @property
    def loanyear(self):
        return self.__loanyear

    @loanyear.setter
    def loanyear(self,value):
        self.__loanyear = value

    @property
    def loanrate(self):
        return self.__loanrate

    @loanrate.setter
    def loanrate(self,value):
        self.__loanrate = value

    
    def flat_rate(self):
        super().flat_rate()
        self.interest = self.loanmount * self.loanyear * self.loanyear
        


    def display_interest(self):
        print (f'******{self.bankname}*****')
        print (f'Loan: {self.loanmount:,.2f}')
        print (f'Rate: {self.loanrate:.2f} %')
        print (f'Year: {self.loanyear}')
        print (f'------Interest------')
        print (f'Interest :{self.interest} baht')
        print (f'Monthly Repayment :{self.monthlypay} baht')



if __name__ == "__main__":
    scb = ABank("SCB Loan Info")
    scb.loanmount = 100000
    scb.loanrate = 3
    scb.loanyear = 2
    scb.display_interest()
    #scb.print_interest()
    
    