import matplotlib.pyplot as plt
import numpy as np
from ipywidgets import interact, IntSlider, SelectMultiple

def plot_firm_profit(job_counts, coop_min_profit, coop_max_profit, direct_jobs, direct_job_profit):
    service_cost = 16000  # Firma maliyeti
    service_price_direct = 25000  # Price when sold directly by the firm
    service_price_coop = 17000  # Price when sold to the cooperative
    coop_members = 18  # Number of cooperative members

    # Range of cooperative profits per transaction
    coop_profits_per_transaction = range(coop_min_profit, coop_max_profit + 1000, 1000)

    # Calculate firm's profit for each cooperative profit increment and job count
    coop_scenarios_profits = {
        job_count: [
            (job_count * ((coop_profit) / coop_members) + (direct_job_profit * direct_jobs)) / 1000
            for coop_profit in coop_profits_per_transaction
        ]
        for job_count in job_counts
    }

    # Firm's profit for direct sales of specified number of jobs
    firm_profit_direct_only = direct_job_profit * direct_jobs / 1000

    # Plotting bar chart for each job count
    x_labels = [f'{profit} TL' for profit in coop_profits_per_transaction]
    x_positions = np.arange(len(coop_profits_per_transaction))  # Positions for bars

    plt.figure(figsize=(14, 8))

    # Bar widths and positions
    bar_width = 0.2
    offsets = [bar_width * i for i in range(len(job_counts))]

    # Plot for each job count
    colors = ['green', 'orange', 'red']
    for i, (job_count, profits) in enumerate(coop_scenarios_profits.items()):
        plt.bar(x_positions + offsets[i], profits, bar_width, label=f'{job_count} İş', color=colors[i % len(colors)])

    # Adding firm's direct sales profit as a horizontal line
    plt.axhline(y=firm_profit_direct_only, color='blue', linestyle='--', label=f'{direct_jobs} hizmetten kazanç: {firm_profit_direct_only:.1f}binTL')
    plt.text(len(coop_profits_per_transaction) - 0.5, firm_profit_direct_only + 2,
             f'{firm_profit_direct_only:.1f}binTL', color='blue', ha='center', fontsize=10)

    # Adding labels to x-axis
    plt.xticks(x_positions + bar_width, x_labels)
    plt.title("Kooperatifin İş Başına Ortalama Karına Göre Firma Kazancı (Bin TL)")
    plt.xlabel("İş Başına Ortalama Kooperatif Karı (TL)")
    plt.ylabel("Firma Karı (Bin TL)")
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

if __name__ == "__main__":
    interact(
        plot_firm_profit,
        job_counts=SelectMultiple(options=[100,200,300, 400, 600, 800, 1000, 1200], value=[400, 600, 800], description='Job Counts'),
        coop_min_profit=IntSlider(min=1000, max=5000, step=500, value=1000, description='İş başına Ortlama Min Koop Karı'),
        coop_max_profit=IntSlider(min=2000, max=10000, step=500, value=6000, description='İş başına Ortalama Max Koop Karı'),
        direct_jobs=IntSlider(min=5, max=40, step=1, value=10, description='Direk satış sayısı'),
        direct_job_profit=IntSlider(min=5000, max=15000, step=1000, value=9000, description='Direk satış karı')
    )
