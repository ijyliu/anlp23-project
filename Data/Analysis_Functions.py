
# Functions useful for analyzing metrics

def means_table(data, metric):

    # Average combined_data metric by model, method, task
    avg_combined_data_metric = data[['model', 'method', 'task', metric]].groupby(['model', 'method', 'task']).agg(['mean'])[metric].reset_index()

    # Pivot table - column method should go wide
    avg_combined_data_metric_pivot = avg_combined_data_metric.set_index(['model', 'task', 'method']).unstack()
    #pivot_table(index=['model', 'task'], columns='method', values='accuracy_quality').reset_index()

    # Fix axis
    avg_combined_data_metric_pivot = avg_combined_data_metric_pivot.rename_axis([None, None], axis=1).reset_index()

    # Sort rows by task - gsm8k task first, then cw
    # Sort by model - text-davinci-003 first, then gpt4
    avg_combined_data_metric_pivot = avg_combined_data_metric_pivot.sort_values(by=['task', 'model'], ascending=[True, True])

    flattened_cols = [''.join(col).strip().replace('mean', '') for col in avg_combined_data_metric_pivot.columns.values]
    avg_combined_data_metric_pivot.columns = flattened_cols

    print(avg_combined_data_metric_pivot)

    # Order columns: direct_prompting, zero_shot_cot, ape_zero_shot_cot, tree_of_thought, self_refine, least_to_most, manual_few_shot, manual_cot
    avg_combined_data_metric_pivot = avg_combined_data_metric_pivot[['model', 'task', 'direct_prompting', 'zero_shot_cot', 'ape_zero_shot_cot', 'tree_of_thought', 'self_refine', 'least_to_most', 'manual_few_shot', 'manual_cot']]

    # Output to LaTeX
    avg_combined_data_metric_pivot.to_latex('../Output/avg_' + metric + '_pivot.tex', index=False)
