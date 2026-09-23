import os
try:
    from  dataset_maker import make_dataset as md
    import analyzer as a
except ImportError as e:
    print(f"The main program files were not found.\nPlease ensure that the files have been fully downloaded\nor are located in the correct path.\nThis is a file which had not been found: {e.name}")
    input('press enter to exit...')
    print('')
    raise SystemExit

try:
    import pandas as pd
    import numpy
except ImportError as e :
    print(f"Required library not installed: {e.name}\nInstall it with:  pip install {e.name}")
    input('press enter to exit...')
    print('')
    raise SystemExit


file = open(r'Analyze_For_You.txt', 'w', encoding='utf-8')

def get_address():
    with open('SAVED_ADDRESS.txt', "r", encoding="utf-8") as f:
        x = f.read()
        return x

def save_address(input_address):
    with open('SAVED_ADDRESS.txt', 'w', encoding='utf-8') as f:
        f.write(input_address.strip())


def out(text):
    file.write(text + '\n')
    print(text)


def get_input():
    if os.path.exists('SAVED_ADDRESS.txt') and os.path.exists(get_address()):
        old_address = get_address()
        print(f'\nIf you want to analyze {old_address} again, type: << old >> ...\n')
        inp = input(r"Enter the address of your xlsx file (Sample: D:\trades\data\your_dataset): ")
        print('')            

        if inp.lower() == 'old':
            address = old_address

        else:
            address = inp if '.xlsx' in inp else inp+'.xlsx'

    else:
        address = input(r"Enter the address of your xlsx file (Sample: D:\trades\data\your_dataset): ")
        print('')
        address = address if '.xlsx' in address else address+'.xlsx'
    (pd.read_excel(address, index_col=False)).to_csv(r'your_dataset.csv',index=False, encoding='utf-8-sig')
    save_address(address)
    return pd.read_csv(r'your_dataset.csv')


def use_sample_or_exit():
    inp = input('File not found, do you want to use the sample dataset? (Y/N) : ')
    print('')
    if inp.upper() == 'Y':
        out("\nWe'll use the sample dataset... (my_dataset.csv) \n")
        md()
        return pd.read_csv(r'my_dataset.csv', index_col=False)
    else:
        out('Program closed...')
        raise SystemExit


def main(df):
    #Total trades per strategy
    cs = (a.count_strategies(df)).to_string(header=None)
    out(f'--- Total trades per strategy ---\n{cs}\n\n')

    #Analyze win rate
    input('press enter to show << Win rates >>...')
    print('')
    out('--- Win rates --- \n')
    for dic in (a.analyze_win_rate_tp1(df)):
        wr = dic['Win Rate']
        tpc = dic['TP count']
        slc = dic['SL count']
        s = dic['Strategy']
        out(f"Strategy: {s} | Stop Loss: {slc} | Take Profit: {tpc} | Win Rate: {wr} % |\n\n")

    #Analyze Number of rewards
    input('press enter to show << Number of rewards >>...')
    print('')
    out('--- Number of rewards --- \n')
    grp = a.tp_rewards(df).items()
    out('position : count × andis = exit rate \n')
    for pos, rate in grp:
        if str(pos).startswith('TP'):
            out(f'{pos} rewards : {rate} \n')
        else:
            out(f'Number of {pos}s : {rate} \n')            

    # Analyze Optimized TPs
    input('press enter to show << Optimized TPs >>...')
    print('')
    out('--- Optimized TPs --- \n')
    lst = a.best_tp(df)
    for i in lst:
        if i != 'SL':
            out(f'{i}\n')

    # Consecutive Wins
    input('press enter to show << Max consecutive wins >>...')
    print('')
    out('--- Max consecutive wins --- \n')
    out(f'{a.tps(df)}\n')

    # Maximum consecutive losses
    input('press enter to show << Max consecutive losses >>...')
    print('')
    out('--- Max consecutive losses --- \n')
    out(f'{a.sls(df)}\n')
    out("--- Good luck! ---")


def run():
    try:
        try:
            df = get_input()

        except FileNotFoundError:
            df = use_sample_or_exit()

        main(df)
        print('\nYou can see this analyze again in this file : << Analyze_For_You.txt >>\n')

    finally:
        input('\npress enter to Save & Exit...')
        print('')

        file.close()

if __name__ == '__main__':
    run()
