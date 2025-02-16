import os

 
class Medication:
    """This class stores information about medication specifics"""

    def __init__(self, med_name, frequency, dosage, time, initial, expirary):
        self.dosage = dosage
        self.frequency = frequency
        self.med_name = med_name
        self.time = time
        self.initial = initial
        self.expirary = expirary

    def print_medical_info(self):
        print(f'{self.med_name}, {self.frequency}, {self.dosage}, {self.time}, {self.initial}, {self.expirary}')
   
    def __str__(self):
        """This function returns a string representation of the object. Requried for printing
        Returns an instance as a string"""
        return (f'{self.med_name}, {self.frequency}, {self.dosage}, {self.time}, {self.initial}, {self.expirary}')
   

class PatientPersonalMedBook:
    """This class stores an individual's information. Used by Doctor"""
    #This class takes in the parameters first name, last name, doctor.

    def __init__(self):
        #This class contains a medication folder.
        self.medication = list()

    def print_med_list(self):
        #if the list is empty, say so.

        if len(self.medication) == 0:
            print("You are currently not on medication.")
        else:
            for meds in self.medication:
                index = self.medication.index(meds) +1
                print(f'{index}. {str(meds)}')


    def add_medication(self, med_name, frequency, dosage, time, initial, expirary):
        """This function is used to append medication to the
        list stored in the medication book"""
        new_medication = Medication(med_name, frequency, dosage, time, initial, expirary)
        self.medication.append(new_medication)

        print(f"Added {new_medication}")

        return(self.medication)
   
    #COME BACK TO DELETE MEDICATION



def main():
    """Main function for the medication book.
    Allows user to perform functions on the book."""
    print("Welcome to the Medication Tracker! Pack, Track, Attack!")

    def strip_non_numerics(dosage_consumed):
        """Removes all non-numeric characters"""
        return ''.join(filter(str.isdigit,dosage_consumed))

    med_folder = PatientPersonalMedBook()

    quit_program = False
    while not quit_program:

        user_input = input(">")
        if user_input != "":
            input_list = user_input.split()
            input_command = input_list[0].lower()


            if input_command == "add":
                med_name = input_list[1]
                frequency = input_list[2]
                dosage = input_list[3]
                time = input_list[4]
                initial = input_list[5]
                expirary = input_list[6]
                           
                med_folder.add_medication(med_name, frequency, dosage, time, initial, expirary)
                   
            elif input_command == "list":
                med_folder.print_med_list()
           
            elif input_command == "quit":
                quit_program = True

            #At this point, the user should then hit the "go to dashboard" button
            #which will exit them out of the while loop and execute the summary.
   
    #Summary
    print("Summary of Medication")
   
    for meds in med_folder.medication:
        medication_name = meds.med_name
        print(medication_name)
        amount_remaining = 0
        initial_amount = meds.initial
        dosage_consumed = meds.dosage
        amount_remaining = int(strip_non_numerics(initial_amount)) - int(strip_non_numerics(dosage_consumed))
        print(f"The amount remaining is {amount_remaining}")
        renew = meds.expirary
        print(renew)
           

main()