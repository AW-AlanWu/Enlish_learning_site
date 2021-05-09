# Enlish_learning_site

## 當前進度

### view:
1. 首頁:
	1. 流量計數(session語法
	2. 登出入(日後處理
	3. 連至其他網頁的連結(html部分
	4. 創站感言(html部分
2. 字集創建區
	1. 瀏覽當前字集以及單字
		>> 分三層瀏覽：第一層字集、第二層單字、第三層解釋(已完成
	2. 增加或是刪減字集或是單字或是解釋
		>> 增加和刪減和編輯功能都用按鈕實作(已完成所有功能，只是內部view的安排和混亂的參數情形還是有待設計
>> 以上兩個優先完成
3. 測驗區
4. 成績查看區

### template:
>> 計畫以bootstrap美化網頁
1. html:
	1. 目前主要是依靠template的render，加上部分簡單的標籤完成的，唯一較複雜的是傳送資料的表單和結合javascript的按鈕
	>> 預計在完成所有主要功能後才會進行美化排版的處理
2. javascript:
	1. 為了能夠不讓網頁頁面太繁雜，因此在實作刪減及編輯功能時利用javascript動態產生表單傳輸資料，結合了html的按鈕
	>> 預計日後的測驗區也會採用javascript實作，不過到時候前後台資料傳輸的方式還正在考慮(目前傾向於Django REST framework)

### model:
單字儲存part(實作完成)：
>> 字集(set_name)->單字(english)->解釋(中、英例句,中譯,詞性)

使用者關聯part(尚未實作)：
>> 歷史成績(答對、錯誤單字,所用字集,字集正確、錯誤數)

## 目前網站外觀

### 首頁

![alt text](https://github.com/AW-AlanWu/Enlish_learning_site/blob/master/images/1.png)

>> (重新刷新首頁)
![alt text](https://github.com/AW-AlanWu/Enlish_learning_site/blob/master/images/2.png)

>> (多次刷新首頁後)
![alt text](https://github.com/AW-AlanWu/Enlish_learning_site/blob/master/images/3.png)

### 字集創建區

>> (無字集)
![alt text](https://github.com/AW-AlanWu/Enlish_learning_site/blob/master/images/4.png)

>> (有一字集)
![alt text](https://github.com/AW-AlanWu/Enlish_learning_site/blob/master/images/5.png)

### 單字創建區

>> (無單字)
![alt text](https://github.com/AW-AlanWu/Enlish_learning_site/blob/master/images/6.png)

>> (有一單字)
![alt text](https://github.com/AW-AlanWu/Enlish_learning_site/blob/master/images/7.png)

### 解釋創建區

>> (無解釋)
![alt text](https://github.com/AW-AlanWu/Enlish_learning_site/blob/master/images/8.png)

>> (有一解釋)
![alt text](https://github.com/AW-AlanWu/Enlish_learning_site/blob/master/images/9.png)

<!--admin_site：
Username=admin
Password=zaq1xsw2-->
