from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework_simplejwt.tokens import RefreshToken


User = get_user_model()



# ==========================
# REGISTER STUDENT
# ==========================

class RegisterView(APIView):

    def post(self, request):

        email = request.data.get("email")
        password = request.data.get("password")


        if not email.endswith("@vidyashilp.edu.in"):

            return Response(
                {"error":"Only Vidyashilp email allowed"},
                status=400
            )


        if User.objects.filter(email=email).exists():

            return Response(
                {"error":"Already registered"},
                status=400
            )


        user = User.objects.create_user(

            username=email.split("@")[0],

            email=email,

            password=password,

            role="student"

        )


        return Response(
            {
                "message":
                "Registration successful"
            }
        )





# ==========================
# LOGIN
# ==========================

class LoginView(APIView):


    def post(self,request):


        email=request.data.get("email")

        password=request.data.get("password")



        user=authenticate(

            username=email,

            password=password

        )



        if user is None:

            return Response(
                {
                "error":
                "Invalid login details"
                },
                status=400
            )



        refresh=RefreshToken.for_user(user)



        return Response({

            "access":
            str(refresh.access_token),


            "refresh":
            str(refresh),


            "role":
            user.role

        })






# ==========================
# CHANGE PASSWORD
# ==========================


class ChangePasswordView(APIView):


    def post(self,request):


        email=request.data.get("email")

        new_password=request.data.get("password")



        user=User.objects.filter(
            email=email
        ).first()



        if not user:

            return Response(
                {
                "error":"User not found"
                },
                status=404
            )



        user.set_password(
            new_password
        )

        user.save()



        return Response(
            {
            "message":
            "Password changed"
            }
        )







# ==========================
# FORGOT PASSWORD
# ==========================


class ForgotPasswordView(APIView):


    def post(self,request):


        email=request.data.get("email")



        user=User.objects.filter(
            email=email
        ).first()



        if not user:


            return Response(
                {
                "error":
                "Email not found"
                },
                status=404
            )



        # demo reset
        # real email can be added later

        return Response(
        {
        "message":
        "Email verified. Reset password now."
        }
        )





# ==========================
# RESET PASSWORD
# ==========================


class ResetPasswordView(APIView):


    def post(self,request):


        email=request.data.get("email")

        password=request.data.get("password")



        user=User.objects.filter(
            email=email
        ).first()



        if not user:

            return Response(
            {
            "error":"User not found"
            },
            status=404
            )



        user.set_password(password)

        user.save()



        return Response(
        {
        "message":
        "Password reset successful"
        }
        )