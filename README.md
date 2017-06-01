# TOC Project 2017
A telegram bot based on a finite state machine

英文單字測驗及邏輯測驗

## Setup

### Prerequisite
* Python 3

#### Install Dependency
```sh
pip install -r requirements.txt
```

* pygraphviz (For visualizing Finite State Machine)
    * [Setup pygraphviz on Ubuntu](http://www.jianshu.com/p/a3da7ecc5303)

### Secret Data

`API_TOKEN` and `WEBHOOK_URL` in app.py **MUST** be set to proper values.

### Run Locally
You can either setup https server or using `ngrok` as a proxy.

**`ngrok` would be used in the following instruction**

```sh
ngrok http 5000
```

After that, `ngrok` would generate a https URL.

You should set `WEBHOOK_URL` (in app.py) to `your-https-URL/hook`.

#### Run the sever

```sh
python app.py
```

## Finite State Machine
![fsm](./img/show-fsm.png)

## Usage and Command
* state 說明

	* 起始 state 為 `user`.
	* 輸入"eng" 
		+ 進入 `level1` state，答對時進入`level1` state，再答對則進入`level3` state
		+ 過程中若答錯則倒退1個state，例如`level2`回到`level1`
		+ 在`level1`答錯或`level3`答對時會回到原本的state 
		+ 10題結束後，回到`user` state
	  
	* 輸入"logic" 
		+ 進入 `logic1` state，三題結束後進入`logic2` state
		+ 6題結束後，回到`user` state
	  
	* 輸入"help"
		+ 進入`description` state 並回到 `user` state


* 功能1:英文單字測驗(高中7000字)

	* 輸入 "eng" 開始遊戲
	* 答對可到下一個難度，答錯則到倒退一個難度 
	* 共有10題，答錯會顯示正確答案
	* 結束時，會顯示答對題數
	
 ? ? ?
* 功能2:簡單智商測驗

	* 輸入 "logic" 開始遊戲
	* 題目均以圖片顯示
	* 共有6題，答錯會顯示正確答案
	* 結束時，會顯示答對題數
	* 前三題為數字題，後三題為圖形題


* 功能3:

	* 輸入: "help" 可查看bot的說明
	


## Author
[石家瑋](https://github.com/F74032099)
