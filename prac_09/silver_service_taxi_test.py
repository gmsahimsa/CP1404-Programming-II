from silver_service_taxi import SilverServiceTaxi

def test_silver_service_taxi():
    sst = SilverServiceTaxi('Hummer', 200, 1.23, 2)
    sst.drive(18)
    print(f'The total fare for the trip is: ${sst.get_fare()}')


test_silver_service_taxi()
