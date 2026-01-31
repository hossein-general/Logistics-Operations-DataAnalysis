#region Import Packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import ipdb
from pathlib import Path

#region Importing CSV files
# preparing the relative path


# TODO implement a class that holds the tables data
# class DataStorage:
#     def __init__(self, name):
#         self.name = name
#         self.tables = []

#     def tables(self):
#         return self.tables
    
#     def add_table(self, new_table: pandas.core.frame.DataFrame):
#         if isinstance(new_table, pd.core.frame.DataFrame):
#             self.tables.append(new_table)
#         else:
#             print("invalid type. tables should be of type pandas.core.frame.DataFrame")

# logistics = DataStorage("logistics database")


# Class to split the operating hours into separated open_hour, close_hour and 24/7_flag columns
class OpenHoursConvert:
    def __init__(self, df: pd.core.frame.DataFrame):
        self.df = df

        # for each row, there is a record in each of these lists, and they are in order
        self.open_time = []
        self.close_time = []
        self.flag_24_7 = []

    # convert time from AM/PM style to 24-hour style and return the resaulted value
    def convert_to_24_hour(self, time: str):
        if "AM" in time:
            time = "{}:00".format(time.strip("AM"))
        elif "PM" in time:
            time = "{}:00".format(int(time.strip("PM")) + 12)
        return time

    def column_convert(self, item: str):
        item = item.strip()
        if item == "24/7":
            # ipdb.set_trace()
            self.open_time.append(pd.NaT)
            self.close_time.append(pd.NaT)
            self.flag_24_7.append(True)

        else:
            open_time, close_time = item.split("-", 1)  # separating open/close times

            # converting to 24 hour style
            open_time = self.convert_to_24_hour(open_time)  
            close_time = self.convert_to_24_hour(close_time)    

            self.open_time.append(open_time)
            self.close_time.append(close_time)
            self.flag_24_7.append(False)

    def generate_columns(self):
        self.df["open_time"] = self.open_time
        self.df['open_time'] = pd.to_datetime(self.df['open_time'])
        self.df['open_time'] = [(time.time() if time is not pd.NaT else time) for time in self.df['open_time']]

        self.df["close_time"] = self.close_time
        self.df['close_time'] = pd.to_datetime(self.df['close_time'])
        self.df['close_time'] = [(time.time() if time is not pd.NaT else time) for time in self.df['close_time']]

        self.df["is_24_7_flag"] = self.flag_24_7




script_dir=Path(__file__).parent    # path to the current directory

customers = pd.read_csv((script_dir / r'logistics/Core Entities/customers.csv').resolve())
drivers = pd.read_csv((script_dir / r'logistics/Core Entities/drivers.csv').resolve())
facilities = pd.read_csv((script_dir / r'logistics/Core Entities/facilities.csv').resolve())
routes = pd.read_csv((script_dir / r'logistics/Core Entities/routes.csv').resolve())
trailers = pd.read_csv((script_dir / r'logistics/Core Entities/trailers.csv').resolve())
trucks = pd.read_csv((script_dir / r'logistics/Core Entities/trucks.csv').resolve())

delivery_events = pd.read_csv((script_dir / r'logistics/Operational Transactions/delivery_events.csv').resolve())
fuel_purchases = pd.read_csv((script_dir / r'logistics/Operational Transactions/fuel_purchases.csv').resolve())
loads = pd.read_csv((script_dir / r'logistics/Operational Transactions/loads.csv').resolve())
maintenance_records = pd.read_csv((script_dir / r'logistics/Operational Transactions/maintenance_records.csv').resolve())
safety_incidents = pd.read_csv((script_dir / r'logistics/Operational Transactions/safety_incidents.csv').resolve())
trips = pd.read_csv((script_dir / r'logistics/Operational Transactions/trips.csv').resolve())

driver_monthly_metrics = pd.read_csv((script_dir / r'logistics/Aggregated Analytics/driver_monthly_metrics.csv').resolve())
truck_utilization_metrics = pd.read_csv((script_dir / r'logistics/Aggregated Analytics/truck_utilization_metrics.csv').resolve())


#region Transforming Data
# **based on the database diagram
# NOTE most of these convertings are not necessary as they are already done during the csv importing process, but i rather do that manually too, in case something went wrong throughout the process
# TODO make a function that does all these works itself, and you only pass the datatype you want, with a list of columns to convert automatically
# TODO make some difference between integer and float numbers conversion by adding some formatting feature for each (like explicitly mention the float values to have two floating point numbers)

# customers
customers.credit_terms_days = pd.to_numeric(customers["credit_terms_days"], errors="coerce")
customers.annual_revenue_potential = pd.to_numeric(customers["annual_revenue_potential"], errors="coerce")
customers.contract_start_date = pd.to_datetime(customers["contract_start_date"], errors="coerce")

# drivers
drivers.hire_date = pd.to_datetime(drivers["hire_date"], errors="coerce")
drivers.termination_date = pd.to_datetime(drivers["termination_date"], errors="coerce")
drivers.date_of_birth = pd.to_datetime(drivers["date_of_birth"], errors="coerce")
drivers.years_experience = pd.to_numeric(drivers["years_experience"], errors="coerce")

# facilities
facilities.latitude = pd.to_numeric(facilities["latitude"], errors="coerce")
facilities.longitude = pd.to_numeric(facilities["longitude"], errors="coerce")
facilities.dock_doors = pd.to_numeric(facilities["dock_doors"], errors="coerce")

# converting facilities.operating_hours from string to time columns, consisiting open_time, close_time, and a 24/7 flag
converter = OpenHoursConvert(facilities)
facilities.operating_hours.apply(converter.column_convert)
converter.generate_columns()


# routes
routes.typical_distance_miles = pd.to_numeric(routes["typical_distance_miles"], errors="coerce")
routes.base_rate_per_mile = pd.to_numeric(routes["base_rate_per_mile"], errors="coerce")
routes.fuel_surcharge_rate = pd.to_numeric(routes["fuel_surcharge_rate"], errors="coerce")
routes.typical_transit_days = pd.to_numeric(routes["typical_transit_days"], errors="coerce")

# trailers
trailers.trailer_number = pd.to_numeric(trailers["trailer_number"], errors="coerce")
trailers.length_feet = pd.to_numeric(trailers["length_feet"], errors="coerce")
trailers.model_year = pd.to_numeric(trailers["model_year"], errors="coerce")
trailers.acquisition_date = pd.to_datetime(trailers["acquisition_date"], errors="coerce")

# trucks
trucks.unit_number = pd.to_numeric(trucks["unit_number"], errors="coerce")
trucks.model_year = pd.to_numeric(trucks["model_year"], errors="coerce")
trucks.acquisition_mileage = pd.to_numeric(trucks["acquisition_mileage"], errors="coerce")
trucks.tank_capacity_gallons = pd.to_numeric(trucks["tank_capacity_gallons"], errors="coerce")
trucks.acquisition_date = pd.to_datetime(trucks["acquisition_date"], errors="coerce")

# delivery_events
delivery_events.scheduled_datetime = pd.to_datetime(delivery_events["scheduled_datetime"], errors="coerce")
delivery_events.actual_datetime = pd.to_datetime(delivery_events["actual_datetime"], errors="coerce")
delivery_events.detention_minutes = pd.to_numeric(delivery_events["detention_minutes"], errors="coerce")
delivery_events.on_time_flag = delivery_events["on_time_flag"].astype(bool)

# fuel_purchases
fuel_purchases.purchase_date = pd.to_datetime(fuel_purchases["purchase_date"], errors="coerce")
fuel_purchases.gallons = pd.to_numeric(fuel_purchases["gallons"], errors="coerce")
fuel_purchases.price_per_gallon = pd.to_numeric(fuel_purchases["price_per_gallon"], errors="coerce")
fuel_purchases.total_cost = pd.to_numeric(fuel_purchases["total_cost"], errors="coerce")

# loads
loads.load_date = pd.to_datetime(loads["load_date"], errors="coerce")
loads.weight_lbs = pd.to_numeric(loads["weight_lbs"], errors="coerce")
loads.pieces = pd.to_numeric(loads["pieces"], errors="coerce")
loads.revenue = pd.to_numeric(loads["revenue"], errors="coerce")
loads.fuel_surcharge = pd.to_numeric(loads["fuel_surcharge"], errors="coerce")
loads.accessorial_charges = pd.to_numeric(loads["accessorial_charges"], errors="coerce")

# maintenance_records
maintenance_records.maintenance_date = pd.to_datetime(maintenance_records["maintenance_date"], errors="coerce")
maintenance_records.odometer_reading = pd.to_numeric(maintenance_records["odometer_reading"], errors="coerce")
maintenance_records.labor_hours = pd.to_numeric(maintenance_records["labor_hours"], errors="coerce")
maintenance_records.labor_cost = pd.to_numeric(maintenance_records["labor_cost"], errors="coerce")
maintenance_records.parts_cost = pd.to_numeric(maintenance_records["parts_cost"], errors="coerce")
maintenance_records.total_cost = pd.to_numeric(maintenance_records["total_cost"], errors="coerce")
maintenance_records.downtime_hours = pd.to_numeric(maintenance_records["downtime_hours"], errors="coerce")

# safety_incidents
safety_incidents.incident_date = pd.to_datetime(safety_incidents["incident_date"], errors="coerce")
safety_incidents.at_fault_flag = safety_incidents["at_fault_flag"].astype(bool)
safety_incidents.injury_flag = safety_incidents["injury_flag"].astype(bool)
safety_incidents.vehicle_damage_cost = pd.to_numeric(safety_incidents["vehicle_damage_cost"], errors="coerce")
safety_incidents.cargo_damage_cost = pd.to_numeric(safety_incidents["cargo_damage_cost"], errors="coerce")
safety_incidents.claim_amount = pd.to_numeric(safety_incidents["claim_amount"], errors="coerce")
safety_incidents.preventable_flag = safety_incidents["preventable_flag"].astype(bool)

# trips
trips.dispatch_date = pd.to_datetime(trips["dispatch_date"], errors="coerce")
trips.actual_distance_miles = pd.to_numeric(trips["actual_distance_miles"], errors="coerce")
trips.actual_duration_hours = pd.to_numeric(trips["actual_duration_hours"], errors="coerce")
trips.fuel_gallons_used = pd.to_numeric(trips["fuel_gallons_used"], errors="coerce")
trips.average_mpg = pd.to_numeric(trips["average_mpg"], errors="coerce")
trips.idle_time_hours = pd.to_numeric(trips["idle_time_hours"], errors="coerce")


# driver_monthly_metrics
driver_monthly_metrics.month = pd.to_datetime(driver_monthly_metrics["month"], errors="coerce")
driver_monthly_metrics.trips_completed = pd.to_numeric(driver_monthly_metrics["trips_completed"], errors="coerce")
driver_monthly_metrics.total_miles = pd.to_numeric(driver_monthly_metrics["total_miles"], errors="coerce")
driver_monthly_metrics.total_revenue = pd.to_numeric(driver_monthly_metrics["total_revenue"], errors="coerce")
driver_monthly_metrics.average_mpg = pd.to_numeric(driver_monthly_metrics["average_mpg"], errors="coerce")
driver_monthly_metrics.total_fuel_gallons = pd.to_numeric(driver_monthly_metrics["total_fuel_gallons"], errors="coerce")
driver_monthly_metrics.on_time_delivery_rate = pd.to_numeric(driver_monthly_metrics["on_time_delivery_rate"], errors="coerce")
driver_monthly_metrics.average_idle_hours = pd.to_numeric(driver_monthly_metrics["average_idle_hours"], errors="coerce")

# truck_utilization_metrics
truck_utilization_metrics.month = pd.to_datetime(truck_utilization_metrics["month"], errors="coerce")
truck_utilization_metrics.trips_completed = pd.to_numeric(truck_utilization_metrics["trips_completed"], errors="coerce")
truck_utilization_metrics.total_miles = pd.to_numeric(truck_utilization_metrics["total_miles"], errors="coerce")
truck_utilization_metrics.total_revenue = pd.to_numeric(truck_utilization_metrics["total_revenue"], errors="coerce")
truck_utilization_metrics.average_mpg = pd.to_numeric(truck_utilization_metrics["average_mpg"], errors="coerce")
truck_utilization_metrics.maintenance_events = pd.to_numeric(truck_utilization_metrics["maintenance_events"], errors="coerce")
truck_utilization_metrics.maintenance_cost = pd.to_numeric(truck_utilization_metrics["maintenance_cost"], errors="coerce")
truck_utilization_metrics.downtime_hours = pd.to_numeric(truck_utilization_metrics["downtime_hours"], errors="coerce")
truck_utilization_metrics.utilization_rate = pd.to_numeric(truck_utilization_metrics["utilization_rate"], errors="coerce")


ipdb.set_trace()