import csv
import json
import random

types = ["Passenger", "Transport", "Fighter", "Experimental"]
models = {
    "Passenger": ["Boeing 737", "Airbus A320", "Boeing 747", "Airbus A380", "Boeing 787", "Embraer E190"],
    "Transport": ["Lockheed C-130", "Boeing C-17", "Antonov An-124", "Airbus A400M"],
    "Fighter": ["F-22 Raptor", "Eurofighter Typhoon", "Lockheed Martin F-35", "Sukhoi Su-35"],
    "Experimental": ["NASA X-59", "Boeing X-37", "Scaled Composites White Knight Two"]
}
def generate_record_csv(record_id):
    typ = random.choice(types)
    model = random.choice(models[typ])
    passenger_capacity = random.randint(100, 500) if typ == "Passenger" else None
    max_takeoff_weight = round(random.uniform(50000, 200000), 2)
    max_payload = round(random.uniform(10000, 50000), 2) if typ == "Transport" else None
    max_speed = random.randint(800, 2500)
    range_ = random.randint(3000, 20000)
    application = "Short and medium-haul" if typ == "Passenger" else "Military" if typ == "Fighter" else "Long-haul" if typ == "Transport" else "Experimental"
    manufacturer = "Boeing" if typ == "Passenger" or typ == "Transport" else "Lockheed Martin" if typ == "Fighter" else "NASA"
    production_year = random.randint(1960, 2022)
    engine_type = random.choice(["Turbojet", "Turboprop", "Turbofan"])
    max_fuel_capacity = round(random.uniform(20000, 100000),
                              2)
    max_range_without_refueling = random.randint(2000, 15000) if typ == "Transport" else None

    return [record_id, typ, model, passenger_capacity, max_takeoff_weight, max_payload, max_speed, range_, application,
            manufacturer, production_year, engine_type, max_fuel_capacity, max_range_without_refueling]

data = [generate_record_csv(record_id) for record_id in range(1, 1001)]

with open('planes_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(
        ["ID", "Type", "Model", "Passenger Capacity", "Max Takeoff Weight", "Max Payload", "Max Speed", "Range",
         "Application", "Manufacturer", "Production Year", "Engine Type", "Max Fuel Capacity",
         "Max Range Without Refueling"])
    writer.writerows(data)

print("CSV generated successfully.")

def generate_record_json(record_id):
    typ = random.choice(types)
    model = random.choice(models[typ])
    passenger_capacity = random.randint(100, 500) if typ == "Passenger" else None
    max_takeoff_weight = round(random.uniform(50000, 200000), 2)
    max_payload = round(random.uniform(10000, 50000), 2) if typ == "Transport" else None
    max_speed = random.randint(800, 2500)
    range_ = random.randint(3000, 20000)
    application = "Short and medium-haul" if typ == "Passenger" else "Military" if typ == "Fighter" else "Long-haul" if typ == "Transport" else "Experimental"
    manufacturer = "Boeing" if typ == "Passenger" or typ == "Transport" else "Lockheed Martin" if typ == "Fighter" else "NASA"
    production_year = random.randint(1960, 2022)
    engine_type = random.choice(["Turbojet", "Turboprop", "Turbofan"])
    max_fuel_capacity = round(random.uniform(20000, 100000),
                              2)
    max_range_without_refueling = random.randint(2000, 15000) if typ == "Transport" else None

    return {
        "ID": record_id,
        "Type": typ,
        "Model": model,
        "Passenger Capacity": passenger_capacity,
        "Max Takeoff Weight": max_takeoff_weight,
        "Max Payload": max_payload,
        "Max Speed": max_speed,
        "Range": range_,
        "Application": application,
        "Manufacturer": manufacturer,
        "Production Year": production_year,
        "Engine Type": engine_type,
        "Max Fuel Capacity": max_fuel_capacity,
        "Max Range Without Refueling": max_range_without_refueling
    }

data = [generate_record_json(record_id) for record_id in range(1, 1001)]
with open('planes_data.json', 'w', encoding='utf-8') as jsonfile:
    json.dump(data, jsonfile, ensure_ascii=False, indent=4)
print("JSON generated successfully.")
