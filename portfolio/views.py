from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from .models import Portfolio, Project, Skill, ContactMessage
from django.contrib import messages

def portfolio_view(request):
    portfolio = Portfolio.objects.first()  # Birinchi portfolio ma'lumotlarini olish
    projects = Project.objects.filter(portfolio=portfolio)
    skills = Skill.objects.filter(portfolio=portfolio)

    context = {
        'portfolio': portfolio,
        'projects': projects,
        'skills': skills,
    }
    return render(request, 'portfolio.html', context)


def contact_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Xabarni bazaga saqlash
        ContactMessage.objects.create(name=name, email=email, message=message)

        # Email jo‘natish
        send_mail(
            subject=f"Portfolio orqali yangi xabar - {name}",
            message=f"Ism: {name}\nEmail: {email}\n\nXabar:\n{message}",
            from_email='your-email@example.com',  # O'zingizning emailingiz
            recipient_list=['your-email@example.com'],  # Xabar tushishi kerak bo'lgan email
            fail_silently=False,
        )

        messages.success(request, "Xabaringiz yuborildi!")
        return redirect('portfolio')

    return redirect('portfolio')
