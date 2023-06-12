from django.core.management.base import BaseCommand
import nltk
from gutendex.models import Book
import requests
import re

nltk.download("punkt")


class Command(BaseCommand):
    help = "Download and store books"
    page_limit = 10

    def handle(self, *args, **options):
        # Fetch a list of books
        response = requests.get("http://gutendex.com/books")
        books = response.json()["results"]

        # Filter books that have 'text/plain' format
        books = [book for book in books if "text/plain" in book["formats"]]

        for book in books:
            try:
                # Download the book text
                response = requests.get(book["formats"]["text/plain"])
                response.raise_for_status()

                # Clean the text
                cleaned_text = re.sub(r"\s+", " ", response.text).strip()
                start_pattern = (
                    r"\*\*\* START OF THE PROJECT GUTENBERG EBOOK .*? \*\*\*"
                )
                end_pattern = r"\*\*\* END OF THE PROJECT GUTENBERG EBOOK .*? \*\*\*"
                start_match = re.search(start_pattern, cleaned_text)
                end_match = re.search(end_pattern, cleaned_text)
                if start_match and end_match:
                    cleaned_text = cleaned_text[start_match.end() : end_match.start()]

                # Filter the sentences
                sentences = nltk.tokenize.sent_tokenize(cleaned_text)
                filtered_sentences = [
                    sentence.strip()
                    for sentence in sentences
                    if len(sentence.split())
                    >= 3  # filters sentences under 3 words long
                    and not re.search(
                        r"\b[A-Z]{2,}\b", sentence
                    )  # filters all-caps words
                    and not re.search(r"\d", sentence)  # filters numbers
                    and not re.search(
                        r"[\[\]/*_@#$%^&=+]", sentence
                    )  # filters special symbols
                    and not re.search(
                        r"[A-Z]\.", sentence
                    )  # filters capital letter followed by period
                    and sum(bool(word.isupper()) for word in sentence.split())
                    <= 2  # filters more than 2 capital words
                    and sentence[0].isupper()
                ]
                final_text = " ".join(filtered_sentences)

                # Store the book in the database
                Book.objects.create(
                    book_id=book["id"],
                    sentence_count=len(filtered_sentences),
                    title=book["title"],
                    text=final_text,
                )

            except requests.exceptions.HTTPError:
                self.stderr.write(
                    self.style.ERROR(f'Failed to download book {book["id"]}')
                )

        self.stdout.write(self.style.SUCCESS("Successfully downloaded all books"))
