import time
from pages.population_page import PopulationPage


def test_live_population(setup):
    driver = setup
    page = PopulationPage(driver)

    page.accept_cookies()              # Close cookie popup

    try:
        while True:                    # Run continuously
            population = page.get_population()   # Fetch population
            print(f"Population: {population}")   # Print value
            time.sleep(1)              # Wait 1 second

    except KeyboardInterrupt:
        print("\nStopped by user")     # Stop manually