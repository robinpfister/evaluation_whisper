from jiwer import wer, mer
import numpy as np


for model in ['Word','Wispher_base', 'Wispher_tiny', 'Wispher_small']:
    print(f'Model: {model}')
    wer_all = []
    mer_all = []
    for size in ['k', 'm', 'l']:
        for number in range(1, 11, 1):
            #print(f'Analyse {size}{number}.txt')

            with open(f'{model}/{size}{number}.txt', 'r', encoding='utf-8') as file_model:
                string_transscribed = file_model.read()
                string_transscribed = string_transscribed.rstrip()
                if not 'Word':
                    string_transscribed = string_transscribed[1:]

            with open(f'Solution/{size}{number}.txt', 'r', encoding='utf-8') as file_sol:
                string_solution = file_sol.read()

            #print(repr(string_transscribed))
            #print(repr(string_solution))

            wer_stat = wer(string_solution, string_transscribed)
            #print(wer_stat)
            wer_all.append(wer_stat)
            mer_stat = mer(string_solution, string_transscribed)
            #print(mer_stat)
            mer_all.append(mer_stat)

    wer_stat = np.mean(wer_all)
    mer_stat = np.mean(mer_all)

    print(round(wer_stat, 2))
    print(round(mer_stat, 2))
