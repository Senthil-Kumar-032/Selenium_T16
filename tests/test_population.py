import time
from pages.population_page import PopulationPage


def test_live_population(setup):
    driver = setup
    page = PopulationPage(driver)

    # ✅ Close cookie popup
    page.accept_cookies()

    try:
        while True:
            population = page.get_population()
            print(f"Population: {population}")
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nStopped by user")