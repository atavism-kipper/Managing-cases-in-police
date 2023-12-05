# police_system.py
from officer import Officer
from case_manager import CaseManager
from report_generator import ReportGenerator

class PoliceSystem:
    def __init__(self):
        self.officer = Officer()
        self.case_manager = CaseManager()
        self.report_generator = ReportGenerator()

    def run(self):
        print("Police System Running")
        # Implement your system logic here
