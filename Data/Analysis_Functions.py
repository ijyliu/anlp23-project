
# Functions useful for analyzing metrics

# import pandas as pd

# def means_table(data, metric):

#     # Average combined_data metric by model, method, task
#     avg_combined_data_metric = data[['model', 'method', 'task', 'Model', 'Task', 'Method', metric]].groupby(['model', 'method', 'task', 'Model', 'Task', 'Method']).agg(['mean', 'var'])[metric].reset_index()

#     # Merge on inference data
#     all_inference = pd.read_excel('all_inference.xlsx')
#     # Filter to where metric = metric
#     metric_inference = all_inference[all_inference['metric'] == metric]
#     # Merge with avg_accuracy_quality_with_variance
#     avg_combined_data_metric = pd.merge(avg_combined_data_metric, metric_inference, how = 'left', on = ['model', 'method', 'task'])

#     # Add stars column
#     avg_combined_data_metric['stars'] = avg_combined_data_metric['Significant at 95%'].apply(lambda x: '*' if x == 'Yes' else '')

#     # Pivot table - column method should go wide
#     avg_combined_data_metric_pivot = avg_combined_data_metric.set_index(['model', 'task', 'method']).unstack()
#     #pivot_table(index=['model', 'task'], columns='method', values='accuracy_quality').reset_index()

#     # Fix axis
#     avg_combined_data_metric_pivot = avg_combined_data_metric_pivot.rename_axis([None, None], axis=1).reset_index()

#     # Sort rows by task - gsm8k task first, then cw
#     # Sort by model - text-davinci-003 first, then gpt4
#     avg_combined_data_metric_pivot = avg_combined_data_metric_pivot.sort_values(by=['task', 'model'], ascending=[True, True])

#     flattened_cols = [''.join(col).strip().replace('mean', '') for col in avg_combined_data_metric_pivot.columns.values]
#     avg_combined_data_metric_pivot.columns = flattened_cols

#     print(avg_combined_data_metric_pivot)

#     # Order columns: direct_prompting, zero_shot_cot, ape_zero_shot_cot, tree_of_thought, self_refine, least_to_most, manual_few_shot, manual_cot
#     avg_combined_data_metric_pivot = avg_combined_data_metric_pivot[['model', 'task', 'direct_prompting', 'zero_shot_cot', 'ape_zero_shot_cot', 'tree_of_thought', 'self_refine', 'least_to_most', 'manual_few_shot', 'manual_cot']]

#     # Output to LaTeX
#     avg_combined_data_metric_pivot.to_latex('../Output/avg_' + metric + '_pivot.tex', index=False)
