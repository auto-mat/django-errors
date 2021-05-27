from django.http import HttpResponse
from django.views import View
from django.db import transaction
from .models import *
from datetime import datetime
from django.core.files.base import ContentFile
import time

class AddThing(View):
    def get(self, request, *args, **kwargs):
        attr = "foo" + datetime.now().strftime("%H:%M:%S")
        thing = Thing1.objects.create(attr=attr)
        return HttpResponse('Thing added!' + str(thing))

class AddThingError(View):
    def get(self, request, *args, **kwargs):
        attr = "foo" + datetime.now().strftime("%H:%M:%S")
        thing = Thing1.objects.create(attr=attr)
        raise Exception()
        return HttpResponse('Thing added!' + str(thing))


class AddThingErrorAtomic(View):
    @transaction.atomic
    def get(self, request, *args, **kwargs):
        attr = "foo" + datetime.now().strftime("%H:%M:%S")
        thing = Thing1.objects.create(attr=attr)
        raise Exception()
        return HttpResponse('Thing added!' + str(thing))


class AddThingWithSaveMethod(View):
    @transaction.atomic
    def get(self, request, *args, **kwargs):
        attr = "foo" + datetime.now().strftime("%H:%M:%S")
        thing = Thing2.objects.create(attr=attr)
        return HttpResponse('Thing added!' + str(thing))


class AddThingErrorAtomicWithSaveMethod(View):
    @transaction.atomic
    def get(self, request, *args, **kwargs):
        attr = "foo" + datetime.now().strftime("%H:%M:%S")
        thing = Thing2.objects.create(attr=attr)
        raise Exception()
        return HttpResponse('Thing added!' + str(thing))


class AddThingWithFile(View):
    @transaction.atomic
    def get(self, request, *args, **kwargs):
        attr = "foo" + datetime.now().strftime("%H:%M:%S")
        myfile = ContentFile("hello world")
        thing = Thing2.objects.create(attr=attr)
        thing.file.save("foo" + datetime.now().strftime("%H.%M.%S"), myfile)
        return HttpResponse('Thing added!' + str(thing))


class AddThingErrorAtomicWithFile(View):
    @transaction.atomic
    def get(self, request, *args, **kwargs):
        attr = "foo" + datetime.now().strftime("%H:%M:%S")
        myfile = ContentFile("hello world")
        thing = Thing2.objects.create(attr=attr)
        thing.file.save("foo" + datetime.now().strftime("%H.%M.%S"), myfile)
        raise Exception()
        return HttpResponse('Thing added!' + str(thing))


class Loop(View):
    def get(self, request, *args, **kwargs):
        while True:
            time.sleep(1)
        return HttpResponse('A price kissed me')




class ViewsList(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("\n".join(['<p><a href="{url}">{url}</a></p>'.format(url=url) for url in [
            "./add-thing",
            "./add-thing-error",
            "./add-thing-error-atomic",
            "./add-thing-with-file",
            "./add-thing-error-atomic-with-file",
            "./add-thing-with-save-method",
            "./add-thing-error-atomic-with-save-method",
            "./loop",
        ]]))

