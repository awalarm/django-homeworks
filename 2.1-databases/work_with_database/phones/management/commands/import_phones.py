import csv

from django.core.management.base import BaseCommand
from phones.models import Phone
from datetime import datetime


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r', encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=';')

            for row in reader:
                try:
                    lte_exists = row['lte_exists'].lower() == 'true'

                    release_date = datetime.strptime(row['release_date'], '%Y-%m-%d').date()

                    phone = Phone(
                        name=row['name'],
                        price=float(row['price']),
                        image=row['image'],
                        release_date=release_date,
                        lte_exists=lte_exists,
                        slug=row['name'].lower().replace(' ', '-')
                    )

                    phone.save()
                    self.stderr.write(self.style.SUCCESS(f"Успешно сохранен {phone.name}"))

                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Ошибка сохранения {row.get("name", "неизвестно")}: {e}"))

        self.stdout.write(self.style.SUCCESS("Импорт завершен"))
