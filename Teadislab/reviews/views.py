from django.shortcuts import render
posts = [
{
'author': 'Teadi',
'title': 'Call of Duty',
'review': 'This game is just ok.',
'date_posted': '25-02-21',
},
{
'author': 'Teadi',
'title': 'Call of Duty',
'review': 'This video game is amazing!',
    'date_posted': '25-02-21',
}]
def home(request):
    context = {
        'posts':posts
    }
    return render(request, 'reviews/home.html', context)
