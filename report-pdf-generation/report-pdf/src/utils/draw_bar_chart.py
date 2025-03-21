import matplotlib.pyplot as plt


def draw_bar_chart(severities, counts, output_path):
    """
    Creates a bar chart showing the severity levels and their corresponding counts.

    Arguments:
    severities -- List of severity levels (e.g., ['critical', 'high', 'medium', 'low'])
    counts -- List of counts corresponding to each severity level
    output_path -- Path where the image file will be saved (e.g., "severity_chart.png")
    """
    # Plotting the bar chart
    fig, ax = plt.subplots()

    # Bar chart
    ax.bar(severities, counts, color=['red', 'orange', 'yellow', 'green'])

    # Add labels and title
    ax.set_xlabel('Severity Level')
    ax.set_ylabel('Number of Vulnerabilities')
    ax.set_title('Vulnerability Severity Distribution')

    # Save the chart as an image file (PNG)
    plt.savefig(output_path, format='png')
    plt.close(fig)  # Close the figure to free up memory

    # print(f"Bar chart saved as {output_path}")

if __name__ == "__main__":
    # Example data for the bar chart
    severities = ['critical', 'high', 'medium', 'low']
    counts = [21, 15, 17, 16]

    # Path where the image will be saved
    output_path = "severity_chart.png"

    # Calling the function to create and save the chart
    draw_bar_chart(severities, counts, output_path)
