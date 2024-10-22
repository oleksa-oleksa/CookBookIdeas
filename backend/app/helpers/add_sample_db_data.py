import sys
import os
# Add the parent directory of 'app' to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from app.models import Receipt
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
                ingredients=["Lachsfilet", "Tomaten", "Avocado", "Koriander", "Limettensaft", "Olivenöl", "Salz", "Pfeffer"],
                
                preparation_steps = (
                "1. Lachsfilets unter kaltem Wasser abspülen, trockentupfen, salzen, pfeffern.\n"
                "Auf einem Gitter (mit einer Fettpfanne darunter) im vorgeheizten Backofen bei 180 °C\n"
                "(Umluft 160 °C; Gas: Stufe 2–3) 6–8 Minuten garen.\n\n"
                "2. Inzwischen für die Salsa Tomaten waschen und grob würfeln.\n"
                "Avocado schälen, halbieren, entkernen und würfeln. Koriander waschen, trockenschütteln,\n"
                "die Blätter hacken. Avocado mit Tomaten, Limettensaft, Koriander und Öl mischen und mit Salz und Pfeffer abschmecken.\n\n"
                "3. Lachsfilets zum Servieren mit der Salsa auf Teller geben."
                ),
                tags=["Fisch", "Salsa", "Low Carb", "Lachs"],
                date_added=date(2024, 10, 11),
                rating=5
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
