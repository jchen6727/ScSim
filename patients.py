import random as rnd
import numpy as np
from math import ceil as ceil

class patients():
    def __init__(self):
        self.patients = {}
        self.rnd = rnd
        self.rnd.seed()
        self.total = 0
    def addPatientType(self, num, patient):
        self.total += num
        self.patients[self.total] = patient
    def rndFetchPatient(self):
        index = int(self.rnd.random() * self.total)
        for patient in self.patients:
            if index < patient:
                return self.patients[patient]
        return None
    def lblFetchPatient(self, label):
        for patient in self.patients:
            if self.patients[patient].label == label:
                return self.patients[patient]


class patient():
    def __init__(self, label, params ):
        self.label = label
        self.params = params

if __name__ == '__main__':
    pop = patients()
    pt0 = patient('pt0', {'LOS': 7, 'threshold0': 3, 'threshold1':4, 'threshold2':5})
    pt1 = patient('pt1', {'LOS': 10, 'threshold0': 4, 'threshold1': 7, 'threshold3': 10})
    pop.addPatientType(3, pt0)
    pop.addPatientType(1, pt1)
    pts = []
    for i in range(10):
        pts.append(pop.rndFetchPatient().label)
