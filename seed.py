"""
SHIELD HER — Demo Seed Script
Populates demo user, trusted contacts, an active journey with check-ins,
and documented cyberbullying incidents for hackathon presentation.
Usage: python seed.py
"""
import os
from datetime import timedelta
from app import create_app
from app.extensions import db
from app.models import User, Contact, Journey, JourneyCheckin, Incident, utc_now

app = create_app('development')

def seed_demo_data():
    with app.app_context():
        db.create_all()

        demo_email = "demo@shieldher.local"
        existing = User.query.filter_by(email=demo_email).first()
        if existing:
            print(f"[*] Demo user '{demo_email}' already exists. Deleting previous demo records to refresh...")
            db.session.delete(existing)
            db.session.commit()

        print("[+] Creating demo account...")
        user = User(
            full_name="Ananya Sharma",
            email=demo_email,
            phone="+91 98765 43210",
            emergency_notes="Blood Group: O+, Asthma (Inhaler in handbag), Primary Contact: Mother"
        )
        user.set_password("ShieldHer2026!")
        db.session.add(user)
        db.session.commit()

        print("[+] Adding trusted contacts...")
        c1 = Contact(
            user_id=user.id,
            name="Sunita Sharma",
            phone="+91 98111 22233",
            relationship="Mother",
            email="sunita@example.com",
            is_primary=True
        )
        c2 = Contact(
            user_id=user.id,
            name="Dr. Riya Sen",
            phone="+91 98222 33344",
            relationship="Campus Counselor / Mentor",
            email="riya.sen@college.edu",
            is_primary=False
        )
        c3 = Contact(
            user_id=user.id,
            name="Pooja Verma",
            phone="+91 98333 44455",
            relationship="Roommate",
            email="pooja.v@college.edu",
            is_primary=False
        )
        db.session.add_all([c1, c2, c3])
        db.session.commit()

        print("[+] Creating active safe journey with check-ins...")
        now = utc_now().replace(microsecond=0)
        journey = Journey(
            user_id=user.id,
            destination="Campus Hostel Block 4",
            origin="Metro Station Gate 2",
            departure_time=now - timedelta(minutes=25),
            expected_arrival_time=now + timedelta(minutes=20),
            contact_id=c1.id,
            notes="Taking e-rickshaw shared with classmate Sneha. Driver ID: DL-1ER-4921",
            status="ACTIVE"
        )
        db.session.add(journey)
        db.session.commit()

        chk1 = JourneyCheckin(
            journey_id=journey.id,
            message="Boarded green e-rickshaw at Metro Gate 2. Moving towards outer ring.",
            location_label="Metro Gate 2",
            status_indicator="SAFE",
            created_at=now - timedelta(minutes=24)
        )
        chk2 = JourneyCheckin(
            journey_id=journey.id,
            message="Heavy traffic near Sector 62 intersection, moving slowly.",
            location_label="Sector 62 Intersection",
            status_indicator="DELAYED",
            created_at=now - timedelta(minutes=10)
        )
        db.session.add_all([chk1, chk2])
        db.session.commit()

        print("[+] Creating documented CyberShield incident...")
        inc1 = Incident(
            user_id=user.id,
            title="Unwanted predatory DMs and spoofed account on Instagram",
            category="Online Harassment",
            incident_datetime=now - timedelta(days=2),
            platform_or_location="Instagram / College Confessions Page",
            perpetrator_info="Handle: @ananya_fan_stalker_99 (now disabled)",
            status="Documented",
            description=(
                "Perpetrator created a clone profile using my photo and sent vulgar DMs to my friends. "
                "Reported to Instagram Trust & Safety team. Preservation of chats completed."
            )
        )
        db.session.add(inc1)
        db.session.commit()

        print("\n" + "=" * 60)
        print("  DEMO DATA POPULATED SUCCESSFULLY!")
        print("=" * 60)
        print("  Login Email:    demo@shieldher.local")
        print("  Login Password: ShieldHer2026!")
        print("  URL:            http://127.0.0.1:5000/login")
        print("=" * 60 + "\n")

if __name__ == '__main__':
    seed_demo_data()
