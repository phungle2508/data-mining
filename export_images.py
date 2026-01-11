#!/usr/bin/env python3
"""
Export all charts from script.ipynb as PNG images.
"""

import os
import warnings
warnings.filterwarnings("ignore")

os.environ["PYTHONDONTWRITEBYTECODE"] = "1"

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from csv import reader
from collections import Counter
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules
import plotly.io as pio

# Set Kaleido to use minimal configuration
pio.kaleido.scope.mathjax = None
pio.kaleido.scope.default_format = "png"
pio.kaleido.scope.default_width = 1200
pio.kaleido.scope.default_height = 800

charts_dir = './charts'
os.makedirs(charts_dir, exist_ok=True)

print('Loading data...')
filepath = './data/groceries.csv'
with open(filepath) as file:
    groceries = [line.strip().split(',') for line in file.readlines()]

# Clean data
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

print('Creating and exporting charts as PNG images...')
print('=' * 60)

# 1. Individual Product Occurrence Count
print('1/11: Individual Product Occurrence Count...')
bar = px.bar(y=sorted_individual_item_count, x=sorted_items, title='Individual Product Occurence Count',
             color=sorted_individual_item_count, color_continuous_scale='Viridis')
bar.update_layout(xaxis_title='Products', yaxis_title='Product Occurence Count', showlegend=False, height=500)
try:
    bar.write_image(os.path.join(charts_dir, '01_individual_product_occurrence.png'), engine='kaleido')
    print('  ✓ Exported: 01_individual_product_occurrence.png')
except Exception as e:
    print(f'  ✗ Error: {e}')

# 2. Top 20 Most Frequent Items
print('2/11: Top 20 Most Frequent Products...')
top_n = 20
top_items = sorted_items[:top_n]
top_counts = sorted_individual_item_count[:top_n]
bar_top20 = px.bar(x=top_counts, y=top_items, orientation='h',
                   title=f'Top {top_n} Most Frequent Products',
                   color=top_counts, color_continuous_scale='Plasma')
bar_top20.update_layout(xaxis_title='Frequency', yaxis_title='Products', showlegend=False, height=600)
try:
    bar_top20.write_image(os.path.join(charts_dir, '02_top_20_frequent_products.png'), engine='kaleido')
    print('  ✓ Exported: 02_top_20_frequent_products.png')
except Exception as e:
    print(f'  ✗ Error: {e}')

# 3. Distribution of Item Frequencies
print('3/11: Item Frequency Distribution...')
hist_freq = px.histogram(x=individual_item_count, nbins=50,
                         title='Distribution of Item Frequencies',
                         labels={'x': 'Frequency Count', 'y': 'Number of Items'})
hist_freq.update_layout(height=400)
try:
    hist_freq.write_image(os.path.join(charts_dir, '03_item_frequency_distribution.png'), engine='kaleido')
    print('  ✓ Exported: 03_item_frequency_distribution.png')
except Exception as e:
    print(f'  ✗ Error: {e}')

# 4. Pie Chart for Top 10 Items
print('4/11: Top 10 Products Pie Chart...')
top_10_items = sorted_items[:10]
top_10_counts = sorted_individual_item_count[:10]
other_count = sum(sorted_individual_item_count[10:])
pie_labels = top_10_items + ['Others']
pie_values = list(top_10_counts) + [other_count]
pie_chart = px.pie(values=pie_values, names=pie_labels,
                   title='Top 10 Products Distribution (Others Grouped)',
                   hole=0.3)
pie_chart.update_layout(height=500)
try:
    pie_chart.write_image(os.path.join(charts_dir, '04_top_10_products_pie_chart.png'), engine='kaleido')
    print('  ✓ Exported: 04_top_10_products_pie_chart.png')
except Exception as e:
    print(f'  ✗ Error: {e}')

# Get frequent itemsets and rules
print('Processing association rules...')
n_rows = len(itemsets)
minimum_support_threshold = round((30/n_rows) * 5, 5)
freq_itemsets = apriori(itemsets, minimum_support_threshold, use_colnames=True)
rules = association_rules(freq_itemsets, metric='confidence', min_threshold=0.25)

# 5. Support vs Confidence Scatter
print('5/11: Support vs Confidence Scatter...')
rules_viz = rules.copy()
rules_viz['antecedents_str'] = rules_viz['antecedents'].apply(lambda x: ', '.join(list(x)))
rules_viz['consequents_str'] = rules_viz['consequents'].apply(lambda x: ', '.join(list(x)))
scatter_rules = px.scatter(rules_viz, x='support', y='confidence', color='lift',
                           title='Association Rules: Support vs Confidence',
                           hover_data=['antecedents_str', 'consequents_str'],
                           color_continuous_scale='RdYlGn',
                           height=500)
scatter_rules.update_layout(xaxis_title='Support', yaxis_title='Confidence')
try:
    scatter_rules.write_image(os.path.join(charts_dir, '05_support_vs_confidence_scatter.png'), engine='kaleido')
    print('  ✓ Exported: 05_support_vs_confidence_scatter.png')
except Exception as e:
    print(f'  ✗ Error: {e}')

# 6. Top 20 Rules by Lift
print('6/11: Top 20 Rules by Lift...')
top_rules_lift = rules.nlargest(20, 'lift').copy()
top_rules_lift['rule'] = top_rules_lift.apply(
    lambda x: f"{list(x['antecedents'])} -> {list(x['consequents'])}", axis=1
)
bar_rules_lift = px.bar(x=top_rules_lift['lift'], y=top_rules_lift['rule'],
                        orientation='h',
                        title='Top 20 Association Rules by Lift',
                        color=top_rules_lift['lift'],
                        color_continuous_scale='Turbo')
bar_rules_lift.update_layout(xaxis_title='Lift', yaxis_title='Rules (Antecedents -> Consequents)', showlegend=False, height=700)
try:
    bar_rules_lift.write_image(os.path.join(charts_dir, '06_top_20_rules_by_lift.png'), engine='kaleido')
    print('  ✓ Exported: 06_top_20_rules_by_lift.png')
except Exception as e:
    print(f'  ✗ Error: {e}')

# 7. Rules Metrics Distribution
print('7/11: Rules Metrics Distribution Boxplot...')
metrics = ['support', 'confidence', 'lift', 'leverage', 'conviction']
fig_metrics = go.Figure()
for metric in metrics:
    fig_metrics.add_trace(go.Box(y=rules[metric], name=metric.capitalize()))
fig_metrics.update_layout(title='Distribution of Association Rule Metrics', yaxis_title='Value', height=500)
try:
    fig_metrics.write_image(os.path.join(charts_dir, '07_rules_metrics_distribution_boxplot.png'), engine='kaleido')
    print('  ✓ Exported: 07_rules_metrics_distribution_boxplot.png')
except Exception as e:
    print(f'  ✗ Error: {e}')

# 8. Correlation Heatmap
print('8/11: Metrics Correlation Heatmap...')
corr_matrix = rules[metrics].corr()
fig_heatmap = px.imshow(corr_matrix,
                        title='Correlation Heatmap of Rule Metrics',
                        color_continuous_scale='RdBu_r',
                        text_auto=True,
                        aspect='auto')
fig_heatmap.update_layout(height=500)
try:
    fig_heatmap.write_image(os.path.join(charts_dir, '08_metrics_correlation_heatmap.png'), engine='kaleido')
    print('  ✓ Exported: 08_metrics_correlation_heatmap.png')
except Exception as e:
    print(f'  ✗ Error: {e}')

# Algorithm comparison data
comparison_data = {
    'Algorithm': ['Apriori (Standard)', 'FP-Growth', 'FP-Max', 'Sampling', 'DHP (Hash-based)',
                  'Transaction Reduction', 'ECLAT (Vertical)', 'DIC (Dynamic Counting)', 'Partitioning'],
    'Num_Frequent_Itemsets': [173, 173, 131, 25, 169, 175, 174, 202, 173],
    'Execution_Time_Float': [0.0600, 2.3068, 2.0583, 0.0351, 0.1932, 0.0736, 0.0683, 3.4055, 0.8112]
}
comparison_df = pd.DataFrame(comparison_data)

# 9. Execution Time Comparison
print('9/11: Algorithm Execution Time...')
bar_time = px.bar(comparison_df, x='Execution_Time_Float', y='Algorithm',
                  orientation='h',
                  title='Algorithm Execution Time Comparison',
                  color='Execution_Time_Float',
                  color_continuous_scale='RdYlGn_r',
                  text='Execution_Time_Float')
bar_time.update_traces(texttemplate='%{text:.3f}s', textposition='outside')
bar_time.update_layout(xaxis_title='Execution Time (seconds)', yaxis_title='Algorithm', showlegend=False, height=500)
try:
    bar_time.write_image(os.path.join(charts_dir, '09_algorithm_execution_time.png'), engine='kaleido')
    print('  ✓ Exported: 09_algorithm_execution_time.png')
except Exception as e:
    print(f'  ✗ Error: {e}')

# 10. Number of Frequent Itemsets
print('10/11: Frequent Itemsets Count...')
bar_itemsets = px.bar(comparison_df, x='Num_Frequent_Itemsets', y='Algorithm',
                      orientation='h',
                      title='Number of Frequent Itemsets Found',
                      color='Num_Frequent_Itemsets',
                      color_continuous_scale='Blues',
                      text='Num_Frequent_Itemsets')
bar_itemsets.update_traces(texttemplate='%{text}', textposition='outside')
bar_itemsets.update_layout(xaxis_title='Number of Frequent Itemsets', yaxis_title='Algorithm', showlegend=False, height=500)
try:
    bar_itemsets.write_image(os.path.join(charts_dir, '10_frequent_itemsets_count.png'), engine='kaleido')
    print('  ✓ Exported: 10_frequent_itemsets_count.png')
except Exception as e:
    print(f'  ✗ Error: {e}')

# 11. Time Efficiency Scatter
print('11/11: Time Efficiency Scatter...')
scatter_efficiency = px.scatter(comparison_df, x='Execution_Time_Float', y='Num_Frequent_Itemsets',
                                title='Algorithm Efficiency: Time vs Itemsets Found',
                                size='Execution_Time_Float',
                                color='Execution_Time_Float',
                                color_continuous_scale='Viridis',
                                hover_data=['Algorithm'])
scatter_efficiency.update_traces(
    marker=dict(line=dict(width=2, color='white'), opacity=0.9),
    selector=dict(mode='markers')
)
# Add text labels with custom positioning for each point to avoid overlap
for i, row in comparison_df.iterrows():
    algo = row['Algorithm']
    x = row['Execution_Time_Float']
    y = row['Num_Frequent_Itemsets']

    # Position text based on quadrant to avoid overlap
    if x < comparison_df['Execution_Time_Float'].median():
        x_text = 'left'
    else:
        x_text = 'right'

    if y < comparison_df['Num_Frequent_Itemsets'].median():
        y_text = 'bottom'
    else:
        y_text = 'top'

    scatter_efficiency.add_annotation(
        x=x, y=y,
        text=algo,
        showarrow=False,
        xanchor='center' if x_text == 'left' else 'center',
        yanchor='bottom' if y_text == 'top' else 'top',
        xshift=-15 if x_text == 'left' else 15,
        yshift=10 if y_text == 'top' else -10,
        font=dict(size=10, color='black')
    )
scatter_efficiency.update_layout(xaxis_title='Execution Time (seconds)', yaxis_title='Number of Frequent Itemsets', height=600, showlegend=False)
try:
    scatter_efficiency.write_image(os.path.join(charts_dir, '11_time_efficiency_scatter.png'), engine='kaleido')
    print('  ✓ Exported: 11_time_efficiency_scatter.png')
except Exception as e:
    print(f'  ✗ Error: {e}')

print('=' * 60)
print('Export process completed!')
print(f'Charts saved to: {os.path.abspath(charts_dir)}')
