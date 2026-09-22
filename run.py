from  dataset_maker import make_dataset as md
import analyzer as a
import pandas as pd


file = open(r'your_analyzed_data.txt', 'w', encoding='utf-8')


def out(text):
    file.write(text + '\n')
    print(text)


try:
    try:
        address = input(r"Enter the address of your xlsx file (Sample: D:\trades\data\my_dataset.xlsx): ")
        (pd.read_excel(address, index_col=0)).to_csv(r'dataset.csv', encoding='utf-8-sig')
        df = pd.read_csv(r'dataset.csv')

    except FileNotFoundError:
        inp = input('File not found, do you want to use the sample dataset? (Y/N) : ')
        if inp.upper() == 'Y':
            out("\nWe'll use the sample dataset... (my_dataset.csv) \n")
            md()
            df = pd.read_csv(r'my_dataset.csv', index_col=0)
    #(address).to_csv()
    #Total trades per strategy
    cs = (a.count_strategies(df)).to_string(header=None)
    out(f'--- Total trades per strategy ---\n{cs}\n\n')

    #Analyze win rate
    input('press enter to show << Win rates >>...')
    out('--- Win rates --- \n')
    for dic in (a.analyze_win_rate_tp1(df)):
        wr = dic['Win Rate']
        tpc = dic['TP count']
        slc = dic['SL count']
        s = dic['Strategy']
        out(f"Strategy: {s} | Stop Loss: {slc} | Take Profit: {tpc} | Win Rate: {wr} % |\n\n")

    #Analyze Number of rewards
    input('press enter to show << Number of rewards >>...')
    out('--- Number of rewards --- \n')
    grp = a.tp_exit_rate(df).items()
    out('position : count × andis = exit rate \n')
    for pos, rate in grp:
        if str(pos).startswith('TP'):
            out(f'{pos} rewards : {rate} \n')
        else:
            out(f'Number of {pos}s : {rate} \n')            

    # Analyze Optimized TPs
    input('press enter to show << Optimized TPs >>...')
    out('--- Optimized TPs --- \n')
    lst = a.best_tp(df)
    for i in lst:
        if i != 'SL':
            out(i + '\n')

    # Consecutive Wins
    input('press enter to show << Max consecutive wins >>...')
    out('--- Max consecutive wins --- \n')
    out(f'{a.tps(df)}\n')

    # Maximum consecutive losses
    input('press enter to show << Max consecutive loses >>...')
    out('--- Max consecutive losses --- \n')
    out(f'{a.sls(df)}\n')
    out("--- Good luck! ---")

except NameError:
    pass
        
except Exception as e:
    out(f'!!! ERROR: {e}')
    raise
finally:
    input('press enter to Save & Exit...')
    file.close()
