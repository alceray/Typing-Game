from django.shortcuts import render
from django.http import JsonResponse
from gutendex.models import Book
import random
import nltk

def book_list(request):
    books = Book.objects.all()
    data = {"books": list(books.values("book_id", "title", "sentence_count", "text"))} 
    return JsonResponse(data)

def random_sentences(request):
    # Fetch all books
    books = list(Book.objects.all())

    while books:
        # Choose a random book
        book = random.choice(books)

        # Split the text into sentences
        sentences = nltk.tokenize.sent_tokenize(book.text)

        # Check if the book has at least 3 sentences
        if len(sentences) < 3:
            # If not, remove it from the list and try another book
            books.remove(book)
            continue

        # Choose 3 random sentences
        random_sentences = random.sample(sentences, 3)

        # Return the random sentences
        return JsonResponse({'sentences': random_sentences})

    return JsonResponse({'error': 'No suitable book found'}, status=500)
