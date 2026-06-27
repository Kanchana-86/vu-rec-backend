from django.core.management.base import BaseCommand
from users.models import User


class Command(BaseCommand):

    help = "Create default VU-REC users"


    def handle(self,*args,**kwargs):


        users = [

            {
            "username":"reviewer",
            "email":"reviewer@vidyashilp.edu.in",
            "password":"reviewer123",
            "role":"reviewer"
            },


            {
            "username":"chairperson",
            "email":"chairperson@vidyashilp.edu.in",
            "password":"vu-rec2026",
            "role":"chairperson"
            },


            {
            "username":"secretary",
            "email":"secretary@vidyashilp.edu.in",
            "password":"vu-rec2026",
            "role":"member_secretary"
            }

        ]



        for data in users:


            if not User.objects.filter(
                email=data["email"]
            ).exists():


                User.objects.create_user(

                    username=data["username"],

                    email=data["email"],

                    password=data["password"],

                    role=data["role"]

                )


                self.stdout.write(
                "Created "+data["email"]
                )


            else:

                self.stdout.write(
                "Already exists "+data["email"]
                )