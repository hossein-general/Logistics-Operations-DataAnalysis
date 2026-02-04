#region Import Libraries
# main imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# other imports
import ipdb     # for debugging purposes
from pathlib import Path    # for finding the relative path to datasets
import os   # for checking the operating system (linux, windows, mac) and using the relevant command to clear the screen
#region Importing CSV files


# TODO implement a class that holds the tables data
# class DataStorage:
#     def __init__(self, name):
#         self.name = name
#         self.tables = dict()

#     def tables(self):
#         return self.tables.keys()

#     def add_table(self, new_table: pandas.core.frame.DataFrame):
#         if isinstance(new_table, pd.core.frame.DataFrame):
#             self.tables.append(new_table)
#         else:
#             print("invalid type. tables should be of type pandas.core.frame.DataFrame")

# logistics = DataStorage("logistics database")


# Class to split the operating hours into separated open_hour, close_hour and 24/7_flag columns
class OpenHoursConvert:
    def __init__(self, df: pd.core.frame.DataFrame): # df is given in order to create new columns directly without needing to pass it later
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



# Class to print each datasets content one by one (for making sure that everything is ok)
class PrintClass:
    def __init__(self, *df: pd.core.frame.DataFrame):
        self.df = df

    def print_df(self, samples: int = 40):   # samples shows the number of rows that will be shown for each itme
        for df in self.df:
            os.system('cls' if os.name == 'nt' else 'clear') # for Linux and Mac it returns 'posix'
            # in order to prevent errors being raised, we should first check the number of items within a dataframe
            if len(df) <= samples:
                print(df)
            else:
                print(df.sample(samples))

            print("\n", df.dtypes)
            input("next")

# applying some modifications to pandas displaying system
pd.options.display.max_rows=200

# preparing the relative path
script_dir=Path(__file__).parent    # path to the current directory

# Core Entities
customers = pd.read_csv((script_dir / r'logistics/Core Entities/customers.csv').resolve())
drivers = pd.read_csv((script_dir / r'logistics/Core Entities/drivers.csv').resolve())
facilities = pd.read_csv((script_dir / r'logistics/Core Entities/facilities.csv').resolve())
routes = pd.read_csv((script_dir / r'logistics/Core Entities/routes.csv').resolve())
trailers = pd.read_csv((script_dir / r'logistics/Core Entities/trailers.csv').resolve())
trucks = pd.read_csv((script_dir / r'logistics/Core Entities/trucks.csv').resolve())

# Operational Transactions
delivery_events = pd.read_csv((script_dir / r'logistics/Operational Transactions/delivery_events.csv').resolve())
fuel_purchases = pd.read_csv((script_dir / r'logistics/Operational Transactions/fuel_purchases.csv').resolve())
loads = pd.read_csv((script_dir / r'logistics/Operational Transactions/loads.csv').resolve())
maintenance_records = pd.read_csv((script_dir / r'logistics/Operational Transactions/maintenance_records.csv').resolve())
safety_incidents = pd.read_csv((script_dir / r'logistics/Operational Transactions/safety_incidents.csv').resolve())
trips = pd.read_csv((script_dir / r'logistics/Operational Transactions/trips.csv').resolve())

# Aggregated Analytics
driver_monthly_metrics = pd.read_csv((script_dir / r'logistics/Aggregated Analytics/driver_monthly_metrics.csv').resolve())
truck_utilization_metrics = pd.read_csv((script_dir / r'logistics/Aggregated Analytics/truck_utilization_metrics.csv').resolve())


#region Transforming Data
# **based on the database diagram
# NOTE most of these convertings are not necessary as they are already done during the csv importing process, but i rather do that manually too, in case something went wrong throughout the process
# TODO make a function that does all these works itself, and you only pass the datatype you want, with a list of columns to convert automatically
# TODO make some difference between integer and float numbers conversion by adding some formatting feature for each (like explicitly mention the float values to have two floating point numbers)


# dict creator
# gets: dataframe, column name
# returns: an indexed dictionary of each category within that column of that dataframe
# this lambda function aims to generate a dictionary, using the groupby funciton to get a generator of a column within the dataframe, containting tuples for each group. 
# first item in each tuple is one of groups names, so we turn them into a single list, check the len, then create a range object based on the length. the we map the list of 
# categories with the numbers within the newly generated range object. this resaults in a list of tuples 
# each tuple contains 2 values, the first one is the name and the second one is the index. then we pass the whole thing into dict() function to create a dictionary
# these dictionaries are used as maps for turning object type values into numeric types in our dataframes
categorizer = lambda df, column: dict(zip(x:=[i[0] for i in df.groupby(column)], range(len(x))))

# this one is a function version for the previous lambda function:
def categorized_func(df: pd.core.frame.DataFrame, column: str):
    gen = df.groupby(column)
    groups = []
    for i in gen:
        groups.append(i[0])

    category_dict = dict(zip(groups, len(groups)))
    return category_dict


# TODO make a process that gets a sample of about 30 rows of each column of a data frame, then if the number of groups found was samaller than a certain number, generate a map dictionary automatically for that specific column, and applies it by itself.
# the previous idea requires a more dynamic design of data frames. something like a container class object for each dataframe that could also hold map dictionaries within themselves
# also add a function to detect columns with only 2 categories, and convert them into boolean types

# TODO convert ids into integer, and separate them (i think it would turn out better than string)

# general maps
# TODO combine similar map dictionaries to make a single refrence dictionary
# states:
# this dictionary contains all states used within this dataset. it will be used to map satets as integers in tables
drivers_license_state = categorizer(drivers, "license_state")
facilities_state = categorizer(facilities, "state")
routes_origin_state = categorizer(routes, "origin_state")
routes_destination_state = categorizer(routes, "destination_state")
delivery_events_location_state = categorizer(delivery_events, "location_state")
fuel_purchases_location_state = categorizer(delivery_events, "location_state")
safety_incidents_location_state = categorizer(safety_incidents, "location_state")
states_map_dict = {
    **drivers_license_state, 
    **facilities_state, 
    **routes_origin_state, 
    **routes_destination_state, 
    **delivery_events_location_state, 
    **fuel_purchases_location_state, 
    **safety_incidents_location_state, 
}

# cities:
# this dictionary contains all cities used within this dataset. it will be used to map satets as integers in tables
# im not sure if there are any similarties between cites, and if some kind of misspell would have resaulted in indexing the same city for the second time. this may require REGEX
drivers_home_terminal = categorizer(drivers, "home_terminal")
facilities_city = categorizer(facilities, "city")
routes_origin_city = categorizer(routes, "origin_city")
routes_destination_city = categorizer(routes, "destination_city")
trailers_current_location = categorizer(trailers, "current_location")
trucks_home_terminal = categorizer(trucks, "home_terminal")
delivery_events_location_city = categorizer(delivery_events, "location_city")
fuel_purchases_location_city = categorizer(fuel_purchases, "location_city")
maintenance_records_facility_location = categorizer(maintenance_records, "facility_location")
safety_incidents_location_city = categorizer(safety_incidents, "location_city")
cities_map_dict = {
    **drivers_home_terminal,
    **facilities_city,
    **routes_origin_city,
    **routes_destination_city,
    **trailers_current_location,
    **trucks_home_terminal,
    **delivery_events_location_city,
    **fuel_purchases_location_city,
    **maintenance_records_facility_location,
    **safety_incidents_location_city,
}



# customers
customers.credit_terms_days = pd.to_numeric(customers["credit_terms_days"], errors="coerce")
customers.annual_revenue_potential = pd.to_numeric(customers["annual_revenue_potential"], errors="coerce")
customers.contract_start_date = pd.to_datetime(customers["contract_start_date"], errors="coerce")
#---
customers_customer_type = categorizer(customers, "customer_type")
customers_primary_freight_type = categorizer(customers, "primary_freight_type")
customers_account_status = categorizer(customers, "account_status")
#---
customers["customer_type"] = customers["customer_type"].map(customers_customer_type)
customers["primary_freight_type"] = customers["primary_freight_type"].map(customers_primary_freight_type)
customers["account_status"] = customers["account_status"].map(customers_account_status).astype(bool)


# drivers
drivers.hire_date = pd.to_datetime(drivers["hire_date"], errors="coerce")
drivers.termination_date = pd.to_datetime(drivers["termination_date"], errors="coerce")
drivers.date_of_birth = pd.to_datetime(drivers["date_of_birth"], errors="coerce")
drivers.years_experience = pd.to_numeric(drivers["years_experience"], errors="coerce")
#---
drivers_employment_status = categorizer(drivers, "employment_status")
drivers_cdl_class = categorizer(drivers, "cdl_class")
#---
drivers["employment_status"] = drivers["employment_status"].map(drivers_employment_status)
drivers["cdl_class"] = drivers["cdl_class"].map(drivers_cdl_class)
drivers["license_state"] = drivers["license_state"].map(states_map_dict)
drivers["home_terminal"] = drivers["home_terminal"].map(cities_map_dict)


# facilities
facilities.latitude = pd.to_numeric(facilities["latitude"], errors="coerce")
facilities.longitude = pd.to_numeric(facilities["longitude"], errors="coerce")
facilities.dock_doors = pd.to_numeric(facilities["dock_doors"], errors="coerce")
#---
facilities_facility_type = categorizer(facilities, "facility_type")
#---
facilities["facility_type"] = facilities["facility_type"].map(facilities_facility_type)
facilities["state"] = facilities["state"].map(states_map_dict)
facilities["city"] = facilities["city"].map(cities_map_dict)

#--- converting facilities.operating_hours from string to time columns, consisiting open_time, close_time, and a 24/7 flag
converter = OpenHoursConvert(facilities)
facilities.operating_hours.apply(converter.column_convert)
converter.generate_columns()
facilities.drop("operating_hours", axis=1, inplace=True)


# routes
routes.typical_distance_miles = pd.to_numeric(routes["typical_distance_miles"], errors="coerce")
routes.base_rate_per_mile = pd.to_numeric(routes["base_rate_per_mile"], errors="coerce")
routes.fuel_surcharge_rate = pd.to_numeric(routes["fuel_surcharge_rate"], errors="coerce")
routes.typical_transit_days = pd.to_numeric(routes["typical_transit_days"], errors="coerce")
#---
routes["origin_state"] = routes["origin_state"].map(states_map_dict)
routes["destination_state"] = routes["destination_state"].map(states_map_dict)
routes["origin_city"] = routes["origin_city"].map(cities_map_dict)
routes["destination_city"] = routes["destination_city"].map(cities_map_dict)


# trailers
trailers.trailer_number = pd.to_numeric(trailers["trailer_number"], errors="coerce")
trailers.length_feet = pd.to_numeric(trailers["length_feet"], errors="coerce")
trailers.model_year = pd.to_numeric(trailers["model_year"], errors="coerce")
trailers.acquisition_date = pd.to_datetime(trailers["acquisition_date"], errors="coerce")
#---
trailers_trailer_type = categorizer(trailers, "trailer_type")
trailers_status = categorizer(trailers, "status")
#---
trailers["status"] = trailers["status"].map(trailers_status)
trailers["trailer_type"] = trailers["trailer_type"].map(trailers_trailer_type)
trailers["current_location"] = trailers["current_location"].map(cities_map_dict)


# trucks
trucks.unit_number = pd.to_numeric(trucks["unit_number"], errors="coerce")
trucks.model_year = pd.to_numeric(trucks["model_year"], errors="coerce")
trucks.acquisition_mileage = pd.to_numeric(trucks["acquisition_mileage"], errors="coerce")
trucks.tank_capacity_gallons = pd.to_numeric(trucks["tank_capacity_gallons"], errors="coerce")
trucks.acquisition_date = pd.to_datetime(trucks["acquisition_date"], errors="coerce")
#---
trucks_make = categorizer(trucks, "make")
trucks_fuel_type = categorizer(trucks, "fuel_type")
trucks_status = categorizer(trucks, "status")
#---
trucks["make"] = trucks["make"].map(trucks_make)
trucks["fuel_type"] = trucks["fuel_type"].map(trucks_fuel_type)
trucks["status"] = trucks["status"].map(trucks_status)
trucks["home_terminal"] = trucks["home_terminal"].map(cities_map_dict)


# delivery_events
delivery_events.scheduled_datetime = pd.to_datetime(delivery_events["scheduled_datetime"], errors="coerce")
delivery_events.actual_datetime = pd.to_datetime(delivery_events["actual_datetime"], errors="coerce")
delivery_events.detention_minutes = pd.to_numeric(delivery_events["detention_minutes"], errors="coerce")
delivery_events.on_time_flag = delivery_events["on_time_flag"].astype(bool)
#---
delivery_events_event_type = categorizer(delivery_events, "event_type")
delivery_events_on_time_flag = categorizer(delivery_events, "on_time_flag")
#---
delivery_events["event_type"] = delivery_events["event_type"].map(delivery_events_event_type)
delivery_events["on_time_flag"] = delivery_events["on_time_flag"].map(delivery_events_on_time_flag)
delivery_events["location_state"] = delivery_events["location_state"].map(states_map_dict)
delivery_events["location_city"] = delivery_events["location_city"].map(cities_map_dict)

# fuel_purchases
fuel_purchases.purchase_date = pd.to_datetime(fuel_purchases["purchase_date"], errors="coerce")
fuel_purchases.gallons = pd.to_numeric(fuel_purchases["gallons"], errors="coerce")
fuel_purchases.price_per_gallon = pd.to_numeric(fuel_purchases["price_per_gallon"], errors="coerce")
fuel_purchases.total_cost = pd.to_numeric(fuel_purchases["total_cost"], errors="coerce")
#---
fuel_purchases["location_state"] = fuel_purchases["location_state"].map(states_map_dict)
fuel_purchases["location_city"] = fuel_purchases["location_city"].map(cities_map_dict)


# loads
loads.load_date = pd.to_datetime(loads["load_date"], errors="coerce")
loads.weight_lbs = pd.to_numeric(loads["weight_lbs"], errors="coerce")
loads.pieces = pd.to_numeric(loads["pieces"], errors="coerce")
loads.revenue = pd.to_numeric(loads["revenue"], errors="coerce")
loads.fuel_surcharge = pd.to_numeric(loads["fuel_surcharge"], errors="coerce")
loads.accessorial_charges = pd.to_numeric(loads["accessorial_charges"], errors="coerce")
#---
loads_load_type = categorizer(loads, "load_type")
loads_load_status = categorizer(loads, "load_status")
loads_booking_type = categorizer(loads, "booking_type")
#---
loads["load_type"] = loads["load_type"].map(loads_load_type)
loads["load_status"] = loads["load_status"].map(loads_load_status)
loads["booking_type"] = loads["booking_type"].map(loads_booking_type)


# maintenance_records
maintenance_records.maintenance_date = pd.to_datetime(maintenance_records["maintenance_date"], errors="coerce")
maintenance_records.odometer_reading = pd.to_numeric(maintenance_records["odometer_reading"], errors="coerce")
maintenance_records.labor_hours = pd.to_numeric(maintenance_records["labor_hours"], errors="coerce")
maintenance_records.labor_cost = pd.to_numeric(maintenance_records["labor_cost"], errors="coerce")
maintenance_records.parts_cost = pd.to_numeric(maintenance_records["parts_cost"], errors="coerce")
maintenance_records.total_cost = pd.to_numeric(maintenance_records["total_cost"], errors="coerce")
maintenance_records.downtime_hours = pd.to_numeric(maintenance_records["downtime_hours"], errors="coerce")
#---
maintenance_records_maintenance_type = categorizer(maintenance_records, "maintenance_type")
maintenance_records_service_description = categorizer(maintenance_records, "service_description")
#---
maintenance_records["maintenance_type"] = maintenance_records["maintenance_type"].map(maintenance_records_maintenance_type)
maintenance_records["service_description"] = maintenance_records["service_description"].map(maintenance_records_service_description)
maintenance_records["facility_location"] = maintenance_records["facility_location"].map(cities_map_dict)

# safety_incidents
safety_incidents.incident_date = pd.to_datetime(safety_incidents["incident_date"], errors="coerce")
safety_incidents.at_fault_flag = safety_incidents["at_fault_flag"].astype(bool)
safety_incidents.injury_flag = safety_incidents["injury_flag"].astype(bool)
safety_incidents.vehicle_damage_cost = pd.to_numeric(safety_incidents["vehicle_damage_cost"], errors="coerce")
safety_incidents.cargo_damage_cost = pd.to_numeric(safety_incidents["cargo_damage_cost"], errors="coerce")
safety_incidents.claim_amount = pd.to_numeric(safety_incidents["claim_amount"], errors="coerce")
safety_incidents.preventable_flag = safety_incidents["preventable_flag"].astype(bool)
#---
safety_incidents_incident_type = categorizer(safety_incidents, "incident_type")
safety_incidents_at_fault_flag = categorizer(safety_incidents, "at_fault_flag")
safety_incidents_injury_flag = categorizer(safety_incidents, "injury_flag")
safety_incidents_preventable_flag = categorizer(safety_incidents, "preventable_flag")
safety_incidents_description = categorizer(safety_incidents, "description")
#---
safety_incidents["incident_type"] = safety_incidents["incident_type"].map(safety_incidents_incident_type)
safety_incidents["at_fault_flag"] = safety_incidents["at_fault_flag"].map(safety_incidents_at_fault_flag)
safety_incidents["injury_flag"] = safety_incidents["injury_flag"].map(safety_incidents_injury_flag)
safety_incidents["preventable_flag"] = safety_incidents["preventable_flag"].map(safety_incidents_preventable_flag)
safety_incidents["description"] = safety_incidents["description"].map(safety_incidents_description)
safety_incidents["location_state"] = safety_incidents["location_state"].map(states_map_dict)
safety_incidents["location_city"] = safety_incidents["location_city"].map(cities_map_dict)

# trips
trips.dispatch_date = pd.to_datetime(trips["dispatch_date"], errors="coerce")
trips.actual_distance_miles = pd.to_numeric(trips["actual_distance_miles"], errors="coerce")
trips.actual_duration_hours = pd.to_numeric(trips["actual_duration_hours"], errors="coerce")
trips.fuel_gallons_used = pd.to_numeric(trips["fuel_gallons_used"], errors="coerce")
trips.average_mpg = pd.to_numeric(trips["average_mpg"], errors="coerce")
trips.idle_time_hours = pd.to_numeric(trips["idle_time_hours"], errors="coerce")
#---
trips_trip_status = categorizer(trips, "trip_status")
#---
trips["trip_status"] = trips["trip_status"].map(trips_trip_status)


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

#region isnull count
# finding the number of nulls in each category and removing them
customers.isnull().sum()                    # nothing
drivers.isnull().sum()                      # termination_date: 124
facilities.isnull().sum()                   # open_time: 16, close_time: 16
routes.isnull().sum()                       # nothing
trailers.isnull().sum()                     # nothing
trucks.isnull().sum()                       # nothing
delivery_events.isnull().sum()              # nothing
fuel_purchases.isnull().sum()               # truck_id: 3880, driver_id: 3988
loads.isnull().sum()                        # nothing
maintenance_records.isnull().sum()          # nothing
safety_incidents.isnull().sum()             # nothing
trips.isnull().sum()                        # driver_id: 1714, truck_id: 1672, trailer_id: 1680
driver_monthly_metrics.isnull().sum()       # nothing
truck_utilization_metrics.isnull().sum()    # nothing

#endregion

printer = PrintClass(customers,
    drivers,
    facilities,
    routes,
    trailers,
    trucks,
    delivery_events,
    fuel_purchases,
    loads,
    maintenance_records,
    safety_incidents,
    trips,
    driver_monthly_metrics,
    truck_utilization_metrics
)




ipdb.set_trace()