def sdf(df):
    df = df.map(lambda x: x.upper().strip()  if isinstance(x, str) else x)
    df.columns = [
    c.lower().strip() if isinstance(c, str) else c
    for c in df.columns
]
    return df


# تعداد هر استراتژی
def count_strategies(df):
    # تعداد هر آیتم از ستون استراتژی
    c = df['strategy'].value_counts()
    return c

# نرخ برد
def analyze_win_rate_by_tp1(df):
    # یک سری از هر استراتژی و تعداد اس ال های اون
    sl_size = (df[df['position'] == 'sl']).groupby('strategy').size().items()
    # یک دیکشنری از هر استراتژی و تعداد تی پی های اون
    tp_size = dict((df[df['position'].str.startswith('TP')]).groupby('strategy').size().items())
    #دیکشنری خالی برای تولید دیکشنری از تعداد اس ال های هر استراتژی
    sl_dic = {}
    main_lst = []
    # اسم هر استراتژی و تعداد اس ال های اون
    for strtgy,sl_count in sl_size:
        dic = {}
        # تعداد تی پی ها . اگه اسم استراتژی توی دیکشنری تی پی ها نبود یعنی اون استراتژی تی پی نداشته و 0 میشه
        tp_count = tp_size[strtgy] if strtgy in tp_size else 0
        # محاسبه درصد برد
        win_percent = (tp_count/(sl_count + tp_count)*100)
        # ذخیره کردن معیار های یک استراتژی در دیکشنری
        dic['Strategy'] = strtgy
        dic['SL count'] = int(sl_count)
        dic['TP count'] = tp_count
        dic['Win Rate'] = float(f'{win_percent:.2f}')
        # تولید دیکشنری از تعداد اس ال های هر استراتژی
        sl_dic[strtgy] = sl_count
        main_lst.append(dic)
    tp_size_items = (df[df['position'].str.startswith('TP')]).groupby('strategy').size().items()
    main_lst2 = []
    # اسم هر استراتژی و تعداد تی پی های اون
    for sgy,tp_count in tp_size_items:
        # بررسی کن اگر اسم استراتژی ما توی دیکشنری 
        if sgy not in sl_dic:
            dic2 = {}
            dic2['Strategy'] = sgy
            dic2['SL count'] = 0
            dic2['TP count'] = int(tp_count)
            dic2['Win Rate'] = 100
            main_lst2.append(dic2)
    # خروجی : یک لیست شامل چند دیکشنری
    return main_lst + main_lst2


# کلید مرتب سازی
def sort_key(p_r):
    return 0 if p_r[0] == 'SL' else int(p_r[0][2:])


# تعداد هر نوع پوزیشن
def positions_count(df):
    return (df.groupby('position').size())


# محاسبه تعداد اس ال ها و محاسبه ریوارد های هر تی پی 
def tp_rewards(df):
    p_count = positions_count(df).items()
    pos_rate = {}
    for pos, count in p_count:
        andis = find_andis(pos)
        pos_rate[pos] = (count * andis)
    return dict(sorted(pos_rate.items(), key=sort_key))


# یافتن تی پی بهینه براساس پرتعداد بودن و اندیس کوچکتری داشتن
def optimized_tp(df):
    rewards_tps = (tp_rewards(df))
    if 'SL' in rewards_tps:
        del rewards_tps['SL']
    if not rewards_tps:
        return (dict())
    rewards = (rewards_tps.values())
    m = max(rewards)
    best_tps = {pos : reward 
                for pos, reward in rewards_tps.items() if reward == m}
    return (best_tps)


# اندیس پوزیشن ورودی 
def find_andis(position):    
    return int(position[2:]) if str(position).startswith('TP') else 1


# تعداد تی پی های بهینه و تی پی های بزرگتر از اون
def count_best_tps(df):
    tps_counts = {}
    tps_rewards = optimized_tp(df)
    if not tps_rewards:
        return {}

    for tp, _ in tps_rewards.items():
        andis = find_andis(tp)
        tdf = df[df['position'] != 'SL']
        best_df = tdf[((tdf['position']).str.startswith('TP')) & ((tdf['position']).str[2:].astype(int)>=andis)]
        tps_counts[tp] = int(best_df['position'].value_counts().sum())

    return tps_counts


# محسابه وین ریت بر اساس تی پی های بهینه
def analyze_win_rate_by_best_tp(df):
    trades_count = len(df)
    tps_rates = {}
    if trades_count == 0:
        return {}
    tps_counts = count_best_tps(df)
    if not tps_counts:
        return {}
    for tp, count in tps_counts.items():
        tps_rates[tp] = (count/trades_count)*100
    return tps_rates


# لیست پوزیشن ها 
def positions_list(df):
    return (df['position']).tolist()


# تعداد بیشترین تی پی های متوالی 
def consecutive_wins(df):
    positions = positions_list(df)
    lst = []
    n = 0
    for p in positions:

        if str(p).startswith('TP'):
            n+=1

        else:
            lst.append(n)
            n = 0
            
    if n != 0:
        lst.append(n)

    return max(lst) if lst else None


# تعداد بیشترین اس ال های متوالی 
def consecutive_losses(df):
    positions = positions_list(df)
    lst = []
    n = 0
    for p in positions:

        if str(p) == 'SL':
            n+=1

        else:
            lst.append(n)
            n = 0
            
    if n != 0:
        lst.append(n)

    return max(lst) if lst else None
