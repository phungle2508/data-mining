# ========================================
# Data Mining Project: Frequent Pattern Mining
# ========================================
# This script implements and compares various frequent pattern mining
# algorithms on the Groceries dataset for Market Basket Analysis.
#
# Algorithms Implemented:
# - Baseline: Apriori, FP-Growth, FP-Max
# - Advanced: Sampling, DHP, Transaction Reduction, ECLAT, DIC, Partitioning
#
# Author: Data Mining Course Project
# Year: 2024-2025
# ========================================

# ========================================
# Setup: Download Data and Install Dependencies
# ========================================
import subprocess
import sys

# Create data directory if it doesn't exist
subprocess.run(['mkdir', '-p', './data'])

# Download Groceries dataset from GitHub
# Source: Machine Learning with R datasets
# Contains 9835 transactions with 169 unique products
subprocess.run(['wget', '-O', './data/groceries.csv',
                'https://raw.githubusercontent.com/stedy/Machine-Learning-with-R-datasets/master/groceries.csv'])

# Install mlxtend library for frequent pattern mining algorithms
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'mlxtend'])

# ========================================
# Import Libraries
# ========================================
import pandas as pd  # Data manipulation and analysis
import numpy as np   # Numerical computing
from csv import reader  # CSV file reading
from collections import Counter  # Frequency counting

# mlxtend: Machine Learning Extensions for frequent pattern mining
from mlxtend.preprocessing import TransactionEncoder  # Encode transaction data
from mlxtend.frequent_patterns import fpmax  # FP-Max algorithm
from mlxtend.frequent_patterns import apriori  # Apriori algorithm
from mlxtend.frequent_patterns import fpgrowth  # FP-Growth algorithm
from mlxtend.frequent_patterns import association_rules  # Generate association rules

# Suppress warnings for cleaner output
import warnings
warnings.filterwarnings("ignore")

# Plotly for interactive visualizations
import plotly.express as px
import plotly.graph_objects as go

# ========================================
# Data Loading
# ========================================
# The Groceries dataset contains transaction data from a grocery store.
# Each row represents a transaction (shopping basket) with comma-separated items.
#
# Expected output after running:
# - Raw transaction data (list of lists)
# - First 5 transactions displayed
filepath = './data/groceries.csv'

# Method 1: Using csv.reader
with open(filepath, 'r') as csv_file:
    csv_reader = reader(csv_file)
    groceries = [row for row in csv_reader]

# Display first 5 transactions
groceries[:5]

# Method 2: Manual parsing (alternative approach)
# This strips whitespace and splits by comma
with open(filepath) as file:
    groceries = [line.strip().split(',') for line in file.readlines()]

groceries[:5]

# ========================================
# Data Cleaning & Preprocessing
# ========================================
# This section performs comprehensive data cleaning to ensure quality input
# for the frequent pattern mining algorithms.
#
# Steps performed:
# 1. Initial statistics - Count transactions and items
# 2. Remove empty items - Clean whitespace and empty strings
# 3. Remove duplicate transactions - Ensure uniqueness
# 4. Item frequency analysis - Understand distribution
# 5. Filter infrequent items - Remove noise (0.1% threshold)
# 6. Filter small transactions - Keep only transactions with >=2 items
# 7. Final statistics - Summary after cleaning

print("\n" + "="*60)
print("DATA CLEANING & PREPROCESSING")
print("="*60)

# --------------------------------------------------------
# Step 1: Initial Data Statistics
# --------------------------------------------------------
print("\n1. INITIAL DATA STATISTICS")
print("-" * 40)
initial_n_transactions = len(groceries)
initial_total_items = sum(len(t) for t in groceries)
initial_avg_items = initial_total_items / initial_n_transactions if initial_n_transactions > 0 else 0

# Expected output: [actual numeric values after running]
print(f"Total transactions: {initial_n_transactions}")
print(f"Total items (with duplicates): {initial_total_items}")
print(f"Avg items per transaction: {initial_avg_items:.2f}")

# --------------------------------------------------------
# Step 2: Remove Empty Items and Strip Whitespace
# --------------------------------------------------------
# Clean each transaction by:
# - Stripping whitespace from item names
# - Removing empty strings
# - Keeping only non-empty transactions
print("\n2. REMOVING EMPTY ITEMS & WHITESPACE")
print("-" * 40)
groceries_cleaned = []
for transaction in groceries:
    # Remove empty strings and strip whitespace
    cleaned = [item.strip() for item in transaction if item.strip()]
    if cleaned:  # Keep only non-empty transactions
        groceries_cleaned.append(cleaned)

n_after_empty_removal = len(groceries_cleaned)
n_removed_empty = initial_n_transactions - n_after_empty_removal

# Expected output: [actual counts after running]
print(f"Transactions removed (empty): {n_removed_empty}")
print(f"Remaining transactions: {n_after_empty_removal}")

# --------------------------------------------------------
# Step 3: Remove Duplicate Transactions
# --------------------------------------------------------
# Use set-based deduplication by:
# - Converting transactions to sorted tuples (hashable)
# - Tracking seen transactions
# - Counting duplicates
print("\n3. REMOVING DUPLICATE TRANSACTIONS")
print("-" * 40)

# Convert to tuples for hashing (lists are not hashable)
unique_transactions = []
seen = set()
duplicates_count = 0

for transaction in groceries_cleaned:
    transaction_tuple = tuple(sorted(transaction))  # Sort for consistency
    if transaction_tuple not in seen:
        seen.add(transaction_tuple)
        unique_transactions.append(list(transaction))  # Keep as list
    else:
        duplicates_count += 1

groceries_cleaned = unique_transactions

# Expected output: [duplicate count and percentage after running]
print(f"Duplicate transactions found: {duplicates_count}")
print(f"Unique transactions: {len(groceries_cleaned)}")
print(f"Duplicate percentage: {round((duplicates_count/initial_n_transactions)*100, 2)}%")

# --------------------------------------------------------
# Step 4: Item Frequency Analysis
# --------------------------------------------------------
# Analyze the distribution of items across transactions:
# - Count total unique items
# - Display top 10 most frequent items
# - Display bottom 10 least frequent items
print("\n4. ITEM FREQUENCY ANALYSIS")
print("-" * 40)

all_items = [item for transaction in groceries_cleaned for item in transaction]
item_freq = Counter(all_items)

# Expected output: [actual counts and percentages after running]
print(f"Total unique items: {len(item_freq)}")
print(f"\nTop 10 most frequent items:")
for item, count in item_freq.most_common(10):
    print(f"  {item:25}: {count:4} ({round((count/len(groceries_cleaned))*100, 2)}%)")

print(f"\nBottom 10 least frequent items:")
for item, count in item_freq.most_common()[-11:-1]:  # Skip single items if any
    print(f"  {item:25}: {count:4} ({round((count/len(groceries_cleaned))*100, 2)}%)")

# --------------------------------------------------------
# Step 5: Filter Infrequent Items (Noise Reduction)
# --------------------------------------------------------
# Remove items that appear in less than 0.1% of transactions.
# This reduces noise and computational complexity.
print("\n5. FILTERING INFREQUENT ITEMS")
print("-" * 40)

min_item_support = 0.001  # Items appearing in less than 0.1% of transactions
min_count = int(min_item_support * len(groceries_cleaned))

frequent_items = {item for item, count in item_freq.items() if count >= min_count}
infrequent_items = {item for item, count in item_freq.items() if count < min_count}

# Expected output: [actual counts after running]
print(f"Minimum support threshold: {min_item_support} (min {min_count} transactions)")
print(f"Frequent items (≥ threshold): {len(frequent_items)}")
print(f"Infrequent items (< threshold): {len(infrequent_items)}")

# Remove infrequent items from transactions
# (Transactions that become empty after filtering are removed)
groceries_filtered = []
for transaction in groceries_cleaned:
    filtered = [item for item in transaction if item in frequent_items]
    if filtered:  # Keep only non-empty transactions
        groceries_filtered.append(filtered)

n_after_filtering = len(groceries_filtered)
n_removed_rare = n_after_empty_removal - n_after_filtering

print(f"Transactions removed (became empty): {n_removed_rare}")
print(f"Remaining transactions: {n_after_filtering}")

# --------------------------------------------------------
# Step 6: Filter Small Transactions
# --------------------------------------------------------
# Remove transactions with fewer than 2 items.
# Single-item transactions cannot generate association rules.
print("\n6. FILTERING SMALL TRANSACTIONS")
print("-" * 40)

min_transaction_size = 2
groceries_final = [t for t in groceries_filtered if len(t) >= min_transaction_size]

n_removed_small = n_after_filtering - len(groceries_final)

print(f"Minimum transaction size: {min_transaction_size} items")
print(f"Transactions removed (< 2 items): {n_removed_small}")
print(f"Remaining transactions: {len(groceries_final)}")

# --------------------------------------------------------
# Step 7: Final Data Statistics
# --------------------------------------------------------
# Display summary statistics after all cleaning steps.
print("\n7. FINAL DATA STATISTICS")
print("-" * 40)

final_n_transactions = len(groceries_final)
final_total_items = sum(len(t) for t in groceries_final)
final_avg_items = final_total_items / final_n_transactions if final_n_transactions > 0 else 0

# Recalculate unique items after filtering
final_all_items = [item for transaction in groceries_final for item in transaction]
final_unique_items = len(set(final_all_items))

# Expected output: [actual final statistics after running]
print(f"Total transactions: {final_n_transactions}")
print(f"Total unique items: {final_unique_items}")
print(f"Total items (with duplicates): {final_total_items}")
print(f"Avg items per transaction: {final_avg_items:.2f}")

# --------------------------------------------------------
# Data Cleaning Summary
# --------------------------------------------------------
# Display a comprehensive summary of the data cleaning process.
print("\n" + "="*60)
print("DATA CLEANING SUMMARY")
print("="*60)
print(f"Initial transactions : {initial_n_transactions}")
print(f"Removed (empty)      : {n_removed_empty}")
print(f"Removed (duplicates) : {duplicates_count}")
print(f"Removed (rare items) : {n_removed_rare}")
print(f"Removed (small tx)   : {n_removed_small}")
print(f"-" * 40)
print(f"Final transactions   : {final_n_transactions}")
print(f"Data reduction       : {round((1 - final_n_transactions/initial_n_transactions) * 100, 2)}%")
print("="*60)

# Update groceries with cleaned data
groceries = groceries_final

# ========================================
# Data Encoding: Transaction Encoder
# ========================================
# Convert transaction data to a one-hot encoded format.
# Each column represents an item, each row a transaction.
# Value 1 = item present, 0 = item absent.
#
# Output: Binary matrix (transactions x items)
encoder = TransactionEncoder()

transactions = encoder.fit(groceries).transform(groceries)
transactions[0]  # Display first encoded transaction

itemsets = pd.DataFrame(transactions, columns=encoder.columns_)
itemsets.head()  # Display first few rows

# ========================================
# Data Analysis: Dataset Statistics
# ========================================
# Compute and display key statistics about the encoded dataset.
n_rows, n_items = itemsets.shape

# Expected output: [actual dimensions and duplicate counts after running]
print(f"No. of Samples  : {n_rows}")
print(f"No. of Products : {n_items}")

n_duplicates = itemsets.duplicated().sum()

print(f"No. Duplicate Values: {n_duplicates}")
print(f"Per% Duplicate Values: {round((n_duplicates/n_rows)*100, 2)}%")

# ========================================
# Data Visualization
# ========================================
# Create interactive visualizations to explore item frequency distribution.
# Generated using Plotly Express for interactive charts.

# Prepare data for visualization
items = list(itemsets.columns)
individual_item_count = [itemsets[item].sum() for item in items]

sorted_individual_item_count = sorted(individual_item_count, reverse=True)
sorted_items = [items[individual_item_count.index(value)] for value in sorted_individual_item_count]

# --------------------------------------------------------
# Visualization 1: Individual Product Occurrence Count (Bar Chart)
# --------------------------------------------------------
# Displays all products sorted by frequency in descending order.
bar = px.bar(y=sorted_individual_item_count, x=sorted_items, title="Individual Product Occurence Count",
             color=sorted_individual_item_count, color_continuous_scale='Viridis')
bar.update_layout(
    xaxis_title="Products",
    yaxis_title="Product Occurence Count",
    showlegend=False,
    height=500
)
bar.show()

# --------------------------------------------------------
# Visualization 2: Top 20 Most Frequent Items (Horizontal Bar Chart)
# --------------------------------------------------------
# Highlights the 20 most frequently purchased products.
top_n = 20
top_items = sorted_items[:top_n]
top_counts = sorted_individual_item_count[:top_n]

bar_top20 = px.bar(x=top_counts, y=top_items, orientation='h',
                   title=f"Top {top_n} Most Frequent Products",
                   color=top_counts, color_continuous_scale='Plasma')
bar_top20.update_layout(
    xaxis_title="Frequency",
    yaxis_title="Products",
    showlegend=False,
    height=600
)
bar_top20.show()

# --------------------------------------------------------
# Visualization 3: Distribution of Item Frequencies (Histogram)
# --------------------------------------------------------
# Shows the overall distribution pattern of item frequencies.
hist_freq = px.histogram(x=individual_item_count, nbins=50,
                         title="Distribution of Item Frequencies",
                         labels={'x': 'Frequency Count', 'y': 'Number of Items'})
hist_freq.update_layout(height=400)
hist_freq.show()

# --------------------------------------------------------
# Visualization 4: Pie Chart for Top 10 Items
# --------------------------------------------------------
# Displays the market share of top 10 products (others grouped).
top_10_items = sorted_items[:10]
top_10_counts = sorted_individual_item_count[:10]
other_count = sum(sorted_individual_item_count[10:])
pie_labels = top_10_items + ['Others']
pie_values = list(top_10_counts) + [other_count]

pie_chart = px.pie(values=pie_values, names=pie_labels,
                   title="Top 10 Products Distribution (Others Grouped)",
                   hole=0.3)
pie_chart.update_layout(height=500)
pie_chart.show()

# ========================================
# Frequent Itemset Mining
# ========================================
# Apply the Apriori algorithm to discover frequent itemsets.
# The minimum support threshold is calculated dynamically based on dataset size.

minimum_support_threshold = round((30/n_rows) * 5, 5)

print(f"Minimum Support Threshold: {minimum_support_threshold}")

# Mine frequent itemsets using Apriori algorithm
freq_itemsets = apriori(itemsets, minimum_support_threshold, use_colnames=True)
freq_itemsets

# Display top 5 single items with highest support
top_5_supports = freq_itemsets[freq_itemsets.itemsets.map(len) == 1].nlargest(5, 'support')

for index, row in top_5_supports.iterrows():
    item_name = list(row['itemsets'])[0].title()
    support_value = row['support']

    print(f"{item_name:20}: {support_value}")

# Sort all frequent itemsets by support (descending)
freq_itemsets.sort_values('support', ascending=False)

# Display itemsets with more than 2 items
lengths = [len(itemset) for itemset in freq_itemsets.itemsets]
freq_itemsets[[val>2 for val in lengths]]

# Group by itemset length and display statistics
freq_itemsets.groupby(lengths)['support'].describe()

# ========================================
# Advanced Frequent Pattern Mining Algorithms
# ========================================
# This section implements 6 advanced algorithms for efficient frequent
# pattern mining, along with helper functions for timing and comparison.
#
# Algorithms:
# 1. Sampling-based FIM - Mine on sample, verify on full dataset
# 2. DHP (Direct Hashing and Pruning) - Hash-based candidate pruning
# 3. Transaction Reduction - Remove transactions incrementally
# 4. ECLAT (Vertical Format) - Use tid-lists for fast intersection
# 5. DIC (Dynamic Itemset Counting) - Interleaved counting
# 6. Partitioning - Divide database, mine locally, verify globally

import random
import time
from datetime import datetime
from itertools import combinations
from collections import defaultdict

# --------------------------------------------------------
# Helper Function: Timing Wrapper
# --------------------------------------------------------
def time_algorithm_execution(algorithm_name, algorithm_func, *args, **kwargs):
    """
    Wrapper function to execute algorithms and return results with consistent format
    including execution time and timestamp.

    Args:
        algorithm_name: Name of the algorithm for identification
        algorithm_func: The algorithm function to execute
        *args, **kwargs: Arguments to pass to the algorithm function

    Returns:
        Dictionary containing:
        - algorithm: Algorithm name
        - timestamp: Execution timestamp
        - execution_time: Time taken in seconds
        - result: Algorithm output (frequent itemsets DataFrame)
        - num_itemsets: Number of frequent itemsets found
    """
    start_time = time.time()
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    result = algorithm_func(*args, **kwargs)

    end_time = time.time()
    execution_time = end_time - start_time

    # Return standardized result dictionary
    return {
        'algorithm': algorithm_name,
        'timestamp': timestamp,
        'execution_time': execution_time,
        'result': result,
        'num_itemsets': len(result)
    }

def print_algorithm_result(algorithm_result):
    """
    Print algorithm result in a consistent format.

    Args:
        algorithm_result: Result dictionary from time_algorithm_execution()
    """
    print(f"\nAlgorithm: {algorithm_result['algorithm']}")
    print(f"Timestamp: {algorithm_result['timestamp']}")
    print(f"Execution Time: {algorithm_result['execution_time']:.4f} seconds")
    print(f"Frequent Itemsets Found: {algorithm_result['num_itemsets']}")
    print("-" * 40)
    print(algorithm_result['result'].sort_values('support', ascending=False).head(10))

# ========================================
# Standard Algorithms (Baseline Comparison)
# ========================================
# Execute the three standard algorithms from mlxtend library:
# - Apriori: Classical level-wise algorithm
# - FP-Growth: FP-tree based algorithm (2 database scans)
# - FP-Max: Maximal frequent itemsets only (most efficient)

print("\n" + "="*60)
print("STANDARD ALGORITHMS (BASELINE)")
print("="*60)

# Time the standard algorithms for consistent comparison
result_apriori = time_algorithm_execution(
    "Apriori (Standard)",
    apriori, itemsets, minimum_support_threshold, True
)
print_algorithm_result(result_apriori)
freq_itemsets_apriori = result_apriori['result']

result_fpgrowth = time_algorithm_execution(
    "FP-Growth",
    fpgrowth, itemsets, minimum_support_threshold, True
)
print_algorithm_result(result_fpgrowth)
freq_itemsets_fpgrowth = result_fpgrowth['result']

result_fpmax = time_algorithm_execution(
    "FP-Max",
    fpmax, itemsets, minimum_support_threshold, True
)
print_algorithm_result(result_fpmax)
freq_itemsets_fpmax = result_fpmax['result']

# ========================================
# Association Rules Mining
# ========================================
# Generate association rules from frequent itemsets using:
# - Minimum confidence threshold: 0.25 (25%)
# - Metric: Confidence (primary filtering metric)
#
# Output: Rules with antecedents, consequents, and quality metrics

rules = association_rules(freq_itemsets, metric='confidence', min_threshold=0.25)
rules.head()

# Expected output: [actual number of rules after running]
print(f'Total Number of Association Rules: {rules.shape[0]}')

# Filter rules by specific items
rules[rules['antecedents'] == {'rolls/buns'}]
rules[rules['consequents'] == {'rolls/buns'}]
rules[rules['antecedents'].str.len()>1]

# Display statistical summary of rule metrics
rules.describe()

# Sort rules by various quality metrics
rules.sort_values('lift', ascending=False).head()  # Rules with highest lift
rules.sort_values('leverage', ascending=False).head()  # Rules with highest leverage
rules.sort_values('conviction', ascending=False).head()  # Rules with highest conviction
rules.sort_values('zhangs_metric', ascending=True).head()  # Negative association rules
rules.sort_values('zhangs_metric', ascending=False).head()  # Positive association rules

# ========================================
# Association Rules Visualizations
# ========================================
# Create interactive visualizations to explore the quality and
# characteristics of generated association rules.

# Convert frozensets to strings for Plotly compatibility
rules_viz = rules.copy()
rules_viz['antecedents_str'] = rules_viz['antecedents'].apply(lambda x: ', '.join(list(x)))
rules_viz['consequents_str'] = rules_viz['consequents'].apply(lambda x: ', '.join(list(x)))

# Visualization 5: Scatter Plot - Support vs Confidence (colored by Lift)
scatter_rules = px.scatter(rules_viz, x='support', y='confidence', color='lift',
                           title='Association Rules: Support vs Confidence',
                           hover_data=['antecedents_str', 'consequents_str'],
                           color_continuous_scale='RdYlGn',
                           height=500)
scatter_rules.update_layout(
    xaxis_title="Support",
    yaxis_title="Confidence"
)
scatter_rules.show()

# Visualization 6: Top 20 Rules by Lift (Bar Chart)
top_rules_lift = rules.nlargest(20, 'lift').copy()
top_rules_lift['rule'] = top_rules_lift.apply(
    lambda x: f"{list(x['antecedents'])} -> {list(x['consequents'])}", axis=1
)

bar_rules_lift = px.bar(x=top_rules_lift['lift'], y=top_rules_lift['rule'],
                        orientation='h',
                        title='Top 20 Association Rules by Lift',
                        color=top_rules_lift['lift'],
                        color_continuous_scale='Turbo')
bar_rules_lift.update_layout(
    xaxis_title="Lift",
    yaxis_title="Rules (Antecedents -> Consequents)",
    showlegend=False,
    height=700
)
bar_rules_lift.show()

# Visualization 7: Rules Metrics Distribution (Box Plot)
metrics = ['support', 'confidence', 'lift', 'leverage', 'conviction']
fig_metrics = go.Figure()
for metric in metrics:
    fig_metrics.add_trace(go.Box(y=rules[metric], name=metric.capitalize()))

fig_metrics.update_layout(
    title='Distribution of Association Rule Metrics',
    yaxis_title='Value',
    height=500
)
fig_metrics.show()

# Visualization 8: Heatmap - Correlation between Rule Metrics
corr_matrix = rules[metrics].corr()
fig_heatmap = px.imshow(corr_matrix,
                        title='Correlation Heatmap of Rule Metrics',
                        color_continuous_scale='RdBu_r',
                        text_auto=True,
                        aspect='auto')
fig_heatmap.update_layout(height=500)
fig_heatmap.show()

# ================================================================
# Advanced Algorithm 1: Sampling-Based Frequent Itemset Mining
# ================================================================
# Approach: Mine frequent itemsets on a random sample, then verify
# support on the full dataset.
#
# Benefits:
# - Reduced computational cost
# - Fast for exploratory analysis
# - Suitable for large datasets
#
# Trade-offs:
# - May miss border itemsets (items near support threshold)
# - Accuracy vs speed trade-off

def sampling_based_fim(df, min_support, sample_ratio=0.3, random_state=None):
    """
    Sampling-based approach: Mine frequent itemsets on a sample of transactions,
    then verify counts on full dataset.

    Args:
        df: Transaction DataFrame (one-hot encoded)
        min_support: Minimum support threshold
        sample_ratio: Proportion of transactions to sample (default: 0.3)
        random_state: Random seed for reproducibility

    Returns:
        DataFrame with verified frequent itemsets and their actual support
    """
    if random_state:
        random.seed(random_state)

    n_transactions = len(df)
    sample_size = int(n_transactions * sample_ratio)

    # Take random sample of transactions
    sampled_indices = random.sample(range(n_transactions), sample_size)
    sampled_df = df.iloc[sampled_indices]

    # Scale min_support for sample
    scaled_min_support = min_support / sample_ratio

    # First pass: find candidate itemsets in sample
    freq_itemsets_sample = fpgrowth(sampled_df, min_support=scaled_min_support, use_colnames=True)

    # Second pass: verify actual support on full dataset
    verified_itemsets = []
    for _, row in freq_itemsets_sample.iterrows():
        itemset = row['itemsets']
        # Calculate actual support on full dataset
        support = df[list(itemset)].all(axis=1).mean()
        if support >= min_support:
            verified_itemsets.append({'itemsets': itemset, 'support': support})

    return pd.DataFrame(verified_itemsets)


print("\n" + "="*60)
print("1. SAMPLING-BASED FREQUENT ITEMSET MINING")
print("="*60)

result_sampling = time_algorithm_execution(
    "Sampling-based FIM",
    sampling_based_fim,
    itemsets, minimum_support_threshold, sample_ratio=0.3, random_state=42
)
print_algorithm_result(result_sampling)
freq_sampling = result_sampling['result']


# ================================================================
# Advanced Algorithm 2: Hash-Based Pruning (DHP)
# ================================================================
# Direct Hashing and Pruning algorithm uses hash tables to reduce
# candidate generation in early passes.
#
# Benefits:
# - Reduces candidate itemsets early using hash buckets
# - Fewer candidates to count in subsequent passes
# - Faster than traditional Apriori for dense datasets
#
# Algorithm:
# - Pass 1: Count 1-itemsets + build hash table for 2-itemsets
# - Pass 2: Prune hash buckets + count 2-itemsets

def dhp_algorithm(transactions, min_support, hash_table_size=10000):
    """
    Direct Hashing and Pruning (DHP) algorithm.
    Uses hashing to reduce candidate generation in early passes.

    Args:
        transactions: List of transaction vectors (binary)
        min_support: Minimum support threshold
        hash_table_size: Size of hash table for bucketing (default: 10000)

    Returns:
        DataFrame with frequent 1-itemsets and 2-itemsets
    """
    n_transactions = len(transactions)

    # Pass 1: Count 1-itemsets and build hash table for 2-itemsets
    item_counts = defaultdict(int)
    hash_bucket = defaultdict(int)

    for transaction in transactions:
        items = [i for i, val in enumerate(transaction) if val]
        for item in items:
            item_counts[item] += 1

        # Hash pairs of items
        for pair in combinations(items, 2):
            # Hash function: (i * large_prime + j) % table_size
            hash_key = (min(pair) * 92821 + max(pair)) % hash_table_size
            hash_bucket[hash_key] += 1

    # Get frequent 1-itemsets
    min_count = int(min_support * n_transactions)
    freq_1_itemsets = {item for item, count in item_counts.items() if count >= min_count}

    # Prune hash buckets: keep only those that could contain frequent pairs
    pruned_buckets = {k: v for k, v in hash_bucket.items() if v >= min_count}

    # Pass 2: Count 2-itemsets using hash-based pruning
    pair_counts = defaultdict(int)

    for transaction in transactions:
        items = [i for i, val in enumerate(transaction) if val if i in freq_1_itemsets]
        for pair in combinations(sorted(items), 2):
            hash_key = (pair[0] * 92821 + pair[1]) % hash_table_size
            if hash_key in pruned_buckets:
                pair_counts[pair] += 1

    # Get frequent 2-itemsets
    freq_2_itemsets = {pair: count for pair, count in pair_counts.items() if count >= min_count}

    # Convert to DataFrame format (return 1 and 2-itemsets)
    results = []
    for item in freq_1_itemsets:
        results.append({'itemsets': frozenset([item]), 'support': item_counts[item] / n_transactions})
    for pair, count in freq_2_itemsets.items():
        results.append({'itemsets': frozenset(pair), 'support': count / n_transactions})

    return pd.DataFrame(results)


print("\n" + "="*60)
print("2. HASH-BASED PRUNING (DHP ALGORITHM)")
print("="*60)

# Convert DataFrame columns to item indices for DHP
col_to_idx = {col: i for i, col in enumerate(itemsets.columns)}
idx_to_col = {i: col for col, i in col_to_idx.items()}

# Run DHP with timing wrapper
def run_dhp_with_mapping(transactions, min_support, hash_table_size):
    freq_dhp = dhp_algorithm(transactions, min_support, hash_table_size)
    # Map indices back to column names for display
    freq_dhp_display = freq_dhp.copy()
    freq_dhp_display['itemsets'] = freq_dhp_display['itemsets'].apply(
        lambda x: frozenset(idx_to_col[i] for i in x)
    )
    return freq_dhp_display

result_dhp = time_algorithm_execution(
    "DHP (Hash-based Pruning)",
    run_dhp_with_mapping,
    transactions, minimum_support_threshold, 10000
)
print_algorithm_result(result_dhp)
freq_dhp_display = result_dhp['result']


# ================================================================
# Advanced Algorithm 3: Transaction Reduction
# ================================================================
# Apriori with transaction reduction removes transactions that cannot
# contribute to new frequent itemsets after each pass.
#
# Benefits:
# - Progressively reduces dataset size
# - Fewer transactions to scan in later passes
# - Memory-efficient for large datasets

def transaction_reduction_apriori(df, min_support):
    """
    Apriori with transaction reduction: Remove transactions that cannot
    contribute to new frequent itemsets after each pass.

    Args:
        df: Transaction DataFrame (one-hot encoded)
        min_support: Minimum support threshold

    Returns:
        DataFrame with all frequent itemsets
    """
    remaining_df = df.copy()
    k = 1
    all_freq_itemsets = []

    while True:
        # Find frequent k-itemsets
        freq_k = apriori(remaining_df, min_support=min_support, max_len=k+1, use_colnames=True)
        freq_k = freq_k[freq_k['itemsets'].apply(len) == k]

        if len(freq_k) == 0:
            break

        all_freq_itemsets.append(freq_k)

        # Get all frequent items in this pass
        freq_items = set()
        for itemset in freq_k['itemsets']:
            freq_items.update(itemset)

        # Reduce transactions: keep only those with frequent items
        remaining_df = remaining_df[list(freq_items)]

        # Remove transactions that are now empty
        remaining_df = remaining_df[remaining_df.sum(axis=1) > 0]

        print(f"Pass {k}: {len(freq_k)} frequent {k}-itemsets, transactions reduced to {len(remaining_df)}")

        k += 1

        if len(remaining_df) == 0:
            break

    if all_freq_itemsets:
        return pd.concat(all_freq_itemsets, ignore_index=True)
    return pd.DataFrame(columns=['itemsets', 'support'])


print("\n" + "="*60)
print("3. TRANSACTION REDUCTION APRIORI")
print("="*60)

result_transaction_reduction = time_algorithm_execution(
    "Transaction Reduction Apriori",
    transaction_reduction_apriori,
    itemsets, minimum_support_threshold
)
print_algorithm_result(result_transaction_reduction)
freq_transaction_reduction = result_transaction_reduction['result']


# ================================================================
# Advanced Algorithm 4: Vertical Format (ECLAT)
# ================================================================
# ECLAT uses vertical data format (tid-lists) instead of horizontal.
# Each item has a list of transaction IDs where it appears.
#
# Benefits:
# - Tid-list intersection is very fast (set operations)
# - Depth-first search reduces memory usage
# - Excellent for sparse datasets with many items
#
# Algorithm:
# - Build vertical format: item -> set of transaction IDs
# - Recursive DFS with tid-list intersections

def eclat_algorithm(df, min_support):
    """
    ECLAT: Equivalence Class Clustering and bottom-up Lattice Traversal.
    Uses vertical data format (tid-lists) instead of horizontal.

    Args:
        df: Transaction DataFrame (one-hot encoded)
        min_support: Minimum support threshold

    Returns:
        DataFrame with all frequent itemsets
    """
    n_transactions = len(df)

    # Build vertical format: item -> set of transaction IDs
    vertical_format = {}
    for col in df.columns:
        tid_list = set(df[df[col] == True].index)
        support = len(tid_list) / n_transactions
        if support >= min_support:
            vertical_format[frozenset([col])] = tid_list

    # Recursive function to mine frequent itemsets
    def mine_eclat(prefix, items, min_support_count):
        frequent_itemsets = []

        while items:
            # Get current item
            item, item_tidlist = items.pop(0)
            new_prefix = prefix | item
            support_count = len(item_tidlist)

            if support_count >= min_support_count:
                frequent_itemsets.append({
                    'itemsets': new_prefix,
                    'support': support_count / n_transactions
                })

                # Generate candidates by combining with remaining items
                new_items = []
                for other_item, other_tidlist in items:
                    new_itemset = item | other_item
                    new_tidlist = item_tidlist & other_tidlist

                    if len(new_tidlist) >= min_support_count:
                        new_items.append((new_itemset, new_tidlist))

                if new_items:
                    frequent_itemsets.extend(
                        mine_eclat(new_prefix, new_items, min_support_count)
                    )

        return frequent_itemsets

    # Convert to list format for processing
    items_list = list(vertical_format.items())
    min_count = int(min_support * n_transactions)

    result = mine_eclat(frozenset(), items_list, min_count)

    return pd.DataFrame(result)


print("\n" + "="*60)
print("4. VERTICAL FORMAT (ECLAT ALGORITHM)")
print("="*60)

result_eclat = time_algorithm_execution(
    "ECLAT (Vertical Format)",
    eclat_algorithm,
    itemsets, minimum_support_threshold
)
print_algorithm_result(result_eclat)
freq_eclat = result_eclat['result']


# ================================================================
# Advanced Algorithm 5: Dynamic Itemset Counting (DIC)
# ================================================================
# DIC interleaves counting of different size itemsets rather than
# processing in separate passes, reducing database scans.
#
# Benefits:
# - Fewer database scans than traditional Apriori
# - Candidates added dynamically during scanning
# - Faster convergence to frequent itemsets

def dic_algorithm(df, min_support):
    """
    Dynamic Itemset Counting (DIC): Interleave counting of different
    size itemsets rather than processing in separate passes.

    Args:
        df: Transaction DataFrame (one-hot encoded)
        min_support: Minimum support threshold

    Returns:
        DataFrame with all frequent itemsets
    """
    n_transactions = len(df)
    min_count = int(min_support * n_transactions)

    # Initialize with frequent 1-itemsets
    item_counts = defaultdict(int)
    for col in df.columns:
        item_counts[frozenset([col])] = df[col].sum()

    frequent_itemsets = {k: v for k, v in item_counts.items() if v >= min_count}
    candidate_itemsets = {k: v for k, v in item_counts.items() if v < min_count}

    # Generate initial 2-itemset candidates
    def generate_candidates(itemsets):
        candidates = set()
        itemsets_list = list(itemsets)
        for i in range(len(itemsets_list)):
            for j in range(i + 1, len(itemsets_list)):
                # Join step
                itemset1 = itemsets_list[i]
                itemset2 = itemsets_list[j]

                # Can join if they share k-1 items
                if len(itemset1 & itemset2) == len(itemset1) - 1:
                    new_itemset = itemset1 | itemset2
                    candidates.add(new_itemset)
        return candidates

    candidates_2 = generate_candidates(set(frequent_itemsets.keys()))
    for cand in candidates_2:
        candidate_itemsets[cand] = 0

    # First pass through data
    for _, row in df.iterrows():
        items_in_trans = set(df.columns[row])

        # Count all candidates
        for itemset in candidate_itemsets:
            if itemset.issubset(items_in_trans):
                candidate_itemsets[itemset] += 1

    # Move frequent candidates to frequent_itemsets
    new_frequent = {k: v for k, v in candidate_itemsets.items() if v >= min_count}
    frequent_itemsets.update(new_frequent)
    candidate_itemsets = {k: v for k, v in candidate_itemsets.items() if v < min_count}

    # Continue for 3-itemsets
    candidates_3 = generate_candidates(set(frequent_itemsets.keys()))
    candidates_3 = {c: 0 for c in candidates_3 if len(c) == 3}

    # Second pass
    for _, row in df.iterrows():
        items_in_trans = set(df.columns[row])
        for itemset in candidates_3:
            if itemset.issubset(items_in_trans):
                candidates_3[itemset] += 1

    # Final results
    result = []
    for itemset, count in frequent_itemsets.items():
        result.append({'itemsets': itemset, 'support': count / n_transactions})

    for itemset, count in candidates_3.items():
        if count >= min_count:
            result.append({'itemsets': itemset, 'support': count / n_transactions})

    return pd.DataFrame(result)


print("\n" + "="*60)
print("5. DYNAMIC ITEMSET COUNTING (DIC)")
print("="*60)

result_dic = time_algorithm_execution(
    "DIC (Dynamic Itemset Counting)",
    dic_algorithm,
    itemsets, minimum_support_threshold
)
print_algorithm_result(result_dic)
freq_dic = result_dic['result']


# ================================================================
# Advanced Algorithm 6: Partitioning
# ================================================================
# Partitioning divides the database into partitions, mines local
# frequent itemsets, then verifies globally.
#
# Benefits:
# - Guarantees completeness (all frequent itemsets found)
# - Only 2 database scans required
# - Memory-efficient for large datasets
#
# Algorithm:
# - Phase 1: Mine local frequent itemsets in each partition
# - Phase 2: Verify support on full dataset

def partitioning_apriori(df, min_support, n_partitions=5):
    """
    Partitioning: Divide database into partitions, mine local frequent
    itemsets, then verify globally. Guarantees all frequent itemsets are found.

    Args:
        df: Transaction DataFrame (one-hot encoded)
        min_support: Minimum support threshold
        n_partitions: Number of partitions to divide dataset (default: 5)

    Returns:
        DataFrame with verified frequent itemsets
    """
    n_transactions = len(df)
    partition_size = n_transactions // n_partitions

    # Collect all potential frequent itemsets from all partitions
    all_candidates = set()

    for i in range(n_partitions):
        start_idx = i * partition_size
        end_idx = start_idx + partition_size if i < n_partitions - 1 else n_transactions

        partition_df = df.iloc[start_idx:end_idx]

        # Lower support threshold for partition (scaled)
        # A local itemset with support s_local might have global support >= min_support
        partition_min_support = min_support * 0.5  # More lenient threshold

        local_freq = fpgrowth(partition_df, min_support=partition_min_support, use_colnames=True)

        for itemset in local_freq['itemsets']:
            all_candidates.add(itemset)

    print(f"Total candidates from all partitions: {len(all_candidates)}")

    # Second pass: verify actual support on full dataset
    verified_itemsets = []
    for itemset in all_candidates:
        support = df[list(itemset)].all(axis=1).mean()
        if support >= min_support:
            verified_itemsets.append({'itemsets': itemset, 'support': support})

    return pd.DataFrame(verified_itemsets)


print("\n" + "="*60)
print("6. PARTITIONING ALGORITHM")
print("="*60)

result_partitioning = time_algorithm_execution(
    "Partitioning Algorithm",
    partitioning_apriori,
    itemsets, minimum_support_threshold, 5
)
print_algorithm_result(result_partitioning)
freq_partitioning = result_partitioning['result']


# ========================================
# Comparison of All Algorithms
# ========================================
# This section compares all 9 algorithms (3 standard + 6 advanced)
# based on execution time and number of frequent itemsets found.

print("\n" + "="*60)
print("COMPARISON OF ALL ALGORITHMS")
print("="*60)

comparison_data = {
    'Algorithm': [
        'Apriori (Standard)',
        'FP-Growth',
        'FP-Max',
        'Sampling',
        'DHP (Hash-based)',
        'Transaction Reduction',
        'ECLAT (Vertical)',
        'DIC (Dynamic Counting)',
        'Partitioning'
    ],
    'Num_Frequent_Itemsets': [
        len(freq_itemsets_apriori),
        len(freq_itemsets_fpgrowth),
        len(freq_itemsets_fpmax),
        len(freq_sampling),
        len(freq_dhp_display),
        len(freq_transaction_reduction),
        len(freq_eclat),
        len(freq_dic),
        len(freq_partitioning)
    ],
    'Execution_Time_Seconds': [
        f"{result_apriori['execution_time']:.4f}",
        f"{result_fpgrowth['execution_time']:.4f}",
        f"{result_fpmax['execution_time']:.4f}",
        f"{result_sampling['execution_time']:.4f}",
        f"{result_dhp['execution_time']:.4f}",
        f"{result_transaction_reduction['execution_time']:.4f}",
        f"{result_eclat['execution_time']:.4f}",
        f"{result_dic['execution_time']:.4f}",
        f"{result_partitioning['execution_time']:.4f}"
    ],
    'Timestamp': [
        result_apriori['timestamp'],
        result_fpgrowth['timestamp'],
        result_fpmax['timestamp'],
        result_sampling['timestamp'],
        result_dhp['timestamp'],
        result_transaction_reduction['timestamp'],
        result_eclat['timestamp'],
        result_dic['timestamp'],
        result_partitioning['timestamp']
    ]
}

comparison_df = pd.DataFrame(comparison_data)
print("\n" + comparison_df.to_string(index=False))

# Summary statistics
print("\n" + "="*60)
print("TIMING SUMMARY")
print("="*60)
print(f"Fastest Algorithm: {comparison_df.loc[comparison_df['Execution_Time_Seconds'].astype(float).idxmin(), 'Algorithm']}")
print(f"Slowest Algorithm: {comparison_df.loc[comparison_df['Execution_Time_Seconds'].astype(float).idxmax(), 'Algorithm']}")

# ========================================
# Algorithm Performance Comparison Visualizations
# ========================================
# Create interactive visualizations to compare algorithm performance.

# Convert execution time to float for plotting
comparison_df['Execution_Time_Float'] = comparison_df['Execution_Time_Seconds'].astype(float)

# Visualization 9: Execution Time Comparison (Bar Chart)
bar_time = px.bar(comparison_df, x='Execution_Time_Float', y='Algorithm',
                  orientation='h',
                  title='Algorithm Execution Time Comparison',
                  color='Execution_Time_Float',
                  color_continuous_scale='RdYlGn_r',
                  text='Execution_Time_Float')
bar_time.update_traces(texttemplate='%{text:.3f}s', textposition='outside')
bar_time.update_layout(
    xaxis_title="Execution Time (seconds)",
    yaxis_title="Algorithm",
    showlegend=False,
    height=500
)
bar_time.show()

# Visualization 10: Number of Frequent Itemsets Found (Bar Chart)
bar_itemsets = px.bar(comparison_df, x='Num_Frequent_Itemsets', y='Algorithm',
                      orientation='h',
                      title='Number of Frequent Itemsets Found',
                      color='Num_Frequent_Itemsets',
                      color_continuous_scale='Blues',
                      text='Num_Frequent_Itemsets')
bar_itemsets.update_traces(texttemplate='%{text}', textposition='outside')
bar_itemsets.update_layout(
    xaxis_title="Number of Frequent Itemsets",
    yaxis_title="Algorithm",
    showlegend=False,
    height=500
)
bar_itemsets.show()

# Visualization 11: Time Efficiency Scatter Plot
scatter_efficiency = px.scatter(comparison_df, x='Execution_Time_Float', y='Num_Frequent_Itemsets',
                                text='Algorithm',
                                title='Algorithm Efficiency: Time vs Itemsets Found',
                                size='Execution_Time_Float',
                                color='Execution_Time_Float',
                                color_continuous_scale='Viridis')
scatter_efficiency.update_traces(textposition='top center')
scatter_efficiency.update_layout(
    xaxis_title="Execution Time (seconds)",
    yaxis_title="Number of Frequent Itemsets",
    height=600,
    showlegend=False
)
scatter_efficiency.show()

# ========================================
# End of Script
# ========================================
# This concludes the Frequent Pattern Mining implementation.
# All algorithms have been executed and compared.
# Results are available in the comparison DataFrame.
print("\n" + "="*60)
print("ANALYSIS COMPLETE")
print("="*60)
