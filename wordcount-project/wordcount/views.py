from django.http import HttpResponse
from django.shortcuts import render
import operator


def homepage(request):
	print ("Who Who Ha Hey now!!!")
	return render(request, 'home.html', {'brand':'Locu Locations Service'})

def locations(request):
	print ("locatins page!!!")
	return HttpResponse("Los Angeles Short Term Lease Optins for Filming and Events!")

def count(request):
	fulltext = request.GET['fulltext']
	wordlist = fulltext.split()
	worddictionary = {}
	for word in wordlist:
		if word in worddictionary:
			#Count Occurences of Words in Dictionary
			worddictionary[word] += 1
		else:
			#Add to Dictionary
			worddictionary[word] = 1

	sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)




	return render(request, 'count.html',{'fulltext':fulltext,'count':len(wordlist),'sortedwords':sortedwords})

	#worddictionary.items()

	## return 'You Are Home'
