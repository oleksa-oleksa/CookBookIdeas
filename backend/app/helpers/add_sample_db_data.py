import sys
import os
# Add the parent directory of 'app' to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from app.models import Receipt
from app.schemas import  UnitEnum 
from app.database import SessionLocal
from datetime import date

# Sample data to add
def add_sample_receipts():
    db = SessionLocal()

    try:
        sample_receipts = [
            Receipt(
                title="Lachsfilet mit Salsa",
                photo_url="https://images.eatsmarter.de/sites/default/files/styles/576x432-webp/public/lachs-mit-avocado-tomaten-salsa-102975.jpg",
                ingredients=[
                    {"name": "Lachsfilet", "amount": 250, "unit": UnitEnum.gram},
                    {"name": "Tomaten", "amount": 100, "unit": UnitEnum.gram},
                    {"name": "Avocado", "amount": 1, "unit": UnitEnum.piece},
                     {"name": "Koriander", "amount": None, "unit": UnitEnum.none},
                    {"name": "Limettensaft", "amount": 2, "unit": UnitEnum.tablespoon},
                    {"name": "Olivenöl", "amount": 1, "unit": UnitEnum.tablespoon},
                    {"name": "Salz", "amount": None, "unit": UnitEnum.none},
                    {"name": "Pfeffer", "amount": None, "unit": UnitEnum.none}
                    
                ],
                preparation_steps=[
                    "Lachsfilets unter kaltem Wasser abspülen, trockentupfen, salzen, pfeffern.",
                    "Auf einem Gitter im vorgeheizten Backofen bei 180 °C (Umluft 160 °C; Gas: Stufe 2–3) 6–8 Minuten garen.",
                    "Inzwischen für die Salsa Tomaten waschen und grob würfeln, Avocado schälen, halbieren, entkernen und würfeln.",
                    "Koriander waschen, trockenschütteln, Blätter hacken und mit Tomaten, Limettensaft, Koriander und Öl mischen.",
                    "Lachsfilets zum Servieren mit der Salsa auf Teller geben."
                ],
                tags=["Fisch", "Salsa", "Low Carb", "Lachs"],
                date_added=date(2024, 10, 23),
                rating=5,
                default_servings=2
            ),
            Receipt(
                title="Vietnamesische Nudelsuppe (Pho)",
                photo_url="https://www.madamecuisine.de/wp-content/uploads/2022/05/vietnamesische-pho01.jpg",
                ingredients=[
                    {"name": "kräftige Rinderbrühe", "amount": 4, "unit": UnitEnum.liter},
                    {"name": "Rindfleisch", "amount": 100, "unit": UnitEnum.gram},
                    {"name": "Knoblauch", "amount": 6, "unit": UnitEnum.piece},
                    {"name": "Reisnudeln", "amount": 600, "unit": UnitEnum.gram},
                    {"name": "Koriander", "amount": 1, "unit": UnitEnum.bunch},
                    {"name": "Thai Basilikum", "amount": 1, "unit": UnitEnum.bunch},
                    {"name": "Frühlingszwiebeln", "amount": 1, "unit": UnitEnum.bunch},
                    {"name": "Limetten", "amount": 2, "unit": UnitEnum.piece},
                    {"name": "Pho Suppe Pasta", "amount": 3, "unit": UnitEnum.tablespoon}
                   
                ],
                preparation_steps=[
                    "Knoblauch und Ingwer schälen und in dünne Scheiben schneiden. Zusammen mit den anderen Zutaten der Suppe für mindestens 1 Stunde kochen. Nach etwa 10 Minuten stellt sich die angenehme Raumnote ein, und Eure Wohnung duftet nach Vietnamesischer Garküche.",
                    "Kräuter waschen und von größeren Stielen befreien. Limetten achteln. Chilis in kleine Ringe schneiden. Fleisch senkrecht zur Faser in 2-4mm dünne Scheiden schneiden.",
                    "Beilagen und Soßen in jeweils getrennten Schälchen servieren.",
                    "Reisnudeln kurz nach Packungsanweisung kochen und in einem Sieb auffangen.",
                    "Fleisch und Nudeln pro Person in einer großen Schale anrichten. Mit kochender Brühe übergießen (das Fleisch gart dabei, bleibt aber innen rosa). Mit Kräutern, Sprossen und Soßen nach Geschmack würzen."
                ],
                tags=["Rindfleisch", "Suppe", "Asiatisch", "Reisnudeln", "Nudelsuppe", "Vietnamesisch"],
                date_added=date(2024, 10, 23),
                rating=5,
                default_servings=2
            )
        ]

        db.add_all(sample_receipts)
        db.commit()

    except Exception as e:
        print(f"Error occurred: {e}")
        db.rollback()

    finally:
        db.close()

if __name__ == "__main__":
    add_sample_receipts()
