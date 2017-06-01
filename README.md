# TOC Project 2017
A telegram bot based on a finite state machine

�^���r������޿����

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
* state ����

	* �_�l state �� `user`.
	* ��J"eng" 
		+ �i�J `level1` state�A����ɶi�J`level1` state�A�A����h�i�J`level3` state
		+ �L�{���Y�����h�˰h1��state�A�Ҧp`level2`�^��`level1`
		+ �b`level1`������`level3`����ɷ|�^��쥻��state 
		+ 10�D������A�^��`user` state
	  
	* ��J"logic" 
		+ �i�J `logic1` state�A�T�D������i�J`logic2` state
		+ 6�D������A�^��`user` state
	  
	* ��J"help"
		+ �i�J`description` state �æ^�� `user` state


* �\��1:�^���r����(����7000�r)

	* ��J "eng" �}�l�C��
	* ����i��U�@�����סA�����h��˰h�@������ 
	* �@��10�D�A�����|��ܥ��T����
	* �����ɡA�|��ܵ����D��
	
 ? ? ?
* �\��2:²�洼�Ӵ���

	* ��J "logic" �}�l�C��
	* �D�ا��H�Ϥ����
	* �@��6�D�A�����|��ܥ��T����
	* �����ɡA�|��ܵ����D��
	* �e�T�D���Ʀr�D�A��T�D���ϧ��D


* �\��3:

	* ��J: "help" �i�d��bot������
	


## Author
[�ۮa޳](https://github.com/F74032099)
