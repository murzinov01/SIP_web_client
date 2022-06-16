from app.forms import InputPhoneForm
from django.views.generic.edit import FormView
from django.http import HttpResponse
from app.asterisk_manager import connect_to_asterisk
from threading import Thread


class CallBackView(FormView):
    template_name = 'app.html'
    form_class = InputPhoneForm
    success_url = '/call/'

    def post(self, request):
        Thread(target=connect_to_asterisk, args=(request.POST['phone'], )).start()
        # connect_to_asterisk(number=request.POST['phone'])
        return HttpResponse('Ожидайте звонка менеджера на номер %s. ' % request.POST['phone'])

    def form_valid(self, form):
        return super(InputPhoneForm, self).form_valid(form)
