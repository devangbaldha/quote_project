import random
from .models import Quote


def update_quote():
    quotes = list(Quote.objects.all())

    if not quotes:
        print("No quotes available.")
        return

    quote = random.choice(quotes)

    Quote.objects.all().update(is_current=False)

    quote.is_current = True
    quote.save()

    print("Quote changed:", quote.quote)