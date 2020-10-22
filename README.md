# Vocab_Extender

<p style="text-align:right">
یه برنامه خیلی ساده برای کسایی که مثل من دامنه لغات محدودی دارن.
استفاده کردن از این برنامه خیلی ساده و راحته، فقط باید

`main.py`

رو اجرا بکنید
</p>

## استفاده کردن از لغات شخصی

1. یک دیکشنری از لغاتتون درست کنید به این شکل :

	{ 'word':'meaning' , 'word':'meaning' , ... }

1. حالا با شکل json این دیتا رو توی فایل **db** بنویسید

	```python
	import json
	
	lst= { 'word':'meaning' , 'word':'meaning' , ... }
	
	with open('','r',encoding='utf-8') as f:
		json.dump(lst,f)
	```

1. در قدم آخر باید فایل **rdb** رو پاک کنید

## توضیحات فایل ها

|file|description|
|:----:|:-----:|
|main.py|main program|
|config.py|main configurations of program|
|db.py|database controller|
|db|main database|
|rdb|additional information about database. remove this file to reset stats or when changing the main database|