import requests
from django.core.management.base import BaseCommand
from news.models import News
from datetime import datetime

class Command(BaseCommand):
    help = 'Fetch news from external site and store it in the database'

    def handle(self, *args, **kwargs):
        # Fetch news from the external website
        res = requests.get("https://www.onmanorama.com/content/mm/en/kerala.html").text.split('<li class="storylist-item storylist-large">')

        # Process and save each news item
        for i in range(1, len(res)):
            try:
                # Extract the news data
                img = res[i].split('data-src="')[1].split('"')[0]
                mc = res[i].split('<h2 class="listing-title-002">')[1].split('target="_self">')
                title = mc[1].split('</a')[0]
                summary = mc[2].split('</a')[0]

                # Save to the database
                news, created = News.objects.get_or_create(
                    title=title,
                    defaults={
                        'image_url': img,
                        'summary': summary,
                        'content': summary,  # Assuming summary as content for now
                        'published_at': datetime.now(),  # You can fetch the exact time from the page if needed
                        'source_url': 'https://www.onmanorama.com/content/mm/en/kerala.html',
                    }
                )

                if created:
                    self.stdout.write(self.style.SUCCESS(f"Successfully added news: {title}"))
                else:
                    self.stdout.write(self.style.WARNING(f"News already exists: {title}"))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Failed to process news: {e}"))

