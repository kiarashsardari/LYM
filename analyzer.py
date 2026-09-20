# تعداد هر استراتژی
def count_strategies(df):
    try:
        # تعداد هر آیتم از ستون استراتژی
        c = df['strategy'].value_counts()
        return c
    except KeyError:
        # اگر ستون استراتژی موجود نبود ارور بده
        return('Error: Strategy column does not exist...')


# نرخ برد
def analyze_win_rate(df):

    # یک سری از هر استراتژی و تعداد اس ال های اون
    sl_size = (df[df['position'] == 'SL']).groupby('strategy').size().items()
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
        dic['Win Rate'] = float(f'{win_percent:.3f}')
        # تولید دیکشنری از تعداد اس ال های هر استراتژی
        sl_dic[strtgy] = sl_count
        main_lst.append(dic)
    ''' تعریف دوباره ی سری از تعداد تی پی های هر استراتژی
    چون با تبدیل اون به دیکشنری دیگه خالی میشه و برای همین مجبوریم دوباره تعریفش کنیم'''
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


def sort_key(p_r):
    return 0 if p_r[0] == 'SL' else int(p_r[0][2:])


# تعداد هر نوع پوزیشن
def position_count(df):
    return (df.groupby('position').size())


def tp_exit_rate(df):
    trades_count = (len(df['position']))
    p_count = position_count(df).items()
    pos_rate = {}
    for pos, count in p_count:
        andis = int(pos[2:]) if str(pos).startswith('TP') else 0
        pos_rate[pos] = ((count * andis)/trades_count)*100
    return dict(sorted(pos_rate.items(), key=sort_key))


def best_tp(df):
    grp = tp_exit_rate(df)
    m = max(grp.values())
    best_tps = [pos for pos, rate in grp.items() if rate == m]
    return (best_tps)


def positions_list(df):
    return (df['position']).tolist()


def tps(df):
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


def sls(df):
    positions = positions_list(df)
    lst = []
    n = 0
    for p in positions:

        if str(p).upper().strip() == 'SL':
            n+=1

        else:
            lst.append(n)
            n = 0
            
    if n != 0:
        lst.append(n)

    return max(lst) if lst else None



'''def analyze_win_rate(df):
    for s,groupe in grouped_strategies:
        print(df[df['strategy'].isin([s]) & df['position'].isin(['SL'])])
        print(groupe[groupe['position'] == 'SL'])
    print(len(df['position']))
    c1 = df['strategy']
    c = df['strategy'].value_counts()
    strategies_name = c.index
    strategies_count = c.iloc[:]
    positions = list(j for j in df['position'] if j!='SL')
    #.startswith('TP')
    for p in positions:
        for o in strategies_name:
            print(df[df['strategy'].isin([o]) & df['position'].isin([p])])
    print(df[c1.isin(['s']) & df['position'].isin(['SL'])])'''
