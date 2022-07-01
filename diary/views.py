from django.views import View
from django.shortcuts import render
from .models import Diary

import diary

# Create your views here.
class DiaryTopView(View):
    def get(self, request, *args, **kwarg):
        diary_list = Diary.objects.all()
        print(diary_list)
        context = {
            'diary_list':diary_list,
        }
        return render(request, 'diary.html', context)

    def post(self, request, *args, **kwarg):
        new_data = Diary(title=request.POST['title'], subtitle=request.POST['subtitle'], body=request.POST['body'])
        new_data.save()
        return render(request, 'diary.html')


diary_top = DiaryTopView.as_view()

