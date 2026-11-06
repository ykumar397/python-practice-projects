from datetime import datetime, date


class Bill():

    def __init__(self, vendor, service, amount, invoice_date, due_date, status="unpaid"):
        self.vendor = vendor.lower()
        self.service = service.lower()
        self.amount = amount
        self.invoice_date = invoice_date
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d").date()
        self.status = status.lower()


    def __repr__(self):
        return f"""
vendor          : {self.vendor}
service         : {self.service}
amount          : {self.amount}
invoice Date    : {self.invoice_date}
due date        : {self.due_date}
status          : {self.status}
"""

    def mark_as_paid(self):
        self.status = "paid"

    def is_overdue(self):
        return self.status == "unpaid" and date.today() > self.due_date

    def to_dict(self):
        return {
            "vendor"       : self.vendor,
            "service"      : self.service,
            "amount"       : self.amount,
            "invoice_date" : self.invoice_date,
            "due_date"     : str(self.due_date),
            "status"       : self.status
        }

