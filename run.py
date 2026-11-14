# ایمپورت کتابخانه های موردنیاز
import os
try:
    from  dataset_maker import make_dataset as md
    import analyzer as a
except ImportError as e:
    print(f"The main program files were not found.\n\nPlease ensure that the files have been fully downloaded\nor are located in the correct path.\n\nThis is a file which had not been found: {e.name}\n\n")
    input('press enter to exit...')
    print('')
    raise SystemExit

try:
    import pandas as pd
    import numpy
except ImportError as e :
    print(f"Required library not installed: {e.name}\n\nInstall it with:  pip install {e.name}\n\n\n")
    input('press enter to exit...')
    print('')
    raise SystemExit


# کلاس کار با فایل های موردنیاز در برنامه
class AddressFile:
    def __init__(self, input_address):
        self.input_address = input_address

    # ذخیره آدرس
    def save(self):
        input_address = self.input_address
        with open('SAVED_ADDRESS.txt', 'w', encoding='utf-8') as f:
            f.write(input_address.strip())

    # خواندن آدرس قبلی از فایل
    @staticmethod
    def read_address():
        with open('SAVED_ADDRESS.txt', "r", encoding="utf-8") as f:
            x = f.read()
            return x


# کلاس تحلیل و آنالیز دیتافریم و ذخیره نتایج
class Analyze:
    # پرینت و سیو کردن همزمان در فایل تکست گزارش 
    def _sprint(self, *texts):
        for text in texts:
            print(text)
            file.write(str(text)+'\n')

    # تحلیل دیتافریم و چاپ و ذخیره نتایج
    def analyze_trades(self, df):
        _sprint = self._sprint
        _sprint('--- Analyze For You ---\n')
        dfs = a.DFSettings(df)
        clc = a.Calculator(df)
        df = dfs.df

        #Total trades per strategy
        cs = clc.count_strategies().to_string(header=None)
        _sprint(f'--- Total trades per strategy ---','\n')
        _sprint('Strategy  Count','\n')
        _sprint(cs,'\n')

        #Analyze Number of rewards
        input('press enter to show << Number of rewards >>...')
        print('')
        _sprint('--- Number of rewards --- \n')
        grp = clc.tp_rewards().items()
        _sprint('Position rewards : count × andis = reward \n')
        for pos, rate in grp:
            if str(pos).startswith('TP'):
                _sprint(f'{pos} rewards : {rate} \n')
            else:
                _sprint(f'Number of {pos}s : {rate} \n')            

        # Analyze win rate with Optimized TPs
        input('press enter to show << Win rate with optimized TP(s) >>...')
        print('')
        _sprint('--- Win rate with optimized TP(s) --- \n')
        _sprint("Position : Win rate \n")
        btps_rates = clc.analyze_win_rate_by_best_tp()
        if not btps_rates:
            _sprint("There's no any TPs...\n")
        else:
            best_andis = min(list(map(dfs.find_andis, btps_rates.keys())))
            for btp, rate in btps_rates.items():
                if int(str(btp)[2:]) == best_andis:
                    _sprint(f"{btp} : {rate:.2f} %  << suggested\n")
                else:
                    _sprint(f"{btp} : {rate:.2f} %\n")
        
        #Analyze Win rates of each strategy with TP1
        input('press enter to show << Win rates of each strategy with TP1 >>...')
        print('')
        _sprint('--- Win rates of each strategy with TP1 --- \n')
        _sprint("Strategy | Stop Loss | Take Profit | Win Rate |\n\n")
        for dic in (clc.analyze_win_rate_by_tp1()):
            wr = dic['Win Rate']
            tpc = dic['TP count']
            slc = dic['SL count']
            s = dic['Strategy']
            _sprint(f"Strategy: {s} | Stop Loss: {slc} | Take Profit: {tpc} | Win Rate: {wr} % |\n\n")

        # Consecutive Wins
        input('press enter to show << Max consecutive wins >>...')
        print('')
        _sprint('--- Max consecutive wins --- \n')
        _sprint(f'{clc.consecutive_wins()}\n')

        # Maximum consecutive losses
        input('press enter to show << Max consecutive losses >>...')
        print('')
        _sprint('--- Max consecutive losses --- \n')
        _sprint(f'{clc.consecutive_losses()}\n')
        _sprint("--- Good luck! ---")


# کلاس اصلی برنامه و تعامل با کاربر و اجرای برنامه
class Main:
    # خواندن دیتافریم ورودی از کاربر و تبدیل آن به فرمت csv
    def get_input_df(self):
        if os.path.exists('SAVED_ADDRESS.txt') and os.path.exists(AddressFile.read_address()): # درصورتی که فایل آدرس های ذخیره شده وجود داشت و محتوای آن هم به عنوان یک آدرس معتبر بود و وجود داشت
            old_address = AddressFile.read_address()
            print(f'\nIf you want to analyze {old_address} again, type: << P >> ...\n')
            print(f'\nIf you need to analyze sample dataset, type: << S >> ...\n')
            inp = input(r"Enter the address of your << .xlsx >> file (example: D:\trades\data\your_dataset): ")
            print('')
            inp = inp.strip()
            if inp.lower() == 'p': # دستور پردازش آدرس قبلی
                address = old_address
            elif inp.lower() == 's': # دستور استفاده از دیتاست نمونه
                return 's'
            else: # درصورت وارد کردن آدرس جدید
                address = inp if '.xlsx' in inp else inp+'.xlsx'  # افزودن پسوند ایکس ال اس ایکس به ورودی کاربر درصورت عدم وجود

        else: # درصورت عدم وجود آدرس یا آدرس صحیح گذشته 
            print(f'\nIf you need to analyze sample dataset, type: << S >> ...\n')
            inp = input(r"Enter the address of your << .xlsx >> file (example: D:\trades\data\your_dataset): ")
            print('')
            inp = inp.strip()
            if inp.lower() == 's': # دستور استفاده از دیتاست نمونه
                return 's'
            address = inp if '.xlsx' in inp else inp+'.xlsx'
            
        # صحت سنجی آدرس
        if os.path.exists(address):
            pd.read_excel(address, index_col=False).to_csv(r'your_dataset.csv',index=False, encoding='utf-8-sig')
        else:
            raise ValueError ("invalid path or no xlsx file in this path")
        AddressFile(address).save()
        return pd.read_csv(r'your_dataset.csv',encoding='utf-8-sig')


    # اجرای برنامه اصلی و تحلیل دیتافریم
    def main(self):
        try:
            df = self.get_input_df()
            if isinstance(df, str):
                df = md()
            Analyze().analyze_trades(df)
            print('\nYou can see this analyze again in this file : << Analyze_For_You.txt >>\n')

        finally:
            print('')
            file.close()
            if os.path.exists(r'your_dataset.csv'):
                os.remove(r'your_dataset.csv')


    # اجرای برنامه و حلقه برای ادامه یا خروج
    def run(self):
        global file
        while True:
            file = open(r'Analyze_For_You.txt', 'w', encoding='utf-8')
            self.main()
            inpt = input('Press enter to exit... (C to Continue) ')
            if inpt.lower() != 'c':
                print('\nbye...\n')
                raise SystemExit


if __name__ == '__main__':
    Main().run()
