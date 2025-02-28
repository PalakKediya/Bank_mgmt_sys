class GenerateReport():
        def __init__(self, acc_no, process, amount, bal):
            self.acc_no = acc_no
            self.process = process
            self.amount = amount
            self.balance = bal

        def __str__(self):
            return f"{self.acc_no}      |{self.process}     |{self.amount}      |{self.balance}"