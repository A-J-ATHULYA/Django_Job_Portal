from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
from .models import Applicant

# Create your views here.

#Welcome API

class WelcomeView(View):
    def get(self, request):
        data = {
            "Message": "Welcome to Job Portal..!"
        }
        return JsonResponse(data)


#Company Information API

class CompanyView(View):
    def get(self, request):
        data = {
            "Company_Name": "Infosys",
            "Location": "Kochi",
            "Industry": "IT",
            "Contact": "9876543210",
            "Status": "Hiring"
        }
        return JsonResponse(data)


#Job Information API

class JobView(View):
    def get(self, request):
        data = {
            "Job_ID": 101,
            "Job_Title": "Python Developer",
            "Company": "Infosys",
            "Location": "Kochi",
            "Salary": 25000,
            "Job_Type": "Full Time",
            "Experience": "Fresher",
            "Qualification": "B.Tech",
            "Status": "Active"
        }
        return JsonResponse(data)


#Applicant Information API

class ApplicantView(View):
    def get(self, request):
        applicants = Applicant.objects.all()

        data = []

        for applicant in applicants:
            data.append({
                "id": applicant.id,
                "name": applicant.name,
                "email": applicant.email,
                "position": applicant.position,
                "experience": applicant.experience,
                "status": applicant.status
            })

        return JsonResponse({"Applicants": data})


#All Available Jobs API

class AllJobsView(View):
    def get(self, request):
        data = {
            "Jobs": [
                {
                    "Job_ID": 101,
                    "Job_Title": "Python Developer",
                    "Company": "Infosys",
                    "Location": "Kochi",
                    "Salary": 25000
                },
                {
                    "Job_ID": 102,
                    "Job_Title": "Frontend Developer",
                    "Company": "TCS",
                    "Location": "Bangalore",
                    "Salary": 30000
                },
                {
                    "Job_ID": 103,
                    "Job_Title": "Django Developer",
                    "Company": "Wipro",
                    "Location": "Chennai",
                    "Salary": 28000
                },
                {
                    "Job_ID": 104,
                    "Job_Title": "Software Tester",
                    "Company": "UST",
                    "Location": "Trivandrum",
                    "Salary": 22000
                }
            ]
        }

        return JsonResponse(data)


#Employer Information API

class EmployerView(View):
    def get(self, request):
        data = {
            "Employer_ID": 1,
            "Employer_Name": "Renjith",
            "Company": "Infosys",
            "Designation": "HR Manager",
            "Contact": "9876543210",
            "Email": "hr@gmail.com",
            "Location": "Kochi"
        }

        return JsonResponse(data)