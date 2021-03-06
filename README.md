# Enlish_learning_site

## 網站規劃及當前進度
>> 部分設計仍有矛盾，期待日後修正

### 首頁
1. 流量計數
	1. 以session語法記錄使用者登陸次數
2. 英語新聞看板(待完成
	1. 以爬蟲爬取CNN或式一些英語新聞的連結到網站看板
3. 網站的header和footer
	1. 套用bootstrap官方網站的template，並利用bootstrap設定的類別美化排版位置及加入置頂圖標
	2. 連至其他網頁的連結
	3. 介紹網站開發人以及聯絡資訊
4. 最新字集顯示(待完成
	1. 將最新數個願意分享的使用者的字集顯示在網站看板
5. 網站使用說明
	1. 利用Bootstrap的互動視窗以表格的形式放在首頁

### 字集創建區
1. 以字集(set_name)->單字(english)->解釋(中、英例句,中譯,詞性)的模式儲存單字及其解釋
	1. 在Model設計單字的儲存方式，並會在之後讓使用者和字集進行關聯，如此就可以很好的管理單字
	2. 使網頁分成三層瀏覽，由上到下的順序如同上面所示
2. 可創建、編輯並刪除字集、單字和解釋
	1. 利用html的表單發送希望對單字修改的要求(post)，其中編輯和刪除借用到javascript對DOM元件的操作功能輔助發送表單，使頁面排版看起來更精簡
	2. 設置一按鍵，按下後以爬蟲到線上英文字典爬取多項字義
3. 基本的排版美化
	1. 以bootstrap美化排版
4. 個人化字集
	1. 使用者只看的到自己創建的字集

### 帳號系統
1. 註冊和登入
	1. 利用正則表達式在前端就過濾掉所有不合適的資料
	2. 套用網路上註冊登入畫面的公開template，並利用bootstrap微調排版，再加入照片
	3. user的後端部分直接用Django內建的驗證系統完成，並借用了UserCreationForm的功能自動產生HTML表單
	4. 加入記住使用者的功能，預計使用session完成
	5. 令字集創建區和測驗區必須登入後才能進入，此功能有內建語法支援
	6. 讓歷史成績和字集的model與讓使用者關聯
2. 使用者個人資訊頁面(待完成
	1. 顯示使用者各項資訊(username、email、password、pub_date)
	2. 讓使用者上傳照片作為頭貼，使用到的技術還正在確定(因此未完成
	3. 可修改密碼
	4. 可看到自己的歷史測驗成績(答對、錯誤單字,所用字集,字集正確、錯誤數)和自己創建的字集

### 測驗區
1. 測驗
	1. 由使用者自己在測驗設定頁面設定要考的字集和題目數
	2. 考試方式有三種：英翻中、中翻英、克漏字
	3. 測驗成績的model和User以及CharacterSet以一對多外鍵關聯
2. 成績查看
	1. 顯示於測驗設定頁面的下方
	2. 可顯示項目有：字集、題目總數/正確數、測驗方式

## 目前網站外觀

### 首頁

>> (登入前)
![alt text](https://github.com/AW-AlanWu/Enlish_learning_site/blob/master/images/index(logout).png)

>> (登入後)
![alt text](https://github.com/AW-AlanWu/Enlish_learning_site/blob/master/images/index(login).png)

### 字集創建區

![alt text](https://github.com/AW-AlanWu/Enlish_learning_site/blob/master/images/CharacterSetEditor.png)

### 單字創建區

![alt text](https://github.com/AW-AlanWu/Enlish_learning_site/blob/master/images/VocabularyEditor.png)

### 解釋創建區

>> (無解釋)
![alt text](https://github.com/AW-AlanWu/Enlish_learning_site/blob/master/images/MeaningEditor.png)
>> (按下"自動產生Meaning")
![alt text](https://github.com/AW-AlanWu/Enlish_learning_site/blob/master/images/MeaningEditor(Auto_get_Meaning).png)

### 帳號系統

>> (登入)
![alt text](https://github.com/AW-AlanWu/Enlish_learning_site/blob/master/images/Login.png)
>> (註冊)
![alt text](https://github.com/AW-AlanWu/Enlish_learning_site/blob/master/images/Sign_up.png)

>> (使用者頁面[字集])
![alt text](https://github.com/AW-AlanWu/Enlish_learning_site/blob/master/images/UserProfile(CharacterSet).png)
>> (使用者頁面[測驗成績])
![alt text](https://github.com/AW-AlanWu/Enlish_learning_site/blob/master/images/UserProfile(Score).png)

### 測驗區

>> (測驗設定)
![alt text](https://github.com/AW-AlanWu/Enlish_learning_site/blob/master/images/Exam.png)
>> (測驗中)
![alt text](https://github.com/AW-AlanWu/Enlish_learning_site/blob/master/images/onExam.png)