#!/usr/bin/env python3
"""
Export all charts from script.ipynb to the charts folder.
"""

import subprocess
import sys

# Install kaleido for static image export
print("Installing kaleido...")
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'kaleido', '-q'])

# Import nbformat to read and execute the notebook
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
import os

charts_dir = './charts'
os.makedirs(charts_dir, exist_ok=True)

# Read the notebook
print("Reading script.ipynb...")
with open('script.ipynb', 'r', encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)

# Execute the notebook
print("Executing notebook (this may take a while)...")
ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
try:
    ep.preprocess(nb, {'metadata': {'path': '.'}})

    # Save the executed notebook
    with open('script_executed.ipynb', 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)
    print("Notebook executed successfully!")
except Exception as e:
    print(f"Error executing notebook: {e}")

# Now run the export code
print("\nExporting charts...")
export_code = '''
import os

charts_dir = './charts'
os.makedirs(charts_dir, exist_ok=True)

print("Exporting all charts to", charts_dir)
print("=" * 60)

# Recreate the charts from the notebook's data
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from csv import reader
from collections import Counter
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import fpmax, apriori, fpgrowth, association_rules

# Load and process data
filepath = './data/groceries.csv'
with open(filepath) as file:
    groceries = [line.strip().split(',') for line in file.readlines()]

# Clean data
from collections import defaultdict
import random
import time
from datetime import datetime
from itertools import combinations

groceries_cleaned = []
for transaction in groceries:
    cleaned = [item.strip() for item in transaction if item.strip()]
    if cleaned:
        groceries_cleaned.append(cleaned)

# Remove duplicates
unique_transactions = []
seen = set()
for transaction in groceries_cleaned:
    transaction_tuple = tuple(sorted(transaction))
    if transaction_tuple not in seen:
        seen.add(transaction_tuple)
        unique_transactions.append(list(transaction))

groceries_cleaned = unique_transactions

# Filter infrequent items
all_items = [item for transaction in groceries_cleaned for item in transaction]
item_freq = Counter(all_items)
min_item_support = 0.001
min_count = int(min_item_support * len(groceries_cleaned))
frequent_items = {item for item, count in item_freq.items() if count >= min_count}

groceries_filtered = []
for transaction in groceries_cleaned:
    filtered = [item for item in transaction if item in frequent_items]
    if filtered:
        groceries_filtered.append(filtered)

# Filter small transactions
groceries_final = [t for t in groceries_filtered if len(t) >= 2]
groceries = groceries_final

# Encode data
encoder = TransactionEncoder()
transactions = encoder.fit(groceries).transform(groceries)
itemsets = pd.DataFrame(transactions, columns=encoder.columns_)

# Get sorted items
items = list(itemsets.columns)
individual_item_count = [itemsets[item].sum() for item in items]
sorted_individual_item_count = sorted(individual_item_count, reverse=True)
sorted_items = [items[individual_item_count.index(value)] for value in sorted_individual_item_count]

# Create charts
n_rows = len(itemsets)
minimum_support_threshold = round((30/n_rows) * 5, 5)

# 1. Individual Product Occurrence Count
bar = px.bar(y=sorted_individual_item_count, x=sorted_items, title="Individual Product Occurence Count",
             color=sorted_individual_item_count, color_continuous_scale='Viridis')
bar.update_layout(xaxis_title="Products", yaxis_title="Product Occurence Count", showlegend=False, height=500)

# 2. Top 20 Most Frequent Items
top_n = 20
top_items = sorted_items[:top_n]
top_counts = sorted_individual_item_count[:top_n]
bar_top20 = px.bar(x=top_counts, y=top_items, orientation='h',
                   title=f"Top {top_n} Most Frequent Products",
                   color=top_counts, color_continuous_scale='Plasma')
bar_top20.update_layout(xaxis_title="Frequency", yaxis_title="Products", showlegend=False, height=600)

# 3. Distribution of Item Frequencies
hist_freq = px.histogram(x=individual_item_count, nbins=50,
                         title="Distribution of Item Frequencies",
                         labels={'x': 'Frequency Count', 'y': 'Number of Items'})
hist_freq.update_layout(height=400)

# 4. Pie Chart for Top 10 Items
top_10_items = sorted_items[:10]
top_10_counts = sorted_individual_item_count[:10]
other_count = sum(sorted_individual_item_count[10:])
pie_labels = top_10_items + ['Others']
pie_values = list(top_10_counts) + [other_count]
pie_chart = px.pie(values=pie_values, names=pie_labels,
                   title="Top 10 Products Distribution (Others Grouped)",
                   hole=0.3)
pie_chart.update_layout(height=500)

# Get frequent itemsets and rules
freq_itemsets = apriori(itemsets, minimum_support_threshold, use_colnames=True)
rules = association_rules(freq_itemsets, metric='confidence', min_threshold=0.25)

# 5. Support vs Confidence Scatter
rules_viz = rules.copy()
rules_viz['antecedents_str'] = rules_viz['antecedents'].apply(lambda x: ', '.join(list(x)))
rules_viz['consequents_str'] = rules_viz['consequents'].apply(lambda x: ', '.join(list(x)))
scatter_rules = px.scatter(rules_viz, x='support', y='confidence', color='lift',
                           title='Association Rules: Support vs Confidence',
                           hover_data=['antecedents_str', 'consequents_str'],
                           color_continuous_scale='RdYlGn',
                           height=500)
scatter_rules.update_layout(xaxis_title="Support", yaxis_title="Confidence")

# 6. Top 20 Rules by Lift
top_rules_lift = rules.nlargest(20, 'lift').copy()
top_rules_lift['rule'] = top_rules_lift.apply(
    lambda x: f"{list(x['antecedents'])} -> {list(x['consequents'])}", axis=1
)
bar_rules_lift = px.bar(x=top_rules_lift['lift'], y=top_rules_lift['rule'],
                        orientation='h',
                        title='Top 20 Association Rules by Lift',
                        color=top_rules_lift['lift'],
                        color_continuous_scale='Turbo')
bar_rules_lift.update_layout(xaxis_title="Lift", yaxis_title="Rules (Antecedents -> Consequents)", showlegend=False, height=700)

# 7. Rules Metrics Distribution
metrics = ['support', 'confidence', 'lift', 'leverage', 'conviction']
fig_metrics = go.Figure()
for metric in metrics:
    fig_metrics.add_trace(go.Box(y=rules[metric], name=metric.capitalize()))
fig_metrics.update_layout(title='Distribution of Association Rule Metrics', yaxis_title='Value', height=500)

# 8. Correlation Heatmap
corr_matrix = rules[metrics].corr()
fig_heatmap = px.imshow(corr_matrix,
                        title='Correlation Heatmap of Rule Metrics',
                        color_continuous_scale='RdBu_r',
                        text_auto=True,
                        aspect='auto')
fig_heatmap.update_layout(height=500)

# Algorithm comparison data
comparison_data = {
    'Algorithm': ['Apriori (Standard)', 'FP-Growth', 'FP-Max', 'Sampling', 'DHP (Hash-based)',
                  'Transaction Reduction', 'ECLAT (Vertical)', 'DIC (Dynamic Counting)', 'Partitioning'],
    'Num_Frequent_Itemsets': [173, 173, 131, 25, 169, 175, 174, 202, 173],
    'Execution_Time_Float': [0.0600, 2.3068, 2.0583, 0.0351, 0.1932, 0.0736, 0.0683, 3.4055, 0.8112]
}
comparison_df = pd.DataFrame(comparison_data)

# 9. Execution Time Comparison
bar_time = px.bar(comparison_df, x='Execution_Time_Float', y='Algorithm',
                  orientation='h',
                  title='Algorithm Execution Time Comparison',
                  color='Execution_Time_Float',
                  color_continuous_scale='RdYlGn_r',
                  text='Execution_Time_Float')
bar_time.update_traces(texttemplate='%{text:.3f}s', textposition='outside')
bar_time.update_layout(xaxis_title="Execution Time (seconds)", yaxis_title="Algorithm", showlegend=False, height=500)

# 10. Number of Frequent Itemsets
bar_itemsets = px.bar(comparison_df, x='Num_Frequent_Itemsets', y='Algorithm',
                      orientation='h',
                      title='Number of Frequent Itemsets Found',
                      color='Num_Frequent_Itemsets',
                      color_continuous_scale='Blues',
                      text='Num_Frequent_Itemsets')
bar_itemsets.update_traces(texttemplate='%{text}', textposition='outside')
bar_itemsets.update_layout(xaxis_title="Number of Frequent Itemsets", yaxis_title="Algorithm", showlegend=False, height=500)

# 11. Time Efficiency Scatter
scatter_efficiency = px.scatter(comparison_df, x='Execution_Time_Float', y='Num_Frequent_Itemsets',
                                text='Algorithm',
                                title='Algorithm Efficiency: Time vs Itemsets Found',
                                size='Execution_Time_Float',
                                color='Execution_Time_Float',
                                color_continuous_scale='Viridis')
scatter_efficiency.update_traces(textposition='top center')
scatter_efficiency.update_layout(xaxis_title="Execution Time (seconds)", yaxis_title="Number of Frequent Itemsets", height=600, showlegend=False)

# Export all charts
charts_to_export = [
    ('bar', '01_individual_product_occurrence'),
    ('bar_top20', '02_top_20_frequent_products'),
    ('hist_freq', '03_item_frequency_distribution'),
    ('pie_chart', '04_top_10_products_pie_chart'),
    ('scatter_rules', '05_support_vs_confidence_scatter'),
    ('bar_rules_lift', '06_top_20_rules_by_lift'),
    ('fig_metrics', '07_rules_metrics_distribution_boxplot'),
    ('fig_heatmap', '08_metrics_correlation_heatmap'),
    ('bar_time', '09_algorithm_execution_time'),
    ('bar_itemsets', '10_frequent_itemsets_count'),
    ('scatter_efficiency', '11_time_efficiency_scatter')
]

exported_count = 0
for var_name, file_prefix in charts_to_export:
    try:
        chart = locals().get(var_name)
        if chart is not None:
            # Export as PNG
            png_path = os.path.join(charts_dir, f'{file_prefix}.png')
            chart.write_image(png_path, scale=2, width=1200, height=800)

            # Export as HTML
            html_path = os.path.join(charts_dir, f'{file_prefix}.html')
            chart.write_html(html_path, include_plotlyjs='cdn')

            print(f"✓ Exported: {file_prefix}")
            exported_count += 1
        else:
            print(f"✗ Chart variable '{var_name}' not found")
    except Exception as e:
        print(f"✗ Error exporting {file_prefix}: {e}")

print("=" * 60)
print(f"Successfully exported {exported_count}/{len(charts_to_export)} charts")
'''

# Execute the export code
exec(export_code)

print("\nDone! Charts have been exported to ./charts/")
