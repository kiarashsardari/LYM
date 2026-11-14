<div align="center">

# LYM

### تحلیل‌گر استراتژی معاملاتی

**ابزاری پایتونی برای تحلیل عملکرد استراتژی‌های معاملاتی از روی فایل‌های اکسل**
**گزارشی خوانا از نرخ برد، توزیع پاداش‌ها، سطوح بهینه‌ی حد سود و رکورد برد/باخت‌های متوالی — از طریق خط فرمان**

<br>

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![openpyxl](https://img.shields.io/badge/openpyxl-3.0%2B-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)](https://openpyxl.readthedocs.io/)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-4CAF50?style=for-the-badge)]()
[![Repository](https://img.shields.io/badge/Repository-LYM-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/kiarashsardari/LYM)

</div>

---

<div align="center">

## فهرست مطالب

[ویژگی‌ها](#features) • [ساختار پروژه](#project-structure) • [نصب](#installation) • [شروع سریع](#quick-start)

[دیتاست نمونه](#sample-dataset) • [نمونه خروجی](#output-example) • [توابع](#functions-reference) • [نحوه کار](#how-it-works) • [نکات مهم](#notes)

</div>

---

<a id="features"></a>
## ویژگی‌ها

| ویژگی | توضیح |
|:---|:---|
| **نرمال‌سازی داده** | مقادیر رشته‌ای را به حروف بزرگ و نام ستون‌ها را به حروف کوچک تبدیل می‌کند |
| **شمارش استراتژی‌ها** | تعداد کل معاملات هر استراتژی را محاسبه می‌کند |
| **محاسبه پاداش** | پاداش هر پوزیشن را با فرمول `تعداد × اندیس` محاسبه می‌کند |
| **تشخیص TP بهینه** | سطح حد سودی را پیدا می‌کند که بیشترین پاداش کل را دارد |
| **نرخ برد بر اساس TP** | نرخ برد هر استراتژی را با در نظر گرفتن مجموع همه‌ی TPها در برابر SL محاسبه می‌کند |
| **نرخ برد بر اساس TP بهینه** | نرخ برد را بر اساس بهترین سطح حد سود محاسبه می‌کند |
| **برد/باخت‌های متوالی** | طولانی‌ترین رکورد TP متوالی و SL متوالی را پیدا می‌کند |
| **خواندن فایل اکسل** | فایل‌های `.xlsx` را مستقیماً می‌خواند و به CSV موقت تبدیل می‌کند |
| **دیتاست نمونه** | در صورت نبود فایل ورودی، یک دیتاست نمونه ۳۶۵ روزه می‌سازد |
| **ذخیره خودکار آدرس** | مسیر آخرین فایل اکسل را برای تحلیل سریع بعدی به خاطر می‌سپارد |
| **خروجی گزارش** | کل تحلیل را در فایل `Analyze_For_You.txt` ذخیره می‌کند |
| **اجرای مرحله‌به‌مرحله** | بین بخش‌های تحلیل، با زدن `Enter` نتایج بعدی نمایش داده می‌شوند |

---

<a id="project-structure"></a>
## ساختار پروژه

```text
LYM/
│
├── run.py                →  نقطه ورود اصلی — مدیریت ورودی، تحلیل و خروجی
├── analyzer.py           →  کلاس‌های DFSettings و Calculator برای تحلیل
├── dataset_maker.py      →  تولید دیتاست نمونه CSV برای تست
├── requirements.txt      →  فهرست پیش‌نیازهای پایتونی پروژه
├── SAMPLE_Excel.xlsx     →  نمونه فایل اکسل ورودی
│
├── SAVED_ADDRESS.txt     →  خودکار ساخته می‌شود — مسیر آخرین فایل اکسل
├── sample_dataset.csv    →  خودکار ساخته می‌شود — دیتاست نمونه
├── your_dataset.csv      →  موقت — تبدیل‌شده از فایل اکسل ورودی
├── Analyze_For_You.txt   →  خروجی — گزارش کامل تحلیل
└── README.md             →  همین فایل