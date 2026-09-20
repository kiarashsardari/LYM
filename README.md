# 📊 Trading Data Analyzer

<div align="center">

![وضعیت پروژه](https://img.shields.io/badge/status-Active%20Development-yellow)
![نسخه](https://img.shields.io/badge/version-0.1.0--beta-blue)
![زبان](https://img.shields.io/badge/language-Python%203-blue?logo=python)

**ابزار تحلیل عملکرد استراتژی‌های معاملاتی بر پایه‌ی داده‌های تاریخی**

[گزارش باگ](../../issues/new) · [درخواست ویژگی](../../issues/new)

</div>

---

## ⚠️ توجه

> **این پروژه در حال حاضر قابل استفاده است، اما همچنان در حال توسعه فعال می‌باشد.**

---

## 📖 فهرست مطالب

- [درباره پروژه](#about)
- [ویژگی‌ها](#features)
- [پیش‌نیازها](#requirements)
- [نصب و راه‌اندازی](#installation)
- [نحوه استفاده](#usage)
- [ساختار پروژه](#structure)
- [فرمت داده ورودی](#input-format)
- [نمونه خروجی](#sample-output)

---

<a id="about"></a>
## 🎯 درباره پروژه

`Trading Data Analyzer` یک ابزار سبک و ماژولار با زبان `Python` است که داده‌های معاملاتی خام (شامل تاریخ، نوع پوزیشن و نام استراتژی) را دریافت کرده و شاخص‌های کلیدی عملکرد را استخراج می‌کند.

این پروژه برای معامله‌گران، توسعه‌دهندگان ربات‌های معاملاتی و تحلیل‌گران بازار طراحی شده تا به سرعت بفهمند:

- کدام استراتژی عملکرد بهتری دارد؟
- هر استراتژی چقدر نرخ برد دارد؟
- سرمایه‌ی معاملات در کدام سطوح `Take Profit` خارج می‌شود؟
- بهترین سطح `TP` برای هر استراتژی چیست؟
- بیشترین `SL` و `TP` اتفاق افتاده پشت سرهم چه تعداد بوده است؟

**چرا این پروژه؟**
- 📦 بدون نیاز به دیتابیس یا سرویس خارجی
- 🧩 معماری ماژولار و قابل توسعه (هر تحلیل در یک تابع مستقل)
- 📄 خروجی متنی خوانا در قالب گزارش

---

<a id="features"></a>
## ✨ ویژگی‌ها

- ✅ شمارش تعداد معاملات هر استراتژی
- ✅ محاسبه‌ی نرخ برد (Win Rate) به تفکیک استراتژی
- ✅ محاسبه‌ی نرخ خروج (Exit Rate) در هر سطح TP
- ✅ تعیین بهترین سطح Take Profit
- ✅ تعداد بیشترین `SL` و `TP` اتفاق افتاده پشت سرهم
- ✅ ذخیره‌ی گزارش کامل در فایل `txt`

---

<a id="requirements"></a>
## ⚙️ پیش‌نیازها

- [Python](https://www.python.org/) نسخه **3.9** یا بالاتر
- `pandas`
- `numpy`

---

<a id="installation"></a>
## 🚀 نصب و راه‌اندازی

### نصب وابستگی‌ها

```bash
pip install pandas numpy
```

---

<a id="usage"></a>
## 💡 نحوه استفاده

### مرحله ۱ — آماده‌سازی داده ورودی

یک فایل CSV با ستون‌های `date`، `position` و `strategy` در مسیر پروژه قرار دهید.

اگر داده‌ی واقعی ندارید، می‌توانید با اجرای اسکریپت زیر یک دیتاست نمونه بسازید:

```bash
python dataset_maker.py
```

### مرحله ۲ — اجرای تحلیل

فایل `run.py` را باز کرده و مسیر فایل CSV خود را در بخش زیر تنظیم کنید:

```python
df = pd.read_csv(r'path/to/your_dataset.csv', index_col=0)
```

سپس اجرا کنید:

```bash
python run.py
```

در طول اجرا با زدن **Enter** هر بخش از گزارش نمایش داده می‌شود.

### مرحله ۳ — مشاهده خروجی

گزارش نهایی به‌صورت خودکار در فایل زیر ذخیره می‌شود:

```
your_analyzed_data.txt
```

---

<a id="structure"></a>
## 📁 ساختار پروژه

```
trading-data-analyzer/
├── analyzer.py              # توابع اصلی تحلیل داده
├── dataset_maker.py         # ساخت دیتاست نمونه
├── run.py                   # اسکریپت اصلی اجرا
├── my_dataset.csv           # نمونه دیتاست
├── your_analyzed_data.txt   # نمونه خروجی تحلیل
└── README.md
```

### توضیح ماژول‌ها

| فایل | توضیح |
|------|-------|
| `analyzer.py` | شامل توابع `count_strategies`، `analyze_win_rate`، `tp_exit_rate` و `best_tp` |
| `dataset_maker.py` | تولید داده‌ی تصادفی برای تست پروژه |
| `run.py` | هماهنگ‌کننده و تولیدکننده‌ی گزارش خروجی |

---

<a id="input-format"></a>
## 📄 فرمت داده ورودی

فایل CSV باید حداقل شامل سه ستون زیر باشد:

| ستون | نوع | توضیح | مثال |
|------|-----|-------|------|
| `date` | تاریخ | تاریخ ثبت معامله | `2025-07-01` |
| `position` | رشته | نتیجه‌ی معامله | `SL`, `TP1`, `TP2`, ... |
| `strategy` | رشته | نام استراتژی | `A`, `B`, `C`, ... |

**نمونه:**

```csv
date,position,strategy
2025-07-01,TP3,C
2025-07-02,TP2,F
2025-07-03,SL,A
2025-07-04,SL,C
```

---

<a id="sample-output"></a>
## 📈 نمونه خروجی

```
--- Total trades per strategy ---
B    38
H    31
C    28
A    27
D    26
F    22
G    22
E    21

--- Win rates ---
Strategy: A | Stop Loss: 11 | Take Profit: 16 | Win Rate: 59.259 %
Strategy: B | Stop Loss: 12 | Take Profit: 26 | Win Rate: 68.421 %
...

--- Exit rates ---
position : (count × andis) ÷ number of trades = exit rate %
TP1  : 7.4 %
TP2  : 67.0 %
TP3  : 36.3 %
...

--- Best TPs ---
TP2
```

---

<div align="center">

ساخته شده با ❤️ برای معامله‌گران و تحلیل‌گران

</div>
