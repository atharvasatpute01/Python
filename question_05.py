
class Patient:
    def __init__(self, patient_id, patient_name, bill_amount):
        self.__patient_id = patient_id
        self.patient_name = patient_name
        self.__bill_amount = bill_amount

    def get_patient_id(self):
        return self.__patient_id

    def update_bill(self, amount):
        if amount >= 0:
            self.__bill_amount = amount
            print("Bill updated successfully")
        else:
            print("Bill amount cannot be negative!")

    def display_details(self):
        print("Patient ID:", self.__patient_id)
        print("Patient Name:", self.patient_name)
        print("Bill Amount:", self.__bill_amount)


p1 = Patient(101, "Rahul", 5000)

p1.display_details()

print("Patient ID:", p1.get_patient_id())

p1.update_bill(7500)

p1.display_details()

p1.update_bill(-1000)