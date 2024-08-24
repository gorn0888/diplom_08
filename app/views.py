from django.shortcuts import render, redirect
from app.models import Person, Category, Division, Dismissed
from django.db.models import Q
from app.forms import PersonForm
from django.views.generic import DeleteView, UpdateView


def index(request):
    # contents = [ # передаем словари в списке 
    #     {'last_name': 'Anikeev', 'first_name': 'Roman', 'unit': 'Ypravlenie'},
    #     {'last_name': 'Smirnov', 'first_name': 'Ivan', 'unit': 'OMON'},
    #     {'last_name': 'Anikeev', 'first_name': 'Roman', 'unit': 'Ypravlenie'},
    #     {'last_name': 'Anikeev', 'first_name': 'Roman', 'unit': 'Ypravlenie'},
    #     {'last_name': 'Anikeev', 'first_name': 'Roman', 'unit': 'Ypravlenie'},
    # ]
    return render(request, 'index.html', context=None)

def build_template(lst: list, cols: int) -> list[list]:
    # new_list = []
    # for i in range(0, len(lst), cols):
    #     new_list.append(lst[i:i + cols])
    # return new_list
    '''refactoring'''
    return [lst[i:i + cols] for i in range(0, len(lst), cols)]
###########################################################################
'''Person'''
###########################################################################
def person_list(request):
    division = Division.objects.all()
    category = Category.objects.all()
    search_query = request.GET.get('search', None)
    if search_query:
        persons = Person.objects.filter(
            Q(first_name__icontains=search_query)
            |
            Q(last_name__icontains=search_query)
        )
    else:
        persons = Person.objects.all()
    return render(request,
                  'app/list_employees.html',
                  context={
                        'persons_list': build_template(persons, 1),
                        'category': category,
                        'division': division,
                  }
    )

def person_detail(request, pk):
    persons = Person.objects.get(pk=pk) 
    category = Category.objects.all()
    division = Division.objects.all()
    return render(
        request,
        'app/person_detail.html',
        context={
            'persons': persons,
            'category': category,
            'division': division,
        }
    )
###########################################################################
'''Category'''
###########################################################################
def category_list(request, pk):
    persons = Person.objects.filter(category=pk) #отсортировывает по категориям в caterory_list.thml
    categories = Category.objects.get(pk=pk) #выводит одну категорию в <h1> category_list.html
    category = Category.objects.all() #чтобы в navbar отображался список сотрудников
    division = Division.objects.all() #чтобы в navbar отображался список подразделений
    return render(
        request,
        'app/category_list.html',
        context={
            'categories': categories,
            'category': category,
            'persons': persons,
            'division': division,
        }
    )

###########################################################################
'''Division'''
###########################################################################
def division_list(request, pk):
    persons = Person.objects.filter(division=pk) #отсортировывает по категориям в division_list.thml
    divisions = Division.objects.get(pk=pk) #выводит одну категорию в <h1> category_list.html
    category = Category.objects.all()
    division = Division.objects.all() #чтобы в navbar отображался список сотрудников
    return render(
        request,
        'app/division_list.html',
        context={
            'divisions': divisions,
            'category': category,
            'persons': persons,
            'division': division,
        }
    )
    

###########################################################################
''' добавление сотрудника '''
###########################################################################
def create_person(request):
    persons = Person.objects.all()
    division = Division.objects.all()
    category = Category.objects.all()
    # form = PersonForm
    return render(
        request,
        'app/create_person.html',
        context={
            'persons': persons,
            'division': division,
            'category': category,
            # 'form': form,
        }
    )

def add_person(request):
    # error = ''
    # if request.method == 'POST':
    #     form = PersonForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('person_list_url')
    #     else:
    #         error = 'форма не валидна'
    #     data = {
    #         'form': form,
    #         'error': error,
    #     }
    #     return render(request, 'app/person_list.html', data)

    persons = Person.objects.all()
    division = Division.objects.all()
    category = Category.objects.all()
    add_person = Person()
    add_person.last_name = request.POST['last_name']
    add_person.first_name = request.POST['first_name']
    add_person.patronymic = request.POST['patronymic']
    add_person.category = Category.objects.get(pk=request.POST['select_category'])
    add_person.division = Division.objects.get(pk=request.POST['select_division'])
    add_person.save()
    return render(
        request,
        'app/add_person.html',
        context = {
            'persons': persons,
            'division': division,
            'category': category,
        }
    )

###########################################################################
""" Увольнение """
###########################################################################
def dismissed_person(request):
    persons = Person.objects.all()
    division = Division.objects.all()
    person_dismissed = Dismissed()
    person_dismissed.last_name = request.POST['last_name']
    person_dismissed.first_name = request.POST['first_name']
    person_dismissed.patronymic = request.POST['patronymic']
    person_dismissed.division = request.POST['division']
    person_dismissed.dismissed_from = request.POST['dismissed_from']
    person_dismissed.order = Division.objects.get(pk=request.POST['order'])
    person_dismissed.number_order = request.POST['number_order']
    person_dismissed.order_from = request.POST['order_from']
    person_dismissed.save()
    if request.method == "POST":
        persons_excluded = Person()    
        persons_excluded.excluded = Person.objects.get(excluded=request.POST['excluded'])
        persons_excluded.save()
    return render(
        request,
        'app/dismissed_person.html',
        context = {
            'persons': persons,
            'division': division,
        }
    )
    
    

###########################################################################
""" Отчет """
###########################################################################
def report(request):
    persons = Person.objects.count()
    division = Division.objects.all()
    form = PersonForm
    return render(
        request,
        'app/report.html',
        context = {
            'persons': persons,
            'division': division,
            'form': form,
        }
    )

###########################################################################
""" Редактирование записи """
###########################################################################
class PersonUpdateView(UpdateView):
    model = Person
    template_name = 'app/edit_person.html'
    fields = ['last_name', 'first_name', 'category'] 

###########################################################################
''' Удаление сотрудника '''
###########################################################################
class PersonDeleteView(DeleteView):
    model = Person
    success_url = '/app/' # перенаправление после удаления объекта
    template_name = 'app/delete_person.html' # старница обработки
    # context_object_name = 'delete_person'
