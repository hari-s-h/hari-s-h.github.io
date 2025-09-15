import subprocess
from datetime import datetime

def run_command(command):
    """Run a shell command and print output/errors."""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout.strip())
    if result.stderr:
        print(result.stderr.strip())

def main():
    # Add all changes
    run_command("git add .")

    # Create commit message with date & time
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    commit_message = f"Auto commit on {now}"

    run_command(f'git commit -m "{commit_message}"')

    # Push changes
    run_command("git push")

if __name__ == "__main__":
    main()

