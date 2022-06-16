from app.forms import InputPhoneForm, InputPhones
from django.views.generic.edit import FormView
from django.http import HttpResponse
from app.asterisk_manager import call_from_manager, call_from_abonent
from django.shortcuts import render
from threading import Thread


class CallFromManager(FormView):
    template_name = 'call_from_manager.html'
    form_class = InputPhoneForm
    success_url = '/call_from_manager/'

    def post(self, request):
        Thread(target=call_from_manager, args=(request.POST['phone_to'], )).start()
        return HttpResponse('Ожидайте звонка менеджера на номер %s. ' % request.POST['phone_to'])

    def form_valid(self, form):
        return super(InputPhoneForm, self).form_valid(form)


class CallFromAbonent(FormView):
    template_name = 'call_from_abonent.html'
    form_class = InputPhones
    success_url = '/call_from_abonent/'

    def post(self, request):
        Thread(target=call_from_abonent, args=(request.POST['phone_from'], request.POST['phone_to'])).start()
        return HttpResponse('Ожидайте звонка менеджера на номер %s. ' % request.POST['phone'])

    def form_valid(self, form):
        return super(InputPhoneForm, self).form_valid(form)


def main_page(request):
    return render(request, 'main_page.html')
