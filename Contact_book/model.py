

class Contacts:

    def __init__(self, name, phone, email, label):
        self.name   = name
        self.phone  = phone
        self.email  = email
        self.label  = label


    def __setattr__(self, name, value):
        if isinstance(value, str) and name not in ["phone"]:
            value = value.lower()

        if isinstance(value, str) and name in ["name", "label"]:
            value = value.title()

        super().__setattr__(name, value)

    def __repr__(self):
        return f"""
Name  : {self.name}
Phone : {self.phone}
Email : {self.email}
Label : {self.label}
"""

    def to_csv(self):
        return [self.name, self.phone, self.email, self.label]


