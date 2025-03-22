import os
import subprocess

# Define the path to the features folder and output folder for Allure results
features_path = "features"  # Adjust this if your features are in a subdirectory
allure_results_path = "reports/allure-results"  # Path to store Allure results

def run_behave():
    try:
        # Ensure the allure-results directory exists
        os.makedirs(allure_results_path, exist_ok=True)

        # Run the Behave command with the Allure formatter
        command = f"behave {features_path} --format allure_behave.formatter:AllureFormatter --outfile {allure_results_path}"
        result = subprocess.run(
            command,
            shell=True,  # Required for commands as a single string
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        # Print Behave output
        print(result.stdout)
        if result.stderr:
            print("Errors:", result.stderr)

    except Exception as e:
        print(f"An error occurred while running Behave: {e}")

def generate_allure_report():
    try:
        # Serve the Allure report directly in a browser
        print("Generating and serving the Allure report...")
        subprocess.run(
            f"allure serve {allure_results_path}",
            shell=True
        )
    except Exception as e:
        print(f"An error occurred while generating the Allure report: {e}")

if __name__ == "__main__":
    print("Running Behave test cases and generating Allure reports...")
    run_behave()
    generate_allure_report()


# Define the path to the features folder
# features_path = "features"  # Adjust this if your features are in a subdirectory

# def run_behave():
#     try:
#         # Run the Behave command
#         result = subprocess.run(
#             ["behave", features_path],  # Points to the features folder
#             stdout=subprocess.PIPE,
#             stderr=subprocess.PIPE,
#             text=True
#         )
#         # Print the output of Behave to the console
#         print(result.stdout)
#         if result.stderr:
#             print("Errors:", result.stderr)
#     except Exception as e:
#         print(f"An error occurred: {e}")
#
# if __name__ == "__main__":
#     print("Running Behave test cases...")
#     run_behave()




