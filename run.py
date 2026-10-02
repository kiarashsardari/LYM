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


def get_address():
    with open('SAVED_ADDRESS.txt', "r", encoding="utf-8") as f:
        x = f.read()
        return x

def save_address(input_address):
    with open('SAVED_ADDRESS.txt', 'w', encoding='utf-8') as f:
        f.write(input_address.strip())


def out(*texts):
    for text in texts:
        print(text)
        file.write(str(text)+'\n')

def get_input():
    if os.path.exists('SAVED_ADDRESS.txt') and os.path.exists(get_address()):
        old_address = get_address()
        print(f'\nIf you want to analyze {old_address} again, type: << O >> ...\n')
        inp = input(r"Enter the address of your xlsx file (Sample: D:\trades\data\your_dataset): ")
        print('')            

        if inp.lower() == 'o':
            address = old_address

        else:
            address = inp if '.xlsx' in inp else inp+'.xlsx'

    else:
        address = input(r"Enter the address of your xlsx file (Sample: D:\trades\data\your_dataset): ")
        print('')
        address = address if '.xlsx' in address else address+'.xlsx'
    (pd.read_excel(address, index_col=False)).to_csv(r'your_dataset.csv',index=False, encoding='utf-8-sig')
    save_address(address)
    return pd.read_csv(r'your_dataset.csv',encoding='utf-8-sig')


def use_sample_or_exit():
    inp = input('File not found, do you want to use the sample dataset? (Y/N) : ')
    print('')
    if inp.upper() == 'Y':
        out("\nWe'll use the sample dataset... (my_dataset.csv) \n")
        md()
        return pd.read_csv(r'my_dataset.csv', index_col=False,encoding='utf-8-sig')
    else:
        out('Program closed...')
        raise SystemExit


def main(df):
    df = a.sdf(df)
    #Total trades per strategy
    cs = (a.count_strategies(df)).to_string(header=None)
    out(f'--- Total trades per strategy ---','\n')
    out('Strategy  Count','\n')
    out(cs,'\n')


    #Analyze Number of rewards
    input('press enter to show << Number of rewards >>...')
    print('')
    out('--- Number of rewards --- \n')
    grp = a.tp_rewards(df).items()
    out('Position rewards : count × andis = reward \n')
    for pos, rate in grp:
        if str(pos).startswith('tp'):
            out(f'{pos} rewards : {rate} \n')
        else:
            out(f'Number of {pos}s : {rate} \n')            

    # Analyze win rate with Optimized TPs
    input('press enter to show << Win rate with optimized TP(s) >>...')
    print('')
    out('--- Win rate with optimized TP(s) --- \n')
    out("Position : Win rate \n")
    btps_rates = a.analyze_win_rate_by_best_tp(df)
    if not btps_rates:
        out("There's no any TPs...\n")
    else:
        best_andis = min(list(map(a.find_andis, btps_rates.keys())))
        for btp, rate in btps_rates.items():
            if int(str(btp)[2:]) == best_andis:
                out(f"{btp} : {rate:.2f} %  << suggested\n")
            else:
                out(f"{btp} : {rate:.2f} %\n")
    
    #Analyze Win rates of each strategy with TP1
    input('press enter to show << Win rates of each strategy with TP1 >>...')
    print('')
    out('--- Win rates of each strategy with TP1 --- \n')
    out("Strategy | Stop Loss | Take Profit | Win Rate |\n\n")
    for dic in (a.analyze_win_rate_by_tp1(df)):
        wr = dic['Win Rate']
        tpc = dic['TP count']
        slc = dic['SL count']
        s = dic['Strategy']
        out(f"Strategy: {s} | Stop Loss: {slc} | Take Profit: {tpc} | Win Rate: {wr} % |\n\n")

    # Consecutive Wins
    input('press enter to show << Max consecutive wins >>...')
    print('')
    out('--- Max consecutive wins --- \n')
    out(f'{a.consecutive_wins(df)}\n')

    # Maximum consecutive losses
    input('press enter to show << Max consecutive losses >>...')
    print('')
    out('--- Max consecutive losses --- \n')
    out(f'{a.consecutive_losses(df)}\n')
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
        print('')
        file.close()
        if os.path.exists(r'your_dataset.csv'):
            os.remove(r'your_dataset.csv')


def exit_or_continue():
    global file
    while True:
        file = open(r'Analyze_For_You.txt', 'w', encoding='utf-8')
        run()
        inpt = input('Press enter to exit... (C to Continue) ')
        if inpt.lower() != 'c':
            print('\nbye...\n')
            raise SystemExit
    

if __name__ == '__main__':
    exit_or_continue()
