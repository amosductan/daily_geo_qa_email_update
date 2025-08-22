import os
import sys
import subprocess
from dotenv import load_dotenv

def main():
    # Load environment variables from .env
    load_dotenv()

    # Read the SCRIPTS variable: a comma-separated list of script paths.
    scripts_env = os.getenv("SCRIPTS")
    if not scripts_env:
        print("No scripts specified in the .env file. Please define the SCRIPTS variable.")
        return

    # Create a list of script file paths
    scripts = [script.strip() for script in scripts_env.split(",") if script.strip()]
    if not scripts:
        print("No valid script paths found in the SCRIPTS variable.")
        return

    processes = []
    for script in scripts:
        if not os.path.exists(script):
            print(f"Script not found: {script}")
            continue

        # Determine the working directory as the script's own directory.
        script_directory = os.path.dirname(os.path.abspath(script))
        print(f"Launching {script} with working directory {script_directory}...")
        
        # Launch the script as a separate process, using the script's own folder as cwd.
        process = subprocess.Popen([sys.executable, script], cwd=script_directory)
        processes.append(process)

    # Optionally, wait for all processes to finish.
    for process in processes:
        process.wait()

if __name__ == "__main__":
    main()
