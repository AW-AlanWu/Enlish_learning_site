# Enlish_learning_site

## 網站規劃及當前進度
>> 部分設計仍有矛盾，期待日後修正

### 首頁:
1. 流量計數
	>> 以session語法記錄使用者登陸次數
2. 英語新聞看板(待完成
	>> 以爬蟲爬取CNN或式一些英語新聞的連結到網站看板
3. 網站的header和footer
	>> 套用bootstrap官方網站的template，並利用bootstrap設定的類別美化排版位置及加入置頂圖標
	>> 連至其他網頁的連結
4. 最新字集顯示
	>> 將最新數個願意分享的使用者的字集顯示在網站看板

### 字集創建區:
1. 以字集(set_name)->單字(english)->解釋(中、英例句,中譯,詞性)的模式儲存單字及其解釋
	>> 在Model設計單字的儲存方式，並會在之後讓使用者和字集進行關聯，如此就可以很好的管理單字
	>> 使網頁分成三層瀏覽，由上到下的順序如同上面所示
2. 可創建、編輯並刪除字集、單字和解釋
	>> 利用html的表單發送希望對單字修改的要求(post)，其中編輯和刪除借用到javascript對DOM元件的操作功能輔助發送表單，使頁面排版看起來更精簡
3. 基本的排版美化
	>> 以bootstrap美化排版

### 帳號系統:
1. 註冊和登入(登入待完成
	>> 利用正則表達式在前端就過濾掉所有不合適的資料
	>> 套用網路上註冊登入畫面的公開template，並利用bootstrap微調排版，再加入照片
	>> user的後端部分直接用Django內建的驗證系統完成，並借用了UserCreationForm的功能自動產生HTML表單
	>> 加入記住使用者的功能，預計使用session完成
	>> 令字集創建區和測驗區必須登入後才能進入，此功能有內建語法支援
	>> 讓歷史成績和字集的model與讓使用者關聯
2. 使用者個人資訊頁面
	>> 顯示使用者各項資訊(username、email、password、pub_date)
	>> 讓使用者上傳照片作為頭貼，使用到的技術還正在確定
	>> 可修改密碼
	>> 可看到自己的歷史測驗成績(答對、錯誤單字,所用字集,字集正確、錯誤數)和自己創建的字集

### 測驗區
>> 計畫利用javascript實作(利用React.js加上Django REST framework)
>> 以翻字卡及克漏字的方式測驗
>> 記錄錯誤單字並將這些資料儲存連接到使用者

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
