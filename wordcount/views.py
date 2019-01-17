from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'wordcount/home.html')

def about(request):
    return render(request, 'wordcount/about.html')

def count(request):
    full_text = request.GET['fulltext']
    words = full_text.split() 
    word_dictionary = {}
    

    for word in words:
        if word in word_dictionary:
            #increase
            word_dictionary[word]+=1
        else:
            # add to dictionary
            word_dictionary[word]=1

    return render(request, 'wordcount/count.html', {'fulltext':full_text, 'total' : len(words),'dictionary': word_dictionary.items()})
