class patient(object):
    nextid=0
    def __init__(self, name, allergies, bed = 0):
        patient.nextid = patient.nextid + 1
        self.id = patient.nextid

        self.name = name
        self.allergies = allergies
        self.bed_number = bed

    def displayinfo(self):
        print "Patient Name:", self.name
        print "Patient ID:", self.id
        print "Allergies:", self.allergies
        print "Bed Number:", self.bed_number

class hospital(object):
    def __init__(self, name, capicity):
        self.patients = []
        self.name = name
        self.capicity = capicity
        self.patientcount = 0
        self.availbeds = []
        for bed in range(0, capicity):
            self.availbeds.append(bed + 1)


    def admit(self, patient):
        if self.patientcount >= self.capicity:
            print "Not admitting new patients. Hospital is at capicity."
        else:
            bed = self.availbeds.pop(0)
            patient.bed_number = bed
            self.patients.append(patient)
            self.patientcount += 1
            print "Patient {} admitted to hosptial {}.".format(patient.name, self.name)

    def discharge(self, patient):
        if patient in self.patients:
            self.patients.remove(patient)
            self.availbeds.append(patient.bed_number)
            patient.bed_number = 0
            self.patientcount -= 1
            print "Patient {} discharged from hosptial {}.".format(patient.name, self.name)
        else:
            print "Patient not found."

    def listpatients(self):
        print "Patients admitted to {}:".format(self.name)
        for patient in self.patients:
            patient.displayinfo()

    def patientlookup(self, id):
        for patient in self.patients:
            if id == patient.id:
                return patient
        return None

h1 = hospital("St Nonsense", 5)
h2 = hospital("St Mundos", 3)

p1 = patient("Frank Write", "none")
p2 = patient("Joe Smoe", "work")
p3 = patient("John Schmidt", "none")
p4 = patient("Sally Young", "benadryl")
p5 = patient("Georgette Perez", "none")

h2.admit(p1)
h2.admit(p2)
h2.admit(p3)
h2.admit(p5)
h1.admit(p4)
h1.discharge(p4)

h2.listpatients()

p=h2.patientlookup(2)
h2.discharge(p)
h2.listpatients()
print "Available bed numbers:", h2.availbeds
h2.admit(p5)
print "Available bed numbers:", h2.availbeds
