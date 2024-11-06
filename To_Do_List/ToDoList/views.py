from django.shortcuts import render ,redirect ,HttpResponseRedirect
from ToDoList.models import Note_data

# Create your views here.

def main(request):
    if request.method=="POST":
        note_name=request.POST.get('note')
        desc=request.POST.get('desc')
        noteData= Note_data(note=note_name, desc=desc ,)
        noteData.save()
    NOTE_d=Note_data.objects.all()  
    return render( request ,'index.html',{ 'note_d':NOTE_d} )

def abc(request ,note):
    NOTE_d=Note_data.objects.get(pk=note)
    NOTE_d.delete()
    return HttpResponseRedirect('/')

# def note_Disply(requst):

 
#     return render(request ,'index.html',NOTE_DATA)