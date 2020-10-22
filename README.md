# Vocab_Extender

<p style="text-align:right">

یه برنامه خیلی ساده برای کسایی که مثل من دامنه لغات محدودی دارن

رو اجرا کنید `main.py` استفاده کردن از این برنامه هم خیلی راحته و فقط باید فایل
</p>

## استفاده کردن از لغات شخصی

1. یک دیکشنری از لغاتتون درست کنید به این شکل

	{ 'word':'meaning' , 'word':'meaning' , ... }

1. بنویسید `db` این دیتا رو تو فایل *json* حالا با شکل

	```python
	import json
	
	lst= { 'word':'meaning' , 'word':'meaning' , ... }
	
	with open('','r',encoding='utf-8') as f:
		json.dump(lst,f)
	```

1. <p style="text-align:left">رو پاک کنید **rdb** در قدم آخر باید فایل </p>

## توضیحات فایل ها

|file|description|
|:----:|:-----:|
|main.py|main program|
|config.py|main configurations of program|
|db.py|database controller|
|db|main database|
|rdb|additional information about database. remove this file to reset stats or when changing the main database|