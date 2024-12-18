import asyncio
import sys

async def loading_bar(total, description="Progress", duration=0.1):
    """
    Displays an ASCII-style loading bar with animation.

    :param total: Total number of steps.
    :param description: Text displayed before the bar.
    :param duration: Time in seconds between updates.
    """
    animation = ['|', '/', '*', '\\']
    bar_length = 50

    for i in range(total + 1):
        percentage = int((i / total) * 100)
        num_hashes = percentage // 2
        animator = animation[i % len(animation)]  # Changes based on the current step
        if percentage == 100:
            animator = "#"
        bar = "#" * num_hashes + animator + "-" * (bar_length - num_hashes)
        sys.stdout.write(f"\r{description}: [{bar}] {percentage}%")
        sys.stdout.flush()
        await asyncio.sleep(duration)
    sys.stdout.write("\n")

# Example usage
async def main():
    await loading_bar(100, "Progress", 0.05)

# Run the example
if __name__ == "__main__":
    asyncio.run(main())
