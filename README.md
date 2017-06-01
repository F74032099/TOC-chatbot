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
Otherwise, you might not be able to run your code.

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

起始 state 為 `user`.
功能1:英文單字測驗(高中7000字)
      答對可到下一個難度，答錯則到對一個難度
功能2:簡單智商測驗
     前三題為數字題，後三題為圖形題
功能3:
	* 輸入: "help" 可查看bot的說明
* user
	* 輸入: "help"
		* Reply: "I'm entering state1"

	* Input: "go to state2"
		* Reply: "I'm entering state2"


## Author
[石家瑋](https://github.com/F74032099)
