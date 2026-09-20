from  dataset_maker import make_dataset as md
import analyzer as a
import pandas as pd


file = open(r'your_analyzed_data.txt', 'w', encoding='utf-8')


def out(text):
    file.write(text + '\n')
    print(text)


try:
    try:
        df = pd.read_csv(r'my_dataset.csv', index_col=0)

    except FileNotFoundError:
        md()
        df = pd.read_csv(r'my_dataset.csv', index_col=0)
        

    #Total trades per strategy
    cs = (a.count_strategies(df)).to_string(header=None)
    out(f'--- Total trades per strategy ---\n{cs}\n\n')

    #Analyze win rate
    input('press enter to show << Win rates >>...')
    out('--- Win rates --- \n')
    for dic in (a.analyze_win_rate(df)):
        wr = dic['Win Rate']
        tpc = dic['TP count']
        slc = dic['SL count']
        s = dic['Strategy']
        out(f"Strategy: {s} | Stop Loss: {slc} | Take Profit: {tpc} | Win Rate: {wr} % |\n\n")

    #Analyze exit rate
    input('press enter to show << Exit rates >>...')
    out('--- Exit rates --- \n')
    grp = a.tp_exit_rate(df)
    out('position : (count × andis) ÷ number of trades = exit rate % \n')
    for pos, rate in grp.items():
        out(f'{pos} : {rate:.1f} %\n')

    # Analyze best tps
    input('press enter to show << Best TPs >>...')
    out('--- Best TPs --- \n')
    lst = a.best_tp(df)
    for i in lst:
        out(i + '\n')

    # Max number of TPs
    input('press enter to show << Max TPs >>...')
    out('--- Max TPs --- \n')
    out(f'{a.tps(df)}\n')

    # Max number of SLs
    input('press enter to show << Max SLs >>...')
    out('--- Max SLs --- \n')
    out(f'{a.sls(df)}\n')

    out("--- That's it ---")

except Exception as e:
    out(f'!!! ERROR: {e}')

finally:
    file.close()
    input('press enter to Exit...')
