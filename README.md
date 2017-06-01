# TOC Project 2017
A telegram bot based on a finite state machine

<<<<<<< HEAD
­^¤å³æ¦r´úÅç¤ÎÅÞ¿è´úÅç
=======
è‹±æ–‡å–®å­—æ¸¬é©—åŠé‚è¼¯æ¸¬é©—
>>>>>>> 5e86206f31b23bdc8c262be3a37ed36e60d34680

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
<<<<<<< HEAD
* state »¡©ú

	* °_©l state ¬° `user`.
	* ¿é¤J"eng" 
		+ ¶i¤J `level1` state¡Aµª¹ï®É¶i¤J`level1` state¡A¦Aµª¹ï«h¶i¤J`level3` state
		+ ¹Lµ{¤¤­Yµª¿ù«h­Ë°h1­Óstate¡A¨Ò¦p`level2`¦^¨ì`level1`
		+ ¦b`level1`µª¿ù©Î`level3`µª¹ï®É·|¦^¨ì­ì¥»ªºstate 
		+ 10ÃDµ²§ô«á¡A¦^¨ì`user` state
	  
	* ¿é¤J"logic" 
		+ ¶i¤J `logic1` state¡A¤TÃDµ²§ô«á¶i¤J`logic2` state
		+ 6ÃDµ²§ô«á¡A¦^¨ì`user` state
	  
	* ¿é¤J"help"
		+ ¶i¤J`description` state ¨Ã¦^¨ì `user` state


* ¥\¯à1:­^¤å³æ¦r´úÅç(°ª¤¤7000¦r)

	* ¿é¤J "eng" ¶}©l¹CÀ¸
	* µª¹ï¥i¨ì¤U¤@­ÓÃø«×¡Aµª¿ù«h¨ì­Ë°h¤@­ÓÃø«× 
	* ¦@¦³10ÃD¡Aµª¿ù·|Åã¥Ü¥¿½Tµª®×
	* µ²§ô®É¡A·|Åã¥Üµª¹ïÃD¼Æ
	
 ? ? ?
* ¥\¯à2:Â²³æ´¼°Ó´úÅç

	* ¿é¤J "logic" ¶}©l¹CÀ¸
	* ÃD¥Ø§¡¥H¹Ï¤ùÅã¥Ü
	* ¦@¦³6ÃD¡Aµª¿ù·|Åã¥Ü¥¿½Tµª®×
	* µ²§ô®É¡A·|Åã¥Üµª¹ïÃD¼Æ
	* «e¤TÃD¬°¼Æ¦rÃD¡A«á¤TÃD¬°¹Ï§ÎÃD


* ¥\¯à3:

	* ¿é¤J: "help" ¥i¬d¬Ýbotªº»¡©ú
=======
* state èªªæ˜Ž

	* èµ·å§‹ state ç‚º `user`.
	* è¼¸å…¥"eng" 
		+ é€²å…¥ `level1` stateï¼Œç­”å°æ™‚é€²å…¥`level1` stateï¼Œå†ç­”å°å‰‡é€²å…¥`level3` state
		+ éŽç¨‹ä¸­è‹¥ç­”éŒ¯å‰‡å€’é€€1å€‹stateï¼Œä¾‹å¦‚`level2`å›žåˆ°`level1`
		+ åœ¨`level1`ç­”éŒ¯æˆ–`level3`ç­”å°æ™‚æœƒå›žåˆ°åŽŸæœ¬çš„state 
		+ 10é¡ŒçµæŸå¾Œï¼Œå›žåˆ°`user` state
	  
	* è¼¸å…¥"logic" 
		+ é€²å…¥ `logic1` stateï¼Œä¸‰é¡ŒçµæŸå¾Œé€²å…¥`logic2` state
		+ 6é¡ŒçµæŸå¾Œï¼Œå›žåˆ°`user` state
	  
	* è¼¸å…¥"help"
		+ é€²å…¥`description` state ä¸¦å›žåˆ° `user` state


* åŠŸèƒ½1:è‹±æ–‡å–®å­—æ¸¬é©—(é«˜ä¸­7000å­—)

	* è¼¸å…¥ "eng" é–‹å§‹éŠæˆ²
	* ç­”å°å¯åˆ°ä¸‹ä¸€å€‹é›£åº¦ï¼Œç­”éŒ¯å‰‡åˆ°å€’é€€ä¸€å€‹é›£åº¦ 
	* å…±æœ‰10é¡Œï¼Œç­”éŒ¯æœƒé¡¯ç¤ºæ­£ç¢ºç­”æ¡ˆ
	* çµæŸæ™‚ï¼Œæœƒé¡¯ç¤ºç­”å°é¡Œæ•¸
	
 Â  Â  Â 
* åŠŸèƒ½2:ç°¡å–®æ™ºå•†æ¸¬é©—

	* è¼¸å…¥ "logic" é–‹å§‹éŠæˆ²
	* é¡Œç›®å‡ä»¥åœ–ç‰‡é¡¯ç¤º
	* å…±æœ‰6é¡Œï¼Œç­”éŒ¯æœƒé¡¯ç¤ºæ­£ç¢ºç­”æ¡ˆ
	* çµæŸæ™‚ï¼Œæœƒé¡¯ç¤ºç­”å°é¡Œæ•¸
	* å‰ä¸‰é¡Œç‚ºæ•¸å­—é¡Œï¼Œå¾Œä¸‰é¡Œç‚ºåœ–å½¢é¡Œ


* åŠŸèƒ½3:

	* è¼¸å…¥: "help" å¯æŸ¥çœ‹botçš„èªªæ˜Ž
>>>>>>> 5e86206f31b23bdc8c262be3a37ed36e60d34680
	


## Author
<<<<<<< HEAD
[¥Û®aÞ³](https://github.com/F74032099)
=======
[çŸ³å®¶ç‘‹](https://github.com/F74032099)
>>>>>>> 5e86206f31b23bdc8c262be3a37ed36e60d34680
